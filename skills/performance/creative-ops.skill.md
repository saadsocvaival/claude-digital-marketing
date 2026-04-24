---
name: creative-ops
description: Defines modular creative production — hook × angle × format matrix, creative-velocity KPI, AI-creative pipeline, fatigue thresholds, and a test-matrix template so paid performance doesn't plateau from creative-starvation.
invoked_by: head-of-performance, motion-acquisition
frameworks:
  - Motion Creative Analytics framework
  - Meta "Creative is the new targeting" thesis
  - Hook × Angle × Format decomposition
---

## Why creative ops

After iOS14 / Privacy Sandbox, audience targeting is commoditized. Creative now explains ~70% of paid-performance variance (Meta internal + Northbeam studies). Teams that ship 30+ creatives/month/channel outperform teams that ship 3. This skill exists to make creative a pipeline, not a quarterly shoot.

## Inputs

```json
{
  "channels": ["meta", "google", "linkedin", "tiktok", "youtube"],
  "monthly_paid_spend": "int",
  "icp_segments": ["string"],
  "brand_voice_path": "clients/{id}/brand-voice.md",
  "product_proof_library": "clients/{id}/assets/proof-library.md"
}
```

## Outputs

```json
{
  "creative_matrix": {
    "hooks": ["problem-agitation", "statistic-led", "customer-quote", "contrarian-POV", "visual-anomaly"],
    "angles": ["saves-time", "saves-money", "reduces-risk", "social-proof", "status", "speed-to-value"],
    "formats": ["static", "carousel", "UGC-video", "talking-head", "screencap", "meme", "comparison-table"]
  },
  "velocity_target": "N creatives/channel/month (by spend tier)",
  "test_matrix_template_path": "templates/creative-test-matrix.md",
  "fatigue_thresholds": { "frequency": "≤3.0 (Meta)", "CPA_drift": "+25% vs week-1 → rotate", "CTR_decay": "−30% vs peak → rotate" },
  "ai_creative_pipeline": {
    "ideation": "claude-opus brief → 20 concepts",
    "variant_generation": "midjourney/runway/elevenlabs",
    "QA": "brand-voice-check + legal review",
    "tagging_taxonomy": "hook/angle/format/emotion/proof-type"
  },
  "winner_promotion_rules": "1.5× blended CPA at statsig → promote to evergreen set"
}
```

## Protocol

1. **Build the matrix.** Enumerate hooks × angles × formats. Target 5×6×7 = 210 theoretical combinations; shortlist 20–30 per sprint.
2. **Set velocity target by spend tier.**
   - <$10k/mo: 6–10 new creatives/channel/month
   - $10–100k: 20–40
   - $100k+: 40–80
3. **Tag every asset** on upload: hook, angle, format, emotion, proof-type, ICP segment. Without tagging, post-hoc analysis is impossible.
4. **Rotate on fatigue.** Frequency >3, CPA drift +25%, or CTR decay −30% → pause, log learning, promote next variant.
5. **Run the test-matrix.** 3-cell rotation: explore (new concepts, 20% budget), exploit (proven winners, 70%), moonshot (high-variance bets, 10%).
6. **Monthly creative review.** Which hooks/angles/formats *at tag level* are winning? Double down on tag combinations, not individual assets.

## Anti-patterns

- **One-and-done hero campaign.** $50k shoot, 6 cut-downs, no iteration.
- **Variant-shuffling dressed as testing.** Changing button color ≠ new creative.
- **Untagged library.** 400 assets, zero retrievability, repeated mistakes.
- **Brand-guard paralysis.** If every creative needs CMO approval, velocity dies. Pre-approve tag combinations instead.

## Failure modes

- **AI-creative slop.** Volume without quality tanks account trust scores. Keep a human-in-loop QA step.
- **Chasing channel TikTok-isms cross-channel.** Format that wins on TikTok may kill brand on LinkedIn. Tag-level analysis must respect channel.
- **Ignoring proof-type.** Customer-quote ads often outperform feature ads 2–3×, but teams under-produce them because they require customer work.

## Rubric gate

`rubrics/skill.yaml` + creative-velocity realism (0–10), tagging taxonomy completeness (0–10), fatigue-policy defensibility (0–10). Pass bar 8.

## Output file

`clients/{id}/performance/creative-ops-{quarter}.md` + `clients/{id}/performance/creative-log.jsonl`
