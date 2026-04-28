---
name: wordpress-application-password
tool_display_name: WordPress Application Password (auth pattern)
category: web-dev
owner_vertical: website-development
used_by_roles: [web-development-lead, front-end-developer, cms-page-builder]
purpose: Sub-spec for the auth pattern used by `wordpress.connector.md` when integrating against the WP REST API.
auth_method: app-password (HTTP Basic over HTTPS)
status: spec
phase: 2
related: web-dev/wordpress.connector.md
---

# WordPress Application Password Auth Pattern

Sub-spec referenced by `web-dev/wordpress.connector.md`. Applies to any WP REST API operation done by an agent (post/page CRUD, media upload, menu update, schema injection).

## 1. Authentication
- **Method**: WP Application Password (introduced WP 5.6+). HTTP Basic with `username:application-password`.
- **TLS required**: refuse over HTTP.
- **Per-agent password**: each automation agent gets its own application password named `costsage-{agent}-{yyyymm}` so revocation is surgical.
- **Storage**: `vault://{client}/wordpress/{site}/app-password/{agent}`.
- **NEVER use the admin password** for API access.
- **2FA / SSO** at the WP login layer does not affect app-password auth — but app passwords MUST be revoked when the human user is offboarded.

## 2. Rate Limits
- WP core has no built-in API rate limit; defer to platform plugins (Wordfence, hosting WAF). Treat as conservative 60 req/min on shared hosts.
- Connector budget: 30 req/min on shared hosts; 120 req/min on managed hosts (WP Engine, Kinsta).

## 3. Idempotency
- **Post / page create**: not natively idempotent. Connector dedupes by `(slug, post_type)` within 24h + decision_id stored as post meta `_decision_id`.
- **Update**: read-modify-write — read `modified_gmt`, refuse PUT if newer than read.
- **Media upload**: hash-based dedupe (sha256 of bytes) before upload.
- **Menu / option write**: HITL gated.

## 4. Retry Policy
Standard. 401/403 → no retry, escalate (likely revoked password). 5xx → up to 5 retries.

## 5. Scopes
- Application passwords inherit the user's role. Map roles least-privilege:
  - `editor` for content publish agents
  - `author` for draft-only agents
  - `subscriber` for read-only agents (note: subscriber cannot read drafts; use `editor` read-only fork if needed)
- `administrator` → HITL only.

## 6. Telemetry
Standard fields + `wp_user_login`, `app_password_label`, `post_id`, `post_type`, `revision_id`. Every write logs the prior `revision_id` for rollback.

## 7. Error Taxonomy
401 → `auth_expired` (password revoked / disabled); 403 → `auth_insufficient` (role mismatch); 409 → `conflict` (slug or revision); 429 (some hosts) → `rate_limited`; 5xx → `server_error`.

## 8. Rollback
- Post create / update: reversible — restore prior revision via `wp/v2/posts/{id}/revisions/{rev}/restore` (custom endpoint or WP-CLI).
- Media: reversible (delete uploaded asset).
- Menu / option: reversible via prior-state snapshot stored in ledger.

## Operator Onboarding Steps (CostSage)
1. WP admin → Users → Profile → Application Passwords → create per agent.
2. Copy generated string into vault path; never store in repo.
3. Update `secrets.pointer.md` with vault path + auth_method `app-password`.
4. Test read (e.g. `GET /wp-json/wp/v2/users/me`) before granting write.
5. Document revocation runbook (admin → Users → Application Passwords → Revoke).

## Refusals
- Operating over HTTP (no TLS) → refused.
- Using the WP admin user's app password for automation → refused (use a service account user).
- Bulk delete >5 posts in one call → HITL.
