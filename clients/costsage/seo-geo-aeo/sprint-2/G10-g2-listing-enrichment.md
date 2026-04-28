# G10 — G2 Listing Enrichment (CostSage)

**Owner:** Marketing operator
**Status:** Template — operator claims/creates the G2 listing, then pastes these fields. `[TBD-OPERATOR]` markers flag fields requiring company-internal data.
**Category:** Cloud Cost Management (primary) + FinOps Platforms (secondary)

---

## 1. Claim or create

- **URL pattern:** `https://www.g2.com/products/costsage/`
- **Claim flow:** g2.com/products/claim → verify domain ownership via TXT record on costsage.ai DNS
- **Operator action:** `[TBD-OPERATOR]` — confirm whether listing already exists or needs creation

## 2. Core profile fields

| Field | Value |
|---|---|
| Product name | CostSage |
| Vendor | CostSage |
| Website | https://costsage.ai/ |
| Year founded | `[TBD-OPERATOR]` |
| HQ | `[TBD-OPERATOR]` |
| Employees | `[TBD-OPERATOR]` |
| Ownership | Private |
| Twitter / X | `[TBD-OPERATOR]` |
| LinkedIn | https://www.linkedin.com/company/costsage (G9) |
| Free trial | Yes — confirm with operator |
| Free version | `[TBD-OPERATOR]` |
| Starting price | See /pricing — `[TBD-OPERATOR]` paste exact tier |

## 3. Description (G2 long-form, 1,500 chars max)

```
CostSage is an agentic AI FinOps platform that finds and fixes cloud cost waste — instead of just reporting it. AI agents reason about your AWS and Azure cost data, plan optimisations (rightsizing, idle cleanup, RI/Savings Plan coverage, anomaly response), and execute with operator approval. Built for engineering-led teams that don't have a dedicated FinOps headcount and don't want another dashboard.

Key capabilities:
• Agentic execution — not dashboards-only
• AWS + Azure connectors with multi-cloud allocation
• Published pricing (no contact-sales gate)
• AWS Marketplace listed
• AI workload coverage — GPU, inference, training spend
• Anomaly detection with action recommendations
• RI / Savings Plan coverage planner

CostSage is suited to AWS- or Azure-first SMBs and growth-stage companies that want closed-loop savings without buying enterprise FinOps tooling.
```

## 4. Features checklist (G2 standard taxonomy)

Tick all that apply (operator verification needed for each):
- [x] Cost Allocation
- [x] Anomaly Detection
- [x] Recommendations / Rightsizing
- [x] Reserved Instance Management
- [x] Savings Plan Management
- [x] Budget Management
- [x] Reporting / Dashboards
- [x] Multi-Cloud (AWS + Azure)
- [ ] GCP — `[TBD-OPERATOR]` not yet
- [x] Agentic / Automated Optimisation
- [x] AI Workload Coverage
- [ ] Kubernetes — `[TBD-OPERATOR]` confirm
- [ ] Snowflake / SaaS spend — `[TBD-OPERATOR]`

## 5. Pricing tiers (paste from /pricing)

`[TBD-OPERATOR]` — paste current tier names, prices, and inclusions exactly as they appear on /pricing. G2 buyers heavily filter by published price.

## 6. Screenshots (5-8 required for "complete" badge)

1. Dashboard overview
2. Anomaly detection view
3. Rightsizing recommendations
4. RI/SP coverage planner
5. Multi-cloud allocation
6. Settings / connectors page

`[TBD-OPERATOR]` — capture from staging environment with redacted account IDs.

## 7. First-review campaign

Goal: 10 verified reviews within 30 days of listing going live.
- 5 from existing customers (operator outreach with G2 review-link)
- 3 from design partners
- 2 from AWS Marketplace buyers (G2 has Marketplace integration — operator to enable)

`[TBD-OPERATOR]` — operator to send review-request emails. Do **not** offer incentives that violate G2's review-policy (gift cards okay if disclosed; cash is not).

## 8. Comparison anchors

G2 surfaces "compared to" lists. Pre-publish comparison pages on our domain matching G2's competitor cards:
- /compare/cloudzero-vs-costsage (live)
- /compare/nops-vs-costsage (live)
- /alternatives/vantage (this sprint)
- /alternatives/prosperops (this sprint)

## 9. Verification

- [ ] Listing claimed
- [ ] Domain verified
- [ ] Description, features, pricing populated
- [ ] 5+ screenshots uploaded
- [ ] First 3 reviews live
- [ ] Profile reaches G2 "complete" status (gold checkmark)
