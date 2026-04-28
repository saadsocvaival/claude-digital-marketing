---
client_id: costsage
vertical: seo-geo-aeo
phase: 1
status: draft-for-review
production_domain: costsage.ai
staging_domain: test-build.rundev.us
owner_agent: .claude/agents/head-of-seo-geo-aeo.md
review_gate: HITL — operator approval required at every Stage-3+ deployment
created_at: 2026-04-27
rubric: rubrics/seo-brief.yaml + rubrics/skill.yaml + rubrics/category-design.yaml
---

# CostSage — Phase 1 SEO + AEO + GEO Strategic Execution Blueprint

> **Review-first execution model.** Nothing in this blueprint deploys without explicit operator approval at Stage-5 (Human Review) of the workflow defined in §8. Staging must remain authority-isolated; production authority accrues to **costsage.ai** only.

> **Credential handling.** All tool credentials referenced in this blueprint are addressed via `clients/costsage/secrets.pointer.md`. **No credential is stored in any repo file.** Operator must complete `vaival-agentic-marketing-engine/04-workflows/secrets-vault-setup.workflow.md` before any tool-calling action is enabled. The cleartext sheet seen during onboarding must be revoked once vault migration is verified.

---

## 0. Pre-flight gates (must pass before any execution)

| Gate | Status | Owner | Action |
|---|---|---|---|
| Onboarding ledger §1–§9 populated | 🟡 partial | Operator | Run `client-onboarding.workflow.md` (12-question intake) |
| Secrets vault populated | 🔴 not started | Operator | Run `secrets-vault-setup.workflow.md`; revoke shared sheet |
| Goal decomposition (NSM + 90-day plan) | 🔴 not started | CMO orchestrator | Run `goal-decomposer.skill.md` v2.0 (metric tree) |
| Brand voice + ICP signed off | 🔴 not started | Head of Brand | Draft + HITL approval |
| Staging isolation enforced | 🔴 not started | Head of SEO/GEO/AEO | §2.1 below — robots/x-robots/canonical/Auth |
| Compromised credentials rotated | 🔴 required | Operator | Rotate WordPress admin + SEMrush/Ahrefs/Surfer/ATP/Trello shared password |

**Until every row is 🟢, this vertical operates in PLANNING-ONLY mode.** No live publishing, no schema deployment, no link outreach, no programmatic content generation.

---

## §1 — Strategic Analysis (CostSage's competitive ecosystem)

### 1.1 Category positioning hypothesis (to validate at intake)
**Inferred category:** *AI cost intelligence & FinOps for LLM/AI workloads.* Not generic cloud FinOps (Vantage/CloudZero), not LLM gateway (Helicone/Portkey), not observability (LangSmith/Arize). Distinct primitive: **unit-economics for AI inference** — cost per task / cost per outcome, not just cost per token.

This positioning must be confirmed in the §3 narrative-thesis before content production begins.

### 1.2 Competitor segmentation (4 layers)

| Layer | Examples | What they own in SERP today |
|---|---|---|
| **Direct AI cost platforms** | Vantage AI, CloudZero AI, Cast AI, ProsperOps (peripheral) | "AI cost optimization", "LLM cost monitoring" |
| **LLM observability + cost** | Helicone, Portkey, LangSmith (Anthropic/OpenAI cost views), Arize, Langfuse | "LLM monitoring", "OpenAI cost tracking", "prompt cost analysis" |
| **Generic cloud FinOps** | Vantage, CloudZero, Apptio Cloudability, Spot.io, ProsperOps | "cloud cost optimization" — strong DR, weaker on AI-specific |
| **Adjacent / commentary** | a16z portfolio blogs, AI Engineer Summit talks, Latent Space podcast, Substacks (Eugene Yan, Chip Huyen) | Topic authority on "AI economics", "cost of inference" — **citation goldmine for GEO** |

### 1.3 Semantic competitor map (for GEO citation share)
LLM answer engines today disproportionately cite: Anthropic + OpenAI pricing pages, a16z essays, Hugging Face cost calculators, Helicone's blog, Vantage's "State of FinOps" report. **CostSage's GEO target: become a top-3 cited source on "cost per LLM task" within 90 days** — measurable via `aeo-citation-audit.skill.md` weekly run.

