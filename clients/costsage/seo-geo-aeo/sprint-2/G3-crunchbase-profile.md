---
client_id: costsage
sprint: 2
gap: G3
artifact: crunchbase-profile-payload
date: 2026-04-27
priority: P0
audience: operator
---

# G3 — Crunchbase profile submission payload

> **Why this is P0:** Crunchbase is a tier-1 authority graph for tech companies. LLMs and SERP knowledge panels heavily weight it. Direct retrieval surface (Crunchbase pages rank in top-10 for `<brand> crunchbase` queries — already verified during Track-4 audit). Vaival Technologies parent already has a Crunchbase entry; CostSage should be linked to it.

## Submission steps (operator)

1. Sign in at https://www.crunchbase.com/ → click **Add a new company** (top-right "+" menu).
2. Fill in the fields below.
3. After save, share the URL — we'll add it to homepage Organization `sameAs` and Wikidata P2087 statement.

## Crunchbase fields

| Field | Value | Notes |
|---|---|---|
| Company name | `CostSage` | |
| Description (short, 75 chars) | `AI-native FinOps platform for cloud cost optimisation across AWS, Azure, GCP.` | exact |
| Description (long) | (paste 200-word section below) | |
| Website | `https://costsage.ai` | |
| LinkedIn | `https://www.linkedin.com/company/costsage` | |
| Twitter / X | `TBD` | confirm if handle exists |
| Founded date | `TBD-CONFIRM-WITH-OPERATOR` | YYYY-MM-DD |
| HQ location | `TBD-CONFIRM-WITH-OPERATOR` | city, region, country |
| Operating status | `Active` | |
| Company type | `For Profit` | |
| Number of employees | `1-10` (or pick range) | |
| Industries | `FinOps`, `Cloud Computing`, `Artificial Intelligence`, `SaaS`, `Cost Management` | up to 5 |
| Categories | `Software`, `Information Technology` | |
| Parent organization | `Vaival Technologies` | link to existing https://www.crunchbase.com/organization/vaival-technologies |
| Founders | `TBD-CONFIRM-WITH-OPERATOR` | names + LinkedIn URLs |
| Funding stage | `TBD` (likely Bootstrapped or Pre-Seed) | |
| Logo | upload PNG (transparent, ≥400×400) | |

## Long description (paste verbatim, edit dates as needed)

> CostSage is an AI-native FinOps platform that helps SaaS and cloud-first companies cut their AWS, Azure, and GCP bills automatically. Unlike traditional FinOps dashboards that surface waste but require humans to act, CostSage's agentic engine identifies savings opportunities — idle workloads, oversized instances, suboptimal Reserved Instance / Savings Plan portfolios, untagged spend, storage tiering — and either applies fixes directly (where guardrails permit) or routes them to engineering with one-click remediation.
>
> CostSage targets AWS-first SaaS teams with $10K–$500K/month cloud spend who have outgrown raw cost-explorer dashboards. Customers report savings of 25–40% on optimised workloads within the first 60 days, with the platform paying for itself in under a quarter.
>
> The product is available via the AWS Marketplace and direct subscription, with transparent self-serve pricing. CostSage is a Vaival Technologies company.

## Operator-confirmation TBDs

Need confirmed before submitting:
- [ ] Founding date (YYYY-MM-DD)
- [ ] HQ city / country
- [ ] Founder names + their LinkedIn URLs
- [ ] Funding stage + any rounds raised
- [ ] Approved customer-savings claim (the "25–40% within 60 days" text — confirm citable or replace)
- [ ] Twitter / X handle if any
- [ ] Logo file (PNG, transparent, ≥400×400)

## Reciprocity hook (after profile is approved)

1. Capture the canonical Crunchbase URL (format: `https://www.crunchbase.com/organization/costsage` or similar).
2. Add to homepage Organization `sameAs[]` array via overlay edit.
3. Add Crunchbase organization ID to Wikidata P2087 statement.
4. Append `entity.crunchbase.created` event to `clients/costsage/ledger-events/`.

## Verification (post-approval, ~24-72h)

- WebSearch `"CostSage" crunchbase` → Crunchbase entry top result.
- Re-run Track-4 entity-graph coverage: Crunchbase row flips ⚠️→✅.
- Check whether Vaival Technologies' Crunchbase profile now lists CostSage as a subsidiary/portfolio company (Crunchbase usually backfills this within a week).
