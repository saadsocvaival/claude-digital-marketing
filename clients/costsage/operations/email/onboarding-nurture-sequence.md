# Onboarding Nurture Sequence — Trial Users (7 emails)

**Audience:** signed up for free trial of CostSage. AWS read-only role connected (or pending).
**Sender:** "{{sender_first}} from CostSage" (founder/team).
**From:** onboarding@costsage.ai [TBD-OPERATOR].
**Reply-to:** founder@costsage.ai (real human).
**UTM:** `?utm_source=email&utm_medium=onboarding&utm_campaign=trial-nurture&utm_content=<email#>`
**Single-CTA per email.**
**Exit conditions:** trial converted to paid (skip remaining), unsubscribed, requested deletion, hard bounced, marked spam.

---

## Email 1 — D0 — Welcome

**Subject A:** Welcome to CostSage, {{first_name}}
**Subject B:** {{first_name}} — your CostSage trial is live
**Preview:** Two things to do in the next 10 minutes.

**Body:**

{{first_name}},

Welcome — your CostSage trial is live.

Two things to do in the next 10 minutes:

1. **Connect your AWS account** (read-only IAM role). Step-by-step: [TBD-OPERATOR — app deeplink]
2. **Confirm your primary cost concern** so the agent prioritizes the right audit angle (commits, idle, tagging, or all three).

Once connected, you'll see your first findings in ~30 minutes.

**One CTA →** Finish setup: [TBD-OPERATOR — app URL]?utm_source=email&utm_medium=onboarding&utm_campaign=trial-nurture&utm_content=e1

Reply if anything is broken — I read every reply.

— {{sender_first}}, Founder

---

## Email 2 — D1 — Setup nudge (only sent if not connected)

**Subject A:** {{first_name}}, one setup step left
**Subject B:** Need a hand connecting AWS?
**Preview:** Common gotchas, fastest path.

**Body:**

{{first_name}},

Noticed you haven't connected an AWS account yet — totally fine if you're still evaluating.

Two common gotchas:

1. The IAM role needs the AWS-managed `ReadOnlyAccess` policy (not full admin — we never need write access).
2. The trust policy uses our account ID + an external ID we generate (per-customer; prevents the confused-deputy problem).

Full guide: [TBD-OPERATOR — docs URL]

**One CTA →** Connect now: [TBD-OPERATOR — app URL]?utm_source=email&utm_medium=onboarding&utm_campaign=trial-nurture&utm_content=e2

Or reply with any blocker and I'll get it sorted today.

— {{sender_first}}

**Branch logic:** if AWS connected at D1, skip and send Email 3 on D3.

---

## Email 3 — D3 — First-value

**Subject A:** Your first CostSage findings
**Subject B:** {{first_name}} — what we found in your account
**Preview:** Three findings, ranked by $ impact.

**Body:**

{{first_name}},

Your account has been live in CostSage for ~72 hours, long enough for a first pass. Three highest-impact findings ranked by estimated annual savings — full detail in-app:

1. {{finding_1_title}} — est. {{finding_1_savings}}/yr
2. {{finding_2_title}} — est. {{finding_2_savings}}/yr
3. {{finding_3_title}} — est. {{finding_3_savings}}/yr

Each has a one-click "draft a PR" or "draft a ticket" action. The PR includes evidence, rollback steps, and an estimated $ impact.

**One CTA →** Open dashboard: [TBD-OPERATOR — app URL]?utm_source=email&utm_medium=onboarding&utm_campaign=trial-nurture&utm_content=e3

— {{sender_first}}

