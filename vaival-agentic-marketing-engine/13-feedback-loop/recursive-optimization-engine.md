---
name: recursive-optimization-engine
owner_tier: cross-cutting
status: draft
phase: 1
---

# Recursive Optimization Engine

The engine that closes the loop between execution and strategy. It ingests performance signals, weighs them, updates SOPs and decision frameworks on defined cadences, and propagates those updates into the running agent hierarchy. It has NO direct execution authority — it proposes, the Orchestrator and gates dispose.

## Ingestion Sources

| Source | Signal Type | Frequency | Consumer Agents |
|---|---|---|---|
| Paid-media platforms (Google Ads, Meta, LinkedIn) | Campaign performance (CTR, CPA, ROAS, pacing) | Hourly | Paid Media Manager, Analytics/Ops |
| GA4 / Search Console | Organic traffic, engagement, rankings, CTR | Daily | SEO Manager, Content Manager, Analytics/Ops |
| CRM (HubSpot / Salesforce) — sales-feedback | MQL→SQL conversion, lead quality scoring, sales rejection reasons | Daily | CRM/Email Manager, CMO |
| CRM — CAC + LTV + retention trends | Unit economics | Weekly | CMO, Founder |
| Attribution system | Channel credit, journey shapes | Weekly | Analytics/Ops, CMO |
| Email platform | Deliverability, open, click, unsubscribe, complaint | Daily | CRM/Email Manager |
| Social platforms | Engagement, follower growth, share-of-voice | Daily | Social Media Manager |
| Experimentation system | A/B results with significance | On test completion | Originating Lead, CMO |
| Founder feedback | Qualitative directives, priority shifts | Ad hoc | CMO (directly) |
| Ledger analytics | Refusal rates, timeout rates, SLA breach rates | Daily | CMO, Recursive Optimizer (self) |

## Weighting Logic (High-Level)

Signals are weighted by three factors combined multiplicatively:

1. **Signal fidelity** — statistical significance, sample size, measurement reliability. A 10-conversion campaign gets less weight than 10,000.
2. **Strategic proximity** — how close the signal is to the current Founder priority. Signals aligned with the quarter's OKRs weigh higher than tangential ones.
3. **Recency decay** — exponential decay with half-life tuned per signal class: paid metrics (7d), organic rankings (30d), retention (90d), Founder feedback (no decay within quarter).

Weights feed into a scoring function that ranks proposed SOP/framework updates. Updates above a confidence threshold are drafted; below-threshold observations accumulate until they cross.

## Update Cadences

- **Daily** — tactical SOP updates: bid-strategy tweaks, creative-rotation rules, send-time adjustments, keyword pause lists. Auto-applied (logged, reversible).
- **Weekly** — operational framework updates: lead-scoring thresholds, attribution model weights, content-calendar cadence, experimentation prioritization. Require CMO approval.
- **Monthly** — strategic framework updates: channel-mix weights, ICP refinement evidence, pricing-narrative guidance. Require Founder approval (strategy-change gate).
- **Continuous** — meta-optimization: refusal-rate, timeout-rate, delegation-depth breach analytics feeding decision-boundary tuning.

## Signal → Consumer Map (Condensed)

- Paid perf ⇒ Paid Media Manager (tactical), CMO (budget re-allocation).
- Organic perf ⇒ SEO + Content Managers.
- MQL quality ⇒ CRM/Email Manager + Content Manager (upstream fit), CMO (ICP drift check).
- CAC/LTV drift ⇒ Founder + CMO (strategic).
- Attribution shifts ⇒ CMO (channel-mix), all Leads (credit recalibration).
- Ledger meta-signals ⇒ Recursive Optimizer itself + CMO (operational health).

## Propagation

Updates are emitted as ledger events of type `policy-update` with `policy_version` incremented. Agents read `policy_version` at the start of each decision and refuse to execute against a superseded version without explicit override. Because `policy_version` is stamped on every ledger event, decisions remain reproducible even after an update lands.

## Guardrails Against Drift

- **No silent strategic change.** Any monthly-cadence update touching ICP, positioning, or channel-mix MUST route through the strategy-change gate. The engine can propose, never ratify, a strategic change.
- **Evidence requirement.** Every proposed update carries a link to the ledger events and signal snapshots that justified it. Updates without evidence are refused by the CMO.
- **Rollback capacity.** Every policy update ships with a rollback descriptor pointing to the prior `policy_version`. If downstream metrics degrade within a defined observation window, the Optimizer auto-proposes reversion.
- **Change-budget per cadence.** At most N SOP updates per day and M framework updates per week, to prevent churn. Excess proposals queue to the next cycle.
- **Cross-signal sanity checks.** Before applying, the engine tests the proposal against the opposing signal class (e.g. a paid-performance-driven change is checked against retention and CAC; if it harms either, it's flagged, not applied).
