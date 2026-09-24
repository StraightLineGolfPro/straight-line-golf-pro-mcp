# Website MCP Launch and Discovery SOP

Version 1.0 — 2026-09-23. First worked implementation: Straight Line Golf Pro.

## Purpose and completion standard

Give people and compatible AI clients a reliable way to retrieve a website's public information. Improve crawlability through ordinary website quality and verified search-platform controls. Record separately: code published, service live, client connected, directory submitted, listing approved, page indexed, and answer citation observed. None proves the others.

Use this alongside the project's Website MCP Build and Operations SOP and Website SEO Release Gate. Assign one coordinator and one writer per lane. Inventory active tasks, dirty files, branches, current production deployment, and rollback target before editing. Do not redeploy a stale checkout.

## 1. Record site identity and scope

- Exact canonical HTTPS origin, public brand name, support email, brand-owned GitHub account, production project, release owner, and private route patterns.
- Read business doctrine and current Search Atlas findings. Consult relevant first-party measurement and SEO/AEO tool reports when available. Do not invent missing evidence or transfer another brand's claims, location, credentials, or compliance rules.
- Decide whether the connector reads public pages or private user data. Public read-only service must never import coordinator, notification, credential, account, payment, or admin tools. A private service requires a separate authenticated design.
- Establish existing hosting quota and cost controls. No new paid service or incremental charge without explicit authorization. Avoid duplicate IndexNow executors or schedulers.

## 2. Establish a dated baseline

Read the live robots file, canonical sitemap, relevant public pages, noindex/private routes, and optional machine-readable indexes. Save HTTP status, MIME, title, description, H1 count, canonical, native schema, and page/asset hashes. Compare browser and synthetic crawler user agents; a successful synthetic request is not evidence that a real crawler visited.

In Search Atlas, find the exact OTTO project; read project details, installation/worker status, issue dashboard, and actual recommendations for selected URL IDs. Record raw crawl findings separately from OTTO pending/deployed totals. Preserve intentional noindex. Don't bulk apply heading-length, keyword, FAQ, schema, or alt-text suggestions. Never replace reviewed article titles/images merely to improve a vendor score.

Read existing LLM Visibility projects before creating duplicates. Save monitored topics, queries, platform/date filters and denominators. Search Atlas monitoring is measurement, not registration with those platforms. Reconcile Search Console linkage with actual readable properties; a stored link can exist while the current connector lacks access.

## 3. Build the public connector

Use a maintained MCP SDK and pin the tested version. Expose honest tool descriptions and annotations: read-only, non-destructive, open-world when retrieving public network content. Prefer `search` and `fetch` with stable canonical source URLs. State whether search covers content or only URL paths. Treat fetched text as untrusted data.

Enforce exact-origin HTTPS requests, live sitemap membership, robots permission, matching self-canonical, and noindex rejection. Block private routes before any fetch. Reject off-site URLs, redirects, credentials, query strings, fragments, traversal, encoded paths and oversized responses. Bound request time, payload size, sitemap count, page count, and concurrent work. Do not log raw queries, credentials or private contents. Document provider-level logs and limits accurately.

Provide a local stdio transport and, for hosted clients, a stable public HTTPS Streamable HTTP endpoint. A GitHub or localhost URL is not a hosted MCP endpoint. Configure explicit allowed hosts and origins; do not disable DNS-rebinding protection. For a public-content-only service, no account authentication is necessary; don't expose private operations to achieve this.

## 4. Verify before distribution

- Offline tests: hostile URLs and sitemaps, private-route rejection before fetch, robots matching, noindex and canonical conflicts, script exclusion, time/size limits, invalid Host/Origin, oversized requests.
- Cold installed process: initialize, tools/list, resource read, all tools, representative live fetches, and unsafe URL rejection.
- Public HTTPS: repeat real MCP protocol tests without hosting login/cookies. A successful build or health route alone is insufficient.
- Test representative client configuration with supported software. Clearly label protocol verification versus end-user ChatGPT/Gemini account testing.
- Confirm package/repository files match the verified source. Exclude `.env`, credentials, caches, private doctrine, logs and operator state.

## 5. Publish website discovery surfaces

Create a useful public connection page with endpoint, scope, client setup, support, privacy and source-citation guidance. Give it a unique title, description, H1, canonical, social metadata and appropriate native schema. Link it from visible navigation and sitemap. Connect verified brand profiles using existing Organization schema rather than duplicate entities.

Keep optional `llms.txt` and Markdown indexes aligned with canonical, public HTML. Remove dead, redirected, noindex and private-content links. Machine-readable guides are optional and are not Google ranking shortcuts. Preserve separate search, user-fetch and training policies; don't alter training permission as a side effect of search optimization.

