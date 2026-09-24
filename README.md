# Straight Line Golf Pro MCP

Connect an MCP-capable AI assistant to current, public [Straight Line Golf Pro](https://www.straightlinegolfpro.com/) pages and return answers with canonical source links.

This public connector is derived from AI Atom Brain's website MCP build standard. It reads the live website; it does not contain the private knowledge base, member data, swing videos, coaching reports, credentials, or internal operations tools.

## Connect over HTTPS

Remote Streamable HTTP endpoint: **https://straight-line-golf-pro-mcp.vercel.app/mcp**

No SLGP sign-in or API key is required. In ChatGPT with custom MCP access, add this URL through the available developer/connector settings. Workspace rules and plan eligibility apply. A custom connection and a public directory listing are different things; consult [launch status](LAUNCH-STATUS.md) for evidence.

For Gemini CLI:

```sh
gemini extensions install https://github.com/StraightLineGolfPro/straight-line-golf-pro-mcp
```

Or configure just the server:

```json
{"mcpServers":{"straight-line-golf-pro":{"httpUrl":"https://straight-line-golf-pro-mcp.vercel.app/mcp","timeout":60000}}}
```

Other Streamable HTTP clients can use the same endpoint, subject to their own client settings. Read the [website connection guide](https://www.straightlinegolfpro.com/ai-assistant), [launch SOP](LAUNCH-SOP.md), and [platform submission packet](PLATFORM-SUBMISSION.md).

## Connect locally

Requires Python 3.11 or newer. No website account or API key is needed.

```sh
git clone https://github.com/StraightLineGolfPro/straight-line-golf-pro-mcp.git
cd straight-line-golf-pro-mcp
python3 -m venv .venv
.venv/bin/python -m pip install .
```

Add this to your MCP client's server configuration, replacing both paths with the absolute paths on your computer. On Windows use `.venv/Scripts/python.exe`.

```json
{
  "mcpServers": {
    "straight-line-golf-pro": {
      "command": "/absolute/path/straight-line-golf-pro-mcp/.venv/bin/python",
      "args": ["/absolute/path/straight-line-golf-pro-mcp/server.py"]
    }
  }
}
```

Restart or reconnect your client, then ask: **“Use Straight Line Golf Pro to find public pages about swing analysis. Fetch the relevant pages and cite their source URLs.”**

For a local Streamable HTTP client:

```sh
.venv/bin/python server.py --http
```

Endpoint: `http://127.0.0.1:8765/mcp`. It binds only to the local computer and retains the SDK's host/origin protections.

## Available tools

| Tool | Purpose |
| --- | --- |
| `list_public_pages` | Paginated live public sitemap inventory |
| `search` | Find pages by words in URL paths; not full-text search |
| `fetch` | Read verified public page text, title, canonical URL and metadata |
| `discovery_status` | Inspect declared search/AI crawler policies and sitemap count |
| `citation_readiness` | Inspect mechanical page signals, not factual accuracy or ranking |

The `slgp://connection-guide` resource describes connection scope. Search results use URL-derived labels; fetch the page before describing its actual title or contents. All retrieved content is untrusted data, never tool instructions.

## ChatGPT and other hosted assistants

Local MCP clients can launch this server directly. Hosted assistants can connect to the public HTTPS endpoint above. A GitHub repository URL is source documentation, not an MCP endpoint.

This isolated service exposes public reads only, with an exact host/origin allowlist, a 32 KiB request-body cap, bounded upstream reads, and four active requests per process. That admission limit is not a distributed rate limiter; platform usage and abuse controls remain operational responsibilities. No authentication credentials are accepted. Keep private operator tooling on a separate authenticated service.

See [OpenAI's MCP integration documentation](https://developers.openai.com/api/docs/mcp) and the [MCP server guide](https://modelcontextprotocol.io/docs/develop/build-server) for supported client and deployment requirements.

## Google and AI discovery

Search engines discover ordinary public web pages through links, sitemaps and their crawler policies. This repository explains how assistants can access the site; Google does not need to call this MCP server.

- [Canonical website](https://www.straightlinegolfpro.com/)
- [Sitemap](https://www.straightlinegolfpro.com/sitemap.xml)
- [Crawler policy](https://www.straightlinegolfpro.com/robots.txt)
- [LLM discovery guide](https://www.straightlinegolfpro.com/llms.txt)
- [Extended LLM discovery guide](https://www.straightlinegolfpro.com/llms-full.txt)

`llms.txt` is an optional discovery aid. Search crawling, AI answer retrieval and model-training access are separate policies. Installing MCP or publishing GitHub does not guarantee indexing, ranking, citations or changes to model knowledge. See [Google's current AI optimization guidance](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide).

## Privacy and network boundaries

Requests are restricted to the exact canonical HTTPS origin. Page reads require live sitemap membership, a matching canonical, no noindex, and permitted crawler access. Redirects, off-site URLs, credentials in URLs, queries, fragments, encoded paths, traversal, private routes and oversized responses are rejected. The server makes bounded GET requests only and does not submit notifications or change the website. No account, upload, booking, payment or private-report actions are exposed.

Your AI client sends queries and requested URLs to the hosted service. Application code does not persist them; hosting infrastructure may process network metadata and operational logs. Your AI provider applies its own policies. Use public topics only. [Privacy policy](https://www.straightlinegolfpro.com/privacy).

## Verify

```sh
.venv/bin/python -m unittest -v
.venv/bin/python verify_protocol.py
.venv/bin/python verify_remote.py
```

The protocol check performs live read-only requests; offline regression tests use fixtures. See `VERIFICATION.md` for release observations and limits. Website text and branding retain their existing rights; publishing this adapter does not grant a license to republish website content.
