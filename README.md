# claude-digital-marketing

Vaival Marketing Department — agentic marketing engine + 190 Claude Code marketing skills mapped to a mid-size SaaS marketing playbook.

## Contents

- `skills/` — 190 marketing skills (SEO, content, paid, CRO, email, social, analytics) sourced from coreyhaines31, OpenClaudia, aaron-he-zhu, AgriciDaniel, alirezarezvani. Each has a valid `SKILL.md`. See [`skills/INDEX.md`](skills/INDEX.md) and [`skills/VERTICAL_MAP.md`](skills/VERTICAL_MAP.md).
- `vaival-agentic-marketing-engine/` — 5-tier agent hierarchy (Founder → CMO/Head → 7 Vertical Managers → Specialists → Coordinators) with workflows, connectors, governance, memory, ledger, QA, approvals. 49 agent specs wired to canonical skills.
- `MARKETING_SKILLS.md` — master index of every marketing/SEO/copywriting/content skill known across GitHub, Smithery, LobeHub, SkillsMP, + CMO/awesome-* lists.
- `PLAN.md` — plan used to wire 190 skills into the engine + playbook.
- `.claude/` — Claude Code project config (permissions; skill junction excluded via `.gitignore`).

## Usage

Open this repo in Claude Code. Skills auto-discover via `.claude/skills` junction to `skills/`. Ask for any marketing task — orchestrator routes to the right agent → canonical skill.

```
# recreate skill junction (Windows)
cmd /c mklink /J ".claude\\skills" "skills"
```

## Playbook source

Mid-Size SaaS Digital Marketing Department Playbook (Executive Reference Edition, April 2026) — 7 verticals, 24 roles, 4 North Star metrics.
