---
name: Email & CRM Marketing Vertical
owner_tier: department-head
status: active
phase: 2
playbook_source: §13.1–§13.6
---

# Email & CRM Marketing Vertical

## Charter
Email and CRM is the highest-converting owned channel in SaaS. Unlike paid or social where reach depends on ongoing spend, the email list is a company-owned asset that appreciates over time (§13.1). At mid-size the priority is: (a) clean, well-segmented database, (b) reliable lifecycle automation, (c) MQL→SQL conversion at a healthy rate.

## Team Roles + Tier (§13.2)
| Role | Tier | Headcount |
|---|---|---|
| CRM & Email Manager | Tier 2 (Vertical Lead) | 1 |
| Email Marketing Specialist | Tier 3 | 1–2 |
| Marketing Automation Specialist | Tier 3 | 1 |

Department Head: `head-of-automation` (Email + CRM + Lifecycle).

## KPIs (§13.6)
| KPI | Benchmark | Cadence |
|---|---|---|
| Email open rate | 35–50% | weekly |
| Email CTR | 2.5–5% | weekly |
| Unsubscribe rate | <0.25% | per campaign |
| Email-sourced MQLs | per OKR | monthly |
| MQL acceptance rate (Sales) | >70% | monthly |
| Trial → paid conversion | 15–25% | monthly |
| List active rate (90-day) | >65% | monthly |
| Database net growth | per OKR | monthly |

## Lifecycle Stages (§13.3)
New Lead → MQL Nurture → Trial User → New Customer → Active Customer → At-Risk → Lapsed/Win-Back. Each stage has defined entry trigger, primary goal, and key flows (welcome, drip, activation, onboarding, milestones, NPS, re-engagement, win-back, sunset).

## Weekly Cadence
- Campaign queue review + 48-hour post-send performance read on prior week's sends.
- Deliverability health (Gmail/Outlook/Apple Mail render, spam score, bounce trends).
- List hygiene: hard bounces removed within 24h.
- A/B test outcomes captured into the test library.

## Monthly Cadence
- Lead-scoring calibration review with Sales (§13.5 — MQL threshold = 50; reviewed quarterly).
- Lifecycle-flow audit: which automations are misfiring or stale.
- Database segmentation review; suppression-list audit.
- MQL handoff retro with Sales (acceptance rate, rejection reasons).
- Quarterly: full automation map review; dead-flow retirement.

## Key Workflows (linked)
- `04-workflows/lead-nurture.workflow.md` (lifecycle nurture flows).
- `04-workflows/campaign-launch.workflow.md` (one-off email sends inside campaigns).
- Email Campaign Build & Send (§13.4 Workflow A) — owned SOP, 9 steps from brief → 48-hour readout.
- `04-workflows/digest-delivery.workflow.md` (transactional email delivery of weekly digest).

## Tools / Connectors (linked)
- `06-connectors/email-crm/hubspot-marketing-hub.connector.md` (primary automation).
- `06-connectors/email-crm/hubspot-crm.connector.md` (CRM source of truth).
- `06-connectors/email-crm/mailchimp.connector.md`, `klaviyo.connector.md` (alt ESPs).
- `06-connectors/email-crm/sendgrid.connector.md`, `resend.connector.md`, `mailgun.connector.md` (transactional).
- `06-connectors/email-crm/mail-tester.connector.md` (spam-score gate).
- `06-connectors/analytics/ga4.connector.md` (downstream attribution).

## Policies + Thresholds (§13.4 Non-Negotiables)
- **Unsubscribe** present + functional, one-click, in every email — CAN-SPAM/GDPR.
- **Physical address** in every footer — CAN-SPAM.
- **From-name consistency** — never change without deliverability test first.
- **Subject line**: 40–55 chars, no ALL CAPS, no deception.
- **Hard bounces** removed within 24h; unsubscribers within 72h (GDPR) / 10 days (CAN-SPAM).
- **Minimum segment size**: 50 contacts.
- **Spam score**: ≥9/10 on mail-tester before send.
- **A/B test window**: ≥4h, two subject-line variants minimum, winner auto-sends.
- **MQL threshold**: 50 points (§13.5); changes require Sales + CRM Manager + Head of Marketing sign-off.

## Refusal / Escalation Triggers
- Send to >100k recipients in single blast → HITL Head of Marketing.
- Promotional send to existing customers in a prospecting campaign → refuse (suppression mandatory).
- Lead-magnet delivery without confirmed double opt-in in EU/CA jurisdictions → refuse (GDPR).
- New domain / subdomain warm-up not complete → refuse high-volume send.
- Sales-rejected MQL rate >30% for 4 consecutive weeks → escalate to scoring recalibration HITL.
- Re-permission / re-consent campaigns on dormant lists → HITL legal review.

## Output Artifacts Produced
- Email briefs, copy, A/B variants, HTML templates, segment definitions.
- Lifecycle flow diagrams + automation specs.
- Per-campaign 48-hour reports + monthly aggregate.
- Lead-scoring model documentation + change log.
- Deliverability health snapshot (weekly).

## Rubrics Applied
- `rubrics/email.yaml`, `rubrics/email-sequence.yaml`.
- `rubrics/lead-scoring.yaml`.
- `rubrics/utm.yaml` (every link).
- `rubrics/weekly-kpi-snapshot.yaml`, `rubrics/monthly-exec.yaml`.
