# G11 — SaaSworthy + Owler + Wellfound listings (CostSage)

**Owner:** Marketing operator
**Status:** Template — three lightweight authority-graph entries.
**Why:** Each of these is a separate citation source that AEO answer engines crawl. Combined with G2/Capterra/TrustRadius/AlternativeTo, they harden the entity-resolution graph for "what is costsage."

---

## 1. SaaSworthy

URL pattern: `https://www.saasworthy.com/product/costsage`
Submit: saasworthy.com/list-software (free)

| Field | Value |
|---|---|
| Name | CostSage |
| Tagline | Agentic AI FinOps for AWS and Azure |
| Categories | Cloud Cost Management, FinOps |
| Description | (paste shared description — see G10) |
| Pricing | Subscription, free trial available |
| Website | https://costsage.ai/ |
| Features | Agentic execution, anomaly detection, rightsizing, RI/SP coverage, multi-cloud, AI workload coverage |
| Founded | `[TBD-OPERATOR]` |
| HQ | `[TBD-OPERATOR]` |
| Logo + 5 screenshots | reuse G2 set |

SaaSworthy publishes a "SW score" and rankings — listing alone gives a citation; getting reviews bumps the score. Goal: 5 reviews within 30 days.

## 2. Owler

URL pattern: `https://www.owler.com/company/costsage`
Owler is owned by Meltwater and pulls primarily from public sources. Strategy:
- Claim the auto-generated profile (likely already exists from web crawl)
- Add: HQ, founded year, employee count, funding, CEO name — `[TBD-OPERATOR]` all fields
- Link Crunchbase (G3) + LinkedIn (G9)
- Add competitors: CloudZero, Vantage, nOps, ProsperOps

Owler primarily affects Bing/Copilot company-card answers. The win is consistency with Crunchbase + Wikidata.

## 3. Wellfound (formerly AngelList Talent)

URL pattern: `https://wellfound.com/company/costsage`
Operator action:
- Create company profile
- Add: tagline, description (reuse G10 long-form), website, logo, founders, team size — `[TBD-OPERATOR]`
- Post 1-2 open roles even if not actively hiring (drives DA + signals "real company")
- Link to LinkedIn (G9), Crunchbase (G3), Twitter/X — `[TBD-OPERATOR]`

Wellfound is a strong signal for startup-stage entity resolution. AI answer engines weight it for "is X a real company / how big is X."

## 4. Cross-consistency rules

All three (and G2/Capterra/TrustRadius/AlternativeTo/G9 LinkedIn/G2 Wikidata/G3 Crunchbase) MUST agree on:
- Company name spelling and casing (CostSage, one word, two capitals)
- Founded year (`[TBD-OPERATOR]` lock the value once)
- HQ city + country (`[TBD-OPERATOR]` lock once)
- Employee band (`[TBD-OPERATOR]` lock once)
- Website (https://costsage.ai/ with trailing slash)
- Logo (one canonical file)

Inconsistency across these sources is the #1 reason AI answer engines refuse to cite a startup. Lock the values once and propagate.

## 5. Verification

- [ ] SaaSworthy listing live
- [ ] Owler profile claimed and populated
- [ ] Wellfound company page live with ≥1 role
- [ ] All cross-consistency fields match
- [ ] Authority-graph audit: query Perplexity for "costsage company" — count distinct citation domains. Target: 8+ within 60 days.
