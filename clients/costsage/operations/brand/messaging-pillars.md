# Messaging Pillars — CostSage

> Four pillars × audience × proof-points. Every asset CostSage ships should map to one pillar.
> Owner: Brand + PMM • v1.0 • 2026-04-28

---

## Pillar Map (one-line)

| # | Pillar | One-liner |
|---|---|---|
| 1 | Agentic, Not Dashboard | The agent ships the savings — not the chart. |
| 2 | 60-Second Time-to-Value | Connect AWS, see savings in under a minute. |
| 3 | Human-in-the-Loop Trust | Approval required. Rollback one click. Audit trail by default. |
| 4 | AWS-First SaaS Native | Built for the $50K–$500K/mo AWS bill, not for the Fortune 500. |

---

## Pillar 1 — Agentic, Not Dashboard

### Core claim
CostSage is the first agentic FinOps operator. It reasons over the bill, plans the cost work, and executes the change. Every legacy FinOps tool stops at visibility; we close the loop.

### Audience resonance

| Audience | What they hear | What they object | How we answer |
|---|---|---|---|
| VP Eng / Head of Platform | "I get my engineers' time back from FinOps tickets." | "AI doing prod changes makes me nervous." | Pillar 3 (HITL + rollback). |
| CFO / Head of Finance | "Cost savings actually land in next quarter's bill." | "Can I trust an AI to be conservative?" | Conservative defaults; approval flow. |
| FinOps Practitioner | "This makes me a director, not a ticket-writer." | "Will this replace my role?" | Reframe: agent runs the playbook *you* design. |
| Founder / CEO | "Runway extension without a hire." | "Is this real or vapor?" | 60-sec demo + before/after numbers. |

### Proof-points
- "Not a dashboard. Not a copilot. An agent that acts." (homepage)
- The action loop: identify → plan → approve → execute → audit → rollback.
- Average 34% reduction in compute costs [TBD-OPERATOR — confirm n].
- Comparison frame: visibility-only platforms vs. action-closing operators.

### Channels
Homepage hero, manifesto piece, comparison pages, founder podcast, LinkedIn organic, X threads.

---

## Pillar 2 — 60-Second Time-to-Value

### Core claim
Connect AWS in under 60 seconds. First recommendations surface the same minute. No 90-day implementation, no professional services SOW, no kickoff call.

### Audience resonance

| Audience | What they hear |
|---|---|
| Engineering buyer | "I can prove value before lunch." |
| Finance buyer | "ROI visible inside the trial." |
| Procurement | "Low-risk pilot — no implementation cost." |

### Proof-points
- "Connect AWS in under 60 seconds" (homepage CTA copy)
- "See first savings in <60s" (3-step onboarding)
- IAM read-only role, no agent, no install
- Side-by-side: typical FinOps tool onboarding (60–90 days) vs. CostSage (60 seconds)

### Channels
Trial CTA, demo video, paid search landing pages, sales one-pager, X threads.

---

## Pillar 3 — Human-in-the-Loop Trust

### Core claim
Every action requires explicit approval. Every change is reversible. Every recommendation is justified with the underlying data. ISO-certified, zero plain-text storage of credentials.

### Audience resonance

| Audience | What they hear |
|---|---|
| Security / SRE | "I am still in control of prod." |
| CFO | "I am not signing for autonomous spend changes." |
| Compliance (fintech/healthtech) | "Audit trail satisfies my reviewers." |

### Proof-points
- "Automation should amplify human judgment, not bypass it." (about page)
- ISO certification + zero plain-text credential storage [TBD-OPERATOR — confirm exact certs: ISO 27001, SOC 2 Type II?]
- Full justification: every recommendation shows underlying data
- One-click rollback on every action
- Confidence-scored recommendations (10 high-confidence over 100 low-confidence)

### Channels
Security page, comparison pages vs. "autonomous" tools, sales deck, regulated-vertical sales motion.

---

## Pillar 4 — AWS-First SaaS Native

### Core claim
We are built for the canonical AWS-first SaaS: $50K–$500K/mo AWS bill, 10–80 person engineering team, no dedicated FinOps hire. We are not trying to be the cost tool for the Fortune 500's multi-cloud footprint.

### Audience resonance

| Audience | What they hear |
|---|---|
| Series A–C SaaS founder | "This was built for me, not for IBM." |
| Platform engineer at scaling SaaS | "Defaults assume my stack — EKS, RDS, Lambda, S3." |
| FinOps practitioner at SMB | "I don't need an enterprise contract to use it." |

### Proof-points
- AWS-first product surface area (EC2, RDS, EKS, Lambda, S3, RI/SP)
- Azure secondary; GCP roadmap [TBD-OPERATOR confirm GCP timeline]
- Pricing aligned to spend tier, not seats — fits SaaS economics
- ICP-aware content: SaaS-specific tagging schemas, ARR-aligned commitment strategies
- "Teams on a $50K/mo cloud bill waste an average of $583/day" — exact ICP framing

### Channels
ICP-targeted blog posts, AWS Marketplace listing [TBD-OPERATOR], AWS partner ecosystem, FinOps Foundation Slack, SaaS-focused podcasts.

---

## Pillar Cross-Map (so nothing duplicates)

| Asset | Primary Pillar | Secondary |
|---|---|---|
| Homepage hero | 1 | 2 |
| "AWS Cost Optimisation 2026" pillar post | 4 | 1 |
| "FinOps for AI Workloads" pillar post | 1 | 4 |
| Whitepaper "AWS-First SaaS FinOps Playbook" | 4 | 1 |
| Comparison page vs. CloudZero | 1 | 3 |
| Newsletter Issue 1 | 1 | 4 |
| Sales one-pager | 2 | 1 |
| Security/Trust page | 3 | — |
| Founder podcast | 1 | 3 |
| Pricing page | 4 | 2 |

---

## Pillar Health-Check (quarterly)

- Are we publishing across all four pillars? (No fewer than 3 pieces per pillar per quarter.)
- Is one pillar over-indexing? (Cap at 40% of quarterly content volume.)
- Have we tested any new proof-point claims through legal/operator? (List in audit log.)
- Have we retired any disproven proof-points? (Record in `content/content-audit-rubric.md`.)
