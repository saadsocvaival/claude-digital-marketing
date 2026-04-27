---
name: trello
tool_display_name: Trello
category: ops-collaboration
owner_vertical: cross-vertical
used_by_roles: [marketing-ops-manager, head-of-content, head-of-search-visibility, vertical-leads]
purpose: Editorial calendar + sprint board + content production tracking (CostSage uses Trello).
auth_method: api-key + oauth-token
status: spec
phase: 2
---

# Trello Connector

Conforms to `connector-standard.md`.

## 1. Authentication
- Trello uses API key + token combo (effectively OAuth1-like). Both sent as query params or headers.
- Storage: `vault://{client}/trello/api-key`, `vault://{client}/trello/token`.
- Token can be scoped read-only or read/write; prefer read-only for reporting agents.

## 2. Rate Limits
- Documented: 300 req per 10s per API key, 100 req per 10s per token.
- Connector budget: 240 req per 10s per key (80%); leaky-bucket; defer non-critical ops on saturation.

## 3. Idempotency
- **Create card**: not idempotent at API. Connector pre-checks by `(board, list, title, decision_id)` to avoid duplicates within 24h dedupe window.
- **Update card / move list**: read-modify-write — connector reads `dateLastActivity`, refuses update if changed.
- **Webhook subscriptions**: idempotent via natural key (callbackURL + idModel).

## 4. Retry Policy
Standard. 429 → backoff with `Retry-After`. 401/403 → no retry, escalate.

## 5. Scopes
- Read-only token for reporting / KPI ingestion.
- Read/write token for content-production agents (create cards, move lists, attach files) — gated.
- Admin token (org/board admin) → HITL only.

## 6. Telemetry
Standard fields + `board_id`, `list_id`, `card_id`, `action_type`. Webhook events for board/card changes feed into `ledger-events` for editorial-calendar tracking.

## 7. Error Taxonomy
401 → `auth_expired`; 403 → `auth_insufficient`; 404 → `not_found`; 409 → `conflict`; 429 → `rate_limited`; 5xx → `server_error`.

## 8. Rollback
- Create card: reversible (delete card; soft-delete via archive preferred).
- Update card: reversible via prior-state record.
- Delete card: irreversible at API layer (Trello archive is reversible; permanent delete is not). Default to archive; never permanent-delete via connector.

## Refusals
- Move card across boards owned by different clients → refused (multi-tenant isolation).
- Bulk-delete >10 cards in one operation → HITL.
