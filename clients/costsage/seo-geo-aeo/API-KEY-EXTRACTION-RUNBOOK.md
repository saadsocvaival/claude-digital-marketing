---
client_id: costsage
artifact: api-key-extraction-runbook
date: 2026-04-27
audience: operator
purpose: unblock programmatic Sprint-2 audits by extracting API keys from each platform's web dashboard and writing them to the vault
---

# API-Key Extraction Runbook — Sprint-2 unblocker

> **Why this exists:** the credential bundle delivered on 2026-04-27 contains web-login pairs (email + password). SaaS web logins ≠ programmatic API access. Each platform requires the operator to log in once, navigate to its API/Settings page, generate a key, and write it to the vault path in `secrets.pointer.md`. Total time: ~30 min for all 8 platforms. Each step is independent and fail-safe.

> **Vault hygiene:** raw values **never** land in this repo. Write to `vault://costsage/<service>/api-key` via your chosen tool (1Password CLI, Doppler, or HashiCorp Vault). The repo only holds the pointer.

---

## 1. Semrush — `vault://costsage/semrush/api-key`
1. Sign in at https://www.semrush.com/ (operator credentials).
2. Top-right avatar → **Subscription info** → **API**.
3. Click **"Generate API key"**. (If the plan tier doesn't include API access, note that and skip — Sprint-2 will fall back to manual exports.)
4. Copy → paste into vault path above.
5. Test: `curl "https://api.semrush.com/?type=domain_overview&key=<KEY>&domain=costsage.ai"` should return CSV.

## 2. Ahrefs — `vault://costsage/ahrefs/api-key`
1. Sign in at https://ahrefs.com/ → **Account → Profile → API access**.
2. Generate token. Note the rate-limit and the units/credits remaining.
3. Vault.
4. Test: `curl -H "Authorization: Bearer <KEY>" "https://api.ahrefs.com/v3/site-explorer/overview?target=costsage.ai&mode=domain"`.

## 3. Surfer SEO — `vault://costsage/surfer/api-key`
1. Sign in at https://surferseo.com/.
2. **Settings → Integrations → API** (Surfer's API requires an Enterprise plan; if 404 the option, mark unavailable).
3. Generate key, vault, test.

## 4. AnswerThePublic — `vault://costsage/atp/api-key`
1. Sign in at https://answerthepublic.com/.
2. **Settings → API**. ATP API is available on Pro/Expert tiers only.
3. If unavailable: ATP can be driven by CSV export — Sprint-2 will use the export pathway.

## 5. Trello — `vault://costsage/trello/api-key` + `vault://costsage/trello/token`
1. Sign in at https://trello.com/.
2. Visit https://trello.com/app-key → copy the API key.
3. Click "Token" link on the same page → authorise → copy the token.
4. Vault both values.
5. Test: `curl "https://api.trello.com/1/members/me?key=<KEY>&token=<TOKEN>"`.

## 6. ChatGPT (OpenAI) — `vault://costsage/openai/api-key`
1. Sign in at https://platform.openai.com/.
2. **API keys** → **Create new secret key** → name it `costsage-marketing-2026`.
3. Vault. (Set a usage limit at **Limits** to bound spend.)
4. Test: `curl https://api.openai.com/v1/models -H "Authorization: Bearer <KEY>"`.

## 7. Gemini — `vault://costsage/gemini/api-key`
1. Sign in at https://aistudio.google.com/.
2. **Get API key** → **Create API key in new project** (or pick existing).
3. Vault.
4. Test: `curl "https://generativelanguage.googleapis.com/v1/models?key=<KEY>"`.

## 8. Perplexity — `vault://costsage/perplexity/api-key`
1. Sign in at https://www.perplexity.ai/.
2. **Settings → API** → generate. (Pro tier required; if not provisioned, skip.)
3. Vault.
4. Test: `curl https://api.perplexity.ai/chat/completions -H "Authorization: Bearer <KEY>" -H "Content-Type: application/json" -d '{"model":"sonar","messages":[{"role":"user","content":"hi"}]}'`.

## 9. Google services (GA4 / GSC / GTM) — OAuth flow
1. Sign in at https://console.cloud.google.com/ (same operator email).
2. Create project `costsage-marketing` (or reuse).
3. **APIs & Services → Library** → enable: Google Analytics Data API, Search Console API, Tag Manager API.
4. **Credentials → Create credentials → OAuth client ID** → Web application; add redirect URI from your agent host.
5. Download client_id.json. Vault. The first programmatic call will trigger a one-time browser-grant flow.

## 10. Screaming Frog — local CLI license
1. Sign in at https://www.screamingfrog.co.uk/log-in/ → **My account** → license key.
2. Vault as `vault://costsage/screaming-frog/license-key`.
3. Install Screaming Frog SEO Spider on the audit host; license via `screamingfrogseospider --crawl-config` first run, paste key.
4. Daily crawl: `screamingfrogseospider --crawl https://costsage.ai/ --headless --save-crawl --output-folder /var/lib/sf-crawls/`.

## 11. Copilot (Microsoft) — SSO only, no API
Web-only. Web login provisioned; programmatic access requires Azure AD app registration → not in scope until Microsoft tenancy is set up.

## 12. WordPress — rotate from admin password to per-agent app-password
1. Sign in at https://costsage.ai/wp-admin/ with operator creds.
2. **Users → Profile → Application Passwords** → create one named `costsage-marketing-claude` → copy the 24-char value.
3. Vault as `vault://costsage/wordpress/app-password/marketing-claude`.
4. Test: `curl -u 'tayyabnaqvi:<APP-PASSWORD>' https://costsage.ai/wp-json/wp/v2/users/me`.
5. The original admin password should NOT be used by any agent — rotate by creating per-agent app passwords for each automation.

---

## After running this runbook

Append a single event to `clients/costsage/ledger-events/`:
```json
{"ts":"2026-04-27T<HH:MM:SS>Z","event":"secrets.vault.populated","platforms":["semrush","ahrefs","surfer","atp","trello","openai","gemini","perplexity","ga4","gsc","gtm","screaming-frog","wordpress"],"actor":"operator"}
```

Then update `clients/costsage/ledger.md`: `secrets_in_vault: true`. This gates the flip from `pending-onboarding` → `active`.

Sprint-2 audits assume these keys are available. If a tier-locked platform (e.g., Surfer/ATP/Perplexity API) cannot be enabled, mark it explicitly in the manifest so the Sprint-2 plan can route around it.
