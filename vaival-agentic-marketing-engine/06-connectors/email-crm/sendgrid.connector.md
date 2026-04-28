---
name: sendgrid
tool_display_name: Twilio SendGrid
category: email-crm
owner_vertical: email-crm
used_by_roles: [crm-email-manager, marketing-automation-specialist, head-of-automation]
purpose: Transactional + bulk email delivery (digest, lifecycle triggers, lead-magnet delivery).
auth_method: api-key
status: spec
phase: 2
---

# SendGrid Connector

Conforms to `connector-standard.md`.

## 1. Authentication
- **Method**: API key (Bearer header `Authorization: Bearer <key>`).
- **Scopes**: separate "Restricted Access" keys per use-case (mail-send, stats, suppressions).
- **Storage**: `vault://{client}/sendgrid/api-key` — never in repo.
- **Refresh**: keys do not expire; rotate every 90 days; revoke on personnel change.

## 2. Rate Limits
- Documented: 600 req/min on Mail Send v3 (Pro+); per-account daily volume per plan.
- Connector budget: 480 req/min (80%); burst via leaky-bucket; back-pressure → defer.
- Webhook: signed events (`X-Twilio-Email-Event-Webhook-Signature`).

## 3. Idempotency
- **Mail Send**: natural-key idempotent via custom header `X-Idempotency-Key = {decision_id}:send:{recipient_hash}` recorded in subject metadata + ledger; duplicate suppression at connector layer (24h dedupe window).
- **Suppression list write**: read-modify-write guarded.
- **Template create/update**: read-modify-write with version pin.

## 4. Retry Policy
Per standard: exp backoff 1s → 60s, factor 2, jitter ±20%, 5 retries on 5xx/429/timeouts, 0 retries on 4xx except 429.

## 5. Scopes (least-privilege)
| Operation | Scope |
|---|---|
| Send transactional | `mail.send` |
| Read stats | `stats.read`, `categories.read` |
| Manage suppressions | `suppressions.read`, `suppressions.write` |
| Read templates | `templates.read` |
| Write templates | `templates.write` (HITL gated) |

## 6. Telemetry
Standard fields + `category`, `template_id`, `bounce_class`, `recipient_domain_hash`. Webhook events (delivered/opened/clicked/bounced/spamreport/unsubscribe) flow into `10-logging/` and reconcile into `ledger-events`.

## 7. Error Taxonomy
Maps SendGrid HTTP codes: 401/403 → `auth_expired`/`auth_insufficient`; 413 → `validation`; 429 → `rate_limited`; 5xx → `server_error`. Soft-bounce → continue; hard-bounce → record + suppress within 24h (playbook §13.4 Non-Negotiables).

## 8. Rollback
- **Send**: irreversible — gated by HITL when audience >100k or new domain warm-up incomplete.
- **Suppression add**: reversible (suppression remove).
- **Template update**: reversible via prior version restore.

## Refusals
- Send when spam score <9/10 on mail-tester (§13.4) → `refused`.
- Send to unsubscribed contact → `refused`.
- Send without unsubscribe link / physical address → `refused`.
