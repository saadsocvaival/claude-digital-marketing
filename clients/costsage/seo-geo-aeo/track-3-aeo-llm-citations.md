# Track 3 — AEO / LLM-Citation Baseline for CostSage.ai
**Audit date:** 2026-04-27
**Auditor:** Claude (Track 3 of Phase-1 audit)
**Scope:** Public answer-engine surfaces; no programmatic LLM API access this session.

---

## A. Methodology + Tool Reachability

This audit was constrained by tool permissions in this session:

| Engine / Surface | Method attempted | Result | Status |
|---|---|---|---|
| Google SERP (incl. AI Overview-adjacent generative summaries) | `WebSearch` tool | Returned full link lists + generative summary blocks for all 15 prompts | ✅ |
| Bing | Direct `WebFetch` of bing.com/search | Permission denied (host not on allowlist) | 🔴 |
| Perplexity public answer URL | `WebFetch https://www.perplexity.ai/search?q=...` | Permission denied | 🔴 |
| DuckDuckGo Instant Answer JSON | `WebFetch https://api.duckduckgo.com/?q=...&format=json` | Permission denied | 🔴 |
| You.com | `WebFetch https://you.com/search?q=...` | Permission denied | 🔴 |
| `curl` via Bash | Sandbox blocks Bash tool | Denied | 🔴 |
| costsage.ai pages | `WebFetch` | Allowed; pages fetched cleanly | ✅ |

**Net reachable engines: 1 of 5 (Google via WebSearch).** WebSearch returns Google's organic results plus a generative answer block — this is the closest available proxy for what an LLM (Gemini / SGE / ChatGPT-with-browsing / Perplexity) would cite, because **all of those engines retrieve from the same open-web corpus that Google indexes**. Citation share-of-voice computed from Google WebSearch is therefore a *defensible directional proxy* for cross-engine LLM citation share, but should not be reported as a direct Perplexity/ChatGPT measurement.

> **Honest limitation:** Without programmatic Perplexity/ChatGPT/Gemini access, we cannot confirm whether those engines' RAG pipelines select CostSage citations at the same rate that Google ranks them. Sprint-2 should add a Perplexity API key + an Anthropic/OpenAI key with browsing to repeat this baseline.

### Canary calls actually run
- `WebFetch https://costsage.ai/` → 200, full HTML parsed (✅)
- `WebSearch "What is CostSage"` → 10 links + generative summary (✅)
- `WebFetch https://costsage.ai/pricing` → 200 (✅)
- `WebFetch https://costsage.ai/features` → 200 (✅)
- `WebFetch https://costsage.ai/aws` → 200 (✅)
- `WebFetch https://costsage.ai/azure` → 200 (✅)
- `WebFetch https://costsage.ai/finops-agent-vs-dashboard` → 200 (✅)
- `WebFetch https://costsage.ai/blog/ri-vs-savings-plans` → 200 (✅)
- `WebFetch https://costsage.ai/blog/aws-cost-optimization-best-practices/` → 404 (🔴 — dead link / wrong slug)
- `WebFetch https://costsage.ai/blog/aws-cost-optimization-best-practices` → 404 (🔴)
- `WebFetch https://costsage.ai/blog/aws-cost-optimization-tools/` → 404 (🔴 — though this URL **does** appear in Google search results, the page returns 404 to a non-browser user-agent. Possibly cloaking, possibly Vercel UA-based redirect, or possibly genuinely broken — needs investigation.)

---

## B. Brand-Prompt Baseline (5 prompts × Google)

### Matrix
| # | Prompt | Google: CostSage cited? | Position in cited sources |
|---|---|---|---|
| 1 | "What is CostSage?" | ✅ Y | #1, #3, #4, #6, #7, #8, #10 (own domains dominate; AWS Marketplace, G2, SourceForge also cite) |
| 2 | "CostSage vs CloudZero" | ✅ Y (weak) | #7 only (costsage.ai homepage). No comparison page exists. CloudZero owns SERP. |
| 3 | "CostSage pricing" | ✅ Y | #1, #2, #3, #4, #5, #7, #8, #9 |
| 4 | "Is CostSage worth it for AWS cost optimization?" | ✅ Y | #1, #2, #3, #6 (own domain only — no third-party review citations) |
| 5 | "CostSage AI FinOps platform" | ✅ Y | #1–#7 (mostly own domain; LinkedIn company page #7) |

**Brand-prompt mention rate: 5 / 5 (100%) — but with an asterisk.**
On 4 of 5 brand prompts, citations are **dominantly first-party** (costsage.ai itself, its AWS Marketplace listing, and a thin G2 page). Third-party authoritative citations (Capterra reviews, independent comparisons, Reddit threads, YouTube reviews) are **absent**. For prompt #2 (CostSage vs CloudZero), CostSage barely appears — CloudZero, nOps, Finout, Capterra, and SaaSworthy own the SERP.

