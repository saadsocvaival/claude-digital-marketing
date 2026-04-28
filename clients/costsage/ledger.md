---
client_id: costsage
status: pending-onboarding
created_at: 2026-04-27
operator: TBD
secrets_in_vault: false
---

# Client Ledger — costsage

> Living source of truth. Onboarding output lands here. Updated by weekly-tick. Append-only event log in `/ledger-events/`.

> Status `pending-onboarding` — must run `04-workflows/client-onboarding.workflow.md` and `04-workflows/secrets-vault-setup.workflow.md` before flipping to `active`.

> Rubric: `/rubrics/client-ledger.yaml`.

## 1. Company
- Name: **CostSage**
- Domain: **costsage.ai**
- Stage / ARR / HC: TBD (intake)
- HQ / geos served: TBD
- Product(s) + pricing model: AI cost optimization SaaS — pricing model TBD
- CMS: **WordPress** (auth: Application Password — see `06-connectors/web-dev/wordpress-application-password.connector.md`)

## 2. Primary Business Goal (SMART)
- Goal: TBD (intake — set during 12-question onboarding)
- Timeframe: TBD
- Accountable operator: TBD

## 3. Current State (with sources)
- Funnel metrics snapshot: TBD (pull from GA4 + HubSpot or chosen CRM at activation)
- Marketing budget: TBD
- Team: TBD
- Tools: see `secrets.pointer.md` (GA4, GSC, GTM, Semrush, Ahrefs, Screaming Frog, Surfer, ATP, Trello, ChatGPT, Claude, Gemini, Perplexity, Copilot, WordPress)

## 4. Constraints
TBD (budget, headcount, legal/compliance, brand guardrails, geography, language).

## 5. ICP Seed
- Vertical (inferred): teams running AI / LLM workloads on cloud infra who need to track and reduce inference / training / API spend. Confirm at intake.
- Lookalike won customers: TBD.

## 6. Competitor Seed
TBD — to be set during intake. Likely categories: cloud cost / FinOps tools, LLM gateway / observability vendors, dedicated AI cost platforms.

## 7. Cadence & Governance
- Operator: TBD
- Approvers: TBD
- Digest delivery: {channel} every {day/time} — TBD
- HITL thresholds: budget reallocation >20%, legal/brand claims, spend >$1k/day on a single campaign, audience sends >100k.

## 8. Open Questions
| Unknown | Owner | Due | Status |
|---|---|---|---|
| ARR + HC + funding stage | operator | onboarding | open |
| Primary NSM choice (e.g. self-serve sign-ups vs sales pipeline) | operator + CMO | onboarding | open |
| ESP choice (HubSpot vs SendGrid vs Resend vs Mailgun) | operator | onboarding | open |
| Ad-platform mix (Google Search / LinkedIn / Microsoft Ads) | Head of Performance | onboarding | open |
| Trello board structure for editorial calendar | Head of Content | onboarding | open |

## 9. Secrets Pointer
See `secrets.pointer.md`. **No raw credentials** in this file — ever. Cleartext credentials supplied during intake must be migrated via `04-workflows/secrets-vault-setup.workflow.md` before status flips to `active`.

## 10. Change Log
| Date | Change | Owner | Event ref |
|---|---|---|---|
| 2026-04-27 | Client scaffolded from `_template/`; status set to `pending-onboarding`. | Gap-fill PR | `ledger-events/0001-scaffolded.md` (TBD) |
