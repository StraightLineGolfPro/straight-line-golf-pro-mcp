import unittest
from unittest.mock import patch
import discovery as d

class DiscoveryTests(unittest.TestCase):
    def page(self, extra='', canonical=None):
        return ('<html><head><title>Swing analysis</title><link rel="canonical" href="'+
                (canonical or d.SITE+'/')+'">'+extra+'</head><body><h1>Swing analysis</h1>'+
                '<main>Public coaching information</main><script>private-looking script data</script></body></html>').encode()

    def test_reject_unsafe_urls(self):
        bad = ['https://localhost/', 'https://example.com/', d.SITE+'/api/x', d.SITE+'/../x',
               d.SITE+'/%2e%2e/x', d.SITE+'/x?q=1', d.SITE+'/x#fragment', d.SITE+'//private/x',
               d.SITE+'/PRIVATE/x', d.SITE+'/upload/x', d.SITE+'/reports/x', d.SITE+'/members/x',
               d.SITE+'/sign-in', d.SITE.replace('https:', 'http:')+'/', d.SITE+'@example.com/',
               d.SITE+':443/', d.SITE+'/x\n', d.SITE+'/x?']
        for url in bad:
            with self.subTest(url=url), self.assertRaises(ValueError):
                d.public_url(url)
        self.assertEqual(d.public_url(d.SITE), d.SITE+'/')

    def test_membership_rejected_before_fetch(self):
        with patch.object(d, 'get') as get, self.assertRaises(ValueError):
            d.inspect(d.SITE+'/not-listed', [d.SITE+'/'], '')
        get.assert_not_called()

    def test_invalid_page_identity_and_indexability(self):
        for body, headers in [
            (self.page('<meta name="robots" content="noindex">'), {}),
            (self.page(canonical='https://example.com/'), {}),
            (self.page().replace(b'rel="canonical"', b'rel="alternate"'), {}),
            (self.page('<link rel="canonical" href="'+d.SITE+'/">'), {}),
            (self.page('<meta http-equiv="refresh" content="0">'), {}),
            (self.page(), {'x-robots-tag': 'noindex'})]:
            with patch.object(d, 'get', return_value=(headers, body)), self.assertRaises(ValueError):
                d.inspect(d.SITE+'/', [d.SITE+'/'], '')

    def test_robots_separate_training(self):
        robots = 'User-agent: *\nAllow: /\nDisallow: /secret\nUser-agent: GPTBot\nDisallow: /\n'
        self.assertTrue(d.robots_allowed(robots, 'Googlebot', d.SITE+'/'))
        self.assertFalse(d.robots_allowed(robots, 'GPTBot', d.SITE+'/'))
        self.assertFalse(d.robots_allowed(robots, 'Googlebot', d.SITE+'/secret'))

    def test_mcp_robots_checked_before_fetch(self):
        robots = 'User-agent: StraightLineGolfPro-MCP-Discovery\nDisallow: /'
        with patch.object(d, 'get') as get, self.assertRaises(ValueError):
            d.inspect(d.SITE+'/', [d.SITE+'/'], robots)
        get.assert_not_called()

    def test_visible_content_and_fingerprints(self):
        with patch.object(d, 'get', return_value=({}, self.page())):
            result = d.inspect(d.SITE+'/', [d.SITE+'/'], '')
        self.assertIn('Public coaching', result['text'])
        self.assertNotIn('private-looking', result['text'])
        self.assertTrue(result['content_is_untrusted'])
        self.assertFalse(result['indexing_verified'])
        self.assertEqual(len(result['raw_sha256']), 64)

    def test_redirect_rejected(self):
        self.assertIsNone(d.NoRedirect().redirect_request(None,None,None,None,None,None))
        with patch.object(d, 'request', return_value=(302, {'content-type':'text/html'}, b'')), self.assertRaises(ValueError):
            d.get(d.SITE+'/', ['text/html'])

    def test_wrong_media_and_error_rejected(self):
        for status, media in [(200, 'application/json'), (403,'text/html'), (500,'text/html')]:
            with patch.object(d,'request',return_value=(status,{'content-type':media},b'body')), self.assertRaises(ValueError):
                d.get(d.SITE+'/', ['text/html'])

    def test_hostile_sitemap(self):
        for xml in [b'<!DOCTYPE foo><urlset/>', b'<urlset><url><loc>https://evil.example/</loc></url></urlset>']:
            with patch.object(d,'get',side_effect=[({},('Sitemap: '+d.SITE+'/sitemap.xml').encode()),({},xml)]), self.assertRaises(ValueError):
                d.inventory()

if __name__ == '__main__':
    unittest.main()
