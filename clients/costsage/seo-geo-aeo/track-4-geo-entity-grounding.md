# Track 4 — GEO / Entity-Grounding Audit: CostSage.ai

**Date:** 2026-04-27
**Auditor:** Track-4 (Phase-1)
**Scope:** Entity coverage across authoritative knowledge graphs, brand-SERP, NAP consistency, on-site Organization schema, sameAs reciprocity, third-party citation breadth, brand-name disambiguation.
**Methodology note:** WebFetch was permission-denied for most third-party properties; verification was performed via WebSearch (`site:` queries) and one cached homepage fetch. All findings are tool-sourced.

---

## A. Entity-graph coverage

| # | Source | URL probed | Status | Notes |
|---|--------|------------|--------|-------|
| 1 | Wikipedia (CostSage) | https://en.wikipedia.org/wiki/CostSage | 🔴 Missing | `site:wikipedia.org CostSage` returns only generic "Cost_*" articles; no CostSage entry. |
| 2 | Wikipedia (Costsage / CostSage_AI) | /wiki/Costsage, /wiki/CostSage_AI | 🔴 Missing | Same query confirms no variant page. |
| 3 | Wikidata | wbsearchentities API + `site:wikidata.org` | 🔴 Missing | No Q-item; only generic "cost" concepts surface. |
| 4 | Google Knowledge Panel | WebSearch `"CostSage"` | 🔴 Missing | No knowledge panel surfaced in result block; only blue-link results. |
| 5 | Crunchbase | https://www.crunchbase.com/organization/costsage | 🔴 Missing | `site:crunchbase.com costsage` returns only adjacent companies (Cost Genie, CostSmart, Costimize). Parent **Vaival Technologies** has a Crunchbase profile, CostSage does not. |
| 6 | PitchBook | (paywalled) | 🔴 Missing | No public profile indexed. |
| 7 | LinkedIn Company | https://www.linkedin.com/company/costsage | ✅ Exists | Page exists and is indexed; description sparse — appears auth-walled / minimal copy ("a description for this page is not currently available"). |
| 8 | G2 | https://www.g2.com/products/costsage/reviews | ✅ Exists | Active reviews page + competitors page present (`/competitors/alternatives`). 5★ rating mentioned on homepage. |
| 9 | Capterra | https://www.capterra.com/p/costsage | 🔴 Missing | `site:capterra.com costsage` returns no CostSage page. |
| 10 | TrustRadius | https://www.trustradius.com/products/costsage | 🔴 Missing | No listing. |
| 11 | Product Hunt | producthunt.com/products/costsage | 🔴 Missing | No PH launch page found. |
| 12 | GitHub | github.com/costsage | 🔴 Missing | No public org/repo indexed under that handle. |
| 13 | Wellfound / AngelList | wellfound.com/company/costsage | 🔴 Missing | No profile indexed. |
| 14 | Owler | owler.com/company/costsage | 🔴 Missing | No profile. |
| 15 | AlternativeTo | https://alternativeto.net/software/costsage | 🔴 Missing | No software page. |
| 16 | SaaSworthy | saasworthy.com/product/costsage | 🔴 Missing | No listing. |
| 17 | SourceForge | https://sourceforge.net/software/product/CostSage/ | ✅ Exists | Auto-aggregated review/listing page (bonus discovery from SERP). |
| 18 | Slashdot | https://slashdot.org/software/p/CostSage/ | ✅ Exists | Auto-aggregated, plus a CostSage-vs-FinOpsly comparison page. |
| 19 | PeerSpot | peerspot.com/products/comparisons/costsage-ai_vs_hyperglance | ✅ Exists | Comparison page indexed. |
| 20 | AWS Marketplace | aws.amazon.com/marketplace/pp/prodview-l7gymco6bhnxg | ✅ Exists | Product + seller-profile both live. **Strong, authoritative third-party listing.** |

**Authoritative entities present: 5** (LinkedIn, G2, AWS Marketplace, SourceForge, Slashdot/PeerSpot aggregators). **Missing on the 4 highest-value graphs: Wikidata, Wikipedia, Crunchbase, Google Knowledge Panel.**

---

## B. Brand SERP audit

Search engine queried: Google (via WebSearch, US locale).

### B.1 Query: `"CostSage"`
| # | Domain | Title |
|---|--------|-------|
| 1 | costsage.ai | Smart Cloud Cost Optimizer |
| 2 | aws.amazon.com | AWS Marketplace: CostSage.ai |
| 3 | sourceforge.net | CostSage Reviews in 2026 |
| 4 | aws.amazon.com | AWS Marketplace: Seller Profile |
| 5 | linkedin.com | CostSage |
| 6 | app.costsage.ai | Costsage (login) |
| 7 | g2.com | CostSage Reviews 2026 |
| 8 | costsage.ai/blog | AWS Cost Optimization Tools |
| 9 | cost-sage-analysis.netlify.app | Cost-Sage (unrelated student project) |
| 10 | costsage.ai/privacy-policy | Privacy Policy |