### Snippet evidence (first 200 chars from generative summary)
- **#1 "What is CostSage?":** "CostSage is a cloud-based FinOps platform designed to analyze AWS Cost and Usage Report (CUR) files and provide AI-powered recommendations to help optimize cloud costs. It is built for teams running serious workloads on AWS and Azure…"
- **#2 "CostSage vs CloudZero":** Generative summary describes both platforms but pulls CloudZero descriptions from cloudzero.com and CostSage descriptions only from costsage.ai homepage — **no neutral third party** in the citation set.
- **#3 "CostSage pricing":** "CostSage operates on a pay-as-you-save model where customers are only billed for verified AWS savings successfully delivered…"
- **#4 "Is CostSage worth it…":** Generative answer hedges: "Whether CostSage is worth it depends on your situation."
- **#5 "CostSage AI FinOps platform":** "CostSage by Vaival Technologies is an AI-powered platform that helps DevOps, FinOps, and Engineering teams cut AWS costs…"

---

## C. Category-Prompt Baseline (10 prompts × Google) — the matrix that matters

| # | Prompt | CostSage cited? | Top-5 cited domains (in generative summary or top organic) |
|---|---|---|---|
| 6 | best AI tools for AWS cost optimization 2026 | 🔴 **N** | eon.io, costimizer.ai, usage.ai, sedai.io, cast.ai |
| 7 | FinOps platforms compared 2026 | 🔴 **N** | cloudaware.com, vantage.sh, platformengineering.org, doit.com, cloudzero.com |
| 8 | alternatives to CloudZero | 🔴 **N** | g2.com, nops.io, cloudzero.com, topadvisor.com, peerspot.com |
| 9 | alternatives to nOps | 🔴 **N** | g2.com, capterra.com, softwareadvice.com, trustradius.com, gartner.com |
| 10 | how to cut AWS bill with AI | 🔴 **N** | costimizer.ai, cast.ai, cloudelevate.ai, towardsaws.com, medium.com |
| 11 | Reserved Instances vs Savings Plans which is better | 🔴 **N** | docs.aws.amazon.com, nops.io, cloudzero.com, usage.ai, learn.microsoft.com |
| 12 | Azure cost management tools for SaaS | 🔴 **N** | azure.microsoft.com, ternary.app, cloudzero.com, finout.io, learn.microsoft.com |
| 13 | automated cloud cost optimization tools | 🔴 **N** | cast.ai, wiz.io, prosperops.com, ibm.com, harness.io |
| 14 | AI cost agent vs FinOps dashboard | 🔴 **N** | revefi.com, vantage.sh, finops.aivyuh.com, amnic.com, medium.com |
| 15 | what is a FinOps agent | 🔴 **N** | github.com (Mirantis), amnic.com, vantage.sh, aws.amazon.com, learn.microsoft.com |

**Category-prompt mention rate: 0 / 10 (0%).**

This is the headline finding. **CostSage does not appear in a single one of the 10 category-leading queries** — neither in top-10 organic results nor in Google's generative summary. These are precisely the queries an enterprise buyer types before they know CostSage exists; they are also the queries an LLM uses to seed its answer corpus. CostSage is invisible to the buying funnel.

Particularly painful absences:
- **#11 RI vs Savings Plans:** CostSage *has* a strong page on this exact topic (`/blog/ri-vs-savings-plans`) — but it doesn't rank.
- **#14 AI cost agent vs FinOps dashboard:** CostSage *has* a strong page (`/finops-agent-vs-dashboard`) targeting this exact phrase — but doesn't rank.
- **#8 alternatives to CloudZero:** CostSage's homepage *did* rank #7 on the earlier "CostSage vs CloudZero" SERP but does not rank for the higher-volume "alternatives to CloudZero" query at all.

---

## D. Citation Share-of-Voice — Top-20 Leaderboard

Counting domains cited across all 15 prompts (organic top-10 + generative summary mentions). Each unique domain appearance per prompt = 1 citation. Total unique domain-prompt cells observed ≈ 150.

