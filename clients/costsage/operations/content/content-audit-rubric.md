# Content Audit Rubric — Quarterly

> Run every 90 days. Outcome: each piece on costsage.ai gets a verdict — **refresh / prune / decline / keep**.
> Owner: Content Lead • v1.0 • 2026-04-28

---

## 1. Why audit

Content compounds, but only if it's maintained. Stale claims, broken internal links, dead competitor references, and outdated statistics quietly erode brand trust and SEO signal. The audit is the maintenance pass that keeps the corpus working.

## 2. Inputs

- Full sitemap (or `costsage.ai/sitemap.xml`).
- Last 90 days of organic traffic per URL ([TBD-OPERATOR] — confirm analytics tool: GA4 / Plausible / Fathom).
- Last 90 days of conversion attribution (trial signups by entry URL).
- Backlinks per URL (Ahrefs/Semrush export).
- Voice-guideline compliance (manual scan).

## 3. The four verdicts

### KEEP
Piece is performing, on-voice, accurate, and current. No action.

**Criteria (all must be true):**
- Traffic stable or growing in the trailing 90 days.
- All numeric claims still accurate (or marked TBD-confirmed).
- All internal links resolve.
- Voice-guideline compliant on a fresh read.
- No competitor reference older than 6 months.

### REFRESH
Piece has earned its rank but the content has drifted from current truth.

**Criteria (any one):**
- ≥1 numeric claim out of date.
- 1+ broken internal/external link.
- An H2 section is materially obsolete (e.g., references a service tier that AWS deprecated).
- Voice has drifted from current `voice-guidelines.md` (e.g., uses banned vocabulary in headings).

**Action:** rewrite affected sections, refresh meta description, re-publish with updated date, internal-relink to newer pillars, ship a new repurposing pass.

### PRUNE
Piece is splitting traffic with a stronger sibling, or is too thin to rank.

**Criteria (any one):**
- <50 organic visits in trailing 90 days AND <2 backlinks AND no conversions.
- Two pieces target the same primary keyword, and one outperforms by ≥3×.
- Word count <500 with no unique angle.

**Action:** redirect (301) to the strongest sibling. Preserve any backlink equity. Remove from sitemap.

### DECLINE
Piece references a claim or customer that the operator has not confirmed (or has retracted), and we cannot fix it without losing the article's spine.

**Criteria (any one):**
- A central data claim is now disputed or unsupported.
- A named customer has asked to be removed.
- The piece's thesis no longer aligns with the current category narrative.

**Action:** unpublish. Document the reason. Add to "do not republish" list.

## 4. Scoring rubric (per piece)

Score each piece 1–5 on five dimensions. Total ≥18 → keep. 13–17 → refresh. 8–12 → prune. ≤7 → decline.

| Dimension | 1 | 3 | 5 |
|---|---|---|---|
| Traffic | <25 visits/90d | 200–500/90d | 2,000+/90d or top-3 SERP |
| Conversion | 0 trials | ≥1 trial attributed | ≥5 trials or whitepaper downloads |
| Voice | banned vocab present | mostly compliant | exemplar |
| Accuracy | ≥2 stale claims | 1 stale claim | all claims current |
| Strategic fit | off-pillar | adjacent to a pillar | core to a pillar |

## 5. Cadence + owner

- **Cadence:** quarterly, weeks 11–12 of each quarter.
- **Owner:** Content Lead drives; Brand approves voice verdicts; PMM approves competitive-page verdicts; [TBD-OPERATOR] approves any DECLINE on customer/claim grounds.
- **Output:** an updated audit log at `operations/content/audit-log/<YYYY-Q>.md` listing every URL, score, verdict, and action taken.

## 6. Audit log template (per quarter)

```
# Content audit — YYYY Qn
Run date:
Auditor:

| URL | T | Cv | V | A | Sf | Total | Verdict | Action | Done? |
|-----|---|----|---|---|----|-------|---------|--------|-------|
| /blog/... | 4 | 3 | 5 | 5 | 5 | 22 | KEEP | — | y |
| /blog/... | 2 | 1 | 3 | 2 | 3 | 11 | PRUNE | redirect → /blog/strongest | y |
```

## 7. Anti-patterns (kill on sight)

- Auditing only the worst performers (you also miss drift in your top performers).
- Refreshing without re-running voice-guideline compliance.
- Pruning without checking backlinks first (you can lose 50+ ref domains by 404'ing).
- Declining a piece without writing down *why* (the next person repeats the mistake).
- Auditing without an SLA on action — pieces flagged but not fixed are worse than not flagging.