### 1.4 Search intent ecosystem (4 query classes)

| Class | Example queries | Volume signal | Funnel stage |
|---|---|---|---|
| **Informational** | "what is LLM cost optimization", "how to reduce OpenAI bill", "Anthropic vs OpenAI cost" | High | ToFu |
| **Commercial-investigation** | "best LLM cost monitoring tool", "Helicone alternative", "AI FinOps platform comparison" | Med | MoFu |
| **Comparison** | "CostSage vs Helicone", "CostSage vs Vantage" | Low (brand-dependent) | BoFu |
| **Branded** | "CostSage pricing", "CostSage SOC2", "CostSage integrations" | Low (initial) | BoFu |

### 1.5 Zero-click + conversational opportunities
- "How much does it cost to run [LLM] at scale" → answer-engine extraction target.
- "What's the cheapest way to run [model X]" → comparison + calculator.
- "How to cut OpenAI API bill" → tactical guide + product-led tie-in.

These are **AEO/GEO-first** content; SERP click-through will be lower but LLM citation share + branded-search lift are the leading indicators.

---

## §2 — Technical SEO Architecture Plan

### 2.1 Staging isolation — enforced before anything else
**Production rule:** `costsage.ai` accrues authority. `test-build.rundev.us` must be invisible.

Required controls (validated weekly):

```
# At test-build.rundev.us — robots.txt
User-agent: *
Disallow: /

# At test-build.rundev.us — every page
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">

# At test-build.rundev.us — every response
X-Robots-Tag: noindex, nofollow, noarchive

# At test-build.rundev.us — HTTP basic auth or IP allowlist
# (defense in depth — robots is a request, not a guarantee)

# At costsage.ai — canonical never points to staging
<link rel="canonical" href="https://costsage.ai/[path]">
```

**Validation:** weekly Bing/Google `site:test-build.rundev.us` check; alert if any URL surfaces.

### 2.2 Crawlability + indexability audit framework
| Check | Tool | Pass criterion |
|---|---|---|
| robots.txt sanity | manual + Search Console | No accidental Disallow on production |
| XML sitemap | Yoast/RankMath (WP) → submit to GSC + Bing Webmaster | All canonical URLs present, lastmod accurate |
| Crawl errors | GSC Coverage report | <0.5% URL error rate; zero soft-404s on money pages |
| Render parity | Mobile-Friendly Test + URL Inspection | DOM rendered HTML matches initial HTML for critical content |
| JavaScript SEO | Screaming Frog (JS rendering on) | No JS-only critical content; SSR or pre-render where required |
| Internal duplicates | Screaming Frog + Sitebulb | No URL parameter duplication; faceted-nav controlled |

### 2.3 URL architecture (production blueprint)
```
costsage.ai/                                  → home (pillar: "AI cost intelligence")
costsage.ai/product/                          → product overview
costsage.ai/product/{feature}/                → feature pages (5–7 max in v1)
costsage.ai/pricing/                          → pricing page (see templates/pricing-page-brief.md)
costsage.ai/blog/{slug}/                      → blog (no /category/ in URL — flat for authority)
costsage.ai/guides/{cluster}/{slug}/          → topical clusters (pillar+spokes)
costsage.ai/compare/{competitor}/             → comparison pages (BoFu, branded+competitor)
costsage.ai/calculators/{tool}/               → free-tool pages (link-bait + AEO answers)
costsage.ai/customers/{slug}/                 → case studies
costsage.ai/docs/                             → product docs (subdomain optional; recommend same domain for authority concentration)
costsage.ai/changelog/                        → changelog (signals freshness)
costsage.ai/about/, /security/, /soc2/        → trust pages (E-E-A-T signals)
```

Rules: lowercase, hyphenated slugs, no trailing parameters in canonical, no `?utm_*` in canonical (use `rel=canonical` to strip), no session IDs.

