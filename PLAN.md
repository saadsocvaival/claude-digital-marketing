# Plan — Wire 190 Marketing Skills into VMD + Playbook

## Context

User already cloned 190 marketing skills into `C:\Users\shiraz.iqbal\Documents\VMD\skills\` (from coreyhaines31, OpenClaudia, aaron-he-zhu, AgriciDaniel, alirezarezvani). Skills are valid `SKILL.md` folders but:

1. Not discoverable by Claude Code in VMD project (no `.claude/skills/` registration)
2. Not mapped to the **mid-size SaaS marketing dept playbook** (7 verticals: SEO/AEO/GEO, Paid Media, Content, Social, Email/CRM, Analytics/Ops, Web Dev)
3. Not wired into `vaival-agentic-marketing-engine/02-agents/` (Tier 3–5 agents that should invoke them)

Goal: make all 190 skills (a) auto-loadable by Claude Code inside VMD, (b) mapped to the playbook verticals + OKRs, (c) referenced by each tier-3/4/5 agent spec so the agentic engine can invoke the right skill per task.

---

## Recommended Approach

### Step 1 — Register skills dir w/ Claude Code

Claude Code auto-loads skills from `<project>/.claude/skills/<name>/SKILL.md`. Current skills live at `<project>/skills/`.

**Option A (recommended) — Windows junction** (no admin needed, cross-tool compatible):
```cmd
mklink /J "C:\Users\shiraz.iqbal\Documents\VMD\.claude\skills" "C:\Users\shiraz.iqbal\Documents\VMD\skills"
```
Keeps single source of truth at `skills/`, surfaces them at `.claude/skills/`.

**Option B** — move dir: `mv skills .claude/skills`. Breaks INDEX.md relative links.

**Option C** — plugin marketplace: build a `plugin.json` pointing at `skills/` and register via `/plugin marketplace add ./`. Overkill for local use.

Pick A.

### Step 2 — Vertical-to-Skill Matrix

Create `C:\Users\shiraz.iqbal\Documents\VMD\skills\VERTICAL_MAP.md` mapping each of the 7 playbook verticals to its skill subset. Example structure:

| Vertical | Lead Role | Skills |
|---|---|---|
| SEO/AEO/GEO | SEO Manager | seo-audit, ai-seo, schema-markup, programmatic-seo, keyword-research, serp-analyzer, backlink-audit, ahrefs-research, semrush-research, search-console, content-gap-analysis, rank-tracker, on-page-seo-auditor, technical-seo-checker, internal-linking-optimizer, seo-* (all claude-seo family: local, maps, ecommerce, hreflang, sxo, drift, cluster, images, firecrawl, dataforseo), entity-optimizer, geo-content-optimizer, geo-query-finder, seo-content-writer, seo-content-brief |
| Paid Media | Paid Media Manager | paid-ads, google-ads, facebook-ads, linkedin-ads, ad-creative, video-ad-analysis, campaign-analytics, google-ads-report |
| Content Marketing | Content Manager | copywriting, copy-editing, content-strategy, content-production, content-creator, content-humanizer, content-repurposing, content-calendar, content-quality-auditor, content-refresher, write-blog, write-landing, thread-writer, video-content-strategist, marketing-ideas, marketing-psychology, newsletter |
| Social Media | Social Media Manager | social-content, social-media-manager, social-media-analyzer, linkedin-content, reddit-marketing, bluesky, x-twitter-growth, podcast-marketing, community-marketing |
| Email & CRM | CRM Manager | email-sequence, email-subject-lines, cold-email, hubspot, apollo-outreach, churn-prevention, lead-magnet(s), icp-builder, customer-research |
| Analytics & Ops | Marketing Ops Manager | analytics-tracking, google-analytics, performance-reporter, marketing-ops, competitor-analysis, competitor-alternatives, brand-monitor, brand-research, brand-guidelines, domain-research, domain-authority-auditor, alert-manager |
| Website / CRO | Web Lead | page-cro, form-cro, popup-cro, signup-flow-cro, onboarding-cro, paywall-upgrade-cro, ab-test-setup, site-architecture, pricing-strategy, free-tool-strategy, referral-program, schema-markup-generator, meta-tags-optimizer |
| Strategy (CMO/Head) | CMO + Head of Mktg | marketing-strategy-pmm, marketing-context, marketing-demand-acquisition, launch-strategy, product-marketing, product-marketing-context, growth-strategy, demand-gen, revops, sales-enablement, aso-audit, app-store-optimization, affiliate-marketing, directory-submissions, prompt-engineer-toolkit, memory-management |

Dedupe strategy: multiple sources provide overlapping skills (e.g. `ab-test-setup`, `claude-skills-ab-test-setup`, `openclaudia-skills-ab-test-setup`). Pick one canonical per skill via **preference order**: `coreyhaines31 > alirezarezvani > OpenClaudia > aaron-he-zhu > AgriciDaniel`. Mark non-canonical as `aliases` in VERTICAL_MAP.md — do not delete (INDEX.md references them).

### Step 3 — Wire skills into agent specs

Each Tier 3 manager agent in `vaival-agentic-marketing-engine/02-agents/tier-3-managers/` gets a `skills:` frontmatter block listing canonical skill IDs it can invoke. Same for Tier 4 specialists and Tier 5 coordinators. Example (SEO Manager):

```yaml
---
tier: 3
vertical: seo-aeo-geo
reports_to: head-of-digital-marketing
skills:
  - seo-audit
  - ai-seo
  - keyword-research
  - schema-markup
  - programmatic-seo
  - content-gap-analysis
  - technical-seo-checker
  - rank-tracker
