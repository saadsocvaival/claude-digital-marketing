# Loopgate — Category Design

## 1. Category POV
- **Problem we name:** Feature-flag platforms were designed for deploy-day risk control, not for the continuous experimentation, permissioning, and runtime config that modern product teams need. Teams are using flag platforms as a crude registry and rebuilding everything else.
- **Old-world assumption we reject:** "A feature flag is a boolean gate controlled by ops."
- **New-world assumption we assert:** A flag is a unit of runtime product policy — experiment, rollout, entitlement, config, kill-switch — owned by the team that ships the feature.
- **Why now:** LLM-generated code + AI agents are 10×-ing deploy frequency, exposing that flag infrastructure designed for quarterly rollouts breaks under continuous AI-authored change.

## 2. Category name
- **Proposed category:** **Runtime Product Policy**
- **One-liner:** The control plane for every runtime decision a product makes.
- **Adjacent we're NOT:** feature-flag-as-a-library (LaunchDarkly OG), config management (LaunchDarkly's other half), experimentation-only (Statsig), entitlement-only (Stigg).

## 3. King-making strategy
- **Lightning-strike:** Publish "The State of Runtime Product Policy 2026" — primary research survey of 400 eng leaders, with a benchmark tool + public dataset. Anchor event at a named engineering conference Q3.
- **Thought-leadership cadence:** weekly essay series ("Flags aren't flags anymore") on company blog + founder LinkedIn.
- **Analyst/press:** target Gartner "Cool Vendor in Modern App Dev" mention + DevClass / The New Stack feature; brief 5 named analysts (Redmonk, IDC, Gartner, Forrester, GigaOm) in Q2.
- **Community:** Loopgate Runtime Summit (virtual, 500 eng leaders Q4) + Slack community + monthly office-hours.

## 4. Proof of category
- **Reference customers (willing to tell the story):** {Acme}, {Fintech Co}, {Devtools Inc} — each unifying ≥3 flag-adjacent use cases on Loopgate.
- **Category-defining metric:** *Runtime Policy Fragmentation Index* — # of separate systems controlling runtime decisions per org. Our customers reduce it from 6–8 → 1.
- **Ecosystem partners:** Vercel, Temporal, and one major APM for integrations that only make sense in this category.

## 5. Anti-patterns avoided
- Not claiming "AI-powered flags" — AI is not a category.
- Not renaming "feature flags" — that's a feature, not a category.
- Not category-of-one until proof is in place.

## 6. Gating
- **Category claim fully live when:** 5 reference customers quoted publicly + 1 analyst mention + first imitation signal from a competitor.
- **Until then:** position *into* feature-management with a "Runtime Product Policy" POV drumbeat.

---
**Self-score:** 87/100 — strong shift, concrete mechanism, honest gating. Loses points on: reference customers fictional in fixture; category name "Runtime Product Policy" will need customer testing.

**Critic-score:** TBD (run `adversarial-critic`).
