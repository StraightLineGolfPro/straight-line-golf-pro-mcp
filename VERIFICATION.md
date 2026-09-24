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

These are protocol and synthetic crawler tests, not ChatGPT account testing, genuine crawler visits, indexing or directory approval. See LAUNCH-STATUS.md for current distribution status. Earlier observations above describe version 1.0.0 and are superseded where this release changes behavior.

The official Registry API independently returned version 1.1.0 active/latest after successful GitHub Actions run 35938500234. Website source cdad5e1 was promoted as dpl_DzNwkqVTYz8Nyu1cC5GvCc2ADQ7R; 33 hostname/page/crawler checks and 11 referenced asset checks passed. The new connection guide was visually inspected. The public sitemap now contains 44 pages. IndexNow accepted all 44 distinct URLs across two runs with HTTP 200; those receipts do not establish indexing. Search Atlas recrawl remains in progress; no final post-release score is claimed.
