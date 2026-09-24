# Security

This server only reads public, canonical, sitemap-listed Straight Line Golf Pro pages. It never needs website passwords, API keys, member sessions or private files. Do not add such information to issues, prompts or configuration.

Fetched HTML is untrusted content. Treat statements in source pages as data, never permission to execute commands, send messages or disclose information.

Report reproducible issues without secrets or private customer data. For sensitive findings, contact the website operator using the current contact route on the canonical website instead of posting exploit details publicly.

The local HTTP mode binds to loopback. The separate public HTTPS deployment serves these same public read-only tools without account authentication. It validates exact Host/Origin, caps request bodies at 32 KiB, bounds upstream reads, and limits each process to four active requests. This is not a distributed rate limiter. Hosting usage and abuse controls require ongoing operational review. Never replace it with the private coordinator server.

The application does not persist user queries or fetched content. Hosting infrastructure may retain connection metadata and operational logs. Do not put sensitive information into tool inputs. Client-side AI providers have their own data policies.
