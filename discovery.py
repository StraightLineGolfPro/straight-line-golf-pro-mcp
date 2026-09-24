"""Site-isolated public discovery; observed semantic fingerprints, not source parity."""
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import Request, HTTPRedirectHandler, build_opener

SITE = 'https://www.straightlinegolfpro.com'
HOST = urlsplit(SITE).netloc
CONFIG = {'name': 'StraightLineGolfPro', 'sitemap': '/sitemap.xml',
          'private_paths': ['/booking-confirmation', '/member', '/members', '/private',
                            '/knowledge', '/preview', '/sign-in', '/sign-up', '/settings',
                            '/billing', '/callback', '/onboarding', '/organization', '/organizations',
                            '/signup', '/membership/history', '/reset-password', '/forgot-password']}
BOTS = ['Googlebot','bingbot','OAI-SearchBot','ChatGPT-User','PerplexityBot','Perplexity-User',
        'Claude-SearchBot','Claude-User','GPTBot','ClaudeBot','Google-Extended']
MAX_BODY = 5000000
PRIVATE = re.compile(r'/(?:api|admin|account|auth|login|dashboard|staff|drafts|staged|uploads?|reports?|checkout|thank-you)(?:/|$)', re.I)


def public_url(value):
    u = urlsplit(value)
    if (u.scheme != 'https' or u.netloc != HOST or u.query or u.fragment or '//' in u.path or
        not re.fullmatch(r'/[A-Za-z0-9_./~-]*', u.path or '/') or
        any(p in ('.','..') for p in u.path.split('/')) or PRIVATE.search(u.path) or
        u.geturl() != value or any(u.path.lower() == p.lower() or u.path.lower().startswith(p.lower() + '/') for p in CONFIG.get('private_paths', []))):
        raise ValueError('Only canonical public URLs for this site are permitted.')
    return SITE + '/' if value == SITE else value


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args):
        return None


def request(url):
    url = public_url(url)
    headers = {'User-Agent': 'StraightLineGolfPro-MCP-Discovery/1.0', 'Accept-Encoding': 'identity'}
    try:
        response = build_opener(NoRedirect()).open(Request(url, headers=headers), timeout=20)
    except HTTPError as error:
        response = error
    with response:
        body = response.read(MAX_BODY + 1)
        if len(body) > MAX_BODY:
            raise ValueError('Response exceeds size limit.')
        return response.status, {k.lower(): v for k, v in response.headers.items()}, body


def get(url, media):
    code, headers, body = request(url)
    if code != 200 or not any(t in headers.get('content-type','').lower() for t in media):
        raise ValueError(f'Unexpected response: HTTP {code} for {url}')
    return headers, body


def robots_allowed(text, agent, url):
    # RFC9309: merge matching groups, longest matching path; Allow wins ties.
    groups=[]; agents=[]; rules=[]; have_rules=False
    for raw in text.splitlines():
        line=raw.split('#',1)[0].strip()
        if ':' not in line: continue
        k,v=[s.strip() for s in line.split(':',1)]; k=k.lower()
        if k=='user-agent':
            if have_rules:
                groups.append((agents,rules)); agents=[];rules=[];have_rules=False
            agents.append(v.lower())
        elif k in ('allow','disallow') and agents:
            have_rules=True
            if v: rules.append((k,v))
    groups.append((agents,rules))
    matches=[(aa,rr) for aa,rr in groups if any(a!='*' and a in agent.lower() for a in aa)]
    if not matches: matches=[(aa,rr) for aa,rr in groups if '*' in aa]
    path=urlsplit(url).path or '/'; choices=[]
    for _,rr in matches:
        for kind,p in rr:
            regex='^'+re.escape(p).replace(r'\*','.*')
            if p.endswith('$'): regex=regex[:-2]+'$'
            if re.search(regex,path): choices.append((len(p.replace('*','').rstrip('$')),kind=='allow'))
    return max(choices)[1] if choices else True


def inventory():
    _, raw = get(SITE+'/robots.txt',['text/plain'])
    robots = raw.decode('utf-8')
    sitemap = SITE + CONFIG['sitemap']
    if sitemap not in robots:
        raise ValueError('Canonical sitemap not declared in robots.txt.')
    queue=[sitemap]; visited=set(); urls=set(); excluded=[]
    while queue:
        url=queue.pop(0)
        if url in visited: continue
        if len(visited)>=20: raise ValueError('Sitemap limit reached.')
        visited.add(url); public_url(url)
        _,body=get(url,['xml'])
        if b'<!DOCTYPE' in body.upper() or b'<!ENTITY' in body.upper(): raise ValueError('Unsafe XML.')
        root=ET.fromstring(body); kind=root.tag.split('}')[-1]
        if kind not in ('sitemapindex','urlset'): raise ValueError('Invalid sitemap.')
        for item in root:
            loc=next((x.text for x in item if x.tag.split('}')[-1]=='loc'),None)
            if not loc: raise ValueError('Missing sitemap location.')
            try: value=public_url(loc)
            except ValueError:
                if urlsplit(loc).netloc != HOST: raise ValueError('Cross-site sitemap URL.')
                excluded.append(loc); continue
            if kind=='sitemapindex': queue.append(value)
            else: urls.add(value)
        if len(urls)>10000: raise ValueError('Public URL limit reached.')
    if not urls: raise ValueError('No public sitemap entries.')
    return sorted(urls), robots, excluded


