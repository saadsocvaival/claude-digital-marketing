# Winback Sequence — Dormant >90d Customers

**Audience:** customers churned or zero-use for 90+ days. Have prior paid relationship.
**Length:** 3 emails over 14 days.
**Sender:** founder@costsage.ai (this is a founder-tone moment).
**UTM:** `?utm_source=email&utm_medium=winback&utm_campaign=winback-90d&utm_content=<email#>`
**Exit conditions:** reply, reactivation, unsubscribe, hard bounce, spam.
**Pre-send check:** verify they haven't been suppressed for any reason; verify no open support escalation; verify no recent-billing-issue context.

---

## Email 1 — D0 — "What changed"

**Subject A:** {{first_name}} — long time
**Subject B:** What's changed in CostSage since you left
**Preview:** No pitch. Honest update.

**Body:**

{{first_name}},

Been a while. Looked at the calendar — it's been ~90 days since you used CostSage actively, which usually means one of three things: the tool wasn't a fit, the priority shifted, or things at {{company}} got busy. All three are normal.

If it helps, here's what's changed since you last logged in:

- {{change_1}} [TBD-OPERATOR — pull from changelog]
- {{change_2}}
- {{change_3}}

Not asking for anything. Just keeping you in the loop in case the original blocker is now solved.

— {{sender_first}}
Founder, CostSage

---

## Email 2 — D7 — "Honest question"

**Subject A:** Honest question, {{first_name}}
**Subject B:** Why CostSage didn't stick — your take?
**Preview:** Two-line reply is plenty.

**Body:**

{{first_name}},

Honest question, no agenda:

When CostSage didn't stick at {{company}}, what was the actual reason? Doesn't have to be polished — a two-line reply is more useful than a paragraph.

The three I hear most often:
1. "Our cloud spend got smaller, didn't justify the tool."
2. "We had a build-vs-buy moment and built internally."
3. "Priority shifted off cost optimization for a quarter or two."

If any of those fit, I'd just like to know — helps me sharpen who we should be talking to. If something else, even more useful.

— {{sender_first}}

**One CTA →** Reply with one line.

---

## Email 3 — D14 — "Closing the loop + door open"

**Subject A:** Closing the loop, {{first_name}}
**Subject B:** Last note — door's open
**Preview:** Won't email again unless you want me to.

**Body:**

{{first_name}},

Closing the loop on the winback thread — won't email again on this unless you want me to.

If anything changes — bigger cloud bill, FinOps refresh, new team owning cost — the door is open. We'll honor your previous account context (saved findings, integrations, role). You can reactivate without re-onboarding.

→ Reactivate: [TBD-OPERATOR app URL]?utm_source=email&utm_medium=winback&utm_campaign=winback-90d&utm_content=e3

If CostSage is permanently a no, click "remove me from outreach" below and I'll suppress immediately. No hard feelings.

Thanks for the time you gave us. Appreciate it.

— {{sender_first}}

---

## Operational notes

- Cap volume to 50/day during winback. These are warm contacts; don't burn them.
- If reply contains "remove", "stop", "no", "not interested" → suppress permanently.
- If reactivates → restore account state, route to CSM, send Engaged Customer onboarding (skip trial-nurture).
- Winback emails should never include marketing copy from current campaigns. Voice is founder-direct.