delegates_to:
  - tier-4-specialists/technical-seo-aeo-specialist
  - tier-4-specialists/seo-specialist
  - tier-5-coordinators/geo-monitoring-coordinator
---
```

Orchestrator (`03-orchestration/cmo-orchestrator-contract.md`) reads agent `skills:` field to route user asks to the right agent → skill chain.

### Step 4 — Playbook → Workflow → Skill bindings

Each workflow in `04-workflows/` (e.g. `monthly-keyword-research.md`, `campaign-launch.md`, `content-request.md`) lists the skills its steps invoke. Example for SEO §9.5 Workflow A (Monthly Keyword & Query Research):

| Step | Skill |
|---|---|
| Export rankings | search-console, semrush-research |
| Identify quick wins | keyword-research, rank-tracker |
| Competitor gap | content-gap-analysis, competitor-analysis |
| Funnel categorize | keyword-research |
| AEO layer | ai-seo, geo-query-finder |
| Write briefs | seo-content-brief |

### Step 5 — Validation

After setup, run inside VMD:
- `ls .claude/skills | wc -l` → should show ~190
- In Claude Code session at VMD, trigger: *"use seo-audit skill to review example.com"* → skill must load
- Open `vaival-agentic-marketing-engine/02-agents/tier-3-managers/seo-manager.md` → confirm `skills:` frontmatter populated
- Open `skills/VERTICAL_MAP.md` → confirm all 7 verticals + strategy pod covered, no skill orphaned

---

## Critical Files

| Action | File |
|---|---|
| Create junction | `.claude/skills` → `skills/` |
| Create | `skills/VERTICAL_MAP.md` |
| Edit | `.claude/settings.local.json` (add skills path if needed) |
| Edit (per agent) | `vaival-agentic-marketing-engine/02-agents/tier-3-managers/*.md` (7 files) |
| Edit (per agent) | `vaival-agentic-marketing-engine/02-agents/tier-4-specialists/*.md` |
| Edit (per agent) | `vaival-agentic-marketing-engine/02-agents/tier-5-executives/*.md` |
| Edit (per workflow) | `vaival-agentic-marketing-engine/04-workflows/*.md` |
| Reference (read-only) | `skills/INDEX.md` (already exists, source of truth for skill list) |
| Reference (read-only) | `C:\Users\shiraz.iqbal\Downloads\Final Playbook Mid Size Team Marketing Department.docx.md` |

## Existing Utilities to Reuse

- `skills/INDEX.md` — already categorizes 190 skills by Ads/Analytics/CRO/etc. Reuse for VERTICAL_MAP generation.
- `skills/_import_log.tsv` — source-of-truth for skill → upstream-repo mapping; use for dedupe + canonical selection.
- `vaival-agentic-marketing-engine/01-playbook/department-level/role-inventory.md` — existing role → tier mapping.
- `vaival-agentic-marketing-engine/01-playbook/department-level/tool-inventory.md` — existing tool coverage to align skills to tools.

## Verification

1. `cmd /c "dir C:\Users\shiraz.iqbal\Documents\VMD\.claude\skills"` → junction resolves
2. New Claude Code session in VMD → `/skills` lists project skills
3. Ask Claude *"I need an SEO audit workflow"* → it selects `seo-audit` skill automatically
4. Open SEO Manager agent spec → `skills:` block present, 8–12 canonical skills listed
5. Run Workflow A from playbook §9.5 → agent invokes matrix-declared skills in sequence
