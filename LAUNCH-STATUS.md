# SLGP MCP launch status

Updated 2026-09-23. This file distinguishes preparation from verified platform outcomes.

| Item | Status |
| --- | --- |
| Brand-owned public repository | Live under StraightLineGolfPro |
| MCP 1.1.0 source | Five public read-only tools; stdio and HTTPS transports |
| Public HTTPS deployment | Live; real MCP initialization, all five tool reads, resource read and three unsafe/private URL rejections passed |
| Official MCP Registry | Published version 1.1.0; Registry API independently returns active/latest; [successful publish run](https://github.com/StraightLineGolfPro/straight-line-golf-pro-mcp/actions/runs/35938500234) |
| Gemini CLI | Root manifest and gallery-discovery topic published; gallery listing and end-user CLI installation not yet verified |
| OpenAI public directory | Submission packet prepared; portal blocks creation until the publisher completes developer identity verification; not submitted or approved |
| Google Search Console | Search Atlas records linked domain property; signed-in owner/support accounts cannot access it. Property owner access is required to verify sitemap and effective Search AI controls |
| Search Atlas AI Visibility | Existing monitoring for ChatGPT, Gemini, Google AI Mode, Perplexity and Copilot; monitoring is not platform registration |
| Website connection guide | [Live and visually verified](https://www.straightlinegolfpro.com/ai-assistant); linked in footer and sitemap; canonical, metadata, privacy and discovery updates deployed |
| IndexNow | 44 distinct public URLs accepted with HTTP 200 across two bounded runs, including the connection guide; indexing not verified |

Website release: source `cdad5e1`, deployment `dpl_DzNwkqVTYz8Nyu1cC5GvCc2ADQ7R`. Thirty-three checks passed across the canonical, apex and existing Vercel hostnames, including expected apex-to-www redirects. Synthetic crawler checks confirm request access, not actual crawler visits. Eleven offline MCP tests and real stdio/HTTPS protocol tests passed. The publisher also reran its tests successfully in GitHub Actions. Existing private account routes remain excluded.

Search Atlas baseline: OTTO score 84; 1,202 pending recommendations, zero approved. Pixel not detected and worker status failed. Raw crawl separately reports 1,196 pages and 12,756 observations, including 1,015 noindex observations. These are not interchangeable counts and not all observations are defects. The baseline public MCP inventory contained 43 pages; all passed canonical/public-content checks. It now contains 44 with the new guide. The requested recrawl still reports `crawling`/`processing`; it began before this release, so post-release recrawl closure and dashboard comparison remain pending. No generated OTTO recommendations were bulk deployed.

No guarantee of indexing, ranking, training inclusion, directory approval, or AI citations is made. See the [launch SOP](LAUNCH-SOP.md) for verification criteria.