(If your account has fewer than three findings, that's a great sign — usually means the obvious leaks are already plugged.)

---

## Email 4 — D5 — Case study

**Subject A:** How a similar SaaS used CostSage in week 1
**Subject B:** {{first_name}} — one customer's first 7 days
**Preview:** Anonymized walkthrough.

**Body:**

{{first_name}},

Anonymized example of what week 1 of CostSage typically looks like at a SaaS like {{company}}:

- Day 1: AWS connected. 17 findings surfaced; 4 over $5K/yr each.
- Day 3: top finding (over-committed Compute SP) flagged. Team modified commit, recovered 11% on next bill cycle.
- Day 5: tagging gap report led to SCP rollout decision.
- Day 7: first agent-drafted PR merged (right-size on a stale staging cluster). $1,840/mo saved.

We wrote this customer-shape up here: costsage.ai/aws?utm_source=email&utm_medium=onboarding&utm_campaign=trial-nurture&utm_content=e4

**One CTA →** See your equivalent week-1 plan in-app: [TBD-OPERATOR app URL]

— {{sender_first}}

---

## Email 5 — D7 — Expansion idea

**Subject A:** Have you seen the Slack integration?
**Subject B:** {{first_name}} — push findings into Slack
**Preview:** Optional, takes 2 minutes.

**Body:**

{{first_name}},

Most teams find CostSage clicks once findings show up where they already work. The two highest-leverage integrations:

1. **Slack** — daily digest + high-value finding alerts in your channel of choice.
2. **GitHub / GitLab** — agent-drafted PRs go directly into your repo with the right reviewers.

Each is a 2-minute setup.

**One CTA →** Add Slack: [TBD-OPERATOR — app integration URL]?utm_source=email&utm_medium=onboarding&utm_campaign=trial-nurture&utm_content=e5

— {{sender_first}}

---

## Email 6 — D12 — Trial-end coming

**Subject A:** Your CostSage trial ends in 2 days
**Subject B:** {{first_name}} — trial ends Friday
**Preview:** What carries over, what doesn't.

**Body:**

{{first_name}},

Quick heads-up: your trial ends {{trial_end_date}} (in ~2 days).

What you've identified so far on {{company}}:
- {{total_findings_count}} findings
- ~{{total_estimated_savings}}/yr in addressable savings
- {{actions_taken_count}} agent-drafted PRs/tickets

Pricing is on the site (no "Contact us" tier): costsage.ai/pricing?utm_source=email&utm_medium=onboarding&utm_campaign=trial-nurture&utm_content=e6

If you'd like an extension to finish evaluating, just reply — happy to extend.

**One CTA →** Convert: [TBD-OPERATOR — billing URL]

— {{sender_first}}

---

## Email 7 — D14 — Trial converted OR extension offer

**Branch A — Converted:**

**Subject A:** Welcome to CostSage proper, {{first_name}}
**Subject B:** {{first_name}} — you're in
**Body:**

{{first_name}},

Glad to have you on board.

Three things that change now:
1. Findings keep refreshing daily, no trial cap.
2. Agent-drafted actions are unlimited.
3. You're routed to {{ae_or_csm}} as your primary contact (cc'd here).

If anything ever feels off, my reply-to is real.

— {{sender_first}}

**One CTA →** Book your 30-min onboarding deep-dive: [TBD-OPERATOR — calendar URL]

---

**Branch B — Not converted, want extension:**

**Subject A:** Want another 14 days, {{first_name}}?
**Subject B:** Extending your trial — no strings
**Body:**

{{first_name}},

Trial ended without a conversion — totally fine. If you want another 14 days to finish evaluating (or get a teammate to look), reply with "extend" and I'll switch it on. No card required.

If CostSage isn't a fit, a one-line "not for us, here's why" reply is the most useful thing — helps me improve the product.

**One CTA →** Reply "extend" or "not for us"

— {{sender_first}}

---

## UTM convention recap

`?utm_source=email&utm_medium=onboarding&utm_campaign=trial-nurture&utm_content=e<#>`
- `e1` = Welcome / D0
- `e2` = Setup nudge / D1
- `e3` = First value / D3
- `e4` = Case study / D5
- `e5` = Expansion / D7
- `e6` = Trial-end / D12
- `e7` = Converted-or-extension / D14