### 2.4 Canonicalization, pagination, redirects
- Canonical points to itself on every indexable page; never to staging; never cross-domain unless syndicated.
- Pagination: `rel=next/prev` deprecated by Google but still useful for Bing/AEO; use `View-all` page where feasible.
- Redirects: 301 only for permanent; never 302 for migrations; chain depth ≤1; track in a redirect ledger.
- Trailing-slash policy: pick one, enforce site-wide via 301 (recommendation: trailing slash for content, no slash for files).

### 2.5 Schema architecture (priority order)
1. **`Organization` + `WebSite`** site-wide (logo, sameAs, search action)
2. **`Product` + `Offer` + `AggregateRating`** on product/pricing
3. **`SoftwareApplication`** (since costsage is SaaS) — duplicates allowed alongside Product
4. **`Article` + `BreadcrumbList`** on blog/guides
5. **`FAQPage`** on every page that answers ≥3 named questions
6. **`HowTo`** on procedural guides
7. **`VideoObject`** if video published
8. **`Person`** on author bios (E-E-A-T anchor)
9. **`Dataset`** on calculator/research outputs (massively GEO-friendly)

JSON-LD only. Server-rendered. Validated via Rich Results Test + Schema.org validator on every deploy.

### 2.6 Performance + Core Web Vitals
WordPress baseline targets: **LCP ≤2.0s p75, INP ≤180ms p75, CLS ≤0.05 p75**. Stack rule of thumb:
- LiteSpeed/Hummingbird/WP Rocket for caching
- Cloudflare in front (CDN + image optimization + early hints)
- Preload hero font + LCP image; defer non-critical JS
- No render-blocking third-party (delay analytics + chat widgets)
- Image policy: AVIF preferred, WebP fallback, max 200kb above-the-fold; lazy-load below-fold.

### 2.7 Internal linking architecture
- **Pillar → spoke → spoke** within each cluster.
- **Cross-cluster** only when semantically defensible (entity overlap).
- Footer + nav: site-wide structural links only (do not stuff with content links).
- Contextual in-body links from new content **back to pillars** (not pillar → spoke unless updated).
- Link audit cadence: monthly Screaming Frog `Inlinks` report; orphans get adopted or pruned.

### 2.8 Crawl-budget + duplicate prevention
- Faceted nav (if any) `noindex,follow`.
- Search results `noindex,nofollow`.
- Tag pages `noindex` until ≥10 posts on a tag.
- Author archives `noindex` unless author is an E-E-A-T anchor.
- Trailing-slash redirects, mixed-case redirects, www→apex (or reverse) all 301'd consistently.

### 2.9 Severity-graded technical issue ledger (template)
For every audit finding, the following row is required in `clients/costsage/seo-geo-aeo/tech-audit-ledger.md` (created at first audit):

| ID | Issue | Severity (P0/P1/P2) | Impact | Reasoning | Fix | Validator | Review checkpoint | Owner | Status |

P0 = blocks indexing or leaks authority to staging. P1 = degrades rankings. P2 = polish.

---

## §3 — Semantic SEO + Entity Strategy

### 3.1 Primary entities to claim
- **CostSage** (brand entity) — Wikidata submission queued; LinkedIn company page; Crunchbase profile; G2 listing; Capterra listing; Product Hunt launch (timed to lightning-strike per `templates/category-design.md`).
- **AI cost optimization** (concept entity) — own this in Wikipedia/Wikidata via authoritative content; cross-link.
- **CostSage founders/leadership** (person entities) — bylines, LinkedIn, GitHub, conference talks.

### 3.2 Entity hierarchy (3 tiers)

| Tier | Entities | Role |
|---|---|---|
| **Primary** | CostSage; "AI cost optimization"; "LLM cost intelligence" | Own these |
| **Secondary** | "Cost per inference"; "Token economics"; "FinOps for AI"; "LLM gateway"; "AI observability" | Co-occur with primary in 80%+ of pillar content |
| **Contextual** | OpenAI, Anthropic, Google Vertex, AWS Bedrock, Azure OpenAI, Hugging Face, Helicone, LangSmith, Vantage, CloudZero | Reference accurately; never plagiarize |

### 3.3 Topical map (pillars + spokes)

