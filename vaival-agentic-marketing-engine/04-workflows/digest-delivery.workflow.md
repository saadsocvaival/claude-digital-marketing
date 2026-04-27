---
name: digest-delivery.workflow
owner_tier: orchestrator
owner_vertical: cross-vertical
primary_agent: cmo-orchestrator
playbook_source: §6, §14.3 B
skills: [orchestration/weekly-tick, performance-reporter, slack-bot]
status: active
phase: 2
---

# Digest Delivery Workflow

Assembles the weekly digest and delivers it via Slack + email.

## Trigger
- Output signal from `kpi-snapshot-pipeline.workflow.md` (Mon ~09:30 client-local).
- On-demand: operator command.

## Actors
- **Owner**: CMO Orchestrator.
- **Channels**: Slack webhook + email via SendGrid (or Resend / Mailgun per `secrets.pointer.md`).

## Inputs
- `clients/{id}/feeds/weekly-kpi-snapshot.md` (rubric ≥8 required).
- Active OKRs (`clients/{id}/okrs/`).
- Open HITL items (`11-approvals/`).
- Last 7 days of `ledger-events/`.
- `clients/{id}/ledger.md` cadence config (digest channel, recipients, day/time).

## Steps
1. **Assemble**: render the CMO digest format (Executive Summary → Client Context → North-Star Status → Vertical Assignments → Autonomous Progress → HITL Requests → Risks).
2. **Self-grade**: `rubrics/weekly-digest.yaml` ≥8. <8 → iterate before delivery.
3. **Slack publish**: POST to client-configured Slack webhook (`06-connectors/ops-collaboration/slack.connector.md`). Use blocks formatting.
4. **Email send**: deliver via configured ESP (SendGrid primary; Resend/Mailgun fallback). Recipients pulled from `ledger.md` §7. Spam-score ≥9/10 gate.
5. **Persist**: append `digest.delivered` to `ledger-events/` with delivery receipts (Slack message_ts, email message_id).
6. **Reaction window**: track Slack reactions / email opens for 24h to feed learning loop.

## Outputs
- Slack message in client's #marketing channel.
- Email to recipients listed in ledger §7.
- Ledger event with receipts.

## Rubric
`rubrics/weekly-digest.yaml` (pass bar 8). Email separately graded against `rubrics/email.yaml`.

## HITL Gates
- Digest contains an unresolved Level 3 risk → require operator ack before publish.
- Recipient list change since last digest → HITL.
- Delivery channel unavailable for >2h → escalate.

## Failure Modes
- Snapshot rubric <8 → workflow refuses publish, raises HITL with gap list.
- Slack webhook revoked → fallback to email-only + HITL.
- ESP suspension (deliverability) → fallback channel; HITL Head of Automation.

## Ledger Events Emitted
`digest.assembled` · `digest.rubric.{score}` · `digest.slack.delivered` · `digest.email.delivered` · `digest.delivery.failed.{channel}` · `digest.engagement.recorded`.
