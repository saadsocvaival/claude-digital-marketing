# Secrets Pointer — {{client-id}}

> Raw secrets never land in this repo. This file is a pointer manifest only.

| Service | Secret name | Vault location | Rotation cadence | Last rotated | Owner |
|---|---|---|---|---|---|
| GA4 | API key | 1Password: "Client/{id}/GA4" | 90d | … | Head of Analytics |
| Google Ads | OAuth refresh token | … | 180d | … | Head of Performance |
| LinkedIn Ads | … | … | 180d | … | Head of Performance |
| Meta Ads | … | … | 180d | … | Head of Performance |
| HubSpot | API key | … | 90d | … | Head of Automation |
| Webflow | API token | … | 180d | … | Head of Content |
| Slack | Webhook | … | on incident | … | Head of Automation |

## Rules
1. No secret in git — enforced by `/.claude/settings.json` pre-commit hook.
2. Access least-privilege; scoped per agent where possible.
3. Rotation tracked; overdue rotations block weekly tick with a HITL.
4. Revoked secrets logged in `/ledger-events/` with timestamp + reason.
