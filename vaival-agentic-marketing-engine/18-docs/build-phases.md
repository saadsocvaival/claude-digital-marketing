---
name: build-phases
owner_tier: infra
status: draft
phase: 1
---

# Build Phases — Tracker

Ten-phase plan for constructing the autonomous GTM Operating System. Phase 1 is currently in progress. Phases 2–10 are not started. No phase may begin before the prior phase is explicitly approved.

Legend: **[in progress]**, **[not started]**, **[complete]**, **[blocked]**.

## Phase 1 — Repository Architecture **[in progress]**

> **Iteration note (2026-04):** Phase 1 was iterated after a full re-extraction of the playbook. Role inventory (`01-playbook/department-level/role-inventory.md`) and tool inventory (`01-playbook/department-level/tool-inventory.md`) are now the authoritative sources; the agent tier structure expanded from 4 tiers to 5 tiers (adding explicit Head of Digital Marketing at Tier 2 and a Tier-5 coordinator/executive layer), and `06-connectors/` now scaffolds every tool named in the playbook MarTech stack and vertical tool tables.

Scaffold the repo, establish vocabulary, and lock the ownership model. No executable code.

Deliverables:
- Directory tree per `plans/make-first-things-clear-stateful-parrot.md`.
- Root docs: `README.md`, `ARCHITECTURE.md`, `CONVENTIONS.md`, `OWNERSHIP.md`, `GLOSSARY.md`.
- Governance seed: `00-governance/approval-matrix.md`.
- Orchestration seeds: `03-orchestration/orchestrator-spec.md`, `decision-boundary-layer.md`.
- Connector contract: `06-connectors/connector-standard.md`.
- Ledger schema: `09-execution-ledger/ledger-schema.md`.
- Approval workflow: `11-approvals/approval-workflow.md`.
- Feedback engine: `13-feedback-loop/recursive-optimization-engine.md`.
- This file.
- ~168 stub files with valid frontmatter under all leaf folders.
- Verbatim playbook copy in `01-playbook/source/`.

Exit criteria: user review + explicit approval.

## Phase 2 — Agent Hierarchy Design **[not started]**

Flesh out every agent spec with full authority fields and decision frameworks.

Deliverables:
- Each `.agent.md` filled with: authority_scope, can_delegate_to, escalates_to, requires_approval_for, refuses_when, audit_fields, decision-framework references.
- Playbook decomposition: `01-playbook/department-level/` and per-vertical folders populated from source.
- Prompt persona structure (not prompt bodies) in `05-prompts/agent-personas/`.
- Decision frameworks in `00-governance/decision-frameworks/` — one per high-level decision class.

## Phase 3 — Orchestrator Logic **[not started]**

Specify (still no runtime code) the CMO orchestration algorithms.

Deliverables:
- `03-orchestration/delegation-rules.md`, `dependency-map.md`, `state-machine/` diagrams.
- Refusal-condition catalog and DAG construction rules.
- Pseudo-code-free specification of routing, decomposition, and escalation algorithms.

## Phase 4 — Workflow Engine **[not started]**

Specify end-to-end workflows.

Deliverables:
- Each file in `04-workflows/` fully authored: trigger, inputs, participating agents, gates, sla, outputs, rollback.
- State-machine diagrams per workflow.
- Cross-workflow dependency matrix.

## Phase 5 — Connector Layer **[not started]**

Specify each platform connector plus deterministic output schemas.

Deliverables:
- Each `.connector.md` fully authored against `connector-standard.md`.
- Output schemas in `05-prompts/output-schemas/` as `.schema.json` (first files with executable-adjacent content).
- Credential store spec finalized in `07-resources/credential-store-spec.md`.
- Resource-discovery protocol validated.

## Phase 6 — Execution Layer **[not started]**

First runtime code. Implements agents against specs from Phases 2–5.

Deliverables:
- Agent runtime (language: Python + LangGraph/CrewAI per decision in plan).
- Connector client implementations.
- Workflow executor.
- Does NOT yet include ledger, logging, feedback, or human approval.

## Phase 7 — Logging + Ledger **[not started]**

Make the system auditable.

Deliverables:
- Ledger storage + hash-chain implementation.
- Telemetry pipeline per `10-logging/`.
- Lineage/query tooling.
- Backfill strategy for Phase 6 events.

## Phase 8 — Feedback Loop Engine **[not started]**

Close the loop.

Deliverables:
- Signal ingestion connectors (inherit Phase 5 connector infra).
- Weighting and scoring implementation.
- Cadence runners (daily/weekly/monthly).
- Policy-update emitter + `policy_version` plumbing.

## Phase 9 — Human Approval Layer **[not started]**

Build the review interface and SLA monitor.

Deliverables:
- Review interface per `16-human-review/review-interface-spec.md`.
- Queue routing per `11-approvals/approval-workflow.md`.
- SLA monitor + escalation runner.
- Notification integrations.

## Phase 10 — Production Deployment **[not started]**

Ship it.

Deliverables:
- Environment definitions (`15-deployment/environments.md`).
- Secrets management implementation.
- CI/CD.
- Runbook + on-call procedures.
- Go-live checklist.

## Status Summary

| Phase | Status | Blocker |
|---|---|---|
| 1 | in progress | — |
| 2 | not started | Phase 1 approval |
| 3 | not started | Phase 2 approval |
| 4 | not started | Phase 3 approval |
| 5 | not started | Phase 4 approval |
| 6 | not started | Phase 5 approval |
| 7 | not started | Phase 6 approval |
| 8 | not started | Phase 7 approval |
| 9 | not started | Phase 8 approval |
| 10 | not started | Phase 9 approval |
