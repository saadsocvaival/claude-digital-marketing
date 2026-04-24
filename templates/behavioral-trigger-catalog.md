# Behavioral Trigger Catalog — {Client}

**Purpose:** Named, versioned, reusable triggers. Every lifecycle program, expansion campaign, or churn-save references a trigger by ID.

| ID | Stage | Event definition (precise) | Window | Segment filter | Cooldown | Action | Owner | Version |
|---|---|---|---|---|---|---|---|---|
| T-001 | New | `signup.completed` without `aha.fired` | 24h | all | 48h | onboarding email 1 | Automation | v1 |
| T-002 | New | `signup.completed` without `aha.fired` | 72h | ICP-A | 5d | AE-personal email | Sales | v1 |
| T-003 | Activated | `aha.fired` count =1, no session in 5d | 5d | all | 7d | re-engage push+email | Automation | v1 |
| T-004 | Habit | `usage.events` >80% of plan-cap over rolling 7d | 7d | plan∈{Free,Starter} | 14d | upgrade banner + email | Automation + CRO | v1 |
| T-005 | Habit | team adds ≥3 new editors in 30d | 30d | plan∈{Pro,Business} | 60d | expansion AE outreach | Motion-Retention | v1 |
| T-006 | Paid | flag-creation 40% below cohort p50 over 30d | 30d | Paid | 90d | CS alert + usage-dip email | Automation + CS | v1 |
| T-007 | At-Risk | Sev-1 ticket open >4h | 4h | Enterprise | 24h | exec alert | Ops | v1 |
| T-008 | At-Risk | login frequency down >60% MoM | 30d | Paid | 60d | re-engagement nurture (3-touch) | Automation | v1 |
| T-009 | Paid | NPS ≥9 + tenure ≥90d | 180d | Paid | 365d | advocacy invite | Brand | v1 |
| T-010 | Churned | 60d post-cancel | one-shot at d60 | — | 180d | win-back campaign | Automation | v1 |
| T-011 | Lead | visits `/pricing` ≥3× in 14d without signup | 14d | un-signed-up | 30d | retargeting ad set + CTA-email if email known | Performance + Auto | v1 |
| T-012 | Habit | two workspaces created by same org-domain | once per domain | all | — | multi-workspace consolidation pitch | Sales | v1 |

## Rules of the catalog
1. **IDs are immutable.** Never reuse after deprecation.
2. **Versioning:** any change to event definition, window, or cooldown → new version (T-001-v2). Old version retained for historical analysis.
3. **Cooldown required.** No user hit by same trigger more than once inside cooldown.
4. **Suppression.** Respect global suppression rules from `lifecycle-map.md`.
5. **Instrumentation contract.** Every trigger firing writes `{trigger_id, user_id, account_id, fired_at, variant}` to the event ledger.
6. **Holdout contract.** 10% random holdout per trigger ID, assigned at user-first-eligible, persistent.

## Retirement criteria
- Any trigger with <100 fires in 90 days → review for removal.
- Any trigger with no measurable downstream lift over holdout in 2 consecutive quarters → retire.
