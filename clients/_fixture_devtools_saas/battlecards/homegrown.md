# Battlecard — Loopgate vs Homegrown (Postgres flag table)

> Last reviewed: 2026-04-23. Largest competitor by volume in our ICP — ~42% of prospects run homegrown.

## Cheat Card
- **They are:** a Postgres table + internal admin UI, maintained by 1–3 engineers.
- **When we win:** post-incident review blames flags, SOC2 pre-assessment flags a gap, headcount freeze means the team can't afford to keep building it, Platform lead pushes consolidation.
- **When they win:** small teams (<20 eng), cost-first CFOs, teams with strong NIH culture + a slack engineer.
- **3 discovery Qs:**
  1. "How many engineer-hours/week does your flag system consume?"
  2. "How do you answer 'who turned that flag on' today?"
  3. "What would your SOC2 auditor say about your flag change-approval process?"
- **Top rebuttal:** TCO calculation: 0.6 FTE × $220k fully-loaded = **$132k/yr** — before counting audit-gap risk, SDK latency variance, and outage from a bad manual flip.

## Full Card

### Who they are
A Postgres table (`features`), perhaps with an internal admin page, maybe a Slack-bot wrapper. Maintained by whichever engineer touched it last. No audit trail beyond `git log` on a config file. No experimentation.

### Why they win
1. **Zero dollar cost.** CFO can't argue with $0.
2. **No vendor review.** Fast and political-risk-free.
3. **Owned by us.** Team feels control.

### Why we win
1. **TCO reality.** 0.6 FTE is conservative; we've measured teams at 1.0+. $132k–$220k/yr in fully-loaded eng cost.
2. **Audit gaps.** Every SOC2/SOX-adjacent audit we've seen flags homegrown flag systems.
3. **SDK perf + safety.** Sub-50ms eval + edge cache + SDK fallback that homegrown almost never does well.
4. **Experimentation for free** once you're on the platform — value they don't get today.
5. **Eng retention.** "Maintenance work" is the #1 cited reason platform engineers leave.

### Trap-setting discovery questions
1. "Walk me through the last flag-related production incident."
2. "How long does it take to clean up a stale flag across the codebase?"
3. "Who approves a flag change in a regulated environment?"
4. "If your lead maintainer leaves, who picks this up?"
5. "What would experimentation look like in the current system?"

### Objection library
| They say | Rebuttal |
|---|---|
| "It works fine for us" | Run the TCO calc with real numbers; almost always surprising |
| "We can't justify a vendor" | We have a Team plan at $25/seat; priced for the "it's cheaper than 0.1 FTE" point |
| "Migration is risky" | Parallel-run mode; keep homegrown as fallback for 30d; migrator covers 90% of schemas |
| "Our auditor hasn't complained" | SOC2 Type II (2026-05) → we can share the controls auditors look for |

### Switch playbook
1. Export flag table + admin UI rules.
2. Map via migrator (covers common patterns: boolean, percentage, target list, attribute rule).
3. Dual-write SDK for 2 weeks; compare evals.
4. Cut over; keep homegrown read-only 30d.

### Landmines
- Teams <15 eng: Flagsmith OSS fits better; sending them to Loopgate Team plan is mis-sell.
- Teams where the homegrown-system builder is now a VP Eng — political landmine, needs champion-led approach.