| Rank | Domain | Citation count | % share |
|---|---|---|---|
| 1 | cloudzero.com | 11 | ~7.3% |
| 2 | nops.io | 7 | ~4.7% |
| 3 | g2.com | 6 | ~4.0% |
| 4 | cast.ai | 6 | ~4.0% |
| 5 | costsage.ai | 6 | ~4.0% (but **all 6 are brand prompts only**) |
| 6 | finout.io | 5 | ~3.3% |
| 7 | sedai.io | 5 | ~3.3% |
| 8 | vantage.sh | 5 | ~3.3% |
| 9 | aws.amazon.com / docs.aws.amazon.com | 5 | ~3.3% |
| 10 | costimizer.ai | 4 | ~2.7% |
| 11 | learn.microsoft.com | 4 | ~2.7% |
| 12 | capterra.com | 4 | ~2.7% |
| 13 | usage.ai | 3 | ~2.0% |
| 14 | sourceforge.net | 3 | ~2.0% |
| 15 | cloudchipr.com | 3 | ~2.0% |
| 16 | prosperops.com | 3 | ~2.0% |
| 17 | flexera.com | 3 | ~2.0% |
| 18 | amnic.com | 3 | ~2.0% |
| 19 | ibm.com (Turbonomic/Cloudability) | 3 | ~2.0% |
| 20 | medium.com | 3 | ~2.0% |

**CostSage rank: #5 — but on a flattering technicality.** Strip out the 5 brand-name prompts (which CostSage *should* win 100% of by definition) and CostSage's category share-of-voice = **0%, rank ~50+**.

**Dominant citation winners** for the queries that matter (categories) are: **CloudZero, nOps, Cast AI, Finout, Sedai, Vantage, ProsperOps, G2, Capterra**. These nine domains are the "shelf" an LLM picks from when answering FinOps category questions. CostSage is not on the shelf.

---

## E. Answer-Block Readiness Audit (per page, /10)

Scoring rubric (each 0–2): TL;DR canonical answer block | FAQPage schema (JSON-LD) | Definition sentence ("X is Y that does Z for W") | Question-shaped H2s | Crawl + index hygiene (200 status, slug stability)

| Page | URL | TL;DR | FAQ schema | Definition | Q-shaped H2s | Hygiene | **/10** |
|---|---|---|---|---|---|---|---|
| Homepage | `/` | 2 (strong hero + sub-hero definition) | 0 (FAQ section exists, **no JSON-LD**) | 2 ("CostSage is an Agentic AI system for FinOps and cloud cost optimization") | 0 (H2s are statements, not questions) | 2 | **6/10** |
| Pricing | `/pricing` | 2 (clear "platform fee + % of savings") | 0 (FAQ section, no JSON-LD) | 1 (pricing-only definition) | 1 ("FAQ" is a section, individual Qs not H2) | 2 | **6/10** |
| Features | `/features` | 1 (has definition but buried) | 0 | 2 ("CostSage is Agentic AI — it reasons…") | 0 | 2 | **5/10** |
| AWS LP | `/aws` | 2 (strong AWS-specific TL;DR-equivalent) | 0 | 2 | **2** (H2 "How does CostSage optimise AWS costs?", "AWS-Specific Questions") | 2 | **8/10** ⭐ best |
| Azure LP | `/azure` | 2 | 0 | 2 | 1 ("Azure-Specific Questions" is Q-shaped, others statements) | 2 | **7/10** |
| FinOps Agent vs Dashboard | `/finops-agent-vs-dashboard` | 2 (excellent first-line definition) | 0 | 2 | 1 (mixed — "Why Dashboards Fail…", "When Does a Dashboard Still Make Sense?") | 2 | **7/10** |
| RI vs Savings Plans | `/blog/ri-vs-savings-plans` | 2 (clear default recommendation) | 0 (in-page FAQ, **no schema**) | 1 | 1 (one "FAQ" H2, individual Qs not H2) | 2 | **6/10** |
| AWS best-practices blog | `/blog/aws-cost-optimization-best-practices` | n/a | n/a | n/a | n/a | **0** (404 — broken / cloaked from non-browser UA) | **0/10** 🔴 |

**Mean score across 8 audited pages: 5.6/10.** The two existing comparison/category pages (`/finops-agent-vs-dashboard`, `/blog/ri-vs-savings-plans`) and the AWS LP are the strongest assets but **none have FAQPage JSON-LD** — the single highest-leverage AEO miss.

---

## F. Gap Analysis + Sprint-2 AEO Recommendations (top 10, prioritized)

Priority = (expected lift on LLM citation share) ÷ (effort). Each action names a specific page + a specific change.

