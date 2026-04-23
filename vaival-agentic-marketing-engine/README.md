# vaival-agentic-marketing-engine

Autonomous GTM Operating System for Vaival. Single-tenant. An agentic marketing department that plans, executes, measures, and optimizes go-to-market work end-to-end with deterministic outputs, audit trails, approval gates, and a recursive feedback loop.

## Purpose

Replace the coordination overhead of a mid-size marketing team with a hierarchy of specialized agents that own verticals (SEO, Paid, Content, Social, Email/CRM, Analytics/Ops, Web), execute against Vaival's canonical playbook, and defer to human review only at well-defined decision boundaries (budget thresholds, external publishing, strategy changes, new credentials).

## 5-Tier Hierarchy

1. **Tier 1 — Founder (Principal)**: Sets ICP, positioning, strategy, budget envelopes. Final authority on strategy-change and major-spend approvals.
2. **Tier 2 — Executive (CMO + Head of Digital Marketing)**: CMO owns brand, messaging, and >$15k spend approval. Head of Digital Marketing reports to CMO and owns department leadership, budget, vertical-lead management, and $3k–$15k approvals. Together they are the cross-vertical orchestration layer.
3. **Tier 3 — Vertical Managers (7)**: SEO Manager, Paid Media Manager, Content Marketing Manager, Social Media Manager, CRM & Email Manager, Marketing Ops Manager, Web Development Lead. Plan and delegate within their vertical, report up to Head of Digital Marketing.
4. **Tier 4 — Specialists / Senior Specialists**: Per-vertical deep-skill ICs (e.g. Technical SEO + AEO Specialist, Paid Media Specialist, Senior Content Writer, Marketing Data Analyst, Front-End Developer, CRO Specialist).
5. **Tier 5 — Coordinators / Executives / Juniors**: Per-vertical execution layer (e.g. GEO Monitoring Coordinator, Community Manager, Email Production Coordinator, Attribution Analyst, CMS Page Builder). Invoked by Tier 3 or Tier 4 within the same vertical.

Five cross-cutting agents (Resource Discovery, Feasibility Validator, QA, Compliance, Recursive Optimizer) operate across tiers.

Every tool named in the playbook MarTech stack (§7, §9.4, §10.3, §14.3, §15.3 and workflow-level mentions) is scaffolded as a connector stub under `06-connectors/`. Canonical inventories live at `01-playbook/department-level/role-inventory.md` and `01-playbook/department-level/tool-inventory.md`.

## 10-Phase Build Order

1. Repo Architecture  ← **current (in progress)**
2. Agent Hierarchy Design
3. Orchestrator Logic
4. Workflow Engine
5. Connector Layer
6. Execution Layer
7. Logging + Ledger
8. Feedback Loop Engine
9. Human Approval Layer
10. Production Deployment

See `18-docs/build-phases.md` for deliverables per phase.

## Navigating the Repo

- `00-governance/` — decision frameworks, SOPs, approval matrix, escalation, refusal, audit policy.
- `01-playbook/` — canonical source of truth (user-provided playbook), decomposed into department-level docs, per-vertical folders, and marketing frameworks.
- `02-agents/` — agent specifications organized by tier, plus cross-cutting agents.
- `03-orchestration/` — CMO orchestrator contract, delegation rules, decision-boundary layer, state machine.
- `04-workflows/` — end-to-end workflow specs (GTM strategy, campaign launch, content production, etc.).
- `05-prompts/` — prompt template structure (populated Phase 2+).
- `06-connectors/` — integration specs for Google, Meta, LinkedIn, CRM, Email, CMS.
- `07-resources/` — access requirements, credential store spec, resource-discovery protocol.
- `08-memory/` — long-term, short-term, and shared memory specifications.
- `09-execution-ledger/` — immutable action log schema and taxonomy.
- `10-logging/` — logging standards, levels, observability.
- `11-approvals/` — approval workflow state machine and gates.
- `12-feasibility/` — pre-flight checks (budget, resource, timeline, capability, platform).
- `13-feedback-loop/` — performance ingestion, sales signal, attribution, recursive optimizer.
- `14-quality-assurance/` — output validation, brand-voice, compliance, deterministic-output contract.
- `15-deployment/` — placeholder until Phase 10.
- `16-human-review/` — reviewer interface spec, roles, SLAs.
- `17-testing/` — agent and workflow test strategies, red-team scenarios.
- `18-docs/` — onboarding, operating manual, phase tracker.
- `99-archive/` — deprecated specs.

## Phase 1 Non-Goals

- No executable code (no Python, no LangGraph/CrewAI wiring).
- No prompt bodies — only template scaffolding.
- No connector credentials or API calls.
- No CI/CD, tests, or runtime deployment artifacts.
- No `git init`.
- No implementation of agent logic, decision trees, or workflows — only their **specifications**.

The Phase 1 deliverable is architecture, vocabulary, and ownership — a readable, review-ready blueprint.
