# Brand Voice — Loopgate

> Rubric: `/rubrics/brand-voice.yaml`.

## 1. Voice Pillars
1. **Engineer-to-engineer (not marketer-to-user).** We talk like a Staff engineer reviewing your RFC — specific, no fluff, willing to say "we don't do that yet."
2. **Proof over promise.** Every claim has a benchmark, a log, a case, or a link. No superlatives without a number.
3. **Calm, not corporate.** Trunk-based releases happen at 2am. We don't add noise.
4. **Generous.** We publish the migration guide, the OSS SDK, the comparison with competitors. We bet the customer will notice.

## 2. Tone Matrix
| Context | Formal ←→ Casual | Technical ←→ Plain | Notes |
|---|---|---|---|
| Homepage | 55 / 45 | 70 / 30 | Engineer speaks plainly to engineer |
| Docs | 65 / 35 | 95 / 5 | Technical, precise |
| Status page | 80 / 20 | 70 / 30 | Calm, factual |
| Error messages | 40 / 60 | 85 / 15 | Terse, action-oriented |
| Sales email | 50 / 50 | 60 / 40 | Respectful of time |
| Ad copy | 45 / 55 | 55 / 45 | Hook + specific number |
| Blog — technical | 40 / 60 | 80 / 20 | Personal voice, code samples |
| Blog — strategic | 55 / 45 | 50 / 50 | Opinion with evidence |
| Legal / security | 85 / 15 | 50 / 50 | Precise, no humor |

## 3. Lexicon
**Prefer:** "ship", "deploy", "flag", "eval", "audit trail", "self-host", "p95", "trunk-based", "post-incident", "kill-switch", "guardrail", "benchmark", "RFC".
**Avoid:** "revolutionary", "cutting-edge", "seamless", "world-class", "unlock", "leverage" (as verb), "synergy", "game-changing", "AI-powered" (unless literally and meaningfully true), "users" when we mean "engineers" or "developers".
**Banned:** "powerful", "turnkey" (exception: the actual migrator — it IS turnkey), "transform your business", "enterprise-grade" (every competitor claims it), "best-in-class".

## 4. Grammar & Mechanics
- Oxford comma: yes.
- Numerals: use digits for 10+; "sub-50ms", "1/3 the TCO" preserved for rhythm.
- Em-dashes: allowed, spaced — like this.
- Sentence length: target ≤22 words; break long ones.
- Reading level: Flesch 50–65 for marketing; not dumbed down, not academic.
- Contractions: yes (don't, we're, it's).
- Code in prose: use backticks.
- Numbers with units: no space (50ms, 100ms, not 50 ms).

## 5. Voice in 10 Rewrites
| Context | Before (off-brand) | After (Loopgate voice) |
|---|---|---|
| Homepage hero | "Unlock the power of feature flags with our revolutionary platform" | "Feature flags and experiments on one audit trail. Sub-50ms eval. Built for platform teams." |
| Feature page | "Our world-class SDK offers seamless integration" | "Drop-in SDK for Go, Node, Python, Ruby, Java, Rust, .NET, PHP. p95 eval: 47ms at the edge." |
| Sales email cold | "I'd love to jump on a call to discuss synergies" | "Saw you're hiring a Platform eng. Most teams that size hit flag-sprawl around month 4. Happy to send the TCO calc — no call needed unless you want one." |
| Support reply | "Thanks for reaching out. We will investigate." | "Got it. Repro'd locally. Tracking in issue #1247 — expect a patch in the next release (Thursday). Will email when out." |
| Status page | "We are experiencing service degradation" | "Eval latency elevated in us-east-1 since 14:02 UTC. SDK fallback cache is serving 100% of reads. No flag state loss. Updates every 15m." |
| Social — LinkedIn | "🚀 Excited to announce our Series B!" | "Closed a $12M Series B led by Fictive. What we're going to do with it: 2x engineering, open-source our stats engine, cut Team pricing 15%. Memo below." |
| Ad — Google search | "Best feature flag platform" | "Homegrown flags eating 0.6 FTE? Migrate in a weekend. Free trial, 10-min setup." |
| Error message | "An unexpected error occurred" | "Eval failed — falling back to default. Flag: `checkout_v2`. Check SDK version ≥ 3.2." |
| CTA | "Learn More" | "See the migration guide" / "Run the TCO calc" / "Try on your stack" |
| Blog title | "5 Amazing Benefits of Feature Flags" | "Why your flag table is eating 0.6 engineers — and what to do about it" |

## 6. Spokesperson Archetype
Three living examples (in public voice):
1. **Gergely Orosz** (Pragmatic Engineer) — specific, evidence-rich, respectful of reader's time.
2. **Charity Majors** (Honeycomb) — strong opinions, honest tradeoffs, observability-native.
3. **Dan Luu** — ruthlessly specific, willing to publish the unflattering number.

Our brand, if a person: Staff engineer with 12 years of shipping, who blogs on weekends, contributes OSS, and speaks at conferences because it's fun — not to sell.

## Rubric Evaluation (`/rubrics/brand-voice.yaml`)
| Criterion | Score | Justification |
|---|---|---|
| pillars_defined | 10 | 4 pillars with definitions + do/don't direction |
| tone_matrix | 10 | 9 contexts × 2 dials with notes |
| lexicon_prescriptive | 10 | Prefer/avoid/banned lists with rationale; persona language included |
| grammar_mechanics | 9 | Oxford, numerals, em-dash, sentence length, contractions, reading level |
| rewrites_before_after | 10 | 10 concrete rewrites across contexts |
| spokesperson_archetype | 9 | 3 living examples + "if a person" statement |
| banned_terms | 10 | Banned list with "enterprise-grade", "powerful", etc. + rationale |
| context_dials | 9 | Legal vs ad vs status page distinct |
**Weighted total: 97/100. PASS.**
