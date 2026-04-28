# Weekly Digest Format — CostSage.ai Marketing

> Posted Monday 10:00 GMT to Slack `#marketing-pulse` and emailed to CMO + DRIs. **Strict 1-page cap.** If it doesn't fit, cut — do not append.

## Layout (markdown template)

```
# CostSage Marketing — Week of {YYYY-MM-DD}

## Top-line
| KPI                    | This wk  | Δ vs last wk | Δ vs MTD avg | Δ vs QTD avg |
|------------------------|---------:|-------------:|-------------:|-------------:|
| New ARR ($)            |          |              |              |              |
| Pipeline created ($)   |          |              |              |              |
| Demo requests          |          |              |              |              |
| SQLs                   |          |              |              |              |
| Blended CPA / demo     |          |              |              |              |
| LTV:CAC (rolling 90d)  |          |              |              |              |
| Sessions               |          |              |              |              |
| Organic clicks (GSC)   |          |              |              |              |
| Trial-to-paid CVR      |          |              |              |              |

## Per-channel highlights (max 3 bullets each)
- **Google Search (AWS):** spend $X, CPA $Y (▲/▼Z%), top keyword: "...", note: ...
- **Google Search (FinOps):** ...
- **LinkedIn (CTO):** ...
- **LinkedIn (FinOps):** ...
- **Bing:** ...
- **Reddit:** ...
- **Organic / SEO:** top moving page, top moving query.
- **Email:** newsletter open/CTR; lifecycle drip key step.
- **Reviews (G2/Capterra):** new reviews, rank, sponsored notes.

## Anomalies (2σ alerts that fired)
- {metric} {value} ({deviation}σ) — root cause hypothesis: {1-liner} — owner: {name} — action: {1-liner}.
(Max 5; if more, link to anomaly-log.)

## Decisions needed
- [ ] {decision}, requested by {name}, deadline {date}.

## Wins / shipped this week (max 3 lines)
- ...

## Coming next week (max 3 lines)
- ...

— Generated {ts} from `dashboard-wireframe.md` Tab 1 source.
```

## Discipline rules
- ≤ 1 printed page (~ 60 lines).
- Numbers without commentary are forbidden — every metric line has a Δ + a one-line cause when materially off.
- No screenshots; link to dashboard tab if visual needed.
- "Decisions needed" section drives Monday standup agenda.
- Anomaly table cross-references `anomaly-detection-spec.md` IDs.
- DRI signs at the bottom (defaults to Marketing DRI).

## Distribution
- Slack post (Block Kit) to `#marketing-pulse`.
- Email digest via Mailchimp transactional or Customer.io — `[TBD-OPERATOR]`.
- Auto-archived to `clients/costsage/operations/analytics/digests/YYYY-WW.md`.

## Generation
- Looker Studio Tab 1 + a `weekly_digest.sql` query feeds a Cloud Function that fills the template, posts to Slack via webhook, and writes to repo via deploy key.
- Failures (no data / API down) post a `:rotating_light:` to `#marketing-pulse` with the error.
