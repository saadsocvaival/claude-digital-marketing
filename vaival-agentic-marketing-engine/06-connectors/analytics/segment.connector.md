---
name: segment
tool_display_name: Twilio Segment (CDP)
category: analytics
owner_vertical: analytics-ops
used_by_roles: [marketing-ops-manager, marketing-data-analyst, head-of-analytics]
purpose: Customer Data Platform — single event spec routed to GA4, Ads, CRM, warehouse.
auth_method: api-key (write key) + token (HTTP API)
status: spec
phase: 2
---

# Segment Connector

Conforms to `connector-standard.md`.

## 1. Authentication
- **Source write key**: per-source key for `track`, `identify`, `page`, `group`, `alias` events.
- **HTTP API token** (Personal Access Token / Workspace token): for CRUD on sources/destinations/tracking-plans.
- Storage: `vault://{client}/segment/{source-write-key, workspace-token}`.
- Rotation: write keys rotated yearly or on incident; workspace tokens 90d.

## 2. Rate Limits
- Documented: HTTP API source — 30k events/sec aggregate for paid plans; 100 events/batch.
- Connector budget: 24k events/sec aggregate (80%); per-source token-bucket.
- Workspace API (CRUD): 60 req/min, conservative 50.

## 3. Idempotency
- **Track / identify / page**: include `messageId` (UUIDv4 per logical event = decision_id-derived). Segment dedupes on `messageId` within 24h.
- **Tracking plan write**: read-modify-write with version pin.
- **Source / destination CRUD**: HITL gated.

## 4. Retry Policy
Standard. 400 (malformed) → no retry. 429 → backoff. 5xx → up to 5 retries.

## 5. Scopes
- Source write key: per-source, write-only events.
- Workspace token roles: Read-Only, Source Admin, Workspace Owner. Agents default Read-Only; Source Admin gated.

## 6. Telemetry
Standard fields + `source_id`, `destination_id`, `event_name`, `tracking_plan_violations`. Tracking-plan violations are first-class signals routed to Analytics-Ops queue.

## 7. Error Taxonomy
401 → `auth_expired`; 403 → `auth_insufficient`; 400 → `validation`; 429 → `rate_limited`; 5xx → `server_error`. Tracking-plan violations are warnings, not errors, but logged.

## 8. Rollback
- Event send: irreversible (events are append-only). Compensating: send a corrected event with `corrects: <messageId>` semantic and document in ledger.
- Tracking-plan change: reversible via version restore.
- Destination enable/disable: reversible.
- Source delete / workspace mutation: HITL.

## Refusals
- PII fields not declared in tracking plan → refused (GDPR/CCPA).
- Event volume spike >5× baseline within 5 min → throttle + alert (likely instrumentation bug).
- Cross-client data routing → refused (multi-tenant isolation).
