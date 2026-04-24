---
name: onboarding
description: Zero-knowledge client onboarding. Runs only the highest-leverage questions (12) to produce a populated Client Ledger. Use when activating a new client; never for an existing client.
invoked_by: cmo-orchestrator
inputs: { client_name: string, goal?: string }
outputs:
  - clients/{id}/ledger.md
  - clients/{id}/icp.md  (draft)
  - clients/{id}/secrets.pointer.md (stub)
rubric: rubrics/client-ledger.yaml
---

# Onboarding Skill — Zero-Knowledge Mode

## Purpose
Produce a populated Client Ledger with only the highest-leverage information, so Phase 2 (Goal Decomposition) can run without fabrication.

## Operating principle
**Ask the fewest questions that unblock the most downstream work.** Every question earns its seat.

## The 12 questions (ask in order; skip only with operator opt-out)

### Business context (3)
1. **What is the product in one sentence, and who is it for?** *(Populates: positioning seed, ICP seed.)*
2. **What is the current revenue stage and growth rate?** *(Seed → Series B → PE / bootstrap → $1M → $10M → $50M+ ARR; and last-12-month growth %). (Populates: ambition bar, budget realism.)*
3. **What is the 12-month business goal set by the CEO/board?** *(Populates: NSM direction + priority.)*

### Ideal customer (2)
4. **Top 1–3 customer segments by revenue today, and is that the segment you want MORE of (or a different one)?** *(Populates: ICP, segment-expansion vs deepening.)*
5. **Most recent 5 closed-won customers: company type + why they bought.** *(Populates: proof points, messaging, positioning refinement.)*

### Competitive & category (1)
6. **Who do you lose to most often, and what do they say that wins?** *(Populates: competitive frame, battlecard seeds, messaging gaps.)*

### Go-to-market reality (2)
7. **Current channels ranked by contribution to pipeline (if known) or spend (if not).** *(Populates: channel priors, reallocation headroom.)*
8. **What is the sales motion — PLG, sales-led, hybrid, partner?** *(Populates: lifecycle programs, lead-scoring weights, attribution window.)*

### Constraints (2)
9. **Marketing budget envelope for the next 90 days (total + rough allocation if any).** *(Populates: budget gates, feasibility.)*
10. **Team size + shape** (in-house vs agency vs freelance, per vertical). *(Populates: execution capacity, what can be automated.)*

### Access & risk (2)
11. **Which tools are live today** — list CRM, ESP, analytics, ads platforms, CMS — with noting whether credentials can be provided now or later. *(Populates: `secrets.pointer.md`, connector readiness, HITL queue.)*
12. **Any hard constraints** — regulated industry, brand pitfalls to avoid, legal or compliance rules, taboo tactics, geos excluded. *(Populates: refusal conditions, policy overlays.)*

## Rules while asking

- Ask ONE question at a time unless operator explicitly says "ask them all at once."
- Never assume an answer. If skipped, mark the field `UNKNOWN — requires validation` and add to `clients/{id}/hitl-queue.md`.
- Never fabricate customer names, revenue figures, or competitive intel. If operator answers vaguely, accept vague — do not sharpen.
- If answer reveals a regulated industry (finance, health, gambling, regulated substances), stop and load the corresponding compliance overlay (see `vaival-agentic-marketing-engine/00-governance/refusal-conditions.md`) before proceeding.

## Output: `clients/{id}/ledger.md`

Use this exact structure:

```markdown
# Client Ledger — {Client Name}
*Onboarded: {ISO date} | Owner: Orchestrator | Status: active*

## 1. Business
- Product (1 sentence): ...
- Revenue stage: {seed/early/growth/expansion}
- ARR (if shared): $...
- Last-12-month growth: ...%
- 12-month goal: ...

## 2. ICP (seed — to be refined)
- Primary segment: ...
- Secondary segment: ...
- Expansion target: {same / new — describe}

## 3. Competitive frame
- Top 3 rivals + their winning narrative: ...

## 4. GTM
- Motion: PLG / sales-led / hybrid / partner
- Channels (ranked): 1. ... 2. ... 3. ...
- Current CAC / LTV (if known): ...

## 5. Constraints
- 90-day budget envelope: $...
- Team shape: ...
- Regulated industry: yes/no → overlay: {...}
- Hard no-gos: ...

## 6. Tool stack & credentials
| Tool | Purpose | Creds available? | Notes |
|---|---|---|---|
| GA4 | analytics | yes/later | ... |
| HubSpot | CRM | yes/later | ... |
| Google Ads | paid search | yes/later | ... |
| LinkedIn | paid social | yes/later | ... |
| ... | ... | ... | ... |

## 7. Open validations (add to HITL queue)
- [ ] {field marked UNKNOWN — reason}
- ...

## 8. Onboarding digest
{3-sentence summary for operator + Orchestrator handoff}
```

## Success criteria (self-rubric)

- All 12 questions asked or explicitly skipped with rationale
- Zero fabricated facts (every field sourced or marked UNKNOWN)
- HITL queue populated with open validations
- Regulated-industry overlay loaded if applicable
- Ledger renders cleanly; handoff to `goal-decomposer.skill.md` is unambiguous

Rubric target: `rubrics/client-ledger.yaml` ≥ 8/10.
