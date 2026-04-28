# Anomaly Detection Spec — CostSage.ai Marketing

> What we monitor, the 2σ thresholds, and where the alert routes.

## 1. Method
- For each metric, compute rolling 28-day mean (μ) and standard deviation (σ) on daily values, weekday-aware where seasonality matters (paid clicks Mon vs. Sat differ materially).
- Alert when today's value ≤ μ − 2σ (drop) or ≥ μ + 2σ (spike — for cost metrics, this is bad; for conversion metrics, good but worth noting).
- Two-day confirmation rule on noisy metrics (LP CVR, INP) to avoid false positives.
- Floor: do not alert if absolute volume < N_min (per metric below) — sample too small.

## 2. Monitored metrics

| # | Metric | KPI ref | Direction | N_min daily | Alert routing | Cadence |
|---|--------|---------|-----------|-------------|---------------|---------|
| 1 | Sessions (total) | #1 | drop | 200 | Slack `#marketing-pulse` | Daily |
| 2 | Organic sessions | #4 | drop | 100 | Slack `#seo-alerts` | Daily |
| 3 | Branded search clicks | #9 | drop | 20 | Slack `#seo-alerts` | Daily |
| 4 | Paid clicks (per channel) | #5 | drop OR spike | 30 | Slack `#paid-alerts`, tag channel owner | Daily |
| 5 | Paid spend (per channel) | — | spike | $50 | Slack `#paid-alerts` + email DRI | Daily — pacing breach |
| 6 | Paid CPC (per channel) | #8 | spike | 30 clicks | Slack `#paid-alerts` | Daily |
| 7 | LP CVR (per LP) | #17 | drop | 100 sessions | Slack `#cro-alerts` | Daily, 2-day confirm |
| 8 | demo_request count | #19 | drop | 3 | Slack `#marketing-pulse` + RevOps tag | Daily |
| 9 | demo_request CPA blended | #56 | spike | 5 demos | Slack `#paid-alerts` | Daily |
| 10 | SQL rate | #22 | drop | 10 demos in 7d | Slack `#revops-alerts` | Weekly |
| 11 | Trial-to-paid CVR | #35 | drop | 10 trials in 14d | Slack `#growth-alerts` | Weekly |
| 12 | Newsletter open rate | #42 | drop | per send | Slack `#email-alerts` | Per send |
| 13 | Lighthouse perf (per URL) | #48 | drop > 0.10 W/W | n/a | Slack `#marketing-perf-alerts` | Daily (handled by Lighthouse runner) |
| 14 | LCP (per URL) | #49 | spike > 25% | n/a | Slack `#marketing-perf-alerts` | Daily |
| 15 | 4xx/5xx rate | #52 | spike | 0.5% | Slack `#eng-alerts` (cross-team) | Hourly |
| 16 | Form-completion rate | #16 | drop | 30 form_starts | Slack `#cro-alerts` | Daily |
| 17 | Search Console impressions | #53 | drop | 500 | Slack `#seo-alerts` | Weekly |
| 18 | Pipeline coverage | #26 | drop | n/a | Email CMO | Weekly |

## 3. Implementation
- Source: GA4 BigQuery export + Ad APIs + GSC + ESP via daily ETL (Airflow / Cloud Scheduler) — `[TBD-OPERATOR: ETL choice]`.
- Detector: simple Python script `anomaly_check.py` that:
  - Pulls last 30 days of metric per dimension.
  - Computes weekday-segmented μ/σ.
  - Emits Slack-formatted webhook payloads (similar shape to `lighthouse-ci-cron-spec.md` §5).
- Suppression: any metric muted for 24h via `/mute <metric>` Slack slash-command (operator) — `[TBD-FUTURE]`.

## 4. False-positive log
Track every alert in `clients/costsage/feeds/anomaly-log.csv` (date, metric, value, deviation, action, false-positive-flag). Quarterly review tunes thresholds.

## 5. Operator deps
- `[TBD-OPERATOR]` Slack webhooks per channel.
- `[TBD-OPERATOR]` ETL host (likely SOC server cron alongside Lighthouse runner).
- `[TBD-OPERATOR]` Initial 28-day baseline data available before activating (cold-start: use absolute floors only).
