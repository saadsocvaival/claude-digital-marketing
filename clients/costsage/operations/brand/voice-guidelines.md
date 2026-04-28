# CostSage Voice & Tone Guidelines

> Source extraction: https://costsage.ai/ • https://costsage.ai/about • https://costsage.ai/blog/aws-cost-optimisation-best-practices • https://costsage.ai/blog/ri-vs-savings-plans
> Owner: Brand • Last updated: 2026-04-28 • Status: v1.0

---

## 1. Brand Essence (≤80 words)

CostSage is the agentic FinOps operator for AWS-first SaaS teams. We don't build dashboards — we build an AI agent that reasons, plans, and executes cost work that would otherwise sit in a backlog. Our voice is the voice of a senior cloud engineer who has run the bill, knows where waste hides, and is allergic to vendor theater. Direct. Specific. Numerate. Skeptical of dashboards. Confident about action — but always with a human in the loop.

---

## 2. The Five Tone Axes

Each axis has a target setting and do/don't pairs grounded in actual site copy.

### Axis 1 — Operator vs. Marketer  (Target: 85% Operator)
We sound like the engineer who fixed it, not the rep who sold it.

- **Do:** "On-demand pricing on stable workloads is a 28–60% premium over commitment pricing."
- **Don't:** "Unlock unparalleled savings with our revolutionary cloud intelligence platform."
- **Do:** "Right-size EC2/RDS. Typical recovery: 15–22% of EC2 spend."
- **Don't:** "Empower your organization to harness next-generation cost insights."

### Axis 2 — Direct vs. Hedged  (Target: 80% Direct)
We make claims and qualify them with data, not with adverbs.

- **Do:** "Your cloud bill is hiding thousands. We find them."
- **Don't:** "We may potentially help you possibly identify some savings opportunities."
- **Do:** "Avg. 34% reduction in compute costs." (a measured average, not a promise)
- **Don't:** "Truly transformative results that customers love."

### Axis 3 — Technical vs. Accessible  (Target: 70% Technical)
We assume the reader knows what an RI is. We do not assume they know our framework.

- **Do:** "RI / SP optimisation. Up to 72% cheaper than on-demand."
- **Don't:** "Reserved Instances are a way to save money on cloud computing by paying upfront."
- **Do:** Use FinOps, rightsizing, RI/SP, on-demand, idle, tagging, audit trail, rollback as base vocabulary.
- **Don't:** Spell out acronyms a practitioner already knows. Spell out our internal jargon every time.

### Axis 4 — Confident vs. Humble  (Target: 65% Confident, 35% Humble)
We are confident about the agent's behavior. We are humble about the operator's authority.

- **Do:** "Not a dashboard. Not a copilot. An agent that acts."
- **Don't:** "We think we might be the best FinOps tool, if you're open to that."
- **Do:** "Automation should amplify human judgment, not bypass it." (humble where it counts)
- **Don't:** "Our AI is smarter than your engineers." (never)

### Axis 5 — Plain vs. Playful  (Target: 80% Plain, 20% Playful)
Dry wit at structural moments — never in the middle of a technical claim.

- **Do:** "Make cloud waste extinct — one recommendation at a time."
- **Don't:** Pun-laden headlines, exclamation points, emoji in body copy.
- **Do:** Italicize a single charged word for emphasis (`extinct`, `wished`, `acts`).
- **Don't:** Bold or ALL CAPS. Ever, in body copy.

---

## 3. Vocabulary List

### Preferred (use freely)
- Agent, agentic, reasons, plans, executes, acts
- Rightsize, commitment coverage, RI, Savings Plan, on-demand premium
- Idle, orphaned, untagged, drift, runaway
- Recommendation, justification, audit trail, rollback, human-in-the-loop
- Bill, line item, monthly run rate, ARR, blast radius
- Waste, leakage, recovery, payback
- "Close the loop", "ship", "approve", "execute"

### Banned (never use)
- "Revolutionary", "game-changing", "next-generation", "cutting-edge"
- "Unlock", "empower", "harness", "leverage" (as verbs)
- "Solutions" as a noun standing alone ("our solutions"). Say what it is.
- "Synergy", "holistic", "robust", "best-in-class", "world-class"
- "Copilot" used about CostSage (we are explicitly not a copilot)
- "Dashboard" used about CostSage (we are explicitly not a dashboard)
- Emoji in body copy. Exclamation points outside of pull quotes.
- Customer names or logos until [TBD-OPERATOR] confirms.

### Contested (use with care)
- "AI" — okay, but prefer "agent" when referring to our product.
- "Platform" — okay in nav/IA; avoid in hero copy.
- "Optimization" / "Optimisation" — match the page; site uses British "optimisation" in titles. Stay consistent within a piece.

---

## 4. Sentence-Level Rules

### Length & rhythm
- Average sentence: 14–18 words.
- Cap any sentence at 28 words. Break with a period, not a semicolon.
- Use sentence fragments deliberately for emphasis. One per paragraph, max.
  - Example: "Not a dashboard. Not a copilot. An agent that acts."
