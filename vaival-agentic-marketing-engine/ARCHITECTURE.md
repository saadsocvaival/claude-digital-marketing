# Architecture

High-level shape of the autonomous GTM Operating System. Five tiers, seven verticals, five cross-cutting agents, one orchestrator layer (CMO + Head of Digital Marketing), one ledger, one feedback loop.

Canonical inventories:
- `01-playbook/department-level/role-inventory.md` — every role extracted from the playbook, by tier and vertical.
- `01-playbook/department-level/tool-inventory.md` — every tool extracted from the playbook MarTech stack and per-vertical tool tables.

## Hierarchy Diagram

```
                            ┌─────────────────────┐
                            │   Tier 1: FOUNDER   │  strategy, ICP, budget envelope
                            │     / CEO           │
                            └──────────┬──────────┘
                                       │ directive / escalation
                            ┌──────────▼──────────┐
                            │    Tier 2: CMO      │  brand, messaging, >$15k approval
                            └──────────┬──────────┘
                                       │
                            ┌──────────▼────────────┐
                            │  Tier 2: HEAD OF      │  dept. leadership, budget,
                            │  DIGITAL MARKETING    │  $3k–$15k approval, routing
                            └──────────┬────────────┘
                                       │ decomposition / routing
       ┌──────────┬──────────┬─────────┼─────────┬──────────┬──────────┬─────────┐
       │          │          │         │         │          │          │         │
   ┌───▼───┐  ┌───▼───┐  ┌────▼───┐ ┌───▼────┐ ┌─▼──────┐ ┌─▼──────┐ ┌─▼────┐
   │  SEO  │  │ Paid  │  │Content │ │ Social │ │ CRM &  │ │ Mktg   │ │ Web  │   Tier 3
   │ Mgr   │  │ Media │  │  Mgr   │ │  Mgr   │ │ Email  │ │ Ops    │ │ Dev  │  (Managers)
   │       │  │  Mgr  │  │        │ │        │ │ Mgr    │ │ Mgr    │ │ Lead │
   └───┬───┘  └───┬───┘  └────┬───┘ └───┬────┘ └──┬─────┘ └──┬─────┘ └──┬───┘
       │          │           │         │         │          │          │
   ┌───▼───┐  ┌───▼───┐    ┌──▼────┐ ┌──▼────┐ ┌──▼────┐  ┌──▼────┐  ┌──▼────┐   Tier 4
   │ spec. │  │ spec. │ … │ spec. │ │ spec. │ │ spec. │  │ spec. │  │ spec. │  (Specialists)
   └───┬───┘  └───┬───┘    └───┬───┘ └───┬───┘ └───┬───┘  └───┬───┘  └───┬───┘
       │          │            │         │         │          │          │
   ┌───▼───┐  ┌───▼───┐    ┌───▼───┐ ┌───▼───┐ ┌───▼───┐  ┌───▼───┐  ┌───▼───┐   Tier 5
   │ coord.│  │ coord.│ … │ coord.│ │ coord.│ │ coord.│  │ coord.│  │ coord.│  (Execs/Coords)
   └───────┘  └───────┘    └───────┘ └───────┘ └───────┘  └───────┘  └───────┘

  Cross-cutting (operate across all tiers, invoked by Head of Digital Marketing and Managers):
    • Resource Discovery   • Feasibility Validator   • Quality Assurance
    • Compliance/Legal     • Recursive Optimizer
```

## Control Flow

**Top-down delegation.** Founder issues a directive. CMO approves strategy-level implications. Head of Digital Marketing decomposes it into vertical-scoped tasks and routes to the relevant Managers. Each Manager plans and delegates to Tier 4 specialists; specialists may further delegate to Tier 5 coordinators within the same vertical.

**Delegation rules:**
- Managers (Tier 3) may delegate to Tier 4 AND Tier 5 within their own vertical.
- Tier 4 specialists may delegate to Tier 5 coordinators within the same vertical only.
- Cross-vertical coordination always routes through the Head of Digital Marketing (and through CMO when brand / strategy / >$15k thresholds trigger).
- No tier may invoke a sibling at the same tier cross-vertical. No specialist-to-specialist calls across verticals.
- Delegation depth is capped at 5 (Founder → CMO → Head of DM → Manager → Specialist → Coordinator).

**Bottom-up escalation.** Coordinators escalate to their Specialist; Specialists escalate to their Manager; Managers escalate to Head of Digital Marketing for cross-vertical conflicts or budget >$3k; Head of DM escalates to CMO for strategy/brand/ >$15k; CMO escalates to Founder on strategy change, crisis, or compliance breach.

## Data Flow

**Execution ledger.** Every meaningful decision and action emits a ledger event (`09-execution-ledger/ledger-schema.md`) — immutable, hash-chained, keyed by `event_id` with a `parent_decision_id` for lineage.

**Feedback loop.** Performance signals (ad metrics, GA4, GSC, CRM MQL/SQL quality, attribution, founder feedback) are ingested into `13-feedback-loop/`. The Recursive Optimizer weighs signals, updates SOPs and decision frameworks on daily/weekly/monthly cadences.

## Cross-Cutting Agents

- **Resource Discovery** — inventories credentials, platforms, and data sources available to agents; gates work behind resource readiness.
- **Feasibility Validator** — pre-flight checks (budget / resource / timeline / capability / platform) before any plan becomes execution.
- **Quality Assurance** — validates outputs against deterministic-output contracts and brand-voice rules.
- **Compliance / Legal** — reviews external-facing artifacts and credential onboarding.
- **Recursive Optimizer** — owns the feedback loop; no direct execution authority.

## Deterministic-Output Contract

Every agent output is schema-bound (JSON schema in `05-prompts/output-schemas/` from Phase 5). Same input + same policy version ⇒ equivalent structured output. Prose is confined to fields explicitly typed as free-text.

## Decision-Boundary Layer

A thin policy layer enforced by the Head of Digital Marketing agent (in cooperation with CMO for strategy-level gates) that prevents runaway or circular agent activity: specialists may not call specialists cross-vertical, managers may not call managers cross-vertical, all cross-vertical coordination routes through Head of Digital Marketing, and delegation depth is capped at 5. Full spec in `03-orchestration/decision-boundary-layer.md`.
