# Client Ledger — `fixture_devtools_saas` (Loopgate)

> FIXTURE CLIENT. Archetype representing a real segment; not a real company. Used to dogfood the system.

## 1. Company
- **Name:** Loopgate
- **Category:** Feature-flag + experimentation platform for engineering teams
- **Stage:** Series B, closed 2025-Q4 ($12M, led by Fictive Ventures)
- **ARR:** $2.1M (2026-04), growth 14% MoM trailing 6
- **Team:** 34 FTE total; Marketing: 8 (VP, 2 demand-gen, 1 content, 1 SEO, 1 PMM, 1 designer, 1 ops)
- **HQ:** Remote-first; majority US/EU; 2 APAC contractors
- **Product:** SaaS (self-serve + sales-assisted for enterprise tier)
- **Pricing:** Free (up to 3 users), Team ($25/user/mo), Business ($99/user/mo), Enterprise (custom, min $50k ACV)

## 2. Primary Business Goal (SMART)
- **Goal:** Grow ARR from $2.1M → $4.0M by 2026-12-31 (90% annual growth).
- **Timeframe:** 2026-04-23 → 2026-12-31 (~8 months).
- **Accountable operator:** VP Marketing (interim CMO).
- **Board commitment:** Series B memo committed $3.5M ARR by EoY; $4.0M = stretch.

## 3. Current State (with sources)
- **Funnel (last 4w avg):**
  - Sessions / mo: 82k (GA4 property 427193, view "Marketing Site")
  - Signups / mo: 1,410 (product DB, `users.created_at`)
  - Activated (created ≥1 flag in 7d): 520 (36.9%) — product telemetry
  - Team-plan conversions / mo: 84 (Stripe)
  - Enterprise opportunities / mo: 11 (HubSpot deal stage = "Qualified")
  - Closed-won enterprise / mo: 2 (avg ACV $68k) + Team SaaS MRR $31k net new
- **Spend / mo:** $62k (Google $22k, LinkedIn $18k, Content/SEO $12k, Events $6k, Tools $4k)
- **CAC blended:** ~$720 for Team, ~$28k for Enterprise
- **Tools:**
  - CRM: HubSpot (access granted)
  - Analytics: GA4 + Amplitude (granted) + internal BigQuery (pending)
  - CMS: Webflow (granted)
  - ESP: Customer.io (granted)
  - Ad platforms: Google Ads (granted), LinkedIn Ads (granted), Meta (not running)
  - Chat: Intercom (granted)
  - Support: Zendesk (read-only)
  - Product telemetry: Segment → Amplitude + Snowflake (pending BigQuery sync)

## 4. Constraints
- **Budget:** $62k/mo baseline; up to $95k/mo if LTV:CAC proves >3× on incremental.
- **Headcount:** no new hires until 2026-Q3.
- **Legal/compliance:** SOC2 Type II in progress; no customer data claims ("our AI analyzes your data") without review.
- **Brand guardrails:** no FUD marketing vs competitors; no "10× better" claims without proof.
- **Geography:** primary US/EU; no APAC paid until localized support.

## 5. ICP Seed
Hypothesis: **mid-market engineering orgs (50–500 engineers), cloud-native stack, with a Platform/DevEx team that owns developer velocity metrics.** Lookalikes: three named won logos in the last 6 months — a fintech (SOC2-driven), a marketplace (experimentation velocity), a digital-health startup (compliance + audit trail).

## 6. Competitor Seed
LaunchDarkly (enterprise, expensive), Statsig (experimentation-led, free tier), Split.io (enterprise, older), Flagsmith (open-source, low price), Unleash (OSS self-host), GrowthBook (stats-strong, lean team). Status quo: homegrown flag tables in Postgres.

## 7. Cadence & Governance
- **Operator:** VP Marketing (Jess)
- **Approvers:** CEO for >$20k spend shifts, Legal for regulated-industry claims, CFO for >10% budget reallocation.
- **Digest delivery:** Mondays 09:00 ET to #marketing-leadership Slack + email summary to CEO.
- **HITL thresholds:** budget reallocation >$10k, any legal/brand-sensitive claim, experiment decision impacting pricing page, spend >$1,000/day on any single campaign.

## 8. Open Questions
| Unknown | Owner | Due | Status |
|---|---|---|---|
| SOC2 Type II audit completion date | CTO | 2026-05-15 | pending |
| BigQuery access for attribution modeling | Data Eng | 2026-05-01 | in progress |
| PMM capacity for 3 battlecards | VP Marketing | 2026-04-30 | pending |
| Localization decision for APAC expansion | CEO | 2026-09-01 | deferred |
| Whether to launch free-tier uplift test in Q2 or Q3 | VP Product + VP Marketing | 2026-05-10 | pending |

## 9. Secrets Pointer
See `secrets.pointer.md`. No raw credentials in this file.

## 10. Change Log
| Date | Change | Owner | Event ref |
|---|---|---|---|
| 2026-04-23 | Ledger initialized by onboarding skill | orchestrator | `ledger-events/2026-04-23-onboarding.jsonl` |

## Rubric Evaluation (`/rubrics/client-ledger.yaml`)
| Criterion | Score | Justification |
|---|---|---|
| company_basics | 10 | All fields populated with sources |
| goal_specificity | 10 | SMART: ARR $2.1M→$4.0M by 2026-12-31, accountable operator named |
| current_state_honest | 10 | Funnel, spend, CAC, tools each with data source |
| constraints_captured | 9 | Budget, HC, legal, brand, geo — all stated |
| stack_inventory | 10 | 11 tools with access state |
| icp_seed | 9 | Hypothesis + 3 lookalike won logos |
| competitor_seed | 9 | 6 named competitors + status-quo alt |
| cadence_owners | 10 | Operator, approvers, HITL thresholds, digest channel/day |
| open_questions | 10 | 5 unknowns with owner + due date |
| secrets_pointer | 10 | Pointer-only, no raw secrets |
**Weighted total: 96/100. PASS.**
