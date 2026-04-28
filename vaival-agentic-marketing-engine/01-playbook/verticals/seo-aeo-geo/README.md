---
name: SEO / AEO / GEO Vertical
owner_tier: department-head
status: active
phase: 2
playbook_source: §9.1–§9.7
---

# SEO / AEO / GEO Vertical

## Charter
Owns the company's discoverability across every surface a SaaS buyer uses to research solutions — traditional search engines, AI Overviews / answer-boxes, and generative engines (ChatGPT, Claude, Perplexity, Gemini, Copilot). Mid-size priority order is sequenced, not parallel: **SEO foundation first, AEO second, GEO third** (§9.1). The vertical resists chasing every new tactic before foundations are solid and reports on trajectory rather than month-to-month noise.

## Team Roles + Tier (§9.3)
| Role | Tier | Headcount |
|---|---|---|
| SEO / Search Visibility Manager | Tier 2 (Vertical Lead) | 1 |
| SEO Specialist | Tier 3 | 1 |
| Technical SEO + AEO (shared with Web Dev) | Tier 3 | 1 |
| AEO Specialist | Tier 3 | 1 |
| GEO Monitoring (rotating) | Tier 4 | 1 |
| Link Building & Digital PR Specialist | Tier 3 | 1 |

Department Head: `head-of-search-visibility`.

## KPIs (§9.6)
**SEO**: Organic Sessions (weekly, GA4), Top-10 keywords (weekly, SEMrush), Top-3 commercial keywords (monthly), Organic MQL share (monthly, GA4+CRM), Domain Rating (monthly, Ahrefs), Core Web Vitals all-good (weekly, GSC), backlinks acquired (monthly).
**AEO**: Featured-snippet ownership ≥25% of tracked commercial queries, PAA presence ≥40% of clusters, AI Overview citation rate (monthly), schema coverage 100% on question-targeting pages.
**GEO**: Brand-mention rate across 5 AI tools (monthly), brand position when mentioned, response-accuracy rate, citation-source coverage (G2/Capterra/Gartner/publications), DR-40+ third-party mentions (Mention.com).

## Weekly Cadence
- Crawl-error / index-issue review (GSC) — submit fixes within 24h.
- Core Web Vitals regression check — flag same-day to Web Dev.
- Featured-snippet + PAA ownership tracking (SEMrush).
- Manual SERP audit on top 30 commercial queries for AI-Overview citations.
- Pull rank-tracker delta into the weekly KPI snapshot for the digest.

## Monthly Cadence
- Keyword & query research (SEO + AEO) — Workflow A (§9.5).
- Technical + AEO audit cycle (§9.5 Workflow B).
- AEO refresh of top question-format queries (§9.5 Workflow C).
- GEO Prompt-Bank audit across ChatGPT, Claude, Gemini, Perplexity, Copilot (§9.5 Workflow D).
- Link Building / Digital PR run, target 4–6 quality links DR 40+ (§9.5 Workflow E).
- Schema-coverage audit (Rich Results Test).
- Quarterly: full technical SEO audit + roadmap to Web Dev.

## Key Workflows (linked)
- `04-workflows/seo-audit.workflow.md`
- `04-workflows/content-production.workflow.md` (SEO brief upstream of content)
- `04-workflows/kpi-snapshot-pipeline.workflow.md` (weekly metric ingest)
- Monthly Keyword Research, AEO, GEO, Link-Building (Workflows A–E from §9.5; SOPs maintained inside this vertical).

## Tools / Connectors (linked, §9.4)
- `06-connectors/seo/google-search-console.connector.md`
- `06-connectors/seo/semrush.connector.md`
- `06-connectors/seo/ahrefs.connector.md`
- `06-connectors/seo/screaming-frog.connector.md`
- `06-connectors/seo/surfer-seo.connector.md` (or Clearscope)
- `06-connectors/analytics/ga4.connector.md`
- AlsoAsked / AnswerThePublic, Mention.com, Google Alerts (manual where no API).
- ChatGPT / Claude / Gemini / Perplexity / Copilot — manual GEO process.

## Policies + Thresholds
- **No cannibalization**: before any new page, confirm no existing page targets the same primary keyword (§9.7).
- **Refresh-before-create**: existing page in positions 8–25 → refresh, not new compete.
- **Internal linking non-negotiable**: every new article links out to ≥3 existing pages and receives ≥2 inbound (§9.7).
- **AEO direct-answer first**: 40–60-word answer in opening; headings as questions (§9.7).
- **GEO accuracy ≥ mention**: inaccurate AI mentions are a higher-priority fix than missing mentions.
- **Backlink quality bar**: DR ≥40, organic traffic >1k/mo, spam score <20% (§9.5 Workflow E).
- Reporting horizon: 6–18 months trajectory; one bad month is not a failure signal (§9.7).

## Refusal / Escalation Triggers
- Buy-links / PBN / private-blog-network outreach → hard refuse (governance).
- Cloaking, hidden text, AI-generated mass programmatic pages without editorial review → hard refuse.
- Disavow file changes → HITL (Head of Search Visibility approval; logged to ledger).
- Robots.txt / `llms.txt` changes affecting indexation → HITL Web Dev + SEO Manager.
- Domain migration / mass-redirect operations → HITL with CMO notification.
- Brand-claim disputes surfaced via GEO audit (inaccurate AI descriptions repeating across tools) → escalate to brand + legal.

## Output Artifacts Produced
- Weekly: rank-delta + Core Web Vitals + crawl-error report → feeds.
- Monthly: keyword-roadmap, AEO targets, GEO Response Log, link-acquisition log, schema audit, technical fix list to Web Dev.
- Quarterly: full technical SEO roadmap, GEO trend report, citation-source coverage map.
- SEO content briefs (handoff to Content vertical).

## Rubrics Applied
- `rubrics/seo-brief.yaml` (every brief, pass bar 8).
- `rubrics/weekly-kpi-snapshot.yaml` (weekly feed).
- `rubrics/monthly-exec.yaml` (monthly executive section).
- `rubrics/agent.yaml` + `rubrics/skill.yaml` for any skill/agent invocation in this vertical.
