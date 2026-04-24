---
name: weekly-tick
description: Weekly operating cadence. Reads cross-pod feeds, runs anomaly detection, enforces stop-loss, compiles HITL queue, produces operator digest. Invoke every Monday (or on-demand).
invoked_by: cmo-orchestrator
inputs:
  - clients/{id}/feeds/weekly-kpi-snapshot.md (required)
  - clients/{id}/heads-digest/*-week-{N-1}.md (required)
  - clients/{id}/experiments/active/*.md
  - clients/{id}/hitl-queue.md
outputs:
  - clients/{id}/memory/short-term/week-{N}.md
  - clients/{id}/digest/week-{N}.md  (operator-facing)
  - clients/{id}/ledger.md (appended with key decisions)
rubric: rubrics/weekly-digest.yaml
---

# Weekly Tick Skill

## Purpose
Run the Monday operational cadence. Convert last week's data + Head digests into a decision set: what to continue, what to kill, what to change, what needs operator input.

## Protocol

### Step 1 — Pre-flight (2 min equivalent)
Verify inputs present:
- `feeds/weekly-kpi-snapshot.md` from Head of Analytics — **blocker** if missing; escalate to Analytics and pause.
- 8 Head digests from previous week — **soft blocker**; note any missing Head and proceed with gaps flagged.
- Active experiments list (any `running` status in `experiments/active/`).
- HITL queue.

### Step 2 — KPI review & anomaly triage
From the snapshot:
1. Flag any NSM off-track (> -15% vs weekly pace to quarterly target).
2. Flag any funnel stage with Δ WoW > 15% (positive or negative — both warrant attention).
3. Cross-check: if Analytics flagged anomalies, confirm root cause ownership assigned.

### Step 3 — Stop-loss enforcement
Walk every active experiment and campaign. For each:
- Paid campaign: ROAS < 1.0 after significance OR CAC > 1.5× target → **auto-pause**.
- Growth experiment: hit stop-loss threshold → **auto-kill + writeup**.
- Content: zero traction at 14d → **do not amplify; schedule refresh or retirement**.
- Email sequence: complaint rate > 0.1% or bounce rate > 2% → **pause send, investigate**.

Document each action in ledger with justification.

### Step 4 — Cross-vertical synthesis
Look for patterns across Head digests:
- Where did two Heads raise the same risk? → elevate to plan-level.
- Where are dependencies breaking? (e.g., Performance waiting on Content briefs; CRO waiting on Web Dev ship.) → add to "unblock queue."
- Where has learning from one vertical transferred to another? → document in memory.

### Step 5 — Re-prioritize the next 7 days
For each Head, produce a 7-day action list (max 5 items) informed by:
- OKR progress vs plan (catch-up where behind, press advantage where ahead).
- New learnings (apply this week).
- Stop-loss actions (reallocate freed budget/capacity).
- Dependency unblocks.

### Step 6 — Compile HITL queue
Gather HITL items from:
- Each Head's digest.
- Stop-loss actions requiring operator note.
- Budget-threshold breaches.
- Credential requests (blocked executions).
- Escalations (legal, strategy-change).

Format per `skills/orchestration/hitl-request.skill.md`. Rank by blocking-impact × urgency.

### Step 7 — Produce operator digest
Write to `clients/{id}/digest/week-{N}.md` using the format specified in `.claude/agents/cmo-orchestrator.md` → "Response format."

Requirements:
- Exec summary ≤ 4 sentences.
- Every KPI table cell sourced from snapshot (no fabrication).
- HITL items ≤ 5 (if more, rank and show top 5 + note "and {N} more in queue").
- Risks section calls out any policy deviation.

### Step 8 — Append memory & ledger
- `memory/short-term/week-{N}.md` — structured notes: what moved, why, what we decided, open threads.
- `ledger.md` — append-only: key decisions, stop-losses, major changes, HITL outcomes.
- `ledger-events/week-{N}.jsonl` — machine-readable events (one JSON per line).

### Step 9 — Self-eval
Score digest against `rubrics/weekly-digest.yaml`. Iterate if < 8/10.

## Timing contract

This skill should complete end-to-end in a single Claude session. It is not meant to block on external inputs. If an external input is missing, fail-soft: note the gap, proceed with available data, flag the gap prominently in the digest.

## Anti-patterns

- Digest full of green; operator stops reading. Call out reality, good or bad.
- Stop-loss skipped "because it's close to threshold." Thresholds exist to remove judgment under pressure.
- HITL queue with >5 items. If >5, Orchestrator has been asking too much; compress or delegate.
- Re-litigating last week's decisions. Ledger is append-only.
