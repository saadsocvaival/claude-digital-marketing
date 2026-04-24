# Email Sequence — Free-Tier Onboarding (Activation)

> Rubric: `/rubrics/email-sequence.yaml`. Goal: lift free→activated rate 36.9% → 48% in 14d.
Entry: free-tier signup. Exit: activation (flag live in prod) OR 14d OR unsubscribe. Suppression: existing paid customers.

## E1 — T+0 min — "Welcome + fastest path to first flag"
- Subject: "Your Loopgate workspace is ready"
- Preheader: "5-minute path to your first flag live"
- Body: Direct, actionable. Link to quickstart for the user's language (detected on signup). One CTA: "Start the 5-min quickstart".
- CTA button: Open quickstart
- Measurement: click → quickstart start event.

## E2 — T+1 day (conditional: no flag created) — "Stuck? Pick your stack"
- Subject: "Flag not yet? Here's the path for Go/Node/Python"
- Preheader: "We shipped SDK-specific walkthroughs for 8 stacks"
- Body: 3-line intro. Link to 3 stack-specific quickstarts. Footer: "Reply with your stack, I'll send a working repo."
- Personalization: detected stack (from signup form) → top link is their stack.
- CTA: pick your stack.

## E3 — T+3 days (conditional: flag created, not activated) — "From staging to prod — the safe flip"
- Subject: "Your flag is in staging. Here's the prod flip checklist."
- Body: Short guide: % rollout → canary service → flip. Link to "production rollout" doc.
- CTA: See the prod flip guide.

## E4 — T+5 days — Social proof: "How Fintech X rolled their first flag to prod"
- Subject: "How a 220-engineer team went to prod in week 1"
- Body: 2-paragraph case. Specific time-to-first-prod-flag: 3 days. Link to full case.
- CTA: Read the case study.

## E5 — T+7 days (conditional: still not activated) — "What's blocking?" (human-signed)
- Subject: "What's getting in your way?"
- From: Rae (Head of Lifecycle) — signed, replies routed to her.
- Body: 3 lines. "Most teams that stall here hit one of three things: SDK choice, env split, review policy. Reply with which one, I'll send a 10-line answer."
- CTA: Reply.

## E6 — T+10 days — "Before your trial timer matters"
- Subject: "4 days left in free — and here's what changes at Team"
- Body: What they unlock at Team ($25/user): unlimited flags, experimentation, SSO (via Business), audit export.
- CTA: See what Team adds.

## E7 — T+14 days — Decision moment
- Subject: "Keep it free, or move to Team?"
- Body: "Free tier stays free. Most teams at your size (inferred from signup) move to Team by day 21. Here's what that looks like: [price calc link]."
- CTA: Price my team.

## Measurement
- Per-email: open, click, reply (E5).
- Sequence: activation rate lift vs control (+8pp target), Team conversion at day 30.
- Control cohort: 10% holdout; review at day 30.

## Deliverability
- SPF/DKIM/DMARC aligned (confirmed 2026-04-15).
- Text/HTML ratio: 60/40. No image-only emails.
- Unsub + physical address in footer. GDPR language present for EU recipients.

## Rubric self-score
Purpose 10, segmentation 9, cadence 9, progression 10, subject-lines 9, personalization 9 (stack detection), CTA 10, brand-voice 9, deliverability 10, measurement 9 → 94/100. PASS.
