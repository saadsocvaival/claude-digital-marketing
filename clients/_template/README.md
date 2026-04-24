# Client Tree — `{{client-id}}`

Directory contract (every client conforms):

```
{client-id}/
├── ledger.md                   # living source of truth
├── icp.md                      # from templates/icp.md
├── positioning.md
├── brand-voice.md
├── messaging.md
├── offer.md
├── secrets.pointer.md
├── okrs/                       # quarter-stamped OKRs, one file per quarter
├── feeds/                      # weekly-kpi-snapshot.md + others
├── experiments/                # one file per experiment (brief → readout → decision)
├── campaigns/                  # one file per campaign (brief + creative + stop-loss)
├── memory/
│   ├── short/                  # per-session working memory
│   ├── long/                   # durable facts (ICP verbatims, won-deal patterns)
│   └── shared/                 # cross-Head shared artifacts
└── ledger-events/              # append-only jsonl of state-changing events
```

## Rules
- Every artifact ends with a `## Rubric Evaluation` block (pass bar 8).
- No raw secrets anywhere — only `secrets.pointer.md`.
- Weekly tick updates `ledger.md §10 Change Log` + writes one `ledger-events/*.jsonl`.
- New client created by copying `_template/` and renaming; onboarding skill populates content.
