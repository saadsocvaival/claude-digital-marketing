# How to run the eval harness

## Today (manual)
1. Open Claude Code in repo root.
2. Pick a case file from `evals/`.
3. Paste the input prompt; let the skill run.
4. Ask the `quality-assurance` subagent (see `.claude/agents/` or Agent tool) to grade the output against the specified rubric.
5. If score ≥8 on weighted total AND each weight-≥9 criterion: PASS. Else: iterate or fail.

## Acceptance bar
- All 10 cases must score ≥8 on 3 independent runs before merging changes to the corresponding skill.
- Any regression below 8 on a previously-passing case blocks the PR.
- New skill → new eval case required.

## Planned (Stage 2.5)
- Scripted runner that invokes each skill with fixture input, captures output, delegates grading to quality-assurance subagent, asserts ≥8.
- Output: machine-readable JSON summary committed to `evals/runs/{date}.json`.
- CI integration (GitHub Actions) once Claude-Code runtime is dockerized and API access is wired.
