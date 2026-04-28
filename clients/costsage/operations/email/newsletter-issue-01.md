# Newsletter Issue 01 — FinOps for AI Workloads

**Subject A:** Why GPU FinOps breaks the old playbook
**Subject B:** An idle G5 costs ~10x an idle M5
**Preview text:** Three ways AI workload economics break classic FinOps — and what to do.
**Send window:** Tuesday or Thursday, 10am ET [TBD-OPERATOR].
**UTM campaign slug:** `nl-issue-01-finops-ai`

---

## Block 1 — Hook

An idle G5 instance on AWS costs roughly 10x an idle M5.

That single number breaks more FinOps spreadsheets than anyone wants to admit. Most cost-optimization playbooks were written for CPU-shaped workloads, where being a little wasteful was fine because the underlying unit was cheap. AI compute isn't cheap, and "a little wasteful" compounds fast.

This issue: three ways AI workload economics break the classic FinOps playbook — and what to do tomorrow morning.

---

## Block 2 — Deep dive

**Break #1: idle cost is non-linear.**

Classic FinOps says "idle is bad." For CPU, *how* bad scales linearly — an idle m5.large at $0.096/hr is annoying, an idle m5.4xlarge is ~8x more annoying. For GPU, the math gets dramatic. A g5.4xlarge sits around ~$1.62/hr; a p4d.24xlarge runs north of ~$32/hr. An overnight idle weekend on a single p4d eclipses an entire idle CPU fleet for the same period. Your "<5% utilization" alert needs a different threshold for GPU resources, and the action is "auto-stop", not "consider downsizing next quarter."

**Break #2: RIs and Savings Plans cover GPU differently.**

Compute Savings Plans cover G/P-series, but the discount tiers are structured differently than the CPU baseline most teams have committed to. If your existing Compute SP was sized when your fleet was 90% M/C-series and you've since added GPUs, your blended utilization probably looks fine while your *actual* coverage on GPU spend is low. Recompute coverage *by instance class*, not in aggregate. The cost-by-class report tells you whether your commits actually map to your fleet today.

**Break #3: inference and training need different commit profiles.**

Inference is steady-state, predictable, and a great candidate for reservations. Training is bursty, often experimental, and a terrible reservation candidate. Lumping them together — "GPU spend" as one line — is the most common mistake. Treat them like two different cost centers, with different commit policies (inference: reserve aggressively; training: spot + short-term commits, capped).

The mental model that helps: AI compute is closer to a managed database in cost behavior than to an EC2 fleet. Idle is expensive, schedules matter, and the optimization motion is mostly upstream — in workload design — not downstream in commit-buying.

For the AWS-side of this, our /aws page goes deeper on instance-class commit strategy: costsage.ai/aws?utm_source=email&utm_medium=newsletter&utm_campaign=nl-issue-01-finops-ai&utm_content=block2

---

## Block 3 — Tactical tip

**Tip: schedule notebook GPU shutdown tonight.**

Most data-science teams use notebook instances (SageMaker, EC2 g-series, etc.). Most don't ssh in at 2am, and most leave them running 24/7 anyway.

Add a daily 8pm local-time auto-stop on every notebook tagged `team=data-science`. Two-line Lambda + EventBridge rule. Recover the time-savings: 12 hrs/day × 5 days + 48 hrs weekend = ~108 idle hours/week eliminated per notebook. On a g5.4xlarge that's ~$175/wk per notebook. Multiply by your fleet.

If anyone needs the resource overnight: an `override-tag` skip pattern + Slack notify keeps it humane.

---

## Block 4 — Community

The FinOps Foundation has a working group on AI workload cost — open and worth joining if you're hands-on with this. ([TBD-OPERATOR confirm link]).

Reader question (paraphrased) from a CTO last week: *"We're paying $40K/mo on inference and management thinks it's high. How do I tell?"*

Short answer: divide it by your monthly inferences-served. If you can't, that's the bigger problem; cost-per-inference is the only honest unit. Once you have it, *trend* over 6 months tells you whether your engineering is improving or your bill is just chasing your traffic.

---

## Block 5 — CTA

Want to see GPU cost broken out by instance class on your account, with idle hours flagged? Run a 10-minute audit:

→ costsage.ai/aws?utm_source=email&utm_medium=newsletter&utm_campaign=nl-issue-01-finops-ai&utm_content=cta

— {{sender_first}}
Founder, CostSage
(Reply works — I read everything.)

---

[Footer per compliance-footers.md]