**Pillar 1: AI Cost Intelligence (foundation)**
- Spoke: What is AI cost intelligence?
- Spoke: Cost per inference vs cost per token
- Spoke: AI cost optimization framework
- Spoke: FinOps for AI workloads
- Spoke: Building an AI cost dashboard

**Pillar 2: LLM Cost Optimization (tactical)**
- Spoke: How to reduce OpenAI API costs
- Spoke: Anthropic Claude cost optimization
- Spoke: Prompt engineering for cost reduction
- Spoke: Caching strategies for LLM apps
- Spoke: Model routing for cost-quality tradeoff

**Pillar 3: AI Vendor Economics (comparison)**
- Spoke: OpenAI vs Anthropic cost comparison (updated quarterly)
- Spoke: Self-hosted vs API economics
- Spoke: Open-source LLM TCO
- Spoke: Multi-provider strategy

**Pillar 4: AI Observability + Cost (intersection)**
- Spoke: AI observability metrics
- Spoke: Linking cost to outcome quality
- Spoke: Cost-aware model evaluation

**Pillar 5: Tools + Calculators (link-bait + AEO)**
- LLM Cost Calculator
- Token-to-Cost converter
- Multi-model cost comparator
- AI ROI calculator

Each spoke has a `seo-content-brief.md` (template exists) AND an `answer-engine-brief.md` (per `skills/seo/answer-engine-brief.skill.md`) before drafting.

### 3.4 Knowledge-graph submissions queue
1. **Wikidata** — create CostSage entity (founders, founding date, HQ, funding, sameAs links)
2. **LinkedIn Company Page** — verified, complete, weekly posting cadence
3. **Crunchbase, Pitchbook, Tracxn** — basic profile + funding records
4. **G2, Capterra, GetApp, Software Advice** — listings + active review collection
5. **Product Hunt** — coordinated launch (one-shot)
6. **AlternativeTo, Slant** — listings
7. **GitHub org** — even if closed-source product, public repos for SDKs/integrations build trust

Critical: every external profile points `sameAs` back to `costsage.ai` and uses identical brand name + logo. **Entity consistency is non-negotiable** — LLMs ground on it.

---

## §4 — AEO (Answer Engine Optimization) Framework

### 4.1 Question architecture (per content piece)
Every pillar/spoke must include:
- **Top-of-page TL;DR** — 50–80 words, self-contained, contains primary entity + 2–3 secondaries.
- **3–5 TL;DR bullets** — each citable in isolation.
- **H2 = sub-question** structure. Each H2 opens with 2–3-sentence direct answer; evidence/elaboration follows.
- **`FAQPage` schema** with 4–8 Q/As pulled from People-Also-Ask + sales call transcripts.

(Spec lives in `skills/seo/answer-engine-brief.skill.md`.)

### 4.2 Semantic chunking standards
- Sections ≤300 words.
- One claim per paragraph.
- Inline citations to authoritative sources (anchor text matters).
- Date-stamp every factual claim (`As of 2026-04`, since LLMs trust dated claims more).
- Named entities ≥15 per 1000 words (target).

### 4.3 Answer-confidence formatting
- Lead with the answer, then the qualification.
- Avoid hedge words ("typically", "often", "sometimes") in answer-blocks; use them in elaboration.
- Numerical claims: cite source + year + methodology in parentheses.
- Use comparison tables for any "X vs Y" content — LLMs extract tables verbatim.

### 4.4 Voice + conversational search
- Long-tail conversational queries (8+ words) get their own H2.
- Featured-snippet-shape paragraphs (40–60 words, definition-first).
- Audio readability: short sentences, active voice, no nested clauses.

### 4.5 AEO-specific KPI: **BMI-LLM** (per `skills/seo/aeo-citation-audit.skill.md`)
```
BMI-LLM = (direct_quotes × 3 + source_links × 2 + paraphrases × 1) / total_queries_in_set
```
Target by query class (90-day):
- Informational: BMI-LLM ≥1.5
- Commercial-investigation: ≥1.0
- Comparison: ≥0.8
- Branded: ≥2.5

Audit cadence: weekly across ChatGPT, Claude, Gemini, Perplexity, Google AIO. n≥3 per query (LLM outputs vary).

---

## §5 — GEO (Generative Engine Optimization) Framework

