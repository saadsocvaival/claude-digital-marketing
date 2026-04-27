---
name: resend
tool_display_name: Resend
category: email-crm
owner_vertical: email-crm
used_by_roles: [crm-email-manager, marketing-automation-specialist, head-of-automation]
purpose: Modern transactional email API; preferred for product-triggered + digest delivery.
auth_method: api-key
status: spec
phase: 2
---

# Resend Connector

Conforms to `connector-standard.md`.

## 1. Authentication
- API key (Bearer); domain-scoped keys preferred.
- Storage: `vault://{client}/resend/api-key`.
- Rotation: 90 days; revoke on personnel change.

## 2. Rate Limits
- Documented: 10 req/sec default; higher on paid tiers.
- Connector budget: 8 req/sec; token-bucket; back-pressure → queue with TTL 60s.

## 3. Idempotency
- **Send**: include `X-Idempotency-Key` (custom) — stored in connector dedupe table 24h. Resend itself dedupes by message id on retry within session.
- **Domain / DKIM ops**: read-modify-write.

## 4. Retry Policy
Standard exp backoff. 422 (validation) → no retry. 429 → backoff. 5xx → up to 5 retries.

## 5. Scopes
- `emails:send`, `emails:read`, `domains:read`. Domain write + API-key create gated to HITL.

## 6. Telemetry
Standard fields + `from_domain`, `tag` (resend tag), `email_id`. Webhook events (delivered, opened, clicked, bounced, complained) → `10-logging/`.

## 7. Error Taxonomy
401 → `auth_expired`; 403 → `auth_insufficient`; 422 → `validation`; 429 → `rate_limited`; 5xx → `server_error`.

## 8. Rollback
- Send: irreversible.
- Domain DKIM/SPF change: reversible by prior-state restore (operator HITL, plus DNS owner).
- Template (React Email): reversible via git revert.
