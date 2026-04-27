---
name: Paid Media & PPC Vertical
owner_tier: department-head
status: active
phase: 2
playbook_source: §10.1–§10.6
---

# Paid Media & PPC Vertical

## Charter
The demand-capture engine. Converts existing market intent into leads efficiently and provides the fastest-feedback loop of any channel — results visible in days, not months (§10.1). For mid-size SaaS, the vertical focuses narrowly on the channels that produce the lowest CAC for the target buyer: typically Google Search and LinkedIn, with Meta for retargeting/brand. Channels are mastered sequentially, not run in parallel under thin budget (§10.2 channel priority).

## Team Roles + Tier (§10.2)
| Role | Tier | Headcount |
|---|---|---|
| Paid Media Manager | Tier 2 (Vertical Lead) | 1 |
| Paid Media Specialist | Tier 3 | 1–2 |
| CRO / Landing Page (shared with Web Dev) | Tier 3 | 1 |

Department Head: `head-of-performance` (Paid).

## KPIs (§10.5)
| KPI | Benchmark / Target | Cadence |
|---|---|---|
| Google Search CTR (non-brand) | 3–6% | weekly |
| Cost per MQL (Paid) | per OKR | weekly |
| Blended ROAS | 3x–7x | monthly |
| LinkedIn CPL | $50–$200 | weekly |
| Landing-Page CVR | ≥3% (paid) | weekly |
| Quality Score (Google) | average ≥7 | weekly |
| MQL → SQL rate (Paid) | 20–35% | monthly |
| Budget utilization | 95–105% of plan | weekly |

## Weekly Cadence (§10.4 Workflow B)
- Pull spend, clicks, CTR, CPL, conversions per campaign.
- Pause campaigns running CPL >2× target for 7+ days.
- Search-term review (Google): converters → exact match; junk → negatives.
- Audience reallocation: shift to top performers, throttle laggards.
- Creative rotation: identify lowest-CTR ads, queue replacements; ≥2 variants live always.
- Budget pacing review.
- Document findings in campaign log; share summary to Head of Marketing.

## Monthly Cadence
- ROAS / CAC reconciliation against blended target.
- Creative library review — winners promoted, losers retired.
- LP CRO test pipeline review with Web Dev.
- Cross-channel attribution check with Analytics-Ops.
- Quarterly: channel-mix review, budget rebase, audience refresh.

## Key Workflows (linked)
- `04-workflows/campaign-launch.workflow.md` (uses §10.4 Workflow A 8-step checklist).
- `04-workflows/paid-campaign-optimize.workflow.md` (weekly optimization).
- `04-workflows/daily-stop-loss.workflow.md` (auto-pause / reallocate / freq-refresh / HITL).
- `04-workflows/kpi-snapshot-pipeline.workflow.md` (KPI ingest).

## Tools / Connectors (linked, §10.3)
- `06-connectors/paid/google-ads.connector.md`
- `06-connectors/paid/meta-business-suite.connector.md`
- `06-connectors/paid/linkedin-campaign-manager.connector.md`
- `06-connectors/paid/microsoft-ads.connector.md`
- `06-connectors/analytics/google-tag-manager.connector.md`
- `06-connectors/analytics/ga4.connector.md`
- `06-connectors/email-crm/hubspot-crm.connector.md`
- `06-connectors/analytics/microsoft-clarity.connector.md`, `hotjar.connector.md`
- `06-connectors/analytics/looker-studio.connector.md`

## Policies + Thresholds
- **Campaign launch checklist mandatory** (§10.4 Workflow A): no live ads without approved brief, QA'd LP, GTM verified, UTMs applied, brand/legal review, audience exclusions (existing customers excluded from prospecting), dual budget caps.
- **Stop-loss**: ROAS <1 for 14 consecutive days → auto-pause; CAC >1.5× target for 21 days → reallocate; ad frequency >3.5 → creative refresh; spend >$1k/day on a single campaign → HITL gate before scale.
- **HITL on $3k+ spend launches** (CLAUDE.md Phase 4 autonomy bounds).
- **UTM compliance**: zero ads ship without UTMs from approved taxonomy.
- **Prospecting vs retargeting separated**: distinct campaigns, audiences, creative, bid strategies.
- **Always ≥2 creative variants** per ad set (§10.6).
- **No optimization for impressions/clicks** alone — CPL + downstream MQL quality only.

## Refusal / Escalation Triggers
- Targeting that touches protected classes / sensitive ad categories → hard refuse.
- Misleading or unsubstantiated claims in ad copy → refuse, escalate to brand/legal.
- Budget reallocation >20% across campaigns → HITL.
- Net-new platform onboarding (e.g., adding TikTok Ads) → HITL Head of Marketing + CMO.
- Tracking discrepancies >10% between platform and GA4 → escalate to Analytics-Ops; pause optimization actions until reconciled.

## Output Artifacts Produced
- Campaign briefs, creative briefs, ad-copy sets, audience definitions.
- Daily / weekly performance reports + campaign log entries.
- Stop-loss event records (ledger-events).
- Monthly Paid Media section of the executive dashboard.
- LP test hypotheses + readouts (joint with Web Dev / CRO).

## Rubrics Applied
- `rubrics/campaign-brief.yaml`, `rubrics/ad-copy.yaml`, `rubrics/landing-page.yaml`.
- `rubrics/utm.yaml` (all live UTMs).
- `rubrics/attribution.yaml` (monthly reconciliation).
- `rubrics/weekly-kpi-snapshot.yaml`, `rubrics/monthly-exec.yaml`.