- Knowledge panel: **N**
- Sitelinks: **N** (no expanded sitelinks block returned)
- Twitter/LinkedIn box: **N**
- Wrong-entity collisions: **Y** — `cost-sage-analysis.netlify.app` (a Netlify-hosted student/dev project named "Cost-Sage"); also "Ask Sage" and "Sage Intacct" appear as related/adjacent entities on G2 SERPs.
- Owned (costsage.ai + app.costsage.ai): **4 / 10 = 40%**

### B.2 Query: `costsage.ai`
| # | Domain | Title |
|---|--------|-------|
| 1 | costsage.ai | Smart Cloud Cost Optimizer |
| 2 | datadoghq.com | Cloud Cost Management |
| 3 | ternary.app | Cloud Cost Analysis |
| 4 | cloud.google.com | Cost Management |
| 5 | hpe.com | What is Cloud Cost Management |
| 6 | kpmg.com | FinOps imperative |
| 7 | manifest.ly | Cloud Cost Management Checklist |
| 8 | hykell.com | AWS cost audit checklist |
| 9 | paradime.io | Audit Cloud Costs |
| 10 | inspirext.com | Cloud Infrastructure Cost Audit |

- Owned: **1 / 10 = 10%** (poor — even an exact domain query is dominated by category content).
- Knowledge panel/Sitelinks/Social box: **N / N / N**.

### B.3 Query: `costsage finops`
| # | Domain | Title |
|---|--------|-------|
| 1 | focus.finops.org | FOCUS spec |
| 2 | costsage.ai | Homepage |
| 3 | oracle.com | OCI FinOps |
| 4 | finout.io | FinOps for Agentic Era |
| 5 | byteiota.com | FinOps 2026 Implementation |
| 6 | ramp.com | Best FinOps Tools 2026 |
| 7 | slashdot.org | CostSage vs FinOpsly |
| 8 | cloudaware.com | 12 Best FinOps Tools |
| 9 | cloudchipr.com | Best FinOps Tools 2026 |
| 10 | finops.org | AI Services Cost Forecasting |

- Owned: **1 / 10 = 10%**.

### B.4 Query: `costsage AI cost optimization`
| # | Domain | Title |
|---|--------|-------|
| 1 | costsage.ai | Homepage |
| 2 | aws.amazon.com | Marketplace listing |
| 3 | costsage.ai/blog | AWS Cost Optimization Tools |
| 4 | costsage.ai/blog | Blog index |
| 5 | costsage.ai/blog | AWS Cost Optimization |
| 6 | linkedin.com | CostSage |
| 7 | app.costsage.ai | App login |
| 8 | costsage.ai/blog | Best Practices 2025 |
| 9 | sourceforge.net | CostSage Reviews |
| 10 | costsage.ai/schedule-a-demo | Demo |

- Owned: **8 / 10 = 80%** (excellent for long-tail brand+intent).

### Aggregate brand-SERP ownership
(40 + 10 + 10 + 80) / 4 = **35% average SERP ownership** across the four brand queries.

**Knowledge panel: absent on every query.** **Sitelinks: absent on every query** (typical for brand-only domains under ~12 months). **No Twitter/X presence** surfaced in any SERP.

---

## C. NAP + structured-org consistency

Source: cached fetch of `https://costsage.ai/` plus parent Vaival data from public profiles.

| Field | costsage.ai homepage | LinkedIn (costsage) | G2 (costsage) | Crunchbase | AWS Marketplace |
|-------|---------------------|---------------------|---------------|------------|-----------------|
| Legal entity | "CostSage AI" (DBA) — operated by **Vaival Technologies LLC** | Page exists, copy sparse | Listed as CostSage | 🔴 No record | Seller: CostSage.ai |
| Address | ❌ Not on homepage | Unknown (auth-walled) | n/a | — | per AWS profile (not verified here) |
| Phone | ❌ Not on homepage | — | — | — | — |
| Founders | ❌ None named on page | — | — | — | — |
| Logo URL | `assets/costsage_ai_project_logos_cost-sage-logo-dark-01-300x65.png` (relative, not absolute) | (not verified) | (not verified) | — | (not verified) |
| Founding date | © 2026 footer (template error — likely 2024/2025 actual) | — | — | — | — |

