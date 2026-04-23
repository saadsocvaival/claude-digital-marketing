# Conventions

Naming, frontmatter, and documentation style for the repository. These rules are normative during Phase 1 and carry into later phases.

## File Naming

- **All filenames are kebab-case.** No spaces, no camelCase, no uppercase letters (except the five root documents: `README.md`, `ARCHITECTURE.md`, `CONVENTIONS.md`, `OWNERSHIP.md`, `GLOSSARY.md`).
- **Type suffixes** identify the file's role:

| Suffix            | Purpose                                     | Example                                |
|-------------------|---------------------------------------------|----------------------------------------|
| `.agent.md`       | Agent specification                         | `seo-manager.agent.md`                 |
| `.connector.md`   | External platform integration spec          | `google-ads.connector.md`              |
| `.workflow.md`    | End-to-end workflow spec                    | `campaign-launch.workflow.md`          |
| `.gate.md`        | Approval gate spec                          | `budget-threshold.gate.md`             |
| `.schema.json`    | Output schema (added Phase 5)               | `campaign-plan.schema.json`            |
| `.prompt.md`      | Prompt template (added Phase 2+)            | `seo-manager.audit.prompt.md`          |

- Prompts use the double-segment form `<agent>.<task>.prompt.md`.

## Folder Numbering

Top-level folders use a `NN-name` prefix (`00-governance` … `18-docs`, `99-archive`). Numbering provides a reading order and groups related concerns. Do not renumber folders once published — add `99-archive/` entries instead.

## Frontmatter Schema (All `.md` Files Except Root Docs)

Every stub and spec file begins with YAML frontmatter:

```yaml
---
name: <kebab-filename-without-ext>
owner_tier: <tier-1|tier-2|tier-3|tier-4|tier-5|cross-cutting|governance|infra>
status: <stub|draft|approved|deprecated>
phase: <1-10>
---
```

Tier semantics (see `ARCHITECTURE.md` for the full hierarchy):
- **tier-1** — Founder / CEO
- **tier-2** — CMO, Head of Digital Marketing
- **tier-3** — Vertical Manager (one per vertical)
- **tier-4** — Specialist / Senior Specialist
- **tier-5** — Coordinator / Executive / Junior IC

**Per-type extensions** (added as files mature):

- **`.agent.md`** adds: `vertical`, `reports_to`, `playbook_source`, `tools`, `authority_scope`, `can_delegate_to`, `escalates_to`, `requires_approval_for`, `refuses_when`, `audit_fields`.
- **`.connector.md`** adds: `tool_display_name`, `category`, `owner_vertical`, `used_by_roles`, `purpose`, `auth_method`, `read_scopes`, `write_scopes`, `rate_limit`, `idempotency`.
- **`.workflow.md`** adds: `trigger`, `inputs`, `outputs`, `participating_agents`, `gates`, `sla`.
- **`.gate.md`** adds: `gate_type`, `required_approvers`, `threshold`, `sla_hours`.

## Documentation Style (Phase 1)

- **No executable code.** No Python, YAML runtime configs, JSON schemas with real values, or shell scripts. Phase 1 is architecture + vocabulary only.
- **Tables over prose** for matrices (authority, approvals, ownership, signal-to-agent maps). Tables are scannable; prose hides ambiguity.
- **ASCII diagrams** are preferred over image files in Phase 1 to keep the repo text-diffable.
- **Short paragraphs** (3–5 sentences). Long, nested bullets are a smell — promote to a table or a sub-heading.
- **Link by relative path** between docs (`03-orchestration/orchestrator-spec.md`), never by absolute path or URL.
- **Define terms once.** All shared vocabulary lives in `GLOSSARY.md`. Other docs reference it, they don't redefine.

## Deterministic-Output Discipline

Even in Phase 1 prose, be precise about decision boundaries. Avoid "the agent should consider…" — prefer "the agent MUST refuse when…" or "the agent MUST escalate when…". Ambiguity in the spec becomes non-determinism in the implementation.

## Archival

Deprecated specs move to `99-archive/<original-path>` with a frontmatter `status: deprecated` and a `superseded_by` pointer. Never delete — the ledger references historical specs by path.
