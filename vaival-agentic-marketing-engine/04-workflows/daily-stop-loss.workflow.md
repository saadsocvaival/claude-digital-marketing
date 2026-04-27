---
name: daily-stop-loss.workflow
owner_tier: department-head
owner_vertical: paid-media-ppc
primary_agent: head-of-performance
playbook_source: §10.4 Workflow B, §10.5
flows_ref: FLOWS.md §6
skills: [paid-ads, campaign-analytics, performance-reporter, hitl-request]
status: active
phase: 2
---

# Daily Stop-Loss Workflow

Daily paid-media health check with policy-driven auto-actions. Owns the §10 stop-loss rules.

## Trigger
- Daily 06:00 client-local (scheduler).
- On-demand on spend spike (>2× rolling 7-day daily mean).

## Actors
- **Owner**: Head of Performance (Paid).
- **Auto-actor**: paid-media agent under policy.
- **Escalation**: CMO Orchestrator on HITL gates.

## Inputs
- Per-active-campaign metrics from connectors: Google Ads, Meta, LinkedIn, Microsoft Ads.
- Trailing 7 / 14 / 21 day windows.
- Targets from `clients/{id}/okrs/` and campaign briefs (CPL, ROAS, CAC).

## Steps
1. **Pull**: fetch yesterday's spend, conversions, ROAS, CAC, frequency per campaign per platform.
2. **ROAS rule**: if ROAS <1 for **14 consecutive days** on any campaign → **auto-pause** + ledger event + Slack alert.
3. **CAC rule**: if CAC >1.5× target for **21 consecutive days** → **reallocate** (cap shift to top-performing campaign per channel; max 20% reallocation without HITL).
4. **Frequency rule**: ad-set frequency >3.5 → **auto-trigger creative refresh task** in Trello/Notion + notify Paid Media Manager.
5. **Spend spike rule**: any campaign with daily spend >$1k → **HITL gate** before any further scale; pause on no-response within 24h.
6. **Cross-platform variance**: if platform vs GA4 variance >10% → pause optimization actions (read-only) and route to Analytics-Ops.
7. **Persist**: append all actions to `ledger-events/` with prior-state snapshot for rollback.
8. **Digest line**: contributes a "Stop-Loss Actions" line to the next weekly digest.

## Outputs
- Ledger events per action.
- Auto-pause / auto-reallocate / refresh-task records.
- HITL requests for spend-spike + reallocations >20%.
- Daily stop-loss summary (machine-readable JSON + human bullet list).

## Rubric
`rubrics/skill.yaml` for the agent execution. Reallocations also re-graded against `rubrics/campaign-brief.yaml` ≥8.

## HITL Gates
- Single-campaign daily spend >$1k.
- Reallocation moving >20% of channel budget.
- Pausing a campaign that is the sole channel for an active OKR commitment.
- Anomaly > 3σ on conversions (could be tracking outage, not performance).

## Failure Modes
- Connector outage → workflow degrades to read-only; surfaces as HITL "stale data, manual review needed."
- Attribution discrepancy → freeze optimization actions on the affected channel.
- Conflicting OKR (growth vs efficiency) → escalate to CMO.

## Ledger Events Emitted
`paid.stoploss.paused` · `paid.stoploss.reallocated` · `paid.stoploss.creative_refresh_queued` · `paid.stoploss.hitl.spend_spike` · `paid.stoploss.skipped.attribution_drift` · `paid.stoploss.summary.daily`.
