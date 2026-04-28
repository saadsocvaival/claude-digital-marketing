# Landing Page Suitability Matrix — CostSage.ai

> Which existing page is right for which campaign, and what must be fixed before paid traffic hits it.

## Existing pages
| Slug | Intent served | Funnel stage | Conversion event | Pre-paid CRO uplift required? |
|------|---------------|--------------|------------------|-------------------------------|
| `/` | Brand-aware, generalist | TOFU/MOFU | `demo_request`, `cta_click` | Low — confirm hero loads ≤ 1.5s LCP |
| `/aws` | AWS-first ICP, primary | MOFU/BOFU | `demo_request` | **Medium — add inline form, social proof bar, FAQ** before scaling LinkedIn spend |
| `/azure` | Azure prospects (tier-2) | TOFU/MOFU | `demo_request` | High — page is thinner; do not push paid until parity with /aws |
| `/pricing` | Bottom-funnel evaluation | BOFU | `trial_start`, `cta_click` (book demo) | **High — needs visible self-serve tier + ROI calculator + FAQ** before sending paid clicks |
| `/compare/cloudzero-vs-costsage` | Switch / competitive | BOFU | `demo_request` | Low — confirm comparison claims sourced ("Per public docs") |
| `/compare/nops-vs-costsage` | Switch / competitive | BOFU | `demo_request` | Low — same |
| `/blog/aws-cost-optimisation-best-practices` | TOFU SEO | TOFU | `cta_click` (newsletter or related) | Medium — ensure inline CTA to /aws and content upgrade form |
| `/blog/ri-vs-savings-plans` | MOFU SEO | MOFU | `cta_click` → /aws | Medium — add inline demo CTA, related-content rail |

## Campaign → LP map

| Campaign | Primary LP | Secondary LP | Why |
|----------|-----------|--------------|-----|
| Google Search — AWS cost tools | `/aws` | `/compare/cloudzero-vs-costsage` for branded-comparison terms; `/pricing` for "pricing/cost"-suffixed queries | High intent, AWS-specific |
| Google Search — FinOps platform | `/aws` | `/blog/ri-vs-savings-plans` for educational queries | Broader query set; some education needed |
| LinkedIn — CTO sponsored | `/aws` | `/` for cold prospecting at top of funnel | CTO needs trust + scope, not feature depth |
| LinkedIn — FinOps lead sponsored | `/aws` | `/compare/cloudzero-vs-costsage` for switch angle | Practitioner wants depth + comparison |
| Microsoft Bing — AWS cost | `/aws` | `/pricing` | Mirror of Google with enterprise lean |
| Reddit — AWS/DevOps | `/blog/aws-cost-optimisation-best-practices` | `/aws` | Reddit users resist hard-sell; lead with content |
| Capterra/G2 sponsored | `/compare/cloudzero-vs-costsage` | `/pricing` | Review-shoppers are BOFU |

## CRO uplift list (blockers before scaling spend)

### `/pricing` — high priority
1. Self-serve tier visible above the fold (`[TBD-OPERATOR: confirm SMB tier price, assumed $499/mo]`).
2. Interactive ROI calculator (input: monthly AWS spend → output: estimated savings + CostSage cost).
3. FAQ: AWS Marketplace, SOC 2, contracts, upgrade/downgrade.
4. Form anti-friction: max 4 fields (work email, company, role, monthly cloud spend).
5. Trust strip: customer logos OR "X companies optimizing $Y M ARR of cloud" — `[TBD-OPERATOR-CLAIM-APPROVAL]`.

### `/aws` — medium priority
1. Sticky inline form (above fold + mid + foot).
2. Persona-segmented value props (CTO / VPE / Platform / FinOps tabs or sections).
3. AWS partner badge if available — `[TBD-OPERATOR]`.
4. 3-step "what happens after demo" timeline to reduce form anxiety.

### `/azure` — high priority (block paid)
- Bring to parity with /aws content depth before any paid Azure traffic. Today not recommended for paid.

### Blog pages
- Add content-upgrade form (RI/SP cheat sheet PDF) on `/blog/ri-vs-savings-plans`.
- Add inline demo CTA in first viewport on both blog posts.

## Page-level conversion event map (cross-ref `analytics/tag-plan.md`)
| Page | Primary event | Secondary events |
|------|---------------|-------------------|
| `/` | `cta_click` | `scroll_75`, `form_start` |
| `/aws` | `demo_request` | `form_start`, `cta_click`, `scroll_75` |
| `/pricing` | `trial_start` | `cta_click` (book demo), `form_start` |
| `/compare/*` | `demo_request` | `cta_click`, `scroll_75` |
| `/blog/*` | `cta_click` | `scroll_75`, `form_start` (newsletter / content upgrade) |
