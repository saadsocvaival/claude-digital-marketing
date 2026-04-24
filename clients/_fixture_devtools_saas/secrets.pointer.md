# Secrets Pointer — Loopgate

| Service | Secret name | Vault location | Rotation | Last rotated | Owner |
|---|---|---|---|---|---|
| GA4 | Service account key | 1Password: Loopgate/GA4 | 90d | 2026-03-12 | Head of Analytics |
| Google Ads | OAuth refresh token | 1Password: Loopgate/GoogleAds | 180d | 2026-01-20 | Head of Performance |
| LinkedIn Ads | OAuth refresh token | 1Password: Loopgate/LinkedIn | 180d | 2026-02-02 | Head of Performance |
| HubSpot | Private App key | 1Password: Loopgate/HubSpot | 90d | 2026-03-18 | Head of Automation |
| Webflow | API token | 1Password: Loopgate/Webflow | 180d | 2026-02-14 | Head of Content |
| Customer.io | App + Track keys | 1Password: Loopgate/CustomerIO | 90d | 2026-03-10 | Head of Automation |
| Amplitude | Project API keys | 1Password: Loopgate/Amplitude | 180d | 2026-02-01 | Head of Analytics |
| Slack | Webhook (#marketing) | 1Password: Loopgate/SlackWebhook | on incident | 2026-03-22 | Head of Automation |

No raw secret lands in repo. Pre-commit secret-scan hook enforced via `.claude/settings.json`.
