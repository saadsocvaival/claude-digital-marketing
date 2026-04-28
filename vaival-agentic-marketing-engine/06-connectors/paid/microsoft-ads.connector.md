---
name: microsoft-ads
tool_display_name: Microsoft Advertising (Bing Ads)
category: paid
owner_vertical: paid-media-ppc
used_by_roles: [paid-media-manager, paid-media-specialist, head-of-performance]
purpose: Search ads on Bing / Yahoo network; complementary to Google Search where audience overlap is partial.
auth_method: oauth2
status: spec
phase: 2
---

# Microsoft Ads Connector

Conforms to `connector-standard.md`.

## 1. Authentication
- OAuth2 (Microsoft identity platform). Developer token additionally required (`DeveloperToken` header).
- Account scope: per ad-account; multi-account requires CustomerId / AccountId headers.
- Storage: `vault://{client}/microsoft-ads/{refresh-token, dev-token}`.
- Refresh: refresh tokens long-lived but revocable; rotate dev token annually.

## 2. Rate Limits
- Documented: 5 calls/sec/account on Reporting; 20 calls/sec on Campaign Management; daily quotas per service.
- Connector budget: 80% of each; token-bucket per service; back-pressure defers reporting before management.

## 3. Idempotency
- **Add Campaign / Ad Group / Ad / Keyword**: include client-supplied IDs where API allows. Otherwise dedupe by `(account, name, type, decision_id)` at connector layer.
- **Update**: read-modify-write with `EditorialStatus` and `Modified` timestamp checks.
- **Bulk uploads**: idempotent via `Status` and `Id`; new entities require client tracking IDs.

## 4. Retry Policy
Standard. 429 / `RateLimitExceeded` → backoff. `EditorialDisapproved` → no retry, escalate to brand/legal review.

## 5. Scopes
- Read-only: `ads.manage` with read endpoints only (CampaignManagement read, Reporting).
- Read/write: full `ads.manage` for build/optimize agents.
- Account admin / billing → HITL.

## 6. Telemetry
Standard fields + `customer_id`, `account_id`, `campaign_id`, `ad_group_id`, `currency`, `editorial_status`. Reporting downloads logged with row count + cost.

## 7. Error Taxonomy
401 → `auth_expired`; 403 → `auth_insufficient`; 400 with `BatchError` → `validation`; `EditorialDisapproved` → `refused`; 429 → `rate_limited`; 5xx → `server_error`.

## 8. Rollback
- Add entity: reversible (delete or pause).
- Update bid / budget: reversible via prior-value record.
- Pause: reversible (resume).
- Account-level changes (currency, time zone): irreversible → HITL.

## Refusals
- Spend >$1k/day single-campaign launch → HITL (matches paid-vertical stop-loss).
- Targeting touching protected classes / sensitive verticals → refused.
- UTM-less destination URL → refused (Analytics-Ops UTM rubric ≥99%).
