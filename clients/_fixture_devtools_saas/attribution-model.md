# Attribution Model — Loopgate

> Owner: Head of Analytics. Target live: Phase 2 week 9. Current: first-touch + last-touch only (gap).

## Principles
1. **Every touch counts, none equally.** First-touch for demand creation credit, last-touch for conversion credit, multi-touch (time-decay) for portfolio decisions.
2. **Human self-report as cross-check.** "How did you hear about us?" free-text captured at demo form; quarterly reconciliation against model.
3. **Honest gaps.** Dark-social (podcasts, Slack, Reddit, word-of-mouth) are under-credited by default; branded-search lift used as proxy.

## Models
| Model | Use for | Data path |
|---|---|---|
| Last non-direct click | paid channel ROI (fast decisions) | GA4 default |
| First-touch | demand-creation channel assessment | GA4 custom + BigQuery |
| Time-decay multi-touch (7d half-life) | portfolio / budget reallocation | BigQuery view (week 9 target) |
| W-shaped (FT 30% / Lead 30% / Opp 30% / other 10%) | Enterprise pipeline attribution | HubSpot + BigQuery |
| Self-report | ground-truth for dark-social | demo form free text → tagged |

## Data flow
```
GA4 → BigQuery export (daily)
HubSpot → BigQuery sync (hourly via Stitch)
Customer.io → BigQuery (daily CSV)
Amplitude → Snowflake → BigQuery federation
Ad platform costs (Google, LinkedIn, Meta) → BigQuery via Fivetran (daily)
```

## Joins
- `user_id` across product (Amplitude), marketing (GA4 client_id via Segment), CRM (HubSpot vid)
- `account_id` for ABM (HubSpot company)
- `campaign_id` from UTM → stored as dim_campaign

## Tracking guardrails
- All outbound URLs preserve UTMs to the form submit.
- Consent-based; EU users: cookieless first-party events where consent missing.
- Sample-ratio-mismatch alarm on experiment tracking.

## HITL flags
- BigQuery access blocked (Data Eng) → escalate 2026-05-01.
- Multi-touch model launch may miss week 9 if join keys fail QA → fallback: deliver W-shaped on HubSpot-only data, defer GA4-side to week 12.

## Reporting surfaces
- Weekly KPI snapshot (`feeds/weekly-kpi-snapshot.md`) cites which model powered each number.
- Monthly executive report includes all 3 model views for NSMs where they materially differ.

## Known unknowns (disclosed)
- iOS 14+ Meta data loss (~20% of Meta attribution).
- Dark-social underweight ~30% based on self-report variance.
- LD-retargeting cross-device loss ~8%.
