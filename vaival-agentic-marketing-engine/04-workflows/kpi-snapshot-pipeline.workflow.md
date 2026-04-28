---
name: kpi-snapshot-pipeline.workflow
owner_tier: department-head
owner_vertical: analytics-ops
primary_agent: head-of-analytics
playbook_source: §6, §7, §14.3 B
skills: [analytics-tracking, google-analytics, search-console, google-ads-report, campaign-analytics, performance-reporter]
status: active
phase: 2
---

# KPI Snapshot Pipeline

Weekly canonical KPI ingestion. Mon 09:00 client-local. Output is the source of truth for the weekly digest.

## Trigger
- Cron: Monday 09:00 client-local (scheduler skill).
- On-demand: operator override.

## Actors
- **Owner**: Head of Analytics.
- **Producers**: GA4, GSC, Google Ads, LinkedIn Ads, Meta Ads, Microsoft Ads, HubSpot CRM, Looker Studio (export), Segment events, BigQuery (warehouse).
- **Consumer**: digest-delivery workflow + CMO Orchestrator weekly tick.

## Inputs
- Connector reads from: `06-connectors/analytics/ga4.connector.md`, `seo/google-search-console.connector.md`, `paid/google-ads.connector.md`, `paid/linkedin-campaign-manager.connector.md`, `paid/meta-business-suite.connector.md`, `paid/microsoft-ads.connector.md`, `email-crm/hubspot-crm.connector.md`, `analytics/bigquery.connector.md`.
- Per-vertical KPI taxonomy + targets from `clients/{id}/okrs/`.

## Steps
1. **Fetch** trailing 7-day + week-on-week metrics from each connector. Read-only scopes only.
2. **Normalize**: map to canonical KPI taxonomy (channel → KPI → value/unit/cadence). Apply UTM taxonomy rubric.
3. **Reconcile**: cross-platform variance check (paid platform vs GA4); flag >10% to Analytics-Ops queue.
4. **Compute**: NSM movement, OKR-KR % to target, channel mix, MQL funnel, CAC/ROAS, content performance, SEO rank deltas, AEO/GEO mention rate.
5. **Write**: render into `clients/{id}/feeds/weekly-kpi-snapshot.md` per `templates/weekly-kpi-snapshot.md`.
6. **Rubric grade**: snapshot self-evaluates against `rubrics/weekly-kpi-snapshot.yaml`. <8 → iterate; surface gaps as HITL ("missing data: …").
7. **Persist**: append `kpi.snapshot.delivered` to `ledger-events/`. Optionally land normalized rows into BigQuery `marketing.weekly_kpi_snapshot`.
8. **Trigger downstream**: emit signal to `digest-delivery.workflow.md`.

## Outputs
- `clients/{id}/feeds/weekly-kpi-snapshot.md` (rubric ≥8).
- BigQuery rows in `{client}.marketing.weekly_kpi_snapshot` (optional, when warehouse wired).
- Ledger event with snapshot path + checksum.

## Rubric
`rubrics/weekly-kpi-snapshot.yaml` (pass bar 8). `rubrics/utm.yaml` and `rubrics/attribution.yaml` referenced for upstream data quality.

## HITL Gates
- Connector auth-expired on a critical source (GA4, Ads) → block snapshot, raise HITL.
- Variance >25% on any NSM week-on-week without external explanation (campaign launch, season) → HITL.
- Missing OKR file for current quarter → HITL.

## Failure Modes
- Partial connector outage → snapshot ships in degraded mode with explicit "data missing" markers; rubric likely fails.
- Schema drift in upstream platform → exception caught, manual ingest path triggered.
- Multi-tenant cross-leak → refuse run, escalate.

## Ledger Events Emitted
`kpi.fetch.started` · `kpi.fetch.connector.{name}.{ok|fail}` · `kpi.normalize.completed` · `kpi.reconcile.variance_flagged` · `kpi.snapshot.written` · `kpi.snapshot.rubric.{score}` · `kpi.snapshot.delivered`.
