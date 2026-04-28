---
name: bigquery
tool_display_name: Google BigQuery
category: analytics
owner_vertical: analytics-ops
used_by_roles: [marketing-ops-manager, marketing-data-analyst, head-of-analytics]
purpose: Warehouse for KPI snapshot pipeline + cross-source joins (GA4 export, CRM, Ads).
auth_method: service-account
status: spec
phase: 2
---

# BigQuery Connector

Conforms to `connector-standard.md`.

## 1. Authentication
- **Service account** (JSON key) or **Workload Identity Federation** (preferred — no static keys).
- Per-client GCP project; per-environment service account (read / write / admin).
- Storage: `vault://{client}/bigquery/sa-key` (JSON) or workload-identity descriptor.
- Rotation: SA keys rotated 90d; prefer WIF to eliminate static keys.

## 2. Rate Limits / Quotas
- Documented: 100 concurrent interactive queries; 6 TB/day query bytes default; 1500 streaming inserts/sec/table.
- Connector budget: 80% of project quota; cost-budget cap per query (`maximum_bytes_billed`) enforced.
- Slot reservations honored where present.

## 3. Idempotency
- **Query (read)**: idempotent — set `request_id` for deduplicated retries.
- **Load job**: idempotent via client-supplied `jobId` (`{decision_id}:load:{table}:{run}`).
- **DML INSERT**: not idempotent unless using MERGE on natural key. Connector enforces MERGE pattern for all writes from agents.
- **Streaming insert**: dedupe via `insertId`.

## 4. Retry Policy
Standard. `quotaExceeded` → backoff with extended ceiling (300s). `rateLimitExceeded` → standard. Permanent (`invalidQuery`, `accessDenied`) → no retry.

## 5. Scopes (least-privilege IAM roles)
| Role | IAM |
|---|---|
| Read-only analyst | `roles/bigquery.dataViewer` + `roles/bigquery.jobUser` |
| Pipeline writer | `roles/bigquery.dataEditor` (table-scoped) + `roles/bigquery.jobUser` |
| Schema admin | `roles/bigquery.dataOwner` (HITL only) |
| Project admin | `roles/bigquery.admin` (HITL only) |

Table-level IAM preferred over dataset/project where supported.

## 6. Telemetry
Standard fields + `project_id`, `dataset`, `table`, `job_id`, `bytes_processed`, `bytes_billed`, `slot_ms`, `cache_hit`. Cost telemetry into `10-logging/` for budget guardrails.

## 7. Error Taxonomy
401 → `auth_expired`; 403 → `auth_insufficient`; 400/`invalidQuery` → `validation`; 429/`quotaExceeded` → `rate_limited`; 5xx → `server_error`; `accessDenied` → `auth_insufficient`.

## 8. Rollback
- SELECT: read-only.
- LOAD into staging table: reversible (drop staging) — pattern: load → validate → MERGE into prod → drop staging.
- MERGE / DML: compensating — write a corrective MERGE; never silent UPDATE in place. Snapshot `(table, partition, schema_hash)` before write.
- Schema change (DDL): reversible only via prior-state record + HITL.
- DROP TABLE / dataset → irreversible without time-travel; HITL with explicit confirmation; rely on 7-day fail-safe.

## Refusals
- Query without `maximum_bytes_billed` cap → refused (cost guardrail).
- Cross-client dataset join in one query → refused (multi-tenant isolation).
- DROP / TRUNCATE on prod tables → HITL with rollback plan.
- PII columns selected without consent flag check → refused.