### 5.1 Why GEO ≠ SEO
LLM retrieval does not crawl pages — it ranks chunks already in its training/RAG index. Winning GEO means:
1. Being **in** the index (Wikipedia, Wikidata, GitHub, authoritative blogs that LLMs sample heavily).
2. Producing **chunks** that retrievers rank highly: dense factual, well-cited, entity-rich, dated.
3. Being **mentioned** by other authorities the LLM trusts.

### 5.2 Citation-worthiness checklist (per asset)
- [ ] Contains ≥1 original data point (proprietary research, customer-aggregated stat).
- [ ] Cites ≥8 authoritative sources per 1000 words.
- [ ] Date-stamped at top + bottom of page.
- [ ] Author bio with credentials (E-E-A-T anchor).
- [ ] Schema: `Article` + `Person` (author) + (where applicable) `Dataset`.
- [ ] Reproducible methodology section if research-based.
- [ ] Permanent URL (no slug changes; no consolidation without 301 + content preservation).

### 5.3 Trust signals LLMs ground on
- Wikidata entity with `sameAs` graph
- Wikipedia mention (high bar; earn through being notable + cited in tier-1 press)
- G2/Gartner Peer Insights with ≥30 reviews
- GitHub presence (public repos — even SDKs are enough)
- Conference proceedings, published papers (arXiv if applicable)
- Tier-1 press: TechCrunch, The Information, The Verge, IEEE Spectrum, Stratechery (citing-worthy)

### 5.4 Retrieval-friendly chunk structure
Every 200–400-word section reads as a **standalone passage**: it answers a specific question, cites sources, and contains the primary + secondary entities. Section-anchor links (`#h2-id`) are first-class for retrieval.

### 5.5 LLM-distribution targets (own these channels)
- **Hugging Face** — datasets/spaces published under CostSage org.
- **GitHub** — SDKs, OpenAPI specs, integration examples.
- **arXiv / Medium / Substack** — original research; permissive licensing for citation.
- **Awesome-lists** — get linked from `awesome-llm-cost`, `awesome-finops`, etc.
- **Podcast circuit** — Latent Space, Practical AI, Changelog, AI Engineer pod.

### 5.6 GEO measurement
- **Citation share** (per `aeo-citation-audit.skill.md`): weekly sample 50 target queries × 5 engines × 3 runs.
- **Mention density in LLM answers** even when not cited (paraphrase counts at weight 1).
- **Branded-LLM lift**: track whether LLMs surface CostSage on adjacent queries over time.

---

## §6 — Content Intelligence System

### 6.1 Editorial cadence (Phase-1 first 90 days)

| Cadence | Output | Owner |
|---|---|---|
| Weekly | 1 spoke article (1500–2500 words) | Head of Content |
| Bi-weekly | 1 pillar update (existing pillar refreshed with new data) | Head of Content + SEO |
| Monthly | 1 comparison page (BoFu, brand+competitor) | SEO + Brand |
| Quarterly | 1 original-research piece (data, calculator, or report) | Head of Content + Analytics |

### 6.2 Per-piece intake (mandatory before drafting)
Each piece gets a brief that combines `templates/seo-content-brief.md` + AEO brief from `answer-engine-brief.skill.md` and includes:
- Target query (primary + 3–5 LSI)
- Search intent class
- Target entity + co-occurring secondary entities
- Pillar/spoke role
- Internal linking plan (in/out)
- Schema plan (Article + FAQPage minimum)
- Canonical URL
- Author + reviewer + date
- Success criteria (rank, BMI-LLM contribution, branded-search lift)

### 6.3 Content quality bar
- Pass `rubrics/seo-brief.yaml` + AEO criteria — pass bar 8.
- Run `adversarial-critic` agent — `min(self, critic) ≥ 8` before publish.
- Brand-voice check against `clients/costsage/brand-voice.md` (to be authored).
- Plagiarism + fact check (Originality.AI + manual source verification).

### 6.4 Refresh policy
- Comparison pages: quarterly (model prices change).
- Statistics-heavy pages: every 6 months.
- Pillars: annual full rewrite + monthly "Last updated" date refresh with non-trivial changes.
- Decay-detection: weekly rank tracking; -3 positions on a money keyword triggers `content-refresher` skill.

