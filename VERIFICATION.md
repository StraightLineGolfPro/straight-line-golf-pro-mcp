# Release verification — 2026-09-23

Public package version 1.0.0, derived from the maintained AI Atom Brain website MCP SOP and the existing site-isolated SLGP discovery implementation.

- Nine offline regression tests passed: exact-origin and private URL rejection, sitemap membership, canonical/noindex/refresh rejection, robots policy separation, MCP crawler denial, visible text extraction, redirect rejection, HTTP/media errors, and hostile sitemap rejection.
- A cold stdio MCP client initialized the server, enumerated five read-only tools, listed live URLs, searched, fetched the canonical homepage, read discovery status, and rejected foreign/private URLs. Connection-guide resource was enumerated.
- Local Streamable HTTP initialize, five-tool enumeration and connection-guide resource read passed.
- Clean virtual-environment package installation built version 1.0.0 successfully using the pinned MCP SDK 2.0.0.
- The live public sitemap contained 43 permitted URLs at verification time. Inventory is an observation, not proof that every page was fetched or indexed.
- Canonical homepage, robots.txt, sitemap.xml, llms.txt and llms-full.txt returned HTTP 200 with their expected HTML/XML/plain-text content types.
- No production website files, crawler rules, customer workflows or existing internal MCP installation were changed by this release.

The public GitHub package is an installable local connector. No public remote HTTPS MCP service, ChatGPT directory listing, search indexing result, model training update or citation gain is claimed. Search Atlas was not changed or recrawled for this separate repository release. Website content remains live and can change after these checks.
# Version 1.1.0 — 2026-09-23

Public endpoint https://straight-line-golf-pro-mcp.vercel.app/mcp passed cold remote initialization, tools/list, five positive live tool calls, resource retrieval and three off-site/private URL denials. Eleven offline tests passed, including Host/Origin and body-size enforcement. Live public sitemap inventory at launch baseline: 43 URLs, all passed canonical/public-content checks.

Vercel deployment dpl_7jGPKKi89mLBB4z1zMDPwrjqG5oA. The first deployment's legacy rewrite caused 404s; the verified configuration uses `tool.vercel.entrypoint = "api.index:app"` without catch-all rewrites. MCP SDK 2.0.0's Streamable HTTP client uses `httpx2` and yields two streams.

These are protocol and synthetic crawler tests, not ChatGPT account testing, genuine crawler visits, indexing or directory approval. See LAUNCH-STATUS.md for current distribution status. Earlier observations below describe version 1.0.0.
