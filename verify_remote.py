"""Exercise a deployed public MCP with real protocol calls, never writes."""
import asyncio
import json
import sys
import httpx2 as httpx
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

async def main():
    url = sys.argv[1] if len(sys.argv)>1 else 'https://straight-line-golf-pro-mcp.vercel.app/mcp'
    async with httpx.AsyncClient(timeout=60) as http:
        async with streamable_http_client(url, http_client=http) as (read, write):
            async with ClientSession(read, write, read_timeout_seconds=60) as s:
                init = await s.initialize()
                tools = (await s.list_tools()).tools
                assert len(tools)==5 and all(t.annotations.read_only_hint for t in tools)
                for name,args in [('list_public_pages',{'limit':3}),('search',{'query':'swing'}),
                                  ('fetch',{'id':'https://www.straightlinegolfpro.com/'}),
                                  ('citation_readiness',{'url':'https://www.straightlinegolfpro.com/coach'}),
                                  ('discovery_status',{})]:
                    r=await s.call_tool(name,args)
                    assert not r.is_error,(name,r)
                for url_bad in ['https://example.com/','https://www.straightlinegolfpro.com/membership/history',
                                'https://www.straightlinegolfpro.com/api/private']:
                    assert (await s.call_tool('fetch',{'id':url_bad})).is_error
                guide=await s.read_resource('slgp://connection-guide')
                print(json.dumps({'endpoint':url,'server':init.server_info.model_dump(),
                    'tools':[t.name for t in tools],'positive_calls':5,'private_url_rejections':3,
                    'resource':guide.model_dump(mode='json')},indent=2))

if __name__=='__main__': asyncio.run(main())
