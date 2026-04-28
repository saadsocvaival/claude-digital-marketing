# Dashboard Wireframe — CostSage.ai Marketing

> 5 tabs. Built in Looker Studio (free) with GA4 + BigQuery export + Sheets connectors. Each tab: charts, filters, refresh cadence, primary KPI. KPI numbers cross-ref `kpi-dictionary.md`.

## Tab 1 — CMO All-Up
- **Primary KPI (hero scorecard):** Pipeline coverage (#26).
- **Refresh:** Daily 09:00 GMT.
- **Filters:** Quarter, segment (SMB/Mid-market), region.
- **Charts:**
  1. Big-number row: New ARR (#29), Pipeline $ (#25), CAC blended (#31), LTV:CAC (#33), Payback months (#34).
  2. Pipeline funnel: Sessions → demo_request → SQL → Opp → Closed-Won (counts + conversion %).
  3. Channel-mix donut: % of demo_requests by source (last 30d).
  4. Spend pacing bar: planned vs actual MTD per channel (#55).
  5. NRR + GRR trend line (#39 #40), 12-month rolling.
  6. G2/Capterra review velocity (#47).

## Tab 2 — Acquisition
- **Primary KPI:** Cost per demo blended (#56).
- **Refresh:** Hourly (paid metrics), daily (organic).
- **Filters:** Date range, channel, campaign, geo, device.
- **Charts:**
  1. Channel scorecard table: spend, clicks, CTR, CPC, demo_requests, CPA, SQL rate (#5–8, 17, 22).
  2. Per-campaign drill-down (sortable).
  3. Branded vs non-branded organic (#9 #10).
  4. Newsletter signups trend (#18).
  5. Top landing pages by conversions.
  6. Search Terms / search query report widget (Google + Bing — flag spend > $X with 0 conversions).

## Tab 3 — Pipeline (RevOps + Marketing joint)
- **Primary KPI:** Pipeline $ created this quarter (#25).
- **Refresh:** Daily.
- **Filters:** Owner (AE), stage, source, ICP-fit score.
- **Charts:**
  1. Pipeline waterfall: open / created / advanced / won / lost.
  2. SLA monitor: demo_request → SDR-touched within 1 business hour (count + %).
  3. SQL rate by source (#22).
  4. Win rate by source (#27).
  5. Sales cycle length (#30).
  6. Avg deal size (#28).
  7. Cohort: demos requested → closed by month-of-request.

## Tab 4 — Lifecycle (Activation, Retention, Expansion)
- **Primary KPI:** Trial-to-paid conversion (#35).
- **Refresh:** Weekly (Mon).
- **Filters:** Cohort month, plan, ICP segment.
- **Charts:**
  1. Trial funnel: trial_start → trial_complete → paid (#35–#37).
  2. Activation-rate trend line.
  3. Logo retention curve by cohort (#38).
  4. NRR / GRR (#39 #40).
  5. Churn drivers list (top 5 reasons from CS notes).
  6. Newsletter health: open/CTR (#42 #43).
  7. NPS (#46) — quarterly bar.
  8. Expansion ARR (#44).

## Tab 5 — Web / CRO
- **Primary KPI:** LP CVR paid (#17).
- **Refresh:** Daily.
- **Filters:** URL, device, source.
- **Charts:**
  1. Per-page conversion table: page, sessions, scroll-75, CTA click, form_start, form_submit, demo_request.
  2. Lighthouse perf trend (median across 18 URLs) (#48–51).
  3. Anomaly callouts: any page with > 2σ drop in CVR or perf (link to `anomaly-detection-spec.md`).
  4. 4xx/5xx rate (#52).
  5. GSC impressions trend per top 20 queries (#53).
  6. CTA leaderboard: top 10 cta_ids by clicks + conversion contribution.
  7. Heatmap snapshot (PostHog session replays — top exits on `/aws`, `/pricing`).

## Operating cadence
- Daily 09:00 GMT auto-snapshot to Slack `#marketing-pulse` (top-line numbers from each tab).
- Weekly Monday 10:00 GMT: full dashboard review (digest format: `weekly-digest-format.md`).
- Monthly: per-channel post-mortem (template in each campaign brief §12).

## Build notes
- Looker Studio sources:
  - GA4 BigQuery export (free; daily).
  - Google Ads connector.
  - Microsoft Advertising via supermetrics or CSV import — `[TBD-OPERATOR]`.
  - LinkedIn via Supermetrics / Funnel.io — `[TBD-OPERATOR]`.
  - Reddit via CSV import (manual weekly until API connector added).
  - GSC connector.
  - CRM connector (HubSpot / Salesforce native to Looker) — `[TBD-OPERATOR]`.
  - PostHog (via SQL connector to its Postgres) once installed.
- Single date control on each tab.
- Theme: dark mode, brand teal accent.
