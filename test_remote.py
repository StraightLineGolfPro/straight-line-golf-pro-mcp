import os
import unittest
from unittest.mock import patch
from starlette.testclient import TestClient
from remote import create_app

class RemoteTests(unittest.TestCase):
    def test_transport_and_limits(self):
        with patch.dict(os.environ, {'SLGP_MCP_PUBLIC_ORIGIN':'https://slgp.example'}):
            with TestClient(create_app(), base_url='https://slgp.example') as c:
                headers={'Accept':'application/json, text/event-stream'}
                payload={'jsonrpc':'2.0','id':1,'method':'initialize','params':{
                    'protocolVersion':'2025-11-25','capabilities':{},'clientInfo':{'name':'test','version':'1'}}}
                r=c.post('/mcp',json=payload,headers=headers)
                self.assertEqual(r.status_code,200)
                self.assertEqual(r.json()['result']['serverInfo']['name'],'straight-line-golf-pro')
                self.assertIn(c.post('/mcp',json=payload,headers={**headers,'Origin':'https://evil.example'}).status_code,(403,421))
                self.assertEqual(c.post('/mcp',json=payload,headers={**headers,'Host':'evil.example'}).status_code,421)
                self.assertEqual(c.post('/mcp',content=b'x'*32769,headers={**headers,'Content-Type':'application/json'}).status_code,413)
                self.assertTrue(c.get('/health').json()['read_only'])

    def test_public_origin_validation(self):
        for origin in ['http://example.com','https://user:pass@example.com','https://example.com/path','https://example.com?x=1']:
            with patch.dict(os.environ,{'SLGP_MCP_PUBLIC_ORIGIN':origin}), self.assertRaises(ValueError):
                create_app()

if __name__=='__main__': unittest.main()
