---
name: ledger-schema
owner_tier: infra
status: draft
phase: 1
---

# Execution Ledger — Schema

The execution ledger is the single source of truth for every meaningful decision and action taken by any agent. It is append-only, hash-chained, and immutable after write. Nothing executes in the system without a corresponding ledger event; nothing is approved or rolled back except by referencing a ledger event.

## Per-Event Fields

| Field | Type | Purpose |
|---|---|---|
| `event_id` | ULID | Globally unique, time-sortable identifier for this event. |
| `timestamp` | ISO-8601 UTC | When the event was written (not when the action completed). |
| `actor_agent` | string | Canonical agent name (e.g. `cmo-orchestrator`, `seo-manager`, `google-ads-specialist`). |
| `actor_tier` | enum | `tier-1` \| `tier-2` \| `tier-3` \| `tier-4` \| `cross-cutting`. |
| `parent_decision_id` | ULID \| null | `event_id` of the decision that caused this one. Null only for root Founder directives. |
| `triggering_input` | object | Structured reference to what caused the event: directive ID, signal ID, lead report, or upstream decision. |
| `decision_framework_used` | string | Relative path to the framework under `00-governance/decision-frameworks/` used to reach this decision. |
| `confidence_score` | float 0.0–1.0 | Agent's self-reported confidence. Below-threshold confidence MAY trigger QA or escalation. |
| `required_approvals` | array<string> | Gate names that apply to this event (e.g. `["budget-threshold", "external-publishing"]`). Empty if none. |
| `approval_status` | enum | `not-required` \| `pending` \| `approved` \| `rejected` \| `needs-revision`. |
| `output_ref` | string \| object | Stable reference to the emitted artifact (task ID, URL, storage key) — not the artifact itself. |
| `expected_business_impact` | object | Structured estimate: `metric`, `direction`, `magnitude`, `horizon_days`, `confidence`. |
| `rollback_path` | object | Concrete inverse/compensating/irreversible classification + instructions. See connector-standard §8. |
| `audit_hash` | hex string | SHA-256 of this event's canonical JSON concatenated with the previous event's `audit_hash`. |

## Auxiliary Fields (Optional, But Standard)

- `policy_version` — version of the agent's spec and decision-framework at time of decision.
- `input_hash` — SHA-256 of the canonical inputs, for deterministic-output verification.
- `cost_estimate` — currency + amount if the decision commits spend.
- `retry_of` — previous `event_id` if this is a retry.
- `notes` — free-text, human-readable; never consulted by agents.

## Retention

- **Minimum retention: 7 years** for all events involving paid spend, external publishing, credential onboarding, strategy change, or any legally-significant action.
- **Minimum retention: 2 years** for all other events.
- **No deletion before retention expiry**, even for deprecated or refused decisions. Refusals are evidence, not exceptions.
- After retention, events are moved to cold storage, not deleted, unless legal requirement dictates purge.

## Immutability

- Ledger is append-only. There is no update operation.
- Corrections are additive: a new event with `corrects: <prior_event_id>` is written. The prior event remains.
- Each event's `audit_hash` chains to the previous event; tampering with any event invalidates the chain from that point forward.
- Periodic (daily) anchor hashes are committed to an external append-only store (future phase) to detect in-place tampering.

## Lineage & Queries

Because every event carries `parent_decision_id`, the ledger forms a DAG. Common queries:

- "Trace this ad spend back to the Founder directive that authorized it" — walk parents.
- "Show all downstream work from Q1 ICP change" — walk children.
- "Which framework version was in effect when this was decided?" — read `policy_version`.
- "Reproduce this decision" — combine `input_hash` + `policy_version` + `decision_framework_used`.
