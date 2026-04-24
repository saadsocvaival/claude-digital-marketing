---
name: hitl-request
description: Produces structured Human-in-the-Loop requests. Every HITL follows this schema — no unstructured questions. Use whenever a decision exceeds the Orchestrator or a Head's authority, a credential is needed, or policy requires human sign-off.
invoked_by: any agent
inputs:
  - reason: string (what requires the human)
  - policy_ref: string (Playbook section or gate file)
  - options: array (A/B/C with tradeoffs)
  - recommendation: string
  - deadline: date
  - blocking: boolean
outputs:
  - clients/{id}/hitl-queue.md  (append)
  - referenced inline in operator digest
rubric: rubrics/hitl-request.yaml
---

# HITL Request Skill

## Purpose
Remove friction from human approvals by structuring every request identically. An operator glancing at any HITL item can decide in < 60 seconds.

## Schema (every HITL uses this exact structure)

```markdown
### HITL {N} — {Short title}
- **Category**: Budget-threshold | Strategy-change | New-credential | Legal/Compliance | Brand | External-publish | Other
- **Why required**: {1–2 sentences}
- **Policy reference**: {file path or Playbook section, e.g., `11-approvals/gates/budget-threshold.gate.md`}
- **Context (≤ 4 bullets)**:
  - ...
- **Options**:
  - **A — {name}**: {1 line}. Pros: {x, y}. Cons: {z}.
  - **B — {name}**: {1 line}. Pros: {x, y}. Cons: {z}.
  - **C — {name}** *(optional)*: ...
- **Recommendation**: Option **{letter}** because {1 sentence rationale + expected outcome + how we'd measure success}.
- **Blocking?**: Yes — work on {vertical/initiative} pauses until decision. / No — other work proceeds.
- **Deadline**: {date}. Impact of miss: {what degrades after this date}.
- **On approval, we will**: {1 sentence — specific next action}.
- **Ledger id**: {client-id}-hitl-{N} (append-only).
```

## Invocation rules

1. **Never mix multiple asks in one HITL.** One decision per item.
2. **Always recommend.** "We don't know" is not a recommendation; do more analysis first.
3. **Always provide ≥ 2 options.** If only one exists, the ask is "notification," not HITL.
4. **Always cite policy.** If no policy applies, this probably should not be HITL (the agent should decide).
5. **Always state blocking vs non-blocking.** Operator prioritizes by this.
6. **Always state the deadline and the cost of missing it.**
7. **Never escalate things under the Head's authority.** Re-read the agent's decision matrix before producing HITL.

## Queue discipline

- Max 5 HITL items in the weekly digest. If >5 are pending, prioritize by (blocking × urgency) and show top 5 + a line: "{N} more items in `hitl-queue.md`."
- Append every HITL to `clients/{id}/hitl-queue.md` (ledger). Never delete — mark resolved.
- On resolution, log the operator's decision verbatim + the action the system took.

## Operator response expected format

```
HITL {N}: A  (or "B — with this tweak: ...")
```

## Anti-patterns

- "Can you review this?" — vague. Ask a specific question with options.
- HITL that includes 10 paragraphs of context. If the operator needs 10 paragraphs, write a memo first and summarize the decision.
- HITL about something the system should just do (within autonomy bounds). Don't outsource your judgment.
- Dumping every small risk into HITL. Risks go in the digest's "Risks & Governance Notes" section; only decision-points go into HITL.

## Self-rubric

- Single decision, not compound: 10/10 target.
- All schema fields present: 10/10.
- ≥ 2 options with honest tradeoffs: 10/10.
- Policy citation resolves to a real file: 10/10.
- Recommendation has rationale + measurement: 10/10.

Below any criterion → rewrite.
