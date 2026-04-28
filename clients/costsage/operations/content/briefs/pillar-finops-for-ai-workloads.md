# Brief — Pillar: "FinOps for AI Workloads: The 2026 Playbook"

> Slot: W1-A • Type: pillar • Length target: 1,800–2,000 words • Status: brief approved, drafting next.
> Author: [TBD-OPERATOR] • Reviewer: Content Lead → Brand sign-off
> Voice contract: `operations/brand/voice-guidelines.md`

---

## TL;DR (60 words)
AI inference is the new highest-variance line item on the AWS bill, and FinOps practices built for steady-state EC2 don't bend to it. This piece is the operator-level playbook for putting cost discipline around training and inference workloads — sized for the AWS-first SaaS shipping AI features in 2026, not the hyperscaler running its own GPU farm.

## ICP / Reader
- **Role:** VP Engineering or Head of Platform at a Series B–C SaaS that has shipped AI features in the last 18 months.
- **Bill profile:** $50K–$500K/mo AWS, with 15–60% of growth coming from GPU spend (`p4`, `p5`, `g5`, Bedrock invocation, SageMaker).
- **Job-to-be-done:** "Stop the AI bill from eating my margin without slowing the AI roadmap."
- **Sophistication:** High. Knows what a `g5.xlarge` is, knows what a token costs, has no time for FinOps 101.
- **Mood:** Frustrated. The bill went up 3× in two quarters. CFO is asking questions. Engineers want to keep shipping.

## Search intent + keywords
- **Primary keyword:** "finops for ai workloads"
- **Cluster:** "ai inference cost optimization", "gpu cost optimization aws", "sagemaker cost", "bedrock cost", "ml cost management", "llm cost"
- **Intent:** Informational with strong commercial undertone (researcher mode → trial).
- **Primary entity:** TechArticle.
- **SERP scan:** Today's top results are vendor-neutral or hyperscaler-blog-shaped (AWS Well-Architected ML lens, a couple of consultant pieces). The missing angle: an *operator's* playbook with concrete %s, not a framework. CostSage's differentiated take = the agentic action loop applied specifically to AI workloads.

## Why this piece is the moat pillar
This is the single category-design piece for CostSage. It is the most defensible content asset because (a) GPU cost is the fastest-growing line item in 2026, (b) legacy FinOps tools have weakest coverage here, and (c) the agentic posture is most necessary here — the workloads are too volatile for a human to chase.

## Outline

### H1: FinOps for AI Workloads: The 2026 Playbook
*(working subhead: "Six places your AI bill is leaking, and the order to fix them.")*

### Intro (~150 words)
Open with the number: a typical AI-shipping SaaS in 2026 has GPU + inference spend growing 8–14% month over month while the rest of the bill grows 1–2%. State the thesis: FinOps practices designed for steady-state EC2 fail on AI workloads because the workloads themselves are non-stationary. Establish the enemy frame: "the dashboard era of FinOps has nothing to say about your AI bill."

### H2: Why AI workloads break FinOps-1.0
- Training is bursty; inference is bimodal (steady baseline + spike). Reservations don't fit.
- Per-token economics shift weekly as models update.
- Engineers can spin up `p5` capacity from a notebook — no procurement gate.
- Tagging discipline is weakest exactly where spend is highest.

### H2: The six leak categories (the ranked playbook)
1. **Idle GPU minutes** — typical recovery 18–34% of GPU spend. Describe `g5`/`p4` idle patterns.
2. **Wrong-tier inference endpoint** — SageMaker real-time vs. async vs. serverless; pick wrong, pay 4–10×.
3. **Bedrock model selection drift** — calling Opus where Haiku would do; cluster the workload.
4. **Untagged ML resources** — typical 25–40% of GPU spend untagged, blocking allocation.
5. **Missed Savings Plans on steady inference baseline** — this is where commitment coverage *does* apply.
6. **Storage tail** — model artifacts in S3 Standard that should be in IA / Glacier.

### H2: The order matters (and why)
Quick wins first (1, 4, 6) before structural moves (2, 3, 5). Reasoning: idle and tagging unlock visibility for the harder calls. State the typical 90-day savings curve: 12–18% in week 1, 28–35% by day 90 — across cohort. [TBD-OPERATOR — confirm cohort numbers before publication.]

### H2: Why an agent does this better than a quarterly review
- Workloads are too volatile for human cadence. By the time the FinOps review meets, the inference traffic shape has changed.
- The agent runs continuously; the human approves.
- Show the action loop: identify → plan → approve → execute → audit → rollback.
- Specifically call out the rollback path for AI workloads — capacity events make rollback non-negotiable.

### H2: The 90-day playbook (week-by-week)
Embed a table or visual: weeks 1–2 (audit + tag), weeks 3–4 (idle cleanup), weeks 5–8 (endpoint right-tiering), weeks 9–12 (commitment coverage on stable inference baseline).

### H2: FAQ
1. **Do Savings Plans cover GPU instances?** Yes — Compute SP covers `p`/`g` families. Coverage gap is on inference endpoints, not raw EC2.
2. **Should we use spot for inference?** Only for async/batch. Real-time inference + spot = SLA violations.
3. **How do we handle Bedrock cost when there's no instance to rightsize?** Model-tier selection + token-budget guardrails. Different mechanism, same FinOps logic.
4. **Does CostSage support Azure OpenAI / Vertex AI?** Azure: yes, secondary. GCP: roadmap [TBD-OPERATOR].
5. **What does the agent need to take action on a SageMaker endpoint?** A scoped IAM role with explicit endpoint update permissions, plus an approval flow.
6. **Will this piece help my team if we use serverless inference?** Yes — same six leak categories apply, just with different mechanisms.

### H2: Conclusion + CTA
Close on the category claim: "Agentic FinOps is the only posture that scales with AI workloads, because human cadence does not." CTA: "Connect AWS in under 60 seconds. The agent will surface your AI workload leaks before this article finishes loading on a slow connection."

## Internal links
- /blog/aws-cost-optimisation-best-practices (sibling pillar)
- /product (product overview)
- /pricing
- /blog/ri-vs-savings-plans (related)
- Whitepaper landing page (deliverable #11)

## External links
- FinOps Foundation framework page
- AWS Well-Architected ML lens
- One reputable analyst piece on inference cost ([TBD-OPERATOR — preferred analyst])

## CTA
- **Primary:** Trial signup ("Connect AWS in under 60 seconds")
- **Secondary:** Whitepaper download — "The AWS-First SaaS FinOps Playbook"

## Distribution map
- **V5:** LinkedIn (3-post sequence + 1 carousel), X (10-post thread), FinOps Foundation Slack #ai-workloads channel, HackerNews Show post, r/MachineLearning (linked from a comment, not a direct post).
- **V6:** Newsletter Issue 1 lead block (full deliverable #13).
- **Repurposing:** 5 LI posts + 3 X threads + 1 NL section + 1 sales card per `repurposing-engine.md`.

## Metadata
- Slug: /blog/finops-for-ai-workloads
- Meta title: "FinOps for AI Workloads: The 2026 Playbook | CostSage"
- Meta description: "Six places your AI bill is leaking and the order to fix them. The operator's playbook for AWS-first SaaS shipping AI in 2026."
- OG image: blog template with title overlay
- Canonical: self
- Length target: 1,800–2,000 words
