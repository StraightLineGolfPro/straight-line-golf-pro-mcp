# SLGP platform submission packet

Prepared 2026-09-23. Preparation is not submission or approval.

- Name: Straight Line Golf Pro
- Short description: Find and cite public SLGP golf learning resources.
- Description: Search current public Straight Line Golf Pro page paths, retrieve public page text and canonical citation links, and explore the golf learning library. Public read-only access; no member accounts, uploads, private swing reports, booking or payments.
- Website: https://www.straightlinegolfpro.com/ai-assistant
- Support: https://www.straightlinegolfpro.com/contact
- Support email: support@straightlinegolfpro.com
- Privacy: https://www.straightlinegolfpro.com/privacy
- Terms: https://www.straightlinegolfpro.com/terms
- Existing brand logo: https://www.straightlinegolfpro.com/images/straight-line-golf-pro-logo.jpg (check portal-specific asset requirements)
- Universal remote URL: https://straight-line-golf-pro-mcp.vercel.app/mcp
- Authentication: none; public information only
- UI: none; text results with canonical links
- Version: 1.1.0
- Availability: public English-language resources; select platform regions consistent with verified business availability
- Publisher: use the owner's verified SLGP identity; do not claim another project's identity.

## Starter prompts

1. Find SLGP resources about fixing a golf slice, fetch one, and cite the page.
2. What does SLGP say about its AI coach? Retrieve the current coach page.
3. List public golf practice resources and link to the originals.

## Five positive cases

| Input / tool | Expected behavior |
| --- | --- |
| `list_public_pages` with limit 3 | Three canonical public URLs and valid pagination |
| `search` with query `swing` | Matching URL-path results; no full-text or verified-title claim |
| `fetch` with canonical home URL | Current visible text, title, canonical URL and source metadata |
| `citation_readiness` for `/coach` | Mechanical metadata observations, no ranking guarantee |
| `discovery_status` | Live sitemap count and declared bot policy, indexing/citation marked unverified |

## Three negative cases

| Input | Expected behavior |
| --- | --- |
| Fetch `https://example.com/` | Reject off-site request |
| Fetch `/membership/history` on canonical origin | Reject private route before upstream request |
| Fetch `/api/private` on canonical origin | Reject operator/API path before upstream request |

Additional fixture coverage: encoded traversal, redirects, noindex, invalid canonical, hostile sitemap XML, incorrect Origin/Host and oversized request body.

## Data handling

The AI client sends queries and URLs to the MCP. Application code does not persist queries or fetched contents; hosting infrastructure may process connection metadata and operational logs. Responses contain public source text and canonical citations. Retrieved content is untrusted. The service never receives SLGP account credentials or accesses private business systems. Review the privacy page and actual configuration before attesting to platform policies.

## Owner-only completion if requested by the portal

Verify the SLGP publisher identity in the correct OpenAI organization, complete any required identity challenge, and review legal attestations. After that, scan the live URL, inspect tool metadata, run the cases above, submit, and preserve the actual status. Approval and publication require their own evidence.