---

## §7 — Implementation Roadmap (90 days)

### Days 1–7 — Foundation
| Task | Dependencies | Outcome | Validator | Approval |
|---|---|---|---|---|
| Run secrets-vault-setup workflow | Operator | Vault populated; sheet revoked | `secrets.pointer.md` shows non-placeholder vault paths only | HITL Stage-7 |
| Run client-onboarding workflow | Operator | `ledger.md` §1–§9 populated | Rubric ≥8 | HITL |
| Goal-decomposer (metric tree + 90-day plan) | Onboarding done | `okrs/2026-q3.md` + `plan.md` | Rubric ≥8 | HITL |
| Staging isolation enforcement | DevOps access | robots/x-robots/auth on staging verified | Manual `curl -I` + GSC + Bing | HITL |
| Tech-SEO baseline audit | Production reachable | `tech-audit-ledger.md` populated (§2.9) | Screaming Frog clean run | HITL |
| Brand-voice + ICP signoff | Brand intake | `brand-voice.md` + `icp.md` | Rubric ≥8 | HITL |
| Compromised credential rotation | Operator | New passwords in vault; old revoked | Vault audit | HITL |

### Days 8–30 — Architecture
- Schema rollout (Organization, WebSite, Product, FAQPage on existing pages)
- URL architecture finalized + redirect ledger
- Sitemap rebuilt + submitted to GSC + Bing Webmaster + IndexNow
- Wikidata submission drafted + filed
- G2 + Capterra listings + review-collection campaign
- LinkedIn company page completed + verified
- Pillar-1 article published (production)
- Author bios + E-E-A-T anchor pages

### Days 31–60 — Content engine
- Pillars 1–3 published (3 pillars)
- 6 spoke articles published (2/week)
- 1 comparison page published
- 1 calculator/free-tool live
- Internal-linking pass on all existing content
- First `aeo-citation-audit` run + remediation queue
- First `incrementality-test` design (organic-only at this stage; baseline measurement)

### Days 61–90 — Authority + measurement
- Pillar-4 + Pillar-5 published
- 6 more spokes (2/week)
- First original research piece (data + calculator + Substack/arXiv distribution)
- First podcast appearance (Latent Space / Practical AI tier)
- Awesome-list inclusion (≥3 lists)
- Hugging Face spaces/datasets if applicable
- Second AEO citation audit; measure BMI-LLM delta
- 90-day review; rubric-calibration event; Phase-2 plan opens

For each task, fields required: objective, dependencies, tasks, outcome, validator, review checkpoint, approval requirement, rollback plan, deployment risk.

---

## §8 — Review Workflow System (mandatory 10-stage gate)

| Stage | Action | Output | Approver |
|---|---|---|---|
| 1 | Analysis | Findings doc | Self |
| 2 | Recommendation | Implementation rec | Head of SEO/GEO/AEO |
| 3 | Draft implementation | Diff / draft asset | Self |
| 4 | Internal validation | Self-rubric ≥8 + adversarial-critic ≥8 | Adversarial-critic agent |
| 5 | **Human review** | HITL request via `hitl-request.skill.md` | **Operator** |
| 6 | Revision (if requested) | Updated draft | Self |
| 7 | Final approval | Operator sign-off in HITL queue | **Operator** |
| 8 | Deployment | Staged → production via change ticket | Head of SEO/GEO/AEO |
| 9 | Validation | Post-deploy checks (rich-results, GSC, sitemap) | Head of Analytics |
| 10 | Monitoring | Anomaly detection (rank, GSC errors, citation share) | Head of Analytics |

**No skipping stages.** Skipping = governance violation, logged to ledger, escalated.

---

## §9 — Automation Architecture (path to autonomy)

### 9.1 Today (Phase-1) — operator-triggered
All actions are operator-initiated; system produces drafts; operator approves.