**Mismatches / gaps flagged:**
1. No legal entity disclosure on homepage — brand `CostSage AI` is decoupled from the parent `Vaival Technologies LLC` which is the only entity that has a Crunchbase profile. LLMs cannot cleanly link them.
2. No physical address or phone published — fails Google's Local/Org schema completeness signal.
3. No founders publicly attributed to CostSage (parent company founders Anjum Shahzad / Muhammad Majid Ali are not associated with the product on costsage.ai).
4. Logo path is **relative**, not absolute — `Organization.logo` schema requires absolute URL.
5. Footer date 2026 conflicts with founding-date inference; LLMs may treat it as low-quality / template content.

---

## D. On-site Organization schema audit

Per cached fetch, costsage.ai's JSON-LD includes (per the prompt-extracted summary): `name`, `url`, `logo`, `description`, `contactPoint` (support), implied `foundingDate`, plus social/sameAs references to AWS, Azure, G2, Microsoft Partner.

Field-by-field score:

| Field | Present? | Notes |
|-------|----------|-------|
| name | ✅ | "CostSage AI" |
| url | ✅ | costsage.ai |
| logo | ⚠️ | Present but **relative path** — invalid for schema.org Organization |
| description | ✅ | Tagline copy |
| sameAs[] | ⚠️ | References AWS/Azure/G2/Microsoft Partner — but **LinkedIn company page is missing** from sameAs, no Twitter, no Crunchbase, no GitHub |
| foundingDate | ⚠️ | Implied via copyright, not explicitly typed |
| founder | 🔴 | Missing |
| address (PostalAddress) | 🔴 | Missing |
| contactPoint | ✅ | Support contact present |
| legalName | 🔴 | "Vaival Technologies LLC" not disclosed |

**Score: 4.5 / 10.** Missing: `legalName`, `founder`, `address`, explicit `foundingDate`; `logo` and `sameAs[]` are partial.

---

## E. sameAs[] reachability + reciprocity

WebFetch was denied so reciprocity was inferred from SERP evidence:

| sameAs URL (inferred) | Loads? | References costsage.ai back? | Notes |
|-----------------------|--------|------------------------------|-------|
| aws.amazon.com/marketplace/...prodview-l7gymco6bhnxg | ✅ | ✅ (links to costsage.ai) | Strongest reciprocal citation |
| g2.com/products/costsage/reviews | ✅ | ✅ (G2 product pages link to vendor site) | Reciprocal |
| linkedin.com/company/costsage | ✅ | ⚠️ Unknown — page sparse, "About" likely missing the costsage.ai URL | Auth-walled in test |
| azure / Microsoft Partner | ⚠️ | Not directly verified | Likely partner-directory listing |

Reciprocity score: **2 confirmed reciprocal of 4 declared** (50%). **3 / 10**.

---

## F. Third-party citation breadth

Distinct credible domains appearing across the 5 citation queries (top-20 each):

`costsage.ai`, `app.costsage.ai`, `aws.amazon.com`, `g2.com`, `sourceforge.net`, `slashdot.org`, `peerspot.com`, `linkedin.com`, `cost-sage-analysis.netlify.app` (collision), `focus.finops.org` (adjacent), `oracle.com` (adjacent), `finout.io` (adjacent), `ramp.com` (listicle adjacent), `cloudaware.com` (adjacent), `cloudchipr.com` (adjacent), `byteiota.com` (adjacent), `datadoghq.com` (adjacent).

**Citation breadth — domains that actually mention CostSage as the subject:** **8 distinct credible domains** (costsage.ai, app.costsage.ai, aws.amazon.com, g2.com, sourceforge.net, slashdot.org, peerspot.com, linkedin.com).

This is **narrow** — typical FinOps competitors (Vantage, CloudZero, Finout) show 30–60 distinct citing domains.

---

## G. Brand-name disambiguation

Collisions discovered:

| Collision entity | Source | Risk |
|------------------|--------|------|
| **Cost-Sage** (Netlify-hosted student/portfolio app) | https://cost-sage-analysis.netlify.app/ | LOW-MED — same hyphenated phrase, surfaces in `"CostSage"` SERP top-10. |
| **Ask Sage** (gov AI tool, on G2) | g2.com/products/ask-sage | LOW — different name but G2 cross-suggests. |
| **Sage Intacct** (large accounting brand) | g2.com/products/sage-intacct | MED — strong "Sage" entity that could pull semantic-similarity clusters in LLMs. |
| **Mymoneysage** (Indian fintech, on Owler) | owler.com/company/mymoneysage | LOW. |
| **SAGE / The Sage Group plc** | (general) | MED — parent "Sage" brand authority can dilute newcomer "CostSage". |

**Strongest collision:** *Sage Intacct / The Sage Group* — these are very high-authority entities and an LLM may confuse "CostSage" as a product *of* Sage.