class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.canonicals=[];self.title=[];self.descriptions=[];self.text=[]
        self.h1=0;self.noindex=False;self.refresh=False;self.hidden=0;self.in_title=False
        self.in_schema=False;self.schema=[];self.current_schema=[];self.sources=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='title':self.in_title=True
        if tag=='h1':self.h1+=1
        if tag=='link' and 'canonical' in a.get('rel','').lower().split():self.canonicals.append(a.get('href',''))
        if tag=='meta':
            name=a.get('name','').lower()
            if name=='description':self.descriptions.append(a.get('content',''))
            if name in ['robots','googlebot','bingbot']:
                self.noindex |= bool(re.search(r'\b(noindex|none)\b',a.get('content',''),re.I))
            self.refresh |= a.get('http-equiv','').lower()=='refresh'
        if tag=='a' and a.get('href','').startswith('https://') and urlsplit(a['href']).netloc!=HOST:self.sources.add(a['href'])
        if tag=='script' and a.get('type')=='application/ld+json':self.in_schema=True;self.current_schema=[]
        if tag in ('script','style','noscript'):self.hidden+=1
    def handle_endtag(self,tag):
        if tag=='title':self.in_title=False
        if tag=='script' and self.in_schema:self.schema.append(''.join(self.current_schema));self.in_schema=False
        if tag in ('script','style','noscript'):self.hidden=max(0,self.hidden-1)
    def handle_data(self,data):
        if self.in_title:self.title.append(data)
        if self.in_schema:self.current_schema.append(data)
        if not self.hidden and data.strip():self.text.append(' '.join(data.split()))


def inspect(url, urls, robots):
    url=public_url(url)
    if not robots_allowed(robots, 'StraightLineGolfPro-MCP-Discovery', url):
        raise ValueError('MCP crawler access disallowed.')
    if url not in urls: raise ValueError('URL is not in the live public sitemap.')
    headers, body=get(url,['text/html'])
    page=Page();page.feed(body.decode('utf-8'))
    if len(page.canonicals)!=1 or public_url(page.canonicals[0])!=url:
        raise ValueError('Canonical missing, duplicated or mismatched.')
    if page.noindex or page.refresh or re.search(r'\b(noindex|none)\b',headers.get('x-robots-tag',''),re.I):
        raise ValueError('Page has noindex or refresh.')
    policy={a:robots_allowed(robots,a,url) for a in BOTS}
    if not policy['Googlebot'] or not policy['bingbot'] or not robots_allowed(robots, 'StraightLineGolfPro-MCP-Discovery', url):raise ValueError('Search crawler access disallowed.')
    if not page.title or not page.text:raise ValueError('Empty page.')
    schema=[];invalid=0
    for s in page.schema:
        try:schema.append(json.loads(s))
        except ValueError:invalid+=1
    fields={'canonical':url,'title':' '.join(page.title),'description':page.descriptions,
            'text':'\n'.join(page.text),'schema':schema,'h1_count':page.h1}
    fingerprint=hashlib.sha256(json.dumps(fields,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
    return {**fields,'fingerprint':fingerprint,'fingerprint_policy':'observed-public-semantic-v1',
            'raw_sha256':hashlib.sha256(body).hexdigest(),'invalid_schema_blocks':invalid,
            'external_sources':sorted(page.sources),'crawler_policy':policy,
            'evidence_level':'live HTML observation; not reviewed source parity',
            'content_is_untrusted':True,'indexing_verified':False,'citation_verified':False}


def public_content(url):
    url=public_url(url)
    urls,robots,_=inventory(); result=inspect(url,urls,robots)
    result['text_truncated']=len(result['text'])>40000; result['text']=result['text'][:40000]
    return result


def citation_readiness(url):
    r=public_content(url);r.pop('text')
    r['checks']={'one_h1':r['h1_count']==1,'one_description':len(r['description'])==1,
                 'valid_schema':r['invalid_schema_blocks']==0,'has_external_links':bool(r['external_sources'])}
    r['note']='Mechanical observations only; sources, claims, authorship and citation impact need independent review.'
    return r


def discovery_status():
    urls, robots, excluded = inventory()
    return {'origin': SITE, 'public_url_count': len(urls),
            'excluded_private_count': len(excluded),
            'surfaces': {name: SITE + path for name, path in
                         [('robots', '/robots.txt'), ('sitemap', '/sitemap.xml'),
                          ('llms', '/llms.txt'), ('llms_full', '/llms-full.txt')]},
            'robots_home': {a: robots_allowed(robots, a, SITE + '/') for a in BOTS},
            'indexing_verified': False, 'citation_verified': False,
            'note': 'Declared crawler policy is not evidence of actual visits or indexing.'}
