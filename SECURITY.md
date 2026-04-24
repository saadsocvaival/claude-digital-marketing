# Security

## Secret handling
- **Never commit raw secrets.** Use `secrets.pointer.md` per client (see `clients/_template/secrets.pointer.md`).
- **Vault-first.** Credentials live in 1Password / Doppler / cloud secret manager; the repo holds pointers + rotation cadence.
- **Pre-commit secret scan** is enforced via `.claude/settings.json` hook (`PreToolUse` on Write/Edit + `pre-commit` in Bash). Regex pattern blocks `ghp_`, `sk-…`, `xox[baprs]-`, `AKIA[0-9A-Z]{16}`, and common secret patterns.
- **Rotation cadence.** 90d for API keys, 180d for OAuth refresh tokens, immediate on incident. Track in `secrets.pointer.md`.

## Access
- **Least privilege** — each agent gets only the scopes it needs. Bindings live in `.claude/skills.manifest.json`.
- **Read-only defaults** for analytics pulls; write scopes granted explicitly per skill (e.g., Ads budget adjustments).

## Reporting
If you believe you have found a security issue:
1. **Do not open a public issue.**
2. Email the repository owner (see `.git/config` or repo settings) with subject line `SECURITY:`.
3. Include: steps to reproduce, affected artifact, suggested mitigation.

## Known historical exposure (disclosed)
During development of this repo, a GitHub Personal Access Token was pasted into a chat context twice by the operator. The token (redacted — full value preserved only in the operator's out-of-band notes) MUST be considered compromised.
**Required action by operator before merging this PR:**
1. Revoke the token on GitHub.
2. Issue a new token with minimum required scopes.
3. Audit `git log` and the CI history for any commits pushed with the revoked token.

## Audit trail
All state-changing agent actions append to `clients/{id}/ledger-events/*.jsonl`. This includes: HITL requests, budget reallocations, experiment decisions, stop-loss triggers, secret rotations.

## Compliance posture (for client work)
- SOC2 applicability: depends on client scope; not applicable to the framework itself.
- GDPR / CCPA: marketing data flows must respect client-side consent — honored via `ledger.md` constraints.
- Regulated industries (health, financial): Legal sign-off required on all outbound claims (enforced by `Head of Brand` + campaign launch gate).
