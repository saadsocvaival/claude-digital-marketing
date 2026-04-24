# Lifecycle Map — {Client}

**Purpose:** Named behavioral triggers → audience → message → goal → measurement. Kills "email blast to everyone."

## 1. Lifecycle stages
| Stage | Entry criteria | Exit criteria | Primary goal |
|---|---|---|---|
| Lead | form fill / signup started | signup completed (→ New) OR 30d no action (→ Dormant) | complete signup |
| New | account created | aha-event (→ Activated) | reach aha within 7d |
| Activated | aha-event fired | habit formed (3+ sessions wk2) | form habit |
| Habit | engaged wk2 | upgrade (→ Paid) OR decay (→ At-Risk) | monetize |
| Paid | payment method / contract | expansion signal (→ Expansion) OR downgrade (→ At-Risk) | retain |
| Expansion | seat/usage growth | renewal / further expansion | grow ARR |
| At-Risk | decay signal or support escalation | re-engagement (→ back) OR churn | save |
| Churned | cancellation | win-back | win-back after 60d |

## 2. Trigger → message → goal table
| Stage | Trigger | Audience filter | Channel | Message core | CTA | KPI | Frequency cap |
|---|---|---|---|---|---|---|---|
| New | signup complete, aha not fired in 24h | all | email+in-app | "2 minutes to your first {aha-event}" | onboarding checklist | TTFV-p50 | 1/day, 3 max |
| New | aha not fired in 72h | ICP-A only | AE-sent email | persona-specific unlock | book 15-min | activation-assist | 1/week |
| Activated | 5 days no session | habit not formed | email+push | personalized usage recap | re-engage | wk2 retention | 1 |
| Habit | usage >80% plan cap | self-serve segment | in-app banner + email | upgrade path | upgrade CTA | plg→paid conv | 1 |
| Habit | team added 3+ editors in 30d | all | AE outreach | expansion pitch | book call | expansion $ | 1 |
| Paid | flag-creation 40% below cohort p50 over 30d | all | CS-alert + email | usage dip pattern | schedule check-in | GRR | 1/quarter |
| Paid | NPS ≥9 + 90d tenure | all | email | advocacy invite | review / reference | advocacy count | 1/year |
| At-Risk | support escalation unresolved 7d | Enterprise | exec outreach | personal save | save-call | logo retention | as-needed |
| Churned | 60d post-cancel | all | email | product improvements since | come back | win-back % | 1/quarter |

## 3. Audience taxonomy (reusable filters)
- **Segment:** SMB | Mid-Market | Enterprise | PLG-self-serve
- **Plan:** Free | Starter | Pro | Business | Enterprise
- **Role:** admin | editor | viewer | billing
- **Vertical:** {top-5 verticals}
- **ICP score:** A | B | C (from `lead-scoring.md`)
- **Engagement:** active | dormant | at-risk (last-30d session count)

## 4. Suppression rules
- Cap: 3 marketing emails/week, 1 sales email/week, unlimited transactional.
- Pause all marketing during active support ticket sev ≤2.
- No upgrade CTA within 7 days of downgrade.
- Time-zone aware send (no pre-8am / post-7pm local).

## 5. Experimentation (per program)
- Control group: 10% holdout on every lifecycle program — mandatory.
- Measured lift: program-on vs holdout over 60 days.
- Program retired if lift <2% on primary goal after 90 days.

## 6. Instrumentation
- [ ] Every trigger is a named event in the warehouse
- [ ] Every message has a `program_id` + `variant_id`
- [ ] Holdout group respected at the trigger level, not message level
- [ ] Downstream outcomes joined back to program via user-id

## 7. Ownership
- Map owner: Head of Automation
- Program owners: named per row
- Quarterly review: Motion leads (acquisition/activation/retention) per their stages
