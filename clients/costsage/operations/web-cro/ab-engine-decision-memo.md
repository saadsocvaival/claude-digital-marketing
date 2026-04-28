# A/B Engine Decision Memo

**Status:** Recommendation, awaiting operator sign-off
**Date:** 2026-04-28
**Decision required:** Pick one A/B testing engine for costsage.ai before launching tests 001-003.

---

## 1. Requirements

1. **Cost** — Sprint-2 budget supports free or ≤$50/month tier
2. **No measurable LCP / CLS hit** — site is on a tight Core Web Vitals budget (G12)
3. **Server-side or hybrid execution preferred** — pure-client engines (Optimizely Web, VWO classic) cause flicker/CLS regressions
4. **Simple JS / no heavy SDK** — current site is static HTML overlay, no React framework
5. **Privacy-friendly + GDPR-compliant** (CostSage targets EU buyers)
6. **Free GA4 / Plausible integration** for outcome tracking
7. **Simple QA** — operator can run a test without engineering

## 2. Candidates

| Engine | Cost | Execution | CWV impact | GDPR | Verdict |
|---|---|---|---|---|---|
| Google Optimize | n/a — sunset Sep 2023 | — | — | — | Dead. |
| GrowthBook (open source self-hosted or cloud) | Free OSS / $0-$200 cloud | Server-side or client | Low (server-side) | Yes | **Strong contender** |
| PostHog | Free up to 1M events / $0 base | Hybrid | Low | Yes | **Strong contender** — also gives session recordings + analytics |
| Optimizely Web | $$$ enterprise | Client | Medium-high | Yes | Out — too expensive, flicker risk |
| VWO | $$$ from ~$200/mo | Client | Medium | Yes | Over budget |
| AB Tasty | $$$ | Client | Medium | Yes | Over budget |
| Statsig | Free up to 1M events | Server-side or client | Low | Yes | Strong contender, more eng-heavy |
| Convert.com | $$ from ~$100/mo | Client | Medium | Yes | OK but paid |
| Custom (50-line JS + cookie + GA4 events) | Free | Client | Very low | Yes | Viable for sequential / 2-arm tests only |

## 3. Recommendation

**PostHog (cloud free tier)** is the recommended choice.

Reasons:
1. Free up to 1M events/month — covers current site traffic 10x over
2. Adds session-recording + product analytics that close the gap identified in `form-funnel-audit.md` §6 — one tool, one snippet, instead of layering Clarity + GA4 + GrowthBook
3. EU hosting region available (eu.posthog.com) — GDPR clean
4. Lightweight snippet (~30KB gzipped, async) — minimal CWV impact
5. Built-in feature-flag + experiment evaluator — supports Tests 001-003 directly
6. Self-host migration path if scale or compliance demands it later

**Runner-up:** GrowthBook OSS self-hosted on the existing soc-server. Lower vendor risk; higher operator overhead. Pick this if data residency forbids any third-party.

## 4. Anti-patterns to avoid

- Don't ship Optimizely / VWO classic-mode — the synchronous-load flicker breaks CWV (G12).
- Don't run >2 concurrent tests on the same page until variance is measured.
- Don't run an SEO-sensitive H1 test (Test 003) without an SSR variant or a Googlebot pin.

## 5. Operator next steps

1. `[TBD-OPERATOR]` — sign off on PostHog vs GrowthBook
2. `[TBD-OPERATOR]` — create org + EU project
3. Eng — add async snippet to overlay `<head>` (one line)
4. Operator — define Tests 001-003 as PostHog experiments
5. Operator — set guardrail metrics (bounce rate, LCP, error rate) before launch

## 6. Decision log

| Date | Decision | Owner |
|---|---|---|
| 2026-04-28 | Recommendation: PostHog | CRO operator |
| `[TBD-OPERATOR]` | Final selection | Founder |
| `[TBD-OPERATOR]` | Snippet shipped | Eng |
