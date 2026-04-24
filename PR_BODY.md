# feat: Autonomous Digital Marketing OS (Stages 0–2)

> **Turns this repo from a blueprint into a runnable operating system.** Every strategic artifact in the fixture client scores ≥94/100 on its rubric.

## ⚠️ Security — before you merge

A GitHub PAT (value redacted; known to the operator) was exposed during development chats. **Revoke it on GitHub now** and issue a new one for pushing this PR. Full disclosure in `SECURITY.md`.

## What ships

### Stage 0 — Foundation
- ✅ **Skill library deduplicated**: removed duplicate `claude-skills-*` and `openclaudia-skills-*` trees; 146 canonical skills retained.
- ✅ **Rubric library** (`/rubrics/`): 19 YAMLs, pass bar 8 (ICP, positioning, messaging, brand voice, 90-day plan, weekly KPI snapshot, weekly digest, campaign brief, ad copy, email, email sequence, SEO brief, LP, battlecard, lead scoring, client ledger, HITL, agent, skill).
- ✅ **Runtime entrypoint**: `/CLAUDE.md` — 6-phase operating protocol, digest format, 7 non-negotiables, key paths.
- ✅ **Permissions + hooks**: `.claude/settings.json` with pre-commit secret-scan regex.
- ✅ **Skill manifest**: `.claude/skills.manifest.json` binds 130+ skills to the 8 Heads.

### Stage 1 — Orchestrator + 8 Department Heads
- ✅ `cmo-orchestrator` agent: 9-step protocol, decision-authority matrix (full / HITL / escalate), digest response format.
- ✅ 8 Head agents: Growth, Performance, SEO/GEO/AEO, Content, CRO, Analytics, Automation, Brand. Each: remit, authority, skill bindings, feeds in/out, KPIs, HITL triggers, policy citations, output formats, self-rubric ≥94/100.
- ✅ 4 orchestration skills: `onboarding`, `goal-decomposer`, `weekly-tick`, `hitl-request`.
- ✅ 15 templates under `/templates/` for every artifact type.
- ✅ Multi-tenant scaffold at `clients/_template/`.

### Stage 2 — Dogfood fixture + evals
- ✅ `clients/_fixture_devtools_saas/` — **Loopgate** (B2B SaaS Series B, feature-flag platform). ~40 rubric-graded artifacts:
  - Ledger, ICP (3 personas), positioning (Moore), brand voice, messaging, offer.
  - 90-day plan with funnel math + phases + exit criteria + risk register.
  - Q2 OKRs (4 NSMs + 8 Head objectives + 32 KRs) with baseline / target / owner / source.
  - UTM taxonomy, lead scoring model (validated vs synthetic cohort), attribution model.
  - 3 battlecards (LaunchDarkly, Statsig, homegrown).
  - Editorial calendar (13 weeks × 5 pillars).
  - 3 campaign briefs with stop-loss + launch gate.
  - 5 ad sets (Google search, LinkedIn, retargeting/display, Reddit/podcast, Meta/X).
  - 3 email sequences (onboarding, enterprise nurture, winback).
  - 1 LP brief (TCO calculator).
  - SEO cluster: pillar + 8 spokes.
  - 10 content outlines with 1→10 repurpose plans.
  - Week-1 KPI snapshot with sourcing footnotes.
  - 1 pre-registered activation experiment.
  - Append-only ledger-events JSONL.
- ✅ 10 golden eval cases + README + run-evals doc.

### Stage 2.5+ — Honest scope callout
- ⚠️ **Self-rubric only.** Every grade is from the same system that generated the artifact. External CMO review is explicitly Stage 2.5 in `ROADMAP.md`.
- 🔲 **No real MCP tool-calling** to GA4/Ads/HubSpot/etc. Connectors specify interfaces; runtime wiring is Stage 3.
- 🔲 **No autonomous scheduler.** Weekly-tick is operator-triggered today.
- 🔲 **No real-client pilot.** The fixture is a designed archetype.

## Files

New: `/CLAUDE.md`, `/.claude/{settings.json,skills.manifest.json,agents/*}`, `/skills/orchestration/*`, `/rubrics/*` (19), `/templates/*` (15), `/clients/_template/**`, `/clients/_fixture_devtools_saas/**` (~40), `/vaival-agentic-marketing-engine/17-testing/evals/**` (11), `/AUDIT.md`, `/ROADMAP.md`, `/SECURITY.md`, `/CONTRIBUTING.md`, `/PR_BODY.md`.

Modified: `/README.md` (rewrite), `/.gitignore` (secret blocks, client-secrets excluded, standard ignore list).

Deleted: `skills/claude-skills-*` (duplicates), `skills/openclaudia-skills-*` (duplicates). Canonical set preserved.

## Verification

1. `find . -type f | wc -l` — roughly +100 net new files vs. `main`.
2. `grep -rE 'ghp_|sk-[a-zA-Z0-9]{20}|xox[baprs]-|AKIA[0-9A-Z]{16}' .` — clean.
3. Cold-read test: open repo, follow `README.md` quick-start, orchestrator should load fixture and produce a digest.
4. Rubric check: every fixture strategic artifact ends with `## Rubric Evaluation` scoring ≥94/100.

## Reviewer checklist

- [ ] GitHub PAT rotated (see SECURITY.md)
- [ ] `AUDIT.md` coverage matrix reviewed; known gaps acceptable?
- [ ] Fixture artifacts sampled (recommend: `plan.md`, `okrs/2026-q2.md`, `campaigns/2026-q2-demand-platform-eb.md`, `seo-cluster/pillar-flag-tco.md`)
- [ ] ROADMAP Stages 3–5 gating agreed
- [ ] Orchestrator dry-run executed

## After merge

1. Stage 2.5: send 3 fixture artifacts to 2 external senior marketing operators for adversarial review.
2. Stage 3: scope MCP tool-calling work for GA4/Ads/HubSpot.
3. Stage 4/5: sign first design-partner pilot.

---

🤖 Generated with [Claude Code](https://claude.com/claude-code). Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>
