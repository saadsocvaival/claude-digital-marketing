# Glossary

Shared vocabulary. One-line definitions. If a term appears in more than one doc, it is defined here and nowhere else.

## Funnel & Lifecycle

- **MQL** — Marketing Qualified Lead. A contact whose engagement signals meet a marketing-defined threshold indicating readiness for sales follow-up.
- **SQL** — Sales Qualified Lead. An MQL that sales has accepted as a genuine opportunity worth pursuing.
- **ICP** — Ideal Customer Profile. The firmographic and behavioral description of the highest-fit customer segment.
- **JTBD** — Jobs To Be Done. Framework defining the progress a customer is trying to make, not their demographic.
- **Pipeline stages** — Ordered states a lead or opportunity progresses through: Lead → MQL → SQL → Opportunity → Proposal → Closed-Won/Lost.
- **AARRR** — Acquisition, Activation, Retention, Referral, Revenue. The "pirate metrics" lifecycle funnel.

## Economics

- **CAC** — Customer Acquisition Cost. Total sales + marketing spend divided by new customers acquired in a period.
- **LTV** — Lifetime Value. Expected gross margin contribution from a customer over their relationship lifetime.
- **ROAS** — Return On Ad Spend. Revenue generated per unit of ad spend (e.g. $4 ROAS = $4 revenue per $1 spent).

## Prioritization Frameworks

- **ICE** — Impact, Confidence, Ease. Lightweight scoring (1–10 each, average or multiply) for rapid prioritization.
- **RICE** — Reach, Impact, Confidence, Effort. Scored as `(Reach × Impact × Confidence) / Effort` for more rigorous backlog ranking.
- **OKR** — Objectives and Key Results. Goal-setting framework: qualitative Objective + 3–5 measurable Key Results per cycle.

## Search

- **AEO** — Answer Engine Optimization. Optimizing content to be surfaced as direct answers in AI-driven search experiences.
- **GEO** — Generative Engine Optimization. Optimizing for inclusion and citation inside generative AI responses (e.g. ChatGPT, Perplexity, Google AI Overviews).

## Attribution

- **First-touch attribution** — 100% of credit assigned to the channel/campaign that produced the first recorded interaction.
- **Last-touch attribution** — 100% of credit assigned to the final interaction before conversion.
- **Multi-touch attribution (MTA)** — Credit distributed across multiple touchpoints along the journey (linear, time-decay, position-based, data-driven).

## Internal Terms

- **Execution ledger** — Immutable, hash-chained log of every meaningful decision and action taken by any agent (see `09-execution-ledger/`).
- **Decision-boundary layer** — Policy layer that prevents infinite loops and enforces delegation topology (see `03-orchestration/decision-boundary-layer.md`).
- **Deterministic-output contract** — Rule that same input + same policy version produces equivalent schema-bound output (see `14-quality-assurance/deterministic-output-contract.md`).
- **Approval gate** — A named decision point where a human or higher-tier agent must sign off before execution proceeds (see `11-approvals/gates/`).