### 9.2 Phase-2 — supervised autonomy (gated to Stage 3 in ROADMAP)
Once MCP runtime tools are wired (`06-connectors/`), enable:
- Automated weekly tech-SEO audit (Screaming Frog/Sitebulb via API → ledger).
- Automated AEO citation audit (LLM API calls per `aeo-citation-audit.skill.md`).
- Automated rank tracking (Search Console API + AccuRanker/SERPapi).
- Automated schema validation on every WordPress publish (CI hook).
- Automated `noindex` audit on staging (cron).
- Automated link health (broken-link detection + redirect-chain audit).

### 9.3 Phase-3 — bounded autonomy
- Auto-publish low-risk content (changelog entries, status pages) under brand-voice eval pass.
- Auto-refresh stats on dated pages (HITL only on >X% delta).
- Auto-pause indexing on production anomaly (sudden drop, malware flag).

### 9.4 Permanent HITL gates (never automate)
- New positioning / category claims
- Pricing-page changes
- Legal-sensitive copy (regulated, comparative)
- Migrations / domain changes / large redirect maps
- Penalty / manual-action response

### 9.5 Monitoring stack
- GSC + Bing Webmaster — daily ingestion → `clients/costsage/feeds/`.
- Rank tracker — weekly delta to ledger.
- LLM citation audit — weekly.
- Core Web Vitals — daily (CrUX + RUM).
- Schema validity — every deploy.
- Semantic drift — monthly (does our content still match our entity claims?).
- Anomaly thresholds: −15% organic clicks WoW; −5 positions on top-20 keyword; new GSC manual action.

---

## §10 — Risk Management

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Staging accidentally indexed | Medium | **Critical** | Robots + x-robots + auth (defense in depth); weekly `site:test-build.rundev.us` check; Cloudflare WAF rule blocking known bot UAs from staging |
| Duplicate content (staging↔prod) | High | High | Canonical to prod always; staging fully `noindex`; WP RankMath set to canonical override |
| Canonical conflicts (parameters, paginated) | Medium | Med | Rule in §2.4; weekly Screaming Frog canonical audit |
| AI hallucinations citing CostSage incorrectly | Medium | Med | `aeo-citation-audit` weekly; correction process via authoritative content + Wikipedia/Wikidata reinforcement |
| Thin content (under-resourced clusters) | Medium | High | 1500-word floor on spokes; rubric ≥8 required; kill clusters that can't be resourced rather than ship thin |
| Crawl traps (faceted nav, search) | Low | Med | §2.8 controls + monthly crawl-budget review |
| Authority dilution (subdomains, microsites) | Low | High | Single-domain policy; only `docs.costsage.ai` allowed if absolutely required; default to `costsage.ai/docs/` |
| LLM citation inconsistency across engines | High | Low | Acceptable variance; track variance, not just mean |
| Compromised credentials (current state) | **HIGH** | **Critical** | Rotate now; vault migration; revoke shared sheet; least-privilege per platform |
| Indexing instability post-launch | Low | High | Phased rollout; small-batch publishing; GSC monitoring |
| Penalty (unnatural links, AI content flag) | Low | **Critical** | No PBN, no tier-2/tier-3 link spam; AI-assisted not AI-only; human review on every piece |

---

## §11 — Execution Priority Matrix

### P0 — Critical (this week)
1. Rotate compromised credentials; vault migration.
2. Staging isolation (robots/x-robots/auth).
3. Onboarding ledger §1–§9.
4. Goal decomposition + 90-day plan.
5. Tech-SEO baseline audit.
6. Brand-voice + ICP signoff.
7. Wikidata submission drafted.

### P1 — High (weeks 2–4)
1. Schema rollout (Organization + WebSite + Product + FAQPage).
2. URL architecture + redirect ledger.
3. Sitemap + IndexNow.
4. Pillar-1 published.
5. G2/Capterra listings + review collection.
6. LinkedIn company page complete.
7. First AEO citation audit baseline.

### P2 — Medium (weeks 5–8)
1. Pillars 2–3.
2. 6 spokes.
3. First comparison page.
4. First calculator.
5. Author E-E-A-T pages.
6. First incrementality baseline (organic-only).

### P3 — Long-term strategic (weeks 9–12+)
1. Original research piece + distribution.
2. Podcast circuit.
3. Awesome-list inclusion.
4. Hugging Face presence (if applicable).
5. Refresh + monitor cycle.
6. Phase-2 plan.