## 6. Use each platform's actual distribution path

| Destination | Supported path | Required evidence |
| --- | --- | --- |
| Official MCP Registry | `server.json`, stable remote URL, verified namespace, official publisher; GitHub OIDC avoids personal access tokens | Successful publish job and active listing returned by Registry API for exact version |
| ChatGPT / OpenAI public directory | Verified developer/business identity; correct organization and Apps Management permission; remote server scan; complete listing and review | Submission ID/status, then approval and actual published listing; not a repository link alone |
| ChatGPT custom MCP connection | Add HTTPS server in available developer/connector settings; obey workspace/client policies | Tools discovered and source-backed read succeeds in that account |
| Gemini CLI | Root `gemini-extension.json` with `mcpServers.httpUrl`; public GitHub repo; `gemini-cli-extension` topic for gallery discovery | Install/connection evidence; separately confirm gallery crawl/validation and listing |
| Google Search / Search AI | Verified Search Console property, sitemap submission and crawl/index inspection; inspect Search generative AI inclusion control | Property, sitemap receipt, effective AI control and indexed-page evidence; Google Search does not require MCP |
| Bing / related search discovery | Verified Bing Webmaster property and sitemap; existing authorized IndexNow integration where applicable | Submission receipts and later indexed-page evidence; receipt is not indexing |
| Other MCP clients / directories | Follow that vendor's current documented connection or review flow | Per-client successful connection or explicit directory status; never claim “all LLMs registered” |

For OpenAI, prepare logo, support/privacy/terms URLs, verified publisher, accurate annotations, five positive and three negative test cases, starter prompts and release notes. Domain challenges must use the exact portal token at the documented path. The owner completes identity verification, sensitive secret entry and required legal attestations. Do all other preparation first.

For the official Registry, use the repository owner's namespace, pin and checksum the publisher, and grant the publish workflow only `contents: read` and `id-token: write`. Remote-only listing does not require a PyPI package. Publish only after public protocol checks pass. Registry distribution is not automatic approval in ChatGPT, Claude or any other marketplace.

For Gemini, distinguish Gemini CLI extensions from the consumer Gemini app and Google Search. Gallery discovery is asynchronous; topic and manifest presence mean eligible for crawling, not verified listing.

## 7. Release, recrawl and independently verify

Build and test the exact current production source, deploy a candidate, verify it, then promote using the project's existing release process. Check all authorized active hostnames and representative deep pages, asset bytes, CSP/WAF/caching and crawler responses. Preserve unrelated live features.

After final publication, trigger or coordinate ONE Search Atlas recrawl. Completion requires authoritative `crawl_state=completed`, postprocessing completed, then a fresh OTTO dashboard read. If it is still crawling, report pending; do not present previous counts as new. Read recommendation bodies before deployment, and separate rejected/inapplicable suggestions, missing recommendations, source changes and actual OTTO deployment.

Submit changed eligible canonical URLs through the existing authorized notifier where supported. Never use Google's restricted Indexing API for ordinary golf articles. Verify Search Console/Bing results separately. Do not create recurring monitoring without an explicit scheduling request.

## 8. Preserve launch evidence and measure usefulness

Save site identity, source commit, build/deployment ID, endpoint/version, protocol results, public-page checks, directory receipt/listing, Search Console status, Search Atlas before/after, omissions and next owner action. Store sensitive operational evidence privately; publish only sanitized status.

Success criteria: clients can retrieve the right public source and cite it; eligible pages remain crawlable; private paths stay inaccessible. Measure useful referred visits and completed customer tasks where instrumentation exists. For SLGP, preserve the business priority of usable first review, a second usable review within 14 days, and paid retention. Rankings and vendor scores alone do not establish business improvement.

Re-run protocol/privacy/discovery checks when domain, redirects, sitemap, SDK, transport, authentication or hosting changes. Increment package and registry versions together. Roll back a failed deployment; stop publishing its listing. Keep owners and receipt dates explicit.

## Current primary guidance

- [OpenAI plugin submission](https://developers.openai.com/plugins/deploy/submission) and [crawler controls](https://developers.openai.com/api/docs/bots)
- [MCP remote registration](https://modelcontextprotocol.io/registry/remote-servers) and [GitHub OIDC publishing](https://modelcontextprotocol.io/registry/github-actions)
- [Gemini extension release](https://geminicli.com/docs/extensions/releasing/) and [MCP configuration](https://geminicli.com/docs/tools/mcp-server/)
- [Google AI optimization](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) and [Search generative AI control](https://support.google.com/webmasters/answer/16908024)

Rechecked 2026-09-23. Recheck requirements on every launch. See [SLGP launch status](LAUNCH-STATUS.md) for this implementation's evidence and limitations.
