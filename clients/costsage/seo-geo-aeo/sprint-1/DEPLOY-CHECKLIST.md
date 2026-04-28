# Sprint-1 Deploy Checklist

> Single source of truth for shipping Sprint-1 to costsage.ai.
> Every item is HITL-gated. Nothing auto-deploys.
> Order matters — F1 (robots) ships **last** so the new content is in place
> before LLM crawlers are invited in.

## Pre-deploy approvals

- [ ] **R1 — robots.txt policy** (Option B recommended) signed off by operator
- [ ] **R2 — blog plan** signed off (hybrid: ship 2 posts, hide other 8)
- [ ] **R3 — `/aws` priority** confirmed for this sprint
- [ ] **R4 — credentials rotated** and `secrets.pointer.md` populated with vault refs
- [ ] **Founder names + bios** confirmed for `Person` schema (`schema/person-about.json`)
- [ ] **AWS Marketplace status** confirmed for `/aws` FAQ ("Is CostSage AWS Marketplace listed?")
- [ ] **Customer-savings claims** ($61K/month, 35%) confirmed as truthful and citable
- [ ] **softwareVersion / datePublished** values for SoftwareApplication confirmed

## Deploy order (each step is its own approval gate)

### Stage 1 — Content + schema (no crawler-policy change yet)
1. [ ] Apply typography fixes (`copy/typography-fixes.md`) — 5 H1/H2 strings
2. [ ] Add `<html lang="en-GB">` site-wide (`patches/html-lang.md`)
3. [ ] Insert canonical answer blocks on home, /features, /pricing, /azure (`copy/canonical-answer-blocks.md`)
4. [ ] Add 9 `BreadcrumbList` blocks (`schema/breadcrumb-patches.md`)
5. [ ] Replace homepage `SoftwareApplication` with enriched version (`schema/softwareapplication-enriched.json`)
6. [ ] Add `HowTo` to `/data-access` and `/azure` (`schema/howto-*.json`)
7. [ ] Add comparison schema graph to `/nops-alternative` and `/cloudzero-alternative` (`schema/comparison-pages.json`)
8. [ ] Add `Person` graph to `/about` (`schema/person-about.json`) — **only after names confirmed**
9. [ ] Apply internal-linking patch (`patches/internal-linking.md`) — 12 link insertions

### Stage 2 — New surface
10. [ ] Ship `/aws` page (`pages/aws.html`) + canonical answer block + HowTo + breadcrumb
11. [ ] Ship `/blog/aws-cost-optimisation-best-practices` (`blog/post-1-aws-best-practices.md`)
12. [ ] Ship `/blog/ri-vs-savings-plans` (`blog/post-2-ri-vs-sp.md`)
13. [ ] Clean up `/blog` index — remove or comment out the 8 dead-link H3s (per `blog/plan.md`)
14. [ ] Replace `sitemap.xml` with `sitemap.xml.proposed`
15. [ ] Ping Google Search Console + Bing Webmaster: re-submit sitemap

### Stage 3 — Crawler policy flip
16. [ ] Replace `robots.txt` with `patches/robots.txt.proposed` (Option B)
17. [ ] Verify with `curl -A "ClaudeBot" https://costsage.ai/robots.txt` returns the new policy
18. [ ] Verify with `curl -A "ClaudeBot" -I https://costsage.ai/aws` returns 200

## Post-deploy validation (within 24h)

- [ ] Re-crawl: `for url in $(grep -oE '<loc>[^<]+' sitemap.xml | sed 's/<loc>//'); do curl -sI -A "Googlebot" "$url" | head -1; done` — every URL returns 200
- [ ] Schema validators clean: paste each page URL into https://validator.schema.org and Google Rich Results test
- [ ] Lighthouse run on `/`, `/aws`, `/azure`, `/finops-agent-vs-dashboard`, `/blog/aws-cost-optimisation-best-practices` — log results to `clients/costsage/feeds/lighthouse-baseline-2026-04-XX.json`
- [ ] BMI-LLM dry-run query against Claude / ChatGPT / Perplexity for "what is CostSage" / "how does CostSage work on AWS" / "nOps vs CostSage" — log to `clients/costsage/feeds/bmi-llm-baseline-2026-04-XX.md`
- [ ] Search Console: verify zero new 404 sources after blog cleanup
- [ ] Update `clients/costsage/ledger.md`: status `pending-onboarding` → `active`, append Sprint-1 events

## Rollback plan

Each artifact is independently reversible:
- robots.txt — revert via Cloudflare Workers / origin file
- New pages (/aws, blog posts) — return 410 Gone or 301 to nearest equivalent
- Schema patches — remove the `<script>` blocks; existing schema unaffected
- Sitemap — revert to current `sitemap.xml`

## Owner matrix

| Stage | Owner | Approver |
|---|---|---|
| Typography + lang + breadcrumbs | Tech lead | Marketing lead |
| Canonical answer blocks | Marketing lead | Brand |
| SoftwareApplication / HowTo / comparison schema | Tech lead | Marketing lead |
| Person schema | Marketing lead | Founder |
| Internal linking | Marketing lead | Tech lead |
| /aws page | Marketing lead | Brand + Tech lead |
| Blog posts | Marketing lead | Brand |
| Sitemap | Tech lead | Marketing lead |
| robots.txt | Tech lead | **Operator (R1)** |
