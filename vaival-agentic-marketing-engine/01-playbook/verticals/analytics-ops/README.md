---
name: Marketing Analytics & Operations Vertical
owner_tier: department-head
status: active
phase: 2
playbook_source: §14.1–§14.4
---

# Marketing Analytics & Operations Vertical

## Charter
Analytics & Ops is the intelligence and infrastructure layer of the department (§14.1). It exists to ensure every marketing decision is backed by accurate data and that the systems, integrations, and tooling powering the department work correctly. At mid-size, this function is lean but critical — without it the department cannot prove commercial value or know where to invest next.

## Team Roles + Tier (§14.2)
| Role | Tier | Headcount |
|---|---|---|
| Marketing Ops Manager | Tier 2 (Vertical Lead) | 1 |
| Marketing Data Analyst | Tier 3 | 1 |
| Marketing Automation Specialist | Tier 3 | 0.5–1 |

Department Head: `head-of-analytics`.

## KPIs (§14.4)
| KPI | Standard | Cadence |
|---|---|---|
| Dashboard uptime / data freshness | 100% within SLA | weekly |
| Attribution coverage | >90% MQLs with attributed source | monthly |
| UTM compliance rate | 100% on active paid campaigns | weekly |
| CRM data completeness | >85% MQL records fully populated | monthly |
| Tool utilization rate | >75% licensed seats actively used | quarterly |
| Report delivery SLA | 100% on time | monthly |

## Weekly Cadence
- UTM compliance audit on active campaigns (§14.3 C).
- Channel performance dashboard refresh + share with Vertical Leads.
- KPI snapshot pipeline run (Mon 09:00) — owns it end-to-end.
- Tracking-tag sanity check (any failed pixel firings).
- Budget tracker reconciliation with Finance.

## Monthly Cadence
- Attribution reconciliation — cross-reference GA4, CRM, ad platforms; investigate >10% discrepancies.
- CRM data-quality scan (dedupe, missing fields, lifecycle accuracy).
- Pixel + tag audit — remove deprecated, validate fires.
- Marketing attribution report → Head of Marketing.
- Executive marketing dashboard publish (auto-refresh weekly, formal share monthly).
- MQL funnel report with Sales.

## Quarterly / Annual Cadence
- Tool-access review (remove stale users).
- Annual martech audit (Q1) — full stack ROI, utilization, redundancy, renewals (§14.3 C).
- KPI taxonomy review + UTM-taxonomy refresh.
- Data-warehouse schema review (BigQuery if used).

## Key Workflows (linked)
- `04-workflows/kpi-snapshot-pipeline.workflow.md` (Mon 09:00 ingestion).
- `04-workflows/monthly-reporting.workflow.md`.
- `04-workflows/digest-delivery.workflow.md` (publishes weekly digest).
- `04-workflows/learning-loop.workflow.md` (telemetry → recursive optimizer).

## Tools / Connectors (linked, §14.3)
- `06-connectors/analytics/ga4.connector.md` (primary attribution).
- `06-connectors/analytics/google-tag-manager.connector.md`.
- `06-connectors/analytics/looker-studio.connector.md` (dashboards).
- `06-connectors/analytics/microsoft-clarity.connector.md`, `hotjar.connector.md` (UX).
- `06-connectors/analytics/segment.connector.md` (CDP).
- `06-connectors/analytics/bigquery.connector.md` (warehouse for KPI pipeline).
- `06-connectors/email-crm/hubspot-crm.connector.md` (attribution + lifecycle source).
- `06-connectors/ops-collaboration/google-sheets.connector.md` (budget tracker).

## Policies + Thresholds (§14.3)
- **Primary attribution model**: GA4 Data-Driven Attribution; supplemental first-touch / last-touch in CRM for Sales reporting.
- **Dedicated attribution platform** (Triple Whale etc.) optional unless ad spend >$50k/mo.
- **UTM taxonomy**: published, version-controlled, audited weekly. Non-compliant UTM = blocking issue for the campaign.
- **CRM data hygiene**: dedupe + field audit monthly; lifecycle-stage accuracy required.
- **Discrepancy threshold**: cross-platform variance >10% on attributed conversions triggers reconciliation; pause optimization actions in affected channel until resolved.
- **Tool access**: least-privilege, reviewed quarterly; departed users removed within 1 business day.
- **Data privacy**: PII never in dashboards; aggregate only; GDPR/CCPA region-handling configured in GA4.

## Refusal / Escalation Triggers
- Custom-event implementation requests that bypass GTM governance → refuse, route through GTM workflow.
- Ad-hoc dashboard builds outside the canonical 7 reports → HITL Head of Analytics.
- Vendor procurement (>$10k/yr) → HITL Head of Marketing + Finance.
- KPI definition changes mid-quarter → HITL CMO; freeze until quarterly review.
- Data-warehouse schema migrations → HITL with rollback plan + SOX/audit notification.

## Output Artifacts Produced
- Weekly KPI snapshot (canonical input to digest).
- Channel + paid + SEO + email + MQL-funnel dashboards (Looker Studio).
- Monthly attribution report.
- UTM compliance audit logs.
- Annual martech audit report.
- Telemetry feed into ledger-events for learning loop.

## Rubrics Applied
- `rubrics/weekly-kpi-snapshot.yaml`, `rubrics/monthly-exec.yaml`.
- `rubrics/attribution.yaml`, `rubrics/utm.yaml`.
- `rubrics/agent.yaml` + `rubrics/skill.yaml` for any cross-vertical instrumentation.
