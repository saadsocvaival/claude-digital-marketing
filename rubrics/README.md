# Rubric Library

Every artifact produced by the system self-evaluates against a rubric before shipping. Artifacts scoring **< 8/10** on any rubric must be iterated or cut; they do not pass the gate.

## Rubric file format

```yaml
name: <artifact type>
criteria:
  - id: <short id>
    weight: <1-10>
    description: <what "good" looks like>
    anti_patterns:
      - <specific thing that fails>
pass_bar: 8
version: 1.0.0
```

## Scoring method

Each criterion is scored 1–10. Weighted average is the artifact score. Any criterion scored ≤ 5 blocks shipment regardless of overall score (a single broken principle is worse than a mediocre average).

## Rubrics in this library

- `agent.yaml` — agent-file quality
- `skill.yaml` — skill-file quality
- `client-ledger.yaml` — onboarding output
- `icp.yaml` — ideal customer profile
- `positioning.yaml` — positioning statement
- `brand-voice.yaml` — brand voice guide
- `messaging.yaml` — messaging framework
- `90-day-plan.yaml` — execution plan
- `weekly-kpi-snapshot.yaml` — Analytics feed
- `weekly-digest.yaml` — operator digest
- `campaign-brief.yaml` — paid campaign brief
- `ad-copy.yaml` — ad creative
- `email-sequence.yaml` — lifecycle sequence
- `email.yaml` — single email
- `seo-brief.yaml` — SEO content brief
- `landing-page.yaml` — landing page brief + asset
- `battlecard.yaml` — competitive battlecard
- `lead-scoring.yaml` — scoring model
- `hitl-request.yaml` — HITL item quality
