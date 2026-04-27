# Canonical answer blocks — F6

Resolves `aeo-citation-audit.skill.md` requirement: every commercial page needs
a 50–80 word factual answer block, question-anchored, near the top, with FAQ
schema mirroring it for redundant LLM grounding.

Insert each block as a `<section>` immediately after the H1 hero, before the
existing body. Pair each with a corresponding `Question`/`Answer` entry in a
page-level `FAQPage` JSON-LD block (template at the bottom of this file).

---

## 1. Home `/` — "What is CostSage?"

**HTML to insert:**
```html
<section class="answer-block" data-question="What is CostSage?">
  <h2>What is CostSage?</h2>
  <p>
    CostSage is an Agentic AI system for FinOps. It connects to AWS and Azure
    in under 60 seconds via read-only IAM, reasons across your full
    infrastructure to identify waste, plans cost optimisations, and — once you
    approve — executes them autonomously. Customers cut cloud spend by 35% on
    average and find their first savings inside the first hour. ISO 27001
    certified. Free 14-day trial, no credit card required.
  </p>
</section>
```
Word count: 67. Anchor question: "What is CostSage?". Entities grounded:
CostSage, AWS, Azure, FinOps, IAM, ISO 27001.

---

## 2. `/features` — "What can the CostSage agent actually do?"

```html
<section class="answer-block" data-question="What can the CostSage agent do?">
  <h2>What does the CostSage agent do?</h2>
  <p>
    CostSage performs six core actions across AWS and Azure: AI rightsizing of
    EC2/RDS/VM instances, idle-resource detection and shutdown, Reserved
    Instance and Savings Plan optimisation, orphaned-disk and snapshot cleanup,
    tagging enforcement, and 12-month cost forecasting. Every recommendation
    shows its reasoning trace. Execution requires one human approval, then
    runs autonomously inside scoped IAM boundaries.
  </p>
</section>
```
Word count: 71. Entities: EC2, RDS, VM, Reserved Instance, Savings Plan, IAM.

---

## 3. `/pricing` — "How much does CostSage cost?"

```html
<section class="answer-block" data-question="How much does CostSage cost?">
  <h2>How much does CostSage cost?</h2>
  <p>
    CostSage uses outcome-based pricing: you pay only when the agent saves you
    money. There are no platform fees, no seat licenses, and no per-account
    charges. Customers identify an average of $61,000/month in cloud savings
    and recover the cost of CostSage inside the first week. Start with a free
    14-day trial — no credit card, no contract. See pricing tiers below.
  </p>
</section>
```
Word count: 73. Entities: outcome-based pricing, cloud savings, free trial.

---

## 4. `/azure` — "How does CostSage optimise Azure costs?"

```html
<section class="answer-block" data-question="How does CostSage optimise Azure costs?">
  <h2>How does CostSage optimise Azure costs?</h2>
  <p>
    CostSage connects to Azure through a Reader-role RBAC subscription in 60
    seconds, then continuously analyses VMs, managed disks, snapshots,
    Reserved Instances, and tag hygiene across every subscription. It surfaces
    oversized VMs, idle resources, orphaned storage, and Reserved Instance
    coverage gaps — typically reducing Azure waste by 35% or more. Execution
    happens only after explicit operator approval inside a scoped Contributor
    role.
  </p>
</section>
```
Word count: 73. Entities: Azure, RBAC, Reader role, Contributor role,
Reserved Instances, Managed Disks.

---

## 5. `/aws` (new — see `pages/aws.html`) — "How does CostSage optimise AWS costs?"

```html
<section class="answer-block" data-question="How does CostSage optimise AWS costs?">
  <h2>How does CostSage optimise AWS costs?</h2>
  <p>
    CostSage connects to AWS through a read-only IAM role in under 60 seconds,
    then continuously analyses EC2, RDS, EBS, S3, and Savings Plan / Reserved
    Instance coverage across every linked account. It identifies oversized
    instances, idle resources, orphaned EBS volumes and snapshots, and
    sub-optimal commitment coverage — typically reducing AWS waste by 35% or
    more. Execution runs only after explicit operator approval inside a scoped
    write role.
  </p>
</section>
```
Word count: 75. Entities: AWS, IAM, EC2, RDS, EBS, S3, Savings Plan,
Reserved Instance.

---

## FAQPage JSON-LD pattern (paired with each answer block)

For pages that already have `FAQPage` schema (e.g. `/pricing`), append the
block. For pages that don't, add a new `FAQPage` script tag that contains
**both** the canonical answer above AND any existing on-page FAQ items.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is CostSage?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "CostSage is an Agentic AI system for FinOps. It connects to AWS and Azure in under 60 seconds via read-only IAM, reasons across your full infrastructure to identify waste, plans cost optimisations, and — once you approve — executes them autonomously. Customers cut cloud spend by 35% on average and find their first savings inside the first hour. ISO 27001 certified. Free 14-day trial, no credit card required."
      }
    }
  ]
}
```

Repeat for each page with the page-specific question/answer above as the
first `mainEntity` item.
