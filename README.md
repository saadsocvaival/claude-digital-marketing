# Claude Digital Marketing — Autonomous Department OS

> **v1.1 — SME-hardened.** An evidence-grade, rubric-gated, client-agnostic Operating System for running a Digital Marketing department with Claude Code. CMO-level Orchestrator → 8 Department Heads + 3 Motion Leads → specialist skills → per-client state. Every artifact graded via `min(self-score, adversarial-critic-score) ≥ 8` before it ships.

## v1.1 diff vs v1.0 (honest)
Senior SME review of v1.0 flagged 17 methodology gaps. v1.1 closes 15 of 17 as authored work; 2 (MMM empirical fit, incrementality empirical proof) require real pipeline data and are gated to Stage 3.5. Headline additions: metric-tree decomposition, triangulated attribution (MTA + MMM + incrementality), two-phase lead scoring, motion-based overlay (acquisition/activation/retention), Head of RevOps, adversarial-critic gate, real GEO/AEO methodology, unit-economics standing section. See [CHANGELOG.md](CHANGELOG.md) for the full diff.

---

## What this is

Most "AI marketing agents" are thin prompt wrappers. This repo is different: it's a full **operating system** modeled on a real marketing org.

- A **CMO Orchestrator** receives a goal like *"Achieve 50% ARR growth for {client}"* and decomposes it into an NSM, supporting metrics, a 90-day plan, and per-Head OKRs.
- **8 Department Heads** — Growth, Performance, SEO/GEO/AEO, Content, CRO, Analytics, Automation, Brand — each with a defined remit, decision authority, skills, feeds they publish, and HITL triggers.
- **Client-agnostic**: each client lives under `clients/{id}/` with a standard directory contract. Onboard a new client by copying `clients/_template/`.
- **Rubric-gated quality**: every artifact type has a rubric in `/rubrics/` with a pass bar of 8. Artifacts below bar do not ship.
- **Dogfooded**: `clients/_fixture_devtools_saas/` is a fully populated reference client (~40 artifacts) proving the system end-to-end.

## Quick start — run the fixture

Prereq: [Claude Code](https://claude.com/claude-code) with this repo cloned.

```bash
cd claude-digital-marketing
claude
```

In the Claude Code session, paste:

> *Acting as the CMO Orchestrator defined in CLAUDE.md, load the fixture client at `clients/_fixture_devtools_saas/`. Read the ledger, the 90-day plan, and this week's KPI snapshot. Produce the weekly operator digest in the format specified, including per-Head actions for the next 7 days and any HITL items.*

The orchestrator will:
1. Load ledger + plan + KPI snapshot.
2. Delegate to 8 Department Heads.
3. Assemble a weekly digest conforming to the rubric `/rubrics/weekly-digest.yaml`.
4. Surface HITL items (e.g., BigQuery access blocker, budget reallocation decision).

## Add a new client

```bash
cp -r clients/_template clients/acme-corp
```

Then invoke the Orchestrator with:

> *Run onboarding for `clients/acme-corp`. Ask me the 12 leverage questions from `skills/orchestration/onboarding.skill.md` one at a time.*

Output: a fully populated `ledger.md` that gates all downstream work.

## Execution flow

See **[FLOWS.md](FLOWS.md)** for 8 Mermaid diagrams covering: system map, onboarding sequence, weekly loop, per-artifact rubric gate, decision-authority matrix, stop-loss enforcement, HITL lifecycle, and a when/what/how table.

## Architecture

```
CLAUDE.md                          ← runtime entrypoint (6-phase operating protocol)
.claude/
  agents/cmo-orchestrator.md       ← hero Director agent
  agents/head-of-{8}.md            ← 8 Department Heads
  skills.manifest.json             ← skill ↔ agent binding
  settings.json                    ← permissions + pre-commit secret scan
skills/
  orchestration/*.skill.md         ← onboarding, goal-decomposer, weekly-tick, hitl-request
  <146 canonical skills>           ← the specialist library
rubrics/                           ← 19 YAML rubrics, pass bar 8
templates/                         ← 15 artifact templates
clients/
  _template/                       ← per-client directory contract
  _fixture_devtools_saas/          ← dogfood fixture, end-to-end
vaival-agentic-marketing-engine/
  01-playbook/                     ← the constitution (policy source)
  02-agents/                       ← existing agent specs (Tiers 1–3)
  04-workflows/                    ← 8 orchestration workflows
  17-testing/evals/                ← 10 golden eval cases
AUDIT.md                           ← coverage matrix
ROADMAP.md                         ← stages 0–5 with honest gating
SECURITY.md
CONTRIBUTING.md
```

## What's real today vs. what needs more work

**Real today (Stages 0–2):**
- Full runtime protocol (CLAUDE.md + 8 agents + 4 orchestration skills).
- 19 rubrics + 15 templates + multi-tenant scaffold.
- Fixture client end-to-end (40 rubric-graded artifacts, every strategic doc ≥94/100).
- 10 golden eval cases.

**Explicitly out of scope (Stages 3–5 — see `ROADMAP.md`):**
- Real MCP tool-calling to GA4 / Google Ads / LinkedIn / HubSpot / Webflow. Connectors are specified; the runtime tool definitions need credentialed integration testing.
- Autonomous cron scheduler. The weekly-tick skill assumes operator-triggered today.
- External CMO review. All quality grades are **self-rubric** — honest but unvalidated.
- Real-client pilot. The fixture is an archetype.

## Quality bar

No artifact ships below 8/10 on its rubric. `AUDIT.md` lists every artifact type in the system with its rubric and status. Contributors: read `CONTRIBUTING.md` before opening a PR.

## Security

Raw secrets never land in the repo. Per-client credentials live in a vault referenced by `secrets.pointer.md`. Pre-commit secret-scan hook blocks common patterns. See `SECURITY.md`.

## Credits

- Playbook: `/vaival-agentic-marketing-engine/01-playbook/` — the policy constitution.
- Skills: canonical set derived from community Claude-skill libraries, deduplicated.
- Architecture: inspired by the CareCart Operating System pattern (pods, ledger, feeds, HITL protocol).
