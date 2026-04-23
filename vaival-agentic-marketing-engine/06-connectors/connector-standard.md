---
name: connector-standard
owner_tier: infra
status: draft
phase: 1
---

# Connector Standard

Every connector in `06-connectors/` MUST conform to this contract. The contract is platform-agnostic and language-agnostic — no Python, no SDK assumptions. Concrete connector specs (`google-ads.connector.md`, etc.) restate each section with platform-specific details.

## 1. Authentication

Declare exactly one primary auth method per connector: `oauth2`, `api-key`, `service-account`, or `session-token`. Declare refresh semantics (token TTL, refresh-token handling) and the credential-store path where secrets resolve from (`07-resources/credential-store-spec.md`). Credentials NEVER live in the repo.

## 2. Rate-Limit Declaration

State the platform's documented limits (per-second, per-minute, per-day, per-endpoint where it differs) and the connector's conservative in-code budget (typically 60–80% of the documented ceiling). Declare burst handling (token-bucket vs leaky-bucket) and back-pressure behavior when saturated (queue, defer, refuse).

## 3. Idempotency Guarantees

Every write operation declares an idempotency contract:

- **Natural-key idempotent** — platform accepts a client-supplied idempotency key; connector generates `{decision_id}:{operation}` as that key.
- **Read-modify-write guarded** — connector reads current state, computes a checksum, and refuses the write if the checksum changed between read and write.
- **Not idempotent** — explicitly flagged; such operations require a named gate in `11-approvals/` before execution.

Retries of already-succeeded calls MUST be no-ops, not duplicates.

## 4. Retry Policy

- Exponential backoff: base 1s, factor 2, max 60s, jitter ±20%.
- Max 5 retries for transient errors (`5xx`, network, rate-limit).
- Zero retries for `4xx` client errors other than `429`.
- Retry budget per logical operation capped at 5 minutes wall-clock regardless of attempt count.

## 5. Required Read / Write Scopes

Enumerate the minimum scopes needed for each operation class. Connectors MUST declare scope separately for read-only vs write operations so operators can deploy read-only variants. Unused scopes are forbidden — principle of least privilege.

## 6. Telemetry Fields

Every connector call emits a telemetry record with at least:

- `connector_name`, `operation`, `decision_id`, `actor_agent`
- `request_size_bytes`, `response_size_bytes`, `latency_ms`
- `rate_limit_remaining`, `rate_limit_reset_at`
- `retry_count`, `final_status` (`success|client_error|server_error|rate_limited|timeout|refused`)
- `idempotency_key`

Telemetry flows to `10-logging/` and cross-links to the execution ledger via `decision_id`.

## 7. Error Taxonomy

Normalized error types all connectors map platform-specific errors into:

| Code | Meaning | Retry? | Escalate? |
|---|---|---|---|
| `auth_expired` | Token/cred expired or invalid | No | Yes — to Resource Discovery |
| `auth_insufficient` | Missing scope | No | Yes — to Compliance |
| `rate_limited` | Platform throttle hit | Yes (backoff) | No |
| `not_found` | Target resource missing | No | To calling agent |
| `conflict` | Idempotency or version mismatch | No | To calling agent |
| `validation` | Client-side payload error | No | To calling agent |
| `server_error` | Platform 5xx | Yes | After budget exhausted |
| `timeout` | Request exceeded wall-clock | Yes (once) | After 1 retry |
| `refused` | Decision-boundary or gate refused call | No | Already logged |

## 8. Rollback Semantics

Every write operation declares one of:

- **Reversible** — connector provides an inverse operation; `rollback_path` in the ledger points to the inverse call.
- **Compensating** — no inverse, but a well-defined compensating action (e.g. pausing a campaign that cannot be un-launched).
- **Irreversible** — explicitly flagged; requires a pre-execution gate and a human-review step.

The ledger entry for any write records which category applies and the concrete `rollback_path`.
