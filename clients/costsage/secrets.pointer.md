# Secrets Pointer — costsage

> **WARNING — READ FIRST**: Sheet creds (operator-supplied spreadsheet listing platform passwords) MUST be migrated to a secrets vault before this client flips to `status: active`. See `vaival-agentic-marketing-engine/04-workflows/secrets-vault-setup.workflow.md`. NO raw passwords, tokens, or API keys belong in this file or anywhere in this repo. The `vault-path` column is a pointer only.

> Vault tooling: choose one per operator preference — 1Password CLI (`op://`) OR Doppler (`doppler://`) OR HashiCorp Vault (`vault://`). The placeholders below use `vault://costsage/...` as a tool-agnostic prefix; replace with the chosen tool's URI scheme at provisioning.

## Pointer manifest

| Service | Purpose | auth_method | Vault path (placeholder) | Rotation cadence | Last rotated | Owner |
|---|---|---|---|---|---|---|
| GA4 (Google Analytics 4) | Web + product analytics | oauth | `vault://costsage/ga4/oauth-refresh-token` | 90d | 2026-04-27 web-login provisioned; OAuth grant pending | Head of Analytics |
| GSC (Google Search Console) | SEO / index health | oauth | `vault://costsage/gsc/oauth-refresh-token` | 90d | 2026-04-27 web-login provisioned; OAuth grant pending | Head of Search Visibility |
| GTM (Google Tag Manager) | Tag + pixel mgmt | oauth | `vault://costsage/gtm/oauth-refresh-token` | 90d | 2026-04-27 web-login provisioned; OAuth grant pending | Head of Analytics |
| Semrush | Keyword + rank + competitors | api-key | `vault://costsage/semrush/api-key` | 180d | 2026-04-27 web-login provisioned; API-key extraction pending | Head of Search Visibility |
| Ahrefs | Backlinks + DR | api-key | `vault://costsage/ahrefs/api-key` | 180d | 2026-04-27 web-login provisioned; API-key extraction pending | Head of Search Visibility |
| Screaming Frog | Site crawl (license) | license | `vault://costsage/screaming-frog/license-key` | annual | 2026-04-27 web-login provisioned; CLI license-key extraction pending | Head of Search Visibility |
| Surfer SEO | Content brief + semantic | api-key | `vault://costsage/surfer/api-key` | 180d | 2026-04-27 web-login provisioned; API-key extraction pending | Head of Content |
| AnswerThePublic (ATP) | Question-format query discovery | api-key | `vault://costsage/atp/api-key` | 180d | 2026-04-27 web-login provisioned; API-key extraction pending | Head of Search Visibility |
| Google Rich Results Test | Schema validation | public | (public endpoint; no auth) | n/a | 2026-04-27 in use | Head of Search Visibility |
| Google Alerts | Brand monitoring | sso | (web-only — no API) | n/a | 2026-04-27 web-login provisioned | Head of Search Visibility |
| Trello | Editorial calendar + sprint board | api-key | `vault://costsage/trello/api-key` + `vault://costsage/trello/token` | 180d | 2026-04-27 web-login provisioned; API-key extraction pending | Head of Content |
| ChatGPT (OpenAI) | GEO audit + research | api-key | `vault://costsage/openai/api-key` | 90d | 2026-04-27 web-login provisioned; API-key extraction pending | Head of Search Visibility |
| Claude (Anthropic) | GEO audit + content + agentic ops | api-key | `vault://costsage/anthropic/api-key` | 90d | 2026-04-27 web-login provisioned; API-key extraction pending | CMO |
| Gemini (Google) | GEO audit + research | api-key | `vault://costsage/gemini/api-key` | 90d | 2026-04-27 web-login provisioned; API-key extraction pending | Head of Search Visibility |
| Perplexity | GEO audit + research | api-key | `vault://costsage/perplexity/api-key` | 90d | 2026-04-27 web-login provisioned; API-key extraction pending | Head of Search Visibility |
| Copilot (Microsoft) | GEO audit | sso | `vault://costsage/copilot/sso-session-note` | per session | 2026-04-27 web-login provisioned | Head of Search Visibility |
| WordPress (costsage.ai CMS) | Page / post / media writes | basic+app-password | `vault://costsage/wordpress/admin-password` (rotate to per-agent app-password ASAP) | 90d | 2026-04-27 admin pw provisioned; rotate to app-password | Head of Web Experience |

> **Provisioning note (2026-04-27):** Operator delivered a credential bundle via Google Sheet ("Marketing Simulatory Credentials for Agentic Workflow Testing"). Per `SECURITY.md`, raw values are NOT in this repo. SaaS web-logins ≠ programmatic API access — for Semrush/Ahrefs/Surfer/ATP/Trello/OpenAI/Gemini/Perplexity an operator must (a) sign in, (b) generate an API key in Settings → API, (c) write the value to the vault path above. See `seo-geo-aeo/API-KEY-EXTRACTION-RUNBOOK.md` for per-platform 30-second walkthroughs. Google services (GA4/GSC/GTM) require a one-time OAuth grant flow.

## Migration runbook
1. Operator delivers the existing credential spreadsheet via secure channel — never to this repo.
2. Run `04-workflows/secrets-vault-setup.workflow.md`:
   - Inventory each row above with current location + expiry.
   - Provision in chosen vault tool under the path shown.
   - Verify per-platform read with least-privilege scope.
   - Revoke / sanitize the spreadsheet source.
3. Update the `Last rotated` column above with the migration date.
4. Append `secrets.vault.migrated` to `ledger-events/`.
5. Flip `clients/costsage/ledger.md` `secrets_in_vault: true` and `status: active`.

## Rules
1. No secret in git — enforced by `/.claude/settings.json` pre-commit hook + `SECURITY.md`.
2. Access least-privilege; per-agent app passwords for WordPress (see `06-connectors/web-dev/wordpress-application-password.connector.md`).
3. Rotation tracked; overdue rotations block the next weekly tick with an HITL.
4. Revoked secrets logged in `/ledger-events/` with timestamp + reason.
5. Cleartext credentials anywhere in this repo (sheet paste, test files, scratch notes) is a SEV incident — see `SECURITY.md`.