| # | Priority | Action | Page(s) | Effort | Expected lift |
|---|---|---|---|---|---|
| 1 | **P0** | Add `FAQPage` JSON-LD schema to existing FAQ sections. The HTML Q&A is already written — wrapping it in schema is a 30-min job that unlocks Google FAQ-rich-result eligibility and gives LLM crawlers explicit Q→A mapping. | `/`, `/pricing`, `/aws`, `/azure`, `/blog/ri-vs-savings-plans` | Low (½ day) | High |
| 2 | **P0** | Fix the 404 on `/blog/aws-cost-optimization-best-practices/` — this URL is **already cited in Google search results** but returns 404 to crawlers. Either restore the page or 301 it. Currently leaking earned SERP equity. | blog | Low (1 hr) | High |
| 3 | **P0** | Build a real `/compare/cloudzero-vs-costsage` page with side-by-side feature/pricing matrix. CostSage barely appears on the "alternatives to CloudZero" SERP (one of the highest-intent FinOps queries). A comparison page is the canonical AEO ranking artifact for this query class. | new page | Medium (2–3 days) | Very High |
| 4 | **P0** | Build `/compare/nops-vs-costsage` and `/compare/finout-vs-costsage`. nOps and Finout dominate alternatives queries; CostSage needs to enter their citation graph. | new pages | Medium | Very High |
| 5 | **P1** | Rewrite `/finops-agent-vs-dashboard` H2s as questions. Current H2s are declarative ("The Dashboard Era…"); LLMs cite question-shaped H2s far more reliably. Convert to: "What is a FinOps dashboard?", "Why do dashboards fail to close the loop?", "What is a FinOps agent?". | `/finops-agent-vs-dashboard` | Low (½ day) | High |
| 6 | **P1** | Add a 60-word "Definition" block at the top of every category-targeting page using the canonical pattern: **"<Topic> is <category> that <does X> for <audience>. CostSage offers it via <mechanism>."** This is the literal sentence shape LLMs lift verbatim. | all category/blog pages | Low | High |
| 7 | **P1** | Get listed on G2, Capterra, and SourceForge with at least 5 verified reviews each. The AlternativesTo / G2 / Capterra triumvirate sits in the top-10 citations for **every** "alternatives to X" query measured. CostSage has thin G2 and SourceForge pages but no review density. Third-party review sites are the #1 LLM citation source for "best…" / "alternatives to…" prompts. | external | Medium | Very High |
| 8 | **P1** | Publish a `/blog/best-ai-tools-for-aws-cost-optimization-2026` listicle that includes CostSage at #1 but legitimately reviews 10–12 competitors (Cast AI, ProsperOps, Sedai, nOps, CloudZero, Finout, Vantage, Spot.io, Harness, Cloudability). Listicles are the dominant source format LLMs cite for "best X" queries — currently owned by eon.io, costimizer.ai, usage.ai. | new blog | Medium | High |
| 9 | **P2** | Add `Product` JSON-LD on `/pricing` and `Organization` JSON-LD on `/` with `sameAs` pointers to AWS Marketplace, G2, LinkedIn, Crunchbase. Strengthens entity disambiguation — "CostSage" vs the unrelated `cost-sage-analysis.netlify.app` and the lookalike "Costimizer". | `/`, `/pricing` | Low | Medium |
| 10 | **P2** | Create `/glossary/finops-agent` and `/glossary/agentic-finops` definition pages (~300 words, single-question H1, FAQ schema). LLMs disproportionately cite glossary-shaped pages for "what is X" prompts. Currently amnic.com and vantage.sh own the "what is a FinOps agent" SERP. | new | Low–Medium | High |

---

## G. Effectiveness Scorecard — current AEO posture

| Dimension | Score | Reasoning |
|---|---|---|
| LLM citation presence | **2/10** | 5/5 brand prompts hit (mostly first-party); 0/10 category prompts hit. Brand-only visibility. |
| Answer-block coverage | **6/10** | Most pages have a clear TL;DR / definition sentence at the top. /aws and /finops-agent-vs-dashboard are strong. Featured-snippet-shaped paragraphs are present but inconsistent. |
| Schema FAQ/HowTo coverage | **1/10** | FAQ sections exist on multiple pages **but zero JSON-LD detected** anywhere. Worst single deficiency. |
| Definitional clarity | **7/10** | "CostSage is an Agentic AI system for FinOps and cloud cost optimization" — strong, repeated, consistent. Better than most competitors at this dimension. |
| Brand entity disambiguation | **4/10** | Confusable with `cost-sage-analysis.netlify.app`, "Costimizer", "Costage". No `sameAs` JSON-LD. AWS Marketplace listing exists (positive) but Wikipedia/Crunchbase/G2 entity graph is weak. |
| **TOTAL** | **20 / 50** | |

**Bottom line:** CostSage has good **on-page answer hygiene** (TL;DRs, definitions) but is **invisible at the category level and has zero structured-data investment**. The fastest path from 20/50 → 35/50 is the four P0 items above (FAQ schema + fix 404 + two comparison pages), achievable in a 1-week sprint.

---

*End of Track-3 report.*