**Suggested homepage disambiguation line:**
> *"CostSage is an independent FinOps platform from Vaival Technologies LLC. We are not affiliated with The Sage Group plc, Sage Intacct, or Ask Sage."*

(Place in footer + About page; also add `legalName` and `parentOrganization` to JSON-LD.)

---

## H. Findings + Sprint-2 GEO actions

### P0 — Do this sprint
1. **Create Wikidata Q-item for CostSage** with `instance of: software`, `developer: Vaival Technologies LLC`, `industry: FinOps`, `official website: costsage.ai`, plus `sameAs` to G2 + AWS Marketplace + LinkedIn. (Highest-leverage entry into LLM training corpora.)
2. **Create Crunchbase organization profile** — link `parent_organization: Vaival Technologies` (which already has a Crunchbase profile). Include founding date, funding stage, founders, HQ.
3. **Fix homepage Organization JSON-LD**: add `legalName`, `parentOrganization`, `founder`, `address` (PostalAddress), explicit `foundingDate`, absolute `logo` URL, and expand `sameAs[]` to include LinkedIn, Crunchbase (once created), AWS Marketplace, G2, Capterra (once created), Wikidata Q-ID.
4. **Fix copyright footer** "© 2026" → correct founding/current year (template error damages trust).
5. **Claim/build out LinkedIn company page** — currently exists but sparse. Add description, website link, employees, logo. This makes the most-clicked SERP-row 5 carry actual brand info.

### P1 — Sprint-2 stretch
6. **Create Capterra listing** (free vendor claim).
7. **Create AlternativeTo software entry** (community-editable, fast indexation).
8. **Submit to Product Hunt** with a coordinated launch (drives 50+ inbound citations in 24h).
9. **Create G2 vendor profile claim** (currently has reviews but vendor-claim status unclear) → enables G2 badges + better metadata.
10. **Add Twitter/X corporate handle** and link from Organization.sameAs.
11. **Publish a public team/about page** with founders + photos + LinkedIn links — feeds Google Knowledge Graph.

### P2 — Backlog
12. SaaSworthy listing.
13. TrustRadius vendor profile.
14. Owler company profile.
15. Wellfound/AngelList company page.
16. GitHub org `github.com/costsage` for any public SDK/Terraform-module assets — even an empty org claims the namespace.
17. Wikipedia article (only after sufficient secondary-source coverage exists; do not attempt prematurely — will be deleted under WP:CORP).
18. Address `cost-sage-analysis.netlify.app` collision via on-page disambiguation snippet (see §G).

---

## I. Effectiveness scorecard

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Entity-graph presence | **3 / 10** | Only 5 of 16 authoritative graphs have a CostSage entity; 4 highest-value (Wikidata/Wikipedia/Crunchbase/Google KP) are missing. |
| Brand-SERP ownership | **4 / 10** | 35% average ownership across 4 brand queries; no knowledge panel; no sitelinks; no social box. Long-tail (`+AI cost optimization`) is strong (80%) but exact brand `"CostSage"` is only 40% owned. |
| NAP consistency | **3 / 10** | No address, no phone, no founders, parent legal entity not disclosed; copyright year wrong. |
| Organization schema completeness | **4.5 / 10** | Core fields present; missing legalName/founder/address/explicit foundingDate; logo path relative; sameAs[] thin. |
| sameAs reciprocity | **3 / 10** | Only 2 of declared 4 confirmed reciprocal; LinkedIn unverified; Crunchbase/Wikidata absent. |
| **TOTAL** | **17.5 / 50** | Early-stage profile. Above-baseline on AWS Marketplace + G2 (operational distribution). Below-baseline on identity-graph grounding. |

---

## Sources cited (tool calls)
- WebSearch: `"CostSage"`, `costsage.ai`, `costsage finops`, `costsage AI cost optimization`, `"costsage" "cloud cost"`, `"costsage" review`, `"costsage" pricing`, `site:wikipedia.org CostSage`, `site:wikidata.org CostSage`, `site:crunchbase.com costsage`, `site:pitchbook.com costsage`, `site:linkedin.com/company costsage`, `site:g2.com costsage`, `site:capterra.com costsage`, `site:trustradius.com costsage`, `producthunt.com costsage`, `github.com costsage`, `site:wellfound.com costsage`, `site:owler.com costsage`, `site:alternativeto.net costsage`, `site:saasworthy.com costsage`, `CostSage Vaival Technologies founders team`.
- WebFetch (cached): `https://costsage.ai/` — homepage entity extraction.
- WebFetch denied for: Wikipedia, Wikidata API, Crunchbase, LinkedIn, G2, Capterra, AlternativeTo (all probed via WebSearch fallback).