---

## §12 — KPI Framework

| Layer | Metric | Source | 30-day target | 90-day target | 180-day target |
|---|---|---|---|---|---|
| **SEO — leading** | Indexed URLs | GSC | 30+ | 80+ | 200+ |
| | Crawl errors | GSC | <2% | <1% | <0.5% |
| | Avg. CWV pass | CrUX | 70% | 85% | 95% |
| | Schema coverage | Rich Results | 60% pages | 90% | 100% |
| **SEO — lagging** | Top-20 keywords | Rank tracker | 10 | 50 | 150 |
| | Top-3 keywords | Rank tracker | 0 | 5 | 25 |
| | Organic clicks/mo | GSC | 500 | 5k | 25k |
| | Branded search impressions | GSC | 200/mo | 1k/mo | 5k/mo |
| **AEO** | BMI-LLM (informational) | aeo-citation-audit | 0.3 | 1.5 | 2.5 |
| | BMI-LLM (commercial) | aeo-citation-audit | 0.2 | 1.0 | 2.0 |
| | BMI-LLM (branded) | aeo-citation-audit | 1.0 | 2.5 | 3.5 |
| | FAQ-block citation rate | Manual + AEO audit | 5% | 25% | 50% |
| **GEO** | Wikidata entity | manual | drafted | live | enriched |
| | Wikipedia mention | manual | 0 | 0 | 1 |
| | Tier-1 press mentions | manual | 0 | 1 | 3 |
| | GitHub repos w/ ≥10 stars | github | 0 | 1 | 3 |
| | Awesome-list inclusions | manual | 0 | 3 | 8 |
| | Hugging Face presence | HF | 0 | 1 dataset/space | 3 |
| **Entity / authority** | sameAs profiles consistent | manual | 5 | 10 | 15 |
| | Backlink RD (referring domains) | Ahrefs | 5 | 30 | 100 |
| | DR / Domain Authority | Ahrefs/Moz | 5 | 20 | 35 |
| **Topical authority** | Pillars live | manual | 1 | 5 | 8 |
| | Spokes per pillar | manual | 2 | 5 avg | 8 avg |
| | Internal-link depth | Sitebulb | n/a | ≥3 | ≥5 |

All metrics flow to `clients/costsage/feeds/weekly-kpi-snapshot.md`; deltas shown in CMO digest's Motion Summary section.

---

## Appendix A — Tooling & access pointers

All tooling references in this blueprint resolve through `clients/costsage/secrets.pointer.md`. Tools confirmed available (per intake screenshot):
- GA4, Google Search Console, Google Tag Manager
- Semrush, Ahrefs, Screaming Frog, Surfer SEO
- Google Rich Results Test, Answer The Public, Google Alerts
- Trello (editorial calendar)
- ChatGPT, Claude, Gemini, Perplexity, Copilot (manual + AEO audit reference)
- WordPress (production CMS)

**No credential is reproduced here.** Every tool action requires a fresh vault read at runtime.

---

## Appendix B — First HITL request (pending operator)

**Category:** Phase-1 kickoff
**Why needed:** Cannot start any execution before pre-flight gates pass.
**Policy ref:** This blueprint §0; `CLAUDE.md` non-negotiables; `secrets-vault-setup.workflow.md`.
**Options:**
- **A** — Approve P0 list (§11) + assign owners + set 7-day target. Recommended.
- **B** — Defer until intake interview scheduled; freeze vertical.
- **C** — Modify scope (e.g. defer Wikidata, skip GEO until Phase-2).
**Recommend:** **A**. Every day staging is un-isolated and credentials are un-rotated is a real risk.
**Needed by:** within 48 hours.

---

**Self-score:** 89/100 — substantive, ties to v1.1 system, honest gating, P0 risk surfaced.
**Critic-score:** TBD (run `adversarial-critic` agent against this artifact + `rubrics/seo-brief.yaml` + `rubrics/category-design.yaml` before approval).

**Ship gate:** `min(self, critic) ≥ 8` per `cmo-orchestrator.md` non-negotiables.
