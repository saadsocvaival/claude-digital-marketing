---
sprint: 1
resolves: F2 + R2
---

# Blog content plan — resolves the 10 dead links

## Decision: R2 Option C (hybrid)

- **Ship now (Sprint 1):** 2 highest-priority posts (`post-1`, `post-2` in this dir).
- **Remove for now:** 8 other H3 links from `/blog`. Re-introduce as drafts ship.
- **Authoring rule:** every blog post must (a) live at `/blog/<slug>`, (b) carry `Article` JSON-LD, (c) appear in `sitemap.xml`, (d) link to ≥2 internal pages including the pillar.

## The 10 listed posts → status

| # | Title (as listed on /blog) | Sprint | Status |
|---|---|---|---|
| 1 | 10 AWS cost optimisation best practices every SaaS company should follow | 1 | ✅ drafted (`post-1-aws-best-practices.md`) |
| 2 | Reserved Instances vs. Savings Plans: how to choose (and how an agent decides for you) | 1 | ✅ drafted (`post-2-ri-vs-sp.md`) |
| 3 | The best AWS cost optimisation tools in 2026 — and why agents beat dashboards | 2 | brief only |
| 4 | How Vulcan Forged cut their RDS costs by 60% in two weeks | 2 | needs case-study consent |
| 5 | Azure FinOps: The complete guide to cost management for 2026 | 2 | brief only |
| 6 | What does "agentic FinOps" actually mean? A practical definition | 2 | brief only |
| 7 | nOps Alternative: Why Teams Switch to CostSage for True FinOps Automation | 2 | duplicate of `/nops-alternative` — convert to /blog/ post or 301 |
| 8 | CloudZero Alternative: Beyond Unit Economics — Getting to Autonomous Savings | 2 | duplicate of `/cloudzero-alternative` — same |
| 9 | Why your AWS bill is 30% higher than it should be — and how an AI agent fixes it | 3 | brief only |
| 10 | Spending over $50K/month on AWS? Your agent is waiting. | 3 | conversion-led; could be a /lp/ rather than /blog/ |

## Routing recommendation

- Posts 1–6, 9: ship as `/blog/<slug>` with full `Article` schema.
- Posts 7–8: don't duplicate — `/blog/nops-alternative` should 301 → `/nops-alternative` (or vice versa); decide canonical.
- Post 10: ship as `/lp/aws-50k` (landing page) with `noindex` if it's a paid funnel asset, otherwise as `/blog/`.

## Until posts ship

Apply this patch to `/blog/index` so the dead H3 links don't render:

```diff
- <h3>10 AWS cost optimisation best practices every SaaS company should follow</h3>
+ <h3><a href="/blog/aws-cost-optimisation-best-practices">10 AWS cost optimisation best practices every SaaS company should follow</a></h3>

- <h3>The best AWS cost optimisation tools in 2026 — and why agents beat dashboards</h3>
+ <!-- Coming soon — author by 2026-05-15 -->
```
For the 8 not-yet-shipped posts, replace each `<h3>` with an HTML comment until the author lands. Don't leave bare titles that look like dead links.
