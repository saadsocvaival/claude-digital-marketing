# Eval — 02-positioning

## Input fixture
`clients/_fixture_devtools_saas/ledger.md` (and related artifacts — read as needed per skill).

Specific prompt to the skill:
> Using the fixture client context, produce the 02-positioning artifact following its template. Self-score using the matching rubric.

## Expected output shape
File written at the expected path (per skill's output schema), ending with a `## Rubric Evaluation` block.

## Rubric gate
Score ≥8 on the matching rubric in `/rubrics/`. Specific criteria with weight ≥9 must each individually score ≥8.

## Pass criteria
1. Output file exists at expected path.
2. Rubric-evaluation block present and complete.
3. Weighted total ≥8.
4. No banned words from `brand-voice.md`.
5. No raw secrets anywhere in output.

## Failure modes to guard against
- Generic content (not referencing fixture specifics).
- Missing sections required by the template.
- Weighted total rounded up to hide failure on heavy-weight criteria.
- Copy-paste between variants (for ad-copy / email sequence).