- Vary cadence: long-explanatory followed by short-declarative.

### Numbers
- Always show the unit and the timeframe ("$61K/mo", not "$61K").
- Ranges beat single points: "15–22% of EC2 spend" reads as data; "20% of EC2 spend" reads as marketing.
- When the operator hasn't confirmed the number, mark it `[TBD-OPERATOR]` rather than guessing.

### Hedging
- Hedge with data, not with adverbs.
  - **Do:** "Average 34% reduction across customers running over $50K/mo on AWS."
  - **Don't:** "Generally we tend to see significant reductions."
- Acceptable hedges: "Average", "Typically", "Up to", "In our cohort".
- Never-acceptable hedges: "Truly", "Really", "Quite", "Pretty much", "Sort of".

### Voice
- Active voice, second person ("your bill", "your team") for outbound copy.
- First person plural ("we find them", "we asked") only when referring to CostSage as a team.
- Avoid third-person abstractions ("companies waste...") — make it about *the reader's* company.

### Punctuation
- Em dashes for asides — sparingly, max one per paragraph.
- Oxford comma always.
- One italic per paragraph for emphasis. No bold in body copy.

---

## 5. Point-of-View Stance

CostSage's POV is built on five non-negotiables:

1. **Visibility is not the product. Action is.** Every legacy FinOps tool stops at a dashboard. The job is the savings, not the chart.
2. **AI-native, not AI-bolted.** The agent is the architecture, not a feature stripe in a release note.
3. **Human-in-the-loop is a feature, not a compromise.** Approval is required. Rollback is one click. We don't apologize for that.
4. **AWS-first SaaS is the wedge.** We can talk Azure and GCP, but the canonical customer is the Series A–C SaaS with a $50K–$500K/mo AWS bill.
5. **The enemy is the dashboard.** Not CloudZero. Not nOps. The dashboard era of FinOps.

We never punch at competitors by name in copy. We punch at the *category* they all live inside.

---

## 6. Sample Paragraph Rewrites (Before / After)

### Rewrite 1 — Vendor-y feature blurb

**Before (off-voice):**
> Our cutting-edge platform leverages advanced AI to deliver world-class cost optimization solutions, empowering enterprises to unlock unprecedented value across their cloud environments.

**After (CostSage voice):**
> CostSage's agent reads your AWS bill, identifies the line items running 28–60% over commitment pricing, and ships a rightsizing plan you can approve in one click. Not a dashboard. An operator.

### Rewrite 2 — Hedged blog intro

**Before (off-voice):**
> AWS costs can sometimes be a bit of a challenge for many growing companies, and there are various strategies that may potentially help reduce them.

**After (CostSage voice):**
> A $500K/mo AWS bill is hiding $120K–$170K of recoverable waste. Most of it is in three places: idle compute, missed commitments, and untagged drift. Here's how the agent finds it.

### Rewrite 3 — Customer quote framing

**Before (off-voice):**
> Customers are absolutely thrilled with the incredible results they've achieved with our amazing platform!

**After (CostSage voice):**
> Within 48 hours of connecting AWS, the agent surfaced $61,898/mo in recoverable spend. The team approved seven of ten recommendations on day one. [TBD-OPERATOR — confirm customer attribution.]

---

## 7. Channel-Specific Modulation

| Channel | Tone tilt | Length | POV |
|---|---|---|---|
| Homepage hero | Plain + Direct, max | ≤12 words | "your" |
| Long-form blog | Operator + Technical | 1,200–1,800 words | "your" + "we" |
| LinkedIn post | Operator + Direct, light playful | 80–220 words | "I" / "we" |
| X thread | Direct + Technical | 6–10 posts | "I" |
| Newsletter | Operator + Plain | 600–900 words | "we" / "you" |
| Sales one-pager | Confident + Numerate | ≤350 words | "you" |
| Whitepaper | Technical + Humble | 2,000–3,000 words | "we" / impersonal |

---

## 8. Voice Anti-Patterns (kill on sight)

- **The Five-Adjective Stack:** "Powerful, intuitive, scalable, secure, intelligent." Replace with one number.
- **The Empty Promise:** "Transform your cloud spend." Replace with a specific mechanism.
- **The Logo Wall Tease:** "Trusted by industry leaders." Show numbers or stay silent.
- **The Buzzword Sandwich:** Any sentence with three of: leverage / synergy / holistic / robust / scalable / next-gen.
- **The Apology:** "We know FinOps is hard..." — skip the throat-clear, start with the claim.

---

## 9. Quick Self-Check (before publishing)

1. Could a CFO or a senior cloud engineer read this and not roll their eyes?
2. Is there a number with a unit and a timeframe in the first 100 words?
3. Did I use "leverage", "unlock", "empower", or "solutions" (noun)? If yes — rewrite.
4. Is there a verb of action in the headline (find, ship, cut, approve, execute)?
5. If I removed every adjective, would the sentence still be true and useful? If yes, ship.
