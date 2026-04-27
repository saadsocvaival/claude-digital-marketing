---
name: mailgun
tool_display_name: Mailgun
category: email-crm
owner_vertical: email-crm
used_by_roles: [crm-email-manager, marketing-automation-specialist, head-of-automation]
purpose: Transactional + bulk email; alt provider with strong EU region option.
auth_method: api-key
status: spec
phase: 2
---

# Mailgun Connector

Conforms to `connector-standard.md`.

## 1. Authentication
- HTTP Basic with API key (user `api`, password = key) OR HMAC for webhooks.
- Region-aware base URL: `api.mailgun.net` (US) / `api.eu.mailgun.net` (EU). Region must match data-residency policy.
- Storage: `vault://{client}/mailgun/api-key`. Webhook signing key stored separately.

## 2. Rate Limits
- Documented: 300 req/min default API; higher on Foundation/Growth.
- Connector budget: 240 req/min; leaky-bucket.
- Outbound throughput: per plan; auto-throttle at 80% to avoid IP-reputation hit.

## 3. Idempotency
- **Send**: dedupe via `o:tag` containing `{decision_id}` + connector dedupe table 24h.
- **Suppression / bounce list**: read-modify-write.
- **Routes / domains**: read-modify-write with version pin.

## 4. Retry Policy
Standard. 451 (regulatory) → no retry, escalate. 429 → backoff with `Retry-After`.

## 5. Scopes
Mailgun uses single API key for domain; create domain-scoped sending keys for least-privilege. Suppression-list write requires elevated key.

## 6. Telemetry
Standard fields + `domain`, `tag`, `mailgun_message_id`, `region`. Events (accepted, delivered, opened, clicked, complained, unsubscribed, failed permanent/temporary) → `10-logging/`.

## 7. Error Taxonomy
401 → `auth_expired`; 402 → `refused` (account suspended); 413 → `validation`; 429 → `rate_limited`; 5xx → `server_error`. Permanent failures → suppress + record.

## 8. Rollback
- Send: irreversible.
- Suppression add: reversible.
- Domain / DNS change: reversible with prior-state record + HITL.

## Refusals
- Spam score <9/10 → refused.
- EU recipient routed via US region without consent → refused (data-residency).
