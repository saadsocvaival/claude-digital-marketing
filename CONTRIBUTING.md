# Contributing

## The non-negotiable rule
**No artifact merges below rubric pass bar 8/10.**

Every marketing artifact (ICP, positioning, campaign brief, ad, email, LP, SEO brief, etc.) must end with a `## Rubric Evaluation` section that:
1. References the correct rubric in `/rubrics/`.
2. Scores each criterion with a one-line justification.
3. Reports a weighted total ≥ pass_bar (typically 8).

PRs that introduce a new client artifact type without a matching rubric will be returned.

## Branching & commits
- Branch from `main`: `feat/<short-name>` or `fix/<short-name>`.
- Commit messages: imperative mood, <72-char subject, body explains *why*.
- Co-author Claude attributions welcome but not required.

## What this repo is for
A **client-agnostic, rubric-gated** operating system for an autonomous digital-marketing department. Contributions are welcome in these directions:
- New rubrics for artifact types not yet covered (see `AUDIT.md` for gaps).
- New templates that pass their rubric.
- New skills with `*.skill.md` format (inputs + output schema + failure modes + invocation example).
- Additional fixture clients (distinct archetypes) to expand dogfood coverage.
- Eval cases that increase coverage of the skill library.

## What this repo is NOT for
- Real-client content — clients live outside the repo or in a private fork.
- Raw secrets — enforced by pre-commit hook.
- Opinionated tool preferences without playbook grounding — cite the policy doc you're extending.

## Style
- Brand voice for meta-artifacts (README, docs): engineer-to-engineer, proof over promise.
- Numbers with units, no space (`47ms`, not `47 ms`).
- Oxford comma.
- No "revolutionary", "seamless", "cutting-edge", or "enterprise-grade" — even in docs.

## Review
- Rubric gate: automated-check or reviewer verification.
- Playbook alignment: reviewer confirms the change cites its policy source.
- Security: pre-commit hook must pass; SECURITY.md rules obeyed.
