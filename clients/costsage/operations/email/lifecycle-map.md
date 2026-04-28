# Lifecycle Map — CostSage

End-to-end email lifecycle from first signup through expansion, retention, and winback. Each node is a state; each edge is a trigger condition.

---

## ASCII state diagram

```
                          ┌──────────────────┐
                          │  Anonymous       │
                          │  visitor         │
                          └────────┬─────────┘
                                   │ submits trial signup
                                   ▼
                          ┌──────────────────┐
                          │  T0: Trial       │  ← entry point
                          │  Signed Up       │
                          └────────┬─────────┘
                                   │ D0 trigger
                                   ▼
                          ┌──────────────────┐
                          │  Onboarding      │
                          │  (Emails 1–7)    │ ◄── retry / nudge edges
                          └──────┬───────────┘
                                 │
        ┌────────────────────────┼─────────────────────────┐
        │ AWS not connected      │ Trial ended,            │ Trial converted
        │ by D7                  │ no conversion           │ to paid
        ▼                        ▼                         ▼
 ┌──────────────┐       ┌──────────────────┐     ┌──────────────────┐
 │ Setup-stalled│       │ Trial Lapsed     │     │ Activated        │
 │ branch       │       │ (offer ext.)     │     │ Customer         │
 └──────┬───────┘       └────────┬─────────┘     └────────┬─────────┘
        │ connects              │ extends                │ first PR merged
        ▼                       ▼                        │ within 14d
 (rejoin onboarding)     (rejoin onboarding D3)           ▼
                                │                ┌──────────────────┐
                                │ no extension   │ Engaged          │
                                ▼                │ Customer         │
                         ┌──────────────┐        └──────┬───────────┘
                         │ Cold Lead    │               │ usage growth
                         │ (drip x6mo)  │               ▼
                         └──────┬───────┘        ┌──────────────────┐
                                │                │ Expansion-Ready  │
                                ▼                └──────┬───────────┘
                         ┌──────────────┐               │ MRR ≥ 2x initial
                         │  Suppressed  │               ▼
                         │  / Removed   │        ┌──────────────────┐
                         └──────────────┘        │ Power Customer   │
                                                 └──────┬───────────┘
                                                        │ usage drop ≥40%, 30d
                                                        ▼
                                                 ┌──────────────────┐
                                                 │ At-Risk          │
                                                 └──────┬───────────┘
                                                        │ no recovery 30d
                                                        ▼
                                                 ┌──────────────────┐
                                                 │ Churned          │
                                                 └──────┬───────────┘
                                                        │ 90d dormant
                                                        ▼
                                                 ┌──────────────────┐
                                                 │ Winback (3 emails)│
                                                 └──────┬───────────┘
                                                        │ no response
                                                        ▼
                                                 ┌──────────────────┐
                                                 │ Suppressed       │
                                                 └──────────────────┘
```

---

## Nodes (16)

| # | Node | Definition |
|---|---|---|
| 1 | Anonymous Visitor | Unidentified site visitor |
| 2 | Trial Signed Up | Form submitted, account created |
| 3 | Onboarding | In 7-email sequence (D0–D14) |
| 4 | Setup-stalled | AWS account not connected by D7 |
| 5 | Trial Lapsed | D14 ended, no paid conversion |
| 6 | Activated Customer | Paid + AWS connected |
| 7 | Engaged Customer | First PR/ticket merged within 14d of activation |
| 8 | Expansion-Ready | Usage growth + advocacy signals |
| 9 | Power Customer | MRR ≥ 2x initial; multi-cloud or multi-team |
| 10 | At-Risk | Usage drop ≥40% over rolling 30d |
| 11 | Churned | Subscription cancelled OR 60d zero-use post-At-Risk |
| 12 | Cold Lead | Trial Lapsed → no extension → 6-mo drip |
| 13 | Winback Active | 90d dormant, in 3-email winback |
| 14 | Suppressed / Removed | Unsubscribed, hard bounce, spam, do-not-contact |
| 15 | Newsletter-only | Opted in to newsletter without trial |
| 16 | Customer + Newsletter | Active customer also opted in to newsletter |

---

## Edges (22)

| # | From → To | Trigger condition |
|---|---|---|
| 1 | Anonymous → Trial Signed Up | Form submit |
| 2 | Anonymous → Newsletter-only | Newsletter form submit |
| 3 | Trial Signed Up → Onboarding | D0 timer fires |
| 4 | Onboarding → Setup-stalled | D7 reached, `aws_connected = false` |
| 5 | Setup-stalled → Onboarding | `aws_connected = true` (rejoin at next sequence step) |
| 6 | Onboarding → Activated Customer | Trial converted to paid plan |
| 7 | Onboarding → Trial Lapsed | D14 reached, no conversion |
| 8 | Trial Lapsed → Onboarding | User accepts extension offer |
| 9 | Trial Lapsed → Cold Lead | No extension, 7d post-trial-end |
| 10 | Cold Lead → Suppressed | 6mo no engagement OR unsubscribe |
| 11 | Cold Lead → Trial Signed Up | Re-signup |
| 12 | Activated Customer → Engaged Customer | First agent action merged within 14d |
| 13 | Activated Customer → At-Risk | 30d, no agent action merged + login frequency drop |
| 14 | Engaged Customer → Expansion-Ready | Identifies new use case (multi-cloud, new team) |
| 15 | Expansion-Ready → Power Customer | MRR ≥ 2x initial |
| 16 | Power Customer → At-Risk | Usage drop ≥40% over 30d |
| 17 | At-Risk → Engaged Customer | Recovery: usage normalizes within 30d |
| 18 | At-Risk → Churned | No recovery in 30d OR cancel |
| 19 | Churned → Winback Active | 90d dormant from churn |
| 20 | Winback Active → Activated Customer | Reactivation signup |
| 21 | Winback Active → Suppressed | No response after 3 emails |
| 22 | Any → Suppressed | Unsubscribe / hard bounce / spam / do-not-contact request |

**Total: 16 nodes, 22 edges.**

---

## Triggers index

- **Time-based:** D0, D1, D3, D5, D7, D12, D14 (onboarding); 30d, 60d, 90d (lifecycle states); 6mo (cold lead suppress).
- **Event-based:** AWS connected, paid plan, agent action merged, MRR change, login frequency, churn signal, unsubscribe, bounce, spam complaint.
- **User-initiated:** trial extension request, reactivation, unsubscribe, manual do-not-contact.

---

## State store [TBD-OPERATOR]

Recommended: store lifecycle state in CRM ([TBD-OPERATOR — HubSpot, Customer.io, etc.]) with these fields per contact:
- `lifecycle_state` (one of the 16 nodes)
- `last_state_transition_at`
- `aws_connected_at`
- `first_action_merged_at`
- `mrr_current`, `mrr_initial`
- `last_login_at`
- `suppression_reason` (nullable)
- `consent_source` (newsletter, trial, sales-led)

---

[TBD-OPERATOR]: confirm CRM/ESP, decide whether newsletter-only contacts are ever moved into trial-conversion campaigns (recommend: yes, but only with explicit re-permission).
