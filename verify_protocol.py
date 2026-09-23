"""Cold-start MCP protocol verification with live public GET requests only."""
import asyncio
import json
import sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    root = Path(__file__).resolve().parent
    async with stdio_client(StdioServerParameters(command=sys.executable, args=[str(root/'server.py')])) as (read, write):
        async with ClientSession(read, write, read_timeout_seconds=120) as session:
            init = await session.initialize()
            tools = (await session.list_tools()).tools
            assert {t.name for t in tools} == {'search','fetch','list_public_pages','discovery_status','citation_readiness'}
            assert all(t.annotations.read_only_hint for t in tools)
            for name, args in [('list_public_pages', {'limit': 3}), ('search', {'query':'golf'}),
                               ('fetch', {'id':'https://www.straightlinegolfpro.com/'}),
                               ('discovery_status', {})]:
                result = await session.call_tool(name, args)
                assert not result.is_error, (name, result)
            for url in ['https://example.com/', 'https://www.straightlinegolfpro.com/api/private']:
                assert (await session.call_tool('fetch', {'id':url})).is_error
            resources = await session.list_resources()
            assert any(str(r.uri)=='slgp://connection-guide' for r in resources.resources)
            print(json.dumps({'server': init.server_info.model_dump(), 'tools':[t.name for t in tools],
                              'live_public_read':True, 'unsafe_urls_rejected':True}))

if __name__ == '__main__':
    asyncio.run(main())
