# Bill of Materials — Issue 02

> "RI vs Savings Plans in 2026"
> Send: Tuesday Q3 W6 • 9:00 ET • From: [TBD-OPERATOR — founder] • Length: ~870 words.
> Subject line: **RIs are not dead. They're just not the answer most of the time.**
> Preview text: When each commitment instrument actually wins, in 2026.

---

## Block 1 — Editor's Note

I keep getting the same question from FinOps leads at Series B SaaS companies: "Should we still buy RIs in 2026, or just go all-in on Savings Plans?" The honest answer is "depends on three things, and most of you are getting one of them wrong." So this issue is the short version of the call I have on Slack three times a week.

## Block 2 — The Teardown

Here is the framework. There are exactly three questions that decide the call.

**Question 1: Is the workload pinned to a specific instance family?**

Reserved Instances are family-locked (with limited convertibility). Savings Plans (Compute SP specifically) are not — they apply across families and even across regions. If your workload is genuinely pinned (think a database that's been on `r6i` for two years and isn't moving), an RI buys you a deeper discount than a Compute SP — usually 5–8 percentage points more. If your workload moves around (which, in 2026, most SaaS compute does), the SP wins because the lock-in cost is too high.

**Default for most AWS-first SaaS:** Compute Savings Plans on the steady baseline, RIs only for explicitly-pinned workloads (RDS, often; ElastiCache, sometimes).

**Question 2: How confident are you in the next 12 months of usage?**

Both instruments come in 1- and 3-year terms. The 3-year term is meaningfully cheaper — typically another 8–14 points of discount on top of the 1-year. The trap: 3-year commitments on a workload that won't exist in 18 months because of a re-architecture. We see this constantly with teams migrating to Graviton or moving to managed services.

**Default:** 1-year on anything you wouldn't bet your job on for 36 months. 3-year only on the explicitly-stable bottom layer of the bill.

**Question 3: Are you covering the right percentage?**

The classic mistake is over-committing. The right coverage isn't 100%. It's the intersection of (a) your reliable steady-state and (b) your tolerance for a stranded commitment if usage drops. For most AWS-first SaaS we see, the right number is 50–70% of the trailing-90-day P50 usage. Anything above that pays for the discount with stranded-commit risk.

**Default:** start at 55%, ladder up monthly based on actual coverage utilization.

**Putting it together (for a $200K/mo SaaS with 65% compute, mostly EKS):**

- Compute SP, 1-year, no upfront, ~55% of EKS+EC2 baseline → ~18–24% recovery on covered spend.
- RDS RIs on the production database tier, 1-year, partial upfront → ~32–38% recovery on covered RDS.
- 3-year SP only on the genuinely-stable platform layer (CI runners, monitoring, ingress) → an extra 8–10 points on a small slice.

Net program impact on the bill: usually 12–18%, all-in.

The thing nobody tells you: the *operations* of this matter more than the math. A perfect ladder mismanaged is worse than a conservative ladder run on a schedule. The agent runs the schedule. (We are biased; we are also right.)

→ [Long version: RI vs Savings Plans](https://costsage.ai/blog/ri-vs-savings-plans)

## Block 3 — One Number

**28–60%.** That's the on-demand premium over commitment pricing on stable workloads, depending on family and region. If your bill has a steady baseline and zero commitment coverage, that's the size of the leak. (Source: AWS public pricing, sampled Q1 2026.)

## Block 4 — Three Links

- **AWS Compute Optimizer** — the free tool gives you decent rightsizing signals; pair with commitments analysis.
- **FinOps Foundation, "Rate vs. Usage Optimization" framework** — the canonical mental model.
- **AWS Savings Plans pricing page** — read it once a quarter; it changes more than you think.

Internally: our 10-step playbook walks through commitments at step 6 — [download here](https://costsage.ai/playbook).

## Block 5 — The Ask

If you have not run a commitment review in the last 90 days, you are probably either over-committed or under-covered. Both are expensive. Connect AWS to CostSage in under 60 seconds and the agent will tell you which one.

→ [Start your trial](https://costsage.ai/trial)

Or: reply with your current SP/RI mix as a percentage and we'll send back a quick read on whether it's in the safe band. (No pitch. We answer them all on Tuesdays.)

— [TBD-OPERATOR]

---

**Word count: ~870** ✅
**Voice checks:** number-with-unit in B1 ✅ • no banned vocabulary ✅ • CTAs present ✅ • no copilot ✅ • competitor-neutral ✅
