---
name: secrets-vault-setup.workflow
owner_tier: department-head
owner_vertical: analytics-ops
primary_agent: head-of-analytics
playbook_source: §5.5 (Tooling Policy), §14.3 C, SECURITY.md
skills: [hitl-request]
status: active
phase: 2
---

# Secrets Vault Setup Workflow

One-time per-client migration of cleartext credentials (e.g. operator-supplied sheet) into a secrets vault. Produces `secrets.pointer.md` with vault paths only and revokes the unsafe source.

## Trigger
- Client onboarding bootstrap (called by `client-onboarding.workflow.md`).
- Re-run on credential rotation, vault migration, or after a credential-leak incident.

## Actors
- **Owner**: Head of Analytics (or Head of Automation).
- **HITL**: human operator (must perform the actual cleartext deletion).
- **Tooling**: 1Password CLI OR Doppler OR HashiCorp Vault — operator chooses one per client.

## Inputs
- Operator-supplied source (e.g. spreadsheet) listing every platform + credential.
- List of platforms from playbook §5.5 + per-client tools: GA4, GSC, GTM, Semrush, Ahrefs, Screaming Frog, Surfer, ATP, Trello, ChatGPT, Claude, Gemini, Perplexity, Copilot, WordPress, plus ad/CRM/email platforms as applicable.
- Vault tool choice + workspace identifier.

## Steps
1. **Inventory**: enumerate every secret with `(service, account, auth_method, scope, expiry, owner, current_location)`. Owner uploads inventory to a private secure channel — never to the repo.
2. **Vault path scheme**: assign per-client path `vault://{client}/{platform}/{secret-name}`. Use auth_method tags: `oauth`, `api-key`, `app-password`, `service-account`, `sso`.
3. **Provision**: operator stores each secret in vault under the assigned path. Set rotation reminders per `secrets.pointer.md` cadence.
4. **Pointer file**: write `clients/{id}/secrets.pointer.md` with vault path + auth_method per platform; NO secret values; NO inferred passwords.
5. **Verify**: per platform, agent attempts a least-privilege read using the vault-resolved credential. Failure → HITL.
6. **Revoke unsafe source**: operator deletes/sanitizes the original spreadsheet/cleartext source. Confirm with checksum or attestation.
7. **Mark complete**: ledger event `secrets.vault.migrated`. Set `clients/{id}/ledger.md` flag `secrets_in_vault: true`. Onboarding can flip status to `active` only after this event lands.

## Outputs
- `clients/{id}/secrets.pointer.md` (vault paths only, no creds).
- Ledger events documenting migration + revocation attestations.
- Rotation reminders configured in vault for each secret.

## Rubric
Pointer file gated against the secrets-pointer convention in `clients/_template/secrets.pointer.md` (no raw secrets ever). Ledger entry rubric-graded against `rubrics/client-ledger.yaml`.

## HITL Gates
- Any cleartext credential cannot be migrated (legacy SSO-only) → HITL with documented exception + compensating controls.
- Original source cannot be revoked (shared spreadsheet inheritance) → HITL with mitigation plan.
- Vault tool changes mid-flight → HITL.

## Failure Modes
- Verify step fails → keep status `pending-onboarding`; raise HITL with platform list.
- Credential rotation overdue at migration time → rotate first, then store.
- Multi-tenant leak risk (shared password across clients) → refuse migration; require per-client credential first.

## Ledger Events Emitted
`secrets.inventory.received` · `secrets.vault.path.assigned` · `secrets.vault.stored.{platform}` · `secrets.verify.{platform}.{ok|fail}` · `secrets.cleartext.revoked` · `secrets.vault.migrated` · `secrets.rotation.scheduled.{platform}`.
