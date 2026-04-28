# Data Warehouse Design — CostSage.ai Marketing

> Schema sketch for when event volume justifies a warehouse. Default destination: **BigQuery free tier** (1 TB query / 10 GB storage free monthly per public docs). Alternate: PostHog ClickHouse if marketing-only insights suffice.

## 1. Decision: BigQuery vs PostHog ClickHouse

| Need | BigQuery | PostHog CH |
|------|----------|------------|
| Joins across CRM + product + marketing | ✅ first-class | ⚠️ limited |
| Self-serve product analytics (funnels, retention) | ❌ build in Looker | ✅ native UI |
| Cost at < 20M events/mo | ~$0 (free tier) | $0 (self-host) |
| Cost at > 100M events/mo | $30–$200/mo | host upgrade |
| Source of truth | ✅ | ❌ secondary |

**Recommendation:** dual-write — PostHog for product analytics UI; BigQuery as warehouse-of-record (CRM-joined business metrics).

## 2. BigQuery dataset layout

```
project: costsage-data
├── dataset: raw          (untouched landing data, one table per source)
├── dataset: stg          (staging — typed, cleaned, deduped)
├── dataset: mart         (business-grade tables for Looker)
└── dataset: snapshots    (point-in-time exports)
```

## 3. Core tables (mart)

### 3.1 `mart.sessions`
```sql
session_id            STRING       -- GA4 ga_session_id + user_pseudo_id
user_pseudo_id        STRING
user_id_hash          STRING       -- when logged in
session_start_ts      TIMESTAMP
session_end_ts        TIMESTAMP
duration_seconds      INT64
landing_page          STRING
exit_page             STRING
device_category       STRING
country               STRING
utm_source            STRING
utm_medium            STRING
utm_campaign          STRING
utm_content           STRING
utm_term              STRING
first_touch_source    STRING       -- denormalized from cookie
event_count           INT64
is_engaged            BOOL
PARTITION BY DATE(session_start_ts)
CLUSTER BY user_pseudo_id, utm_source
```

### 3.2 `mart.events`
```sql
event_id          STRING        -- UUID
event_ts          TIMESTAMP
event_name        STRING
session_id        STRING
user_pseudo_id    STRING
user_id_hash      STRING
page_path         STRING
page_type         STRING
cta_id            STRING
form_id           STRING
form_type         STRING
value             FLOAT64
currency          STRING
event_params      JSON
PARTITION BY DATE(event_ts)
CLUSTER BY event_name, user_pseudo_id
```

### 3.3 `mart.users`
```sql
user_pseudo_id     STRING
user_id_hash       STRING
email_hash         STRING
first_seen_ts      TIMESTAMP
first_touch_source STRING
first_touch_campaign STRING
last_seen_ts       TIMESTAMP
total_sessions     INT64
total_events       INT64
became_lead_ts     TIMESTAMP   -- first demo_request
became_trial_ts    TIMESTAMP
became_customer_ts TIMESTAMP
account_id         STRING      -- FK accounts
```

### 3.4 `mart.accounts`
```sql
account_id          STRING
company_name        STRING
company_domain      STRING
industry            STRING
employee_band       STRING       -- e.g. "51-200"
country             STRING
arr_current         FLOAT64
arr_committed       FLOAT64
plan                STRING
created_ts          TIMESTAMP
churned_ts          TIMESTAMP
status              STRING       -- prospect / trial / paying / churned / closed_lost
csm_owner           STRING
ae_owner            STRING
```

### 3.5 `mart.opportunities`
```sql
opp_id           STRING
account_id       STRING
created_ts       TIMESTAMP
closed_ts        TIMESTAMP
stage            STRING
amount_arr       FLOAT64
status           STRING        -- open / won / lost
loss_reason      STRING
source           STRING        -- mapped from first/last touch
ae_owner         STRING
PARTITION BY DATE(created_ts)
```

### 3.6 `mart.campaigns`
```sql
campaign_id        STRING        -- platform-internal id
platform           STRING        -- google_ads / linkedin / bing / reddit / meta / g2 / capterra / email
campaign_name      STRING
status             STRING
launched_ts       TIMESTAMP
paused_ts         TIMESTAMP
audience_spec_ref STRING        -- file path in repo
```

### 3.7 `mart.costs`
```sql
date          DATE
platform      STRING
campaign_id   STRING
ad_group_id   STRING
ad_id         STRING
spend         FLOAT64
impressions   INT64
clicks        INT64
conversions   FLOAT64
ccy           STRING
PARTITION BY date
CLUSTER BY platform, campaign_id
```

### 3.8 `mart.attribution_touches`
```sql
touch_id        STRING
user_pseudo_id  STRING
user_id_hash    STRING
ts              TIMESTAMP
channel         STRING
utm_source      STRING
utm_medium      STRING
utm_campaign    STRING
landing_page    STRING
position_in_journey INT64    -- 1=first; N=last
journey_id      STRING        -- groups touches that led to a conversion
PARTITION BY DATE(ts)
```

## 4. Loading
- GA4 → BigQuery: native daily export (free).
- Ad platforms → BQ: Fivetran / Stitch / supermetrics — `[TBD-OPERATOR]`. Free-tier: write a thin Cloud Function pulling daily.
- CRM → BQ: HubSpot / Salesforce native connector — `[TBD-OPERATOR]`.
- PostHog → BQ: PostHog batch export to BQ (built-in).
- ESP → BQ: native if Mailchimp/Customer.io; else CSV nightly.

## 5. Models / lineage
- dbt-core (open-source) recommended.
- Layers: `raw → stg → mart`.
- Key models: `stg_ga4_events`, `stg_hubspot_deals`, `stg_google_ads_costs`, `mart_sessions`, `mart_attribution_touches`, `mart_kpi_daily`.

## 6. Privacy
- No raw email at rest; only sha256 hashes in `mart`.
- IP truncation per GA4 default.
- 26-month retention on `raw`; 7-year on `mart.opportunities` (audit).

## 7. Cost guard
- Looker queries restricted to clustered tables; weekly cost report from BQ INFORMATION_SCHEMA.JOBS.
- Set BigQuery slot reservation only when monthly query bytes > 1 TB sustained.

## 8. Operator deps
- `[TBD-OPERATOR]` GCP project + billing.
- `[TBD-OPERATOR]` GA4 → BQ link enabled.
- `[TBD-OPERATOR]` CRM choice (HubSpot vs Salesforce) — drives connector pattern.
- `[TBD-OPERATOR]` Service-account key for ETL.
