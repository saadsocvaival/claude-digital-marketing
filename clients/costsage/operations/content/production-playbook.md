---
artifact: content-production-playbook
date: 2026-04-30
status: active
purpose: the actual brief→draft→review→schema-pack→publish flow for every CostSage content piece
---

# Content Production Playbook

> Every content piece on costsage.ai goes through these 5 stages. No exceptions, no shortcuts.

## Stage 1 — Brief

**Owner:** Content strategist agent (or Head of Content)
**Input:** keyword cluster + target ICP segment
**Output:** brief in `operations/content/briefs/<slug>.md`
**Time:** 30-60 min

Required sections (use `brief-template.md`):
- ICP / Audience
- Search intent
- Target keyword cluster (primary + 8-12 secondary)
- Competitor SERP analysis
- Outline (10-14 H2s)
- Internal-link plan (8 internal links)
- FAQ block (5 Q+As)
- CTA + length target + distribution map
- Brand-voice notes (banned terms, preferred patterns)

**Quality gate:** does the brief mention specific numbers / examples / decision-frames? Or is it generic?

## Stage 2 — Draft

**Owner:** Writer agent (or Head of Content)
**Input:** approved brief
**Output:** markdown draft at `operations/content/drafts/<slug>.md` (or HTML pillar at `pages/<slug>.html`)
**Time:** 2-4 hours per pillar (1,800-2,400 words); 1 hour per how-to (800-1,200 words)

Rules:
- Single canonical-answer paragraph (50-80 words) immediately after H1 — for AEO/featured snippets
- Question-shaped H2s where natural (improves LLM citation rate)
- One concrete number per H2 minimum
- Internal links inserted per brief plan
- No fabricated stats; mark `[unverified]` if uncertain

## Stage 3 — Review (brand-voice + factual)

**Owner:** Brand-voice review agent (`operations/brand/brand-review.py`)
**Input:** draft
**Output:** review report (pass/fail + line-numbered fixes)
**Time:** 5 min automated + 15-30 min human review

Auto-checks:
- Banned terms (synergy, leverage, best-in-class, etc.)
- Voice attribute drift
- Category-claim consistency ("Agentic, Not Dashboard")
- Forbidden-stat patterns (any [TBD] flagged claim)
- Missing footer disclaimer (Sage Group disambiguation)

Human checks:
- Factual accuracy of any claim
- Tone match to ICP
- Does it answer the search intent?

**Quality gate:** can a senior CMO ship this? If not, kick back to Stage 2.

## Stage 4 — Schema pack

**Owner:** SEO agent (`vaival-agentic-marketing-engine` skills)
**Input:** approved draft
**Output:** HTML with full schema graphs injected
**Time:** 10 min

Required schema per piece type:
| Type | Required schemas |
|---|---|
| Pillar page | WebPage + Article + FAQPage + BreadcrumbList + WebSite ref + Organization @id ref |
| Comparison page | + ItemList (vendors as SoftwareApplication) |
| How-to | + HowTo + HowToStep |
| Blog post | Article + BreadcrumbList + Author Person ref |

OG + Twitter Card metadata mandatory. Lang attribute mandatory.

## Stage 5 — Publish

**Owner:** Web/CRO agent (server-side overlay edit) OR D1 source-repo PR (when collaborator access lands)
**Input:** schema-packed HTML
**Output:** live URL at https://costsage.ai/<slug>
**Time:** 5 min via overlay path; 30 min via source-repo PR

Overlay path:
```bash
ssh marketing-claude-soc 'cat > /opt/wordpress/web-overlay/<slug>.html' < draft.html
ssh marketing-claude-soc 'docker exec costsage-web nginx -s reload'
```

If new directory created (e.g., `/whitepaper/<slug>`): force-recreate:
```bash
ssh marketing-claude-soc 'docker compose -f /opt/wordpress/docker-compose.yml up -d --force-recreate costsage-web'
```

Post-publish:
- Curl URL: expect 200
- Validate every JSON-LD with `python3 json.loads`
- Update `pages/sitemap-core.xml` with new entry
- Submit ping: `curl https://www.google.com/ping?sitemap=https://costsage.ai/sitemap-index.xml`

## Cadence

| Type | Cadence |
|---|---|
| Pillar | 1 / 2 weeks |
| How-to | 2 / week |
| Blog post | 1 / week |
| Newsletter | 1 / 2 weeks |
| Whitepaper | 1 / quarter |
| Customer story | 1 / month (ops-permitting) |

## Quality gates summary

A piece can NOT publish unless:
- ✅ brand-review.py exits 0
- ✅ All JSON-LD parses with json.loads
- ✅ All internal links return 200
- ✅ FAQ block has at least 4 Q+As
- ✅ Brand-voice attribute count ≥3 of the 5 axes
- ✅ At least one specific number per H2 (or `[unverified]` flag)

## Rollback

If a piece needs to come down:
1. Remove from sitemap (don't 404)
2. 301 redirect to nearest equivalent (or homepage)
3. Mark in `operations/content/decommissioned-log.md`
4. Don't delete the asset; archive in `pages/_archive/`

## Weekly retro

Every Friday, the Head of Content reviews:
- Pieces published this week
- Pieces that missed quality gates (and why)
- Engagement signals (organic clicks, social amplification, time-on-page)
- One specific improvement to add to the playbook
