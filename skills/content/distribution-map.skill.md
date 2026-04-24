---
name: distribution-map
description: Produces a per-asset distribution plan so content doesn't publish-and-pray. Forces a named channel mix, dark-social tracking plan, amplification math, and sales-enablement routing before any asset is greenlit.
invoked_by: head-of-content, motion-acquisition
frameworks:
  - Dark-social attribution (SparkToro / Chris Walker)
  - 1:N content atomization (Gary Vee pyramid)
  - POEM (Paid/Owned/Earned/Mixed) channel model
---

## Why a separate skill

Most content calendars stop at "publish date." Distribution is assumed. In reality, 80% of B2B buying journey happens in dark social (Slack DMs, podcasts, LinkedIn posts, peer forums) where no URL click can be tracked. If you can't name *which humans in which channels will see this*, the asset is a wish, not a campaign.

## Inputs

```json
{
  "asset": { "title": "string", "type": "blog|podcast|video|webinar|whitepaper|tool|case_study", "target_icp": "string", "funnel_stage": "tofu|mofu|bofu" },
  "distribution_budget": "int (USD, 0 for organic-only)",
  "internal_amplifiers": [ { "name": "string", "audience_size": "int", "channel": "string" } ],
  "owned_channels": ["newsletter", "community", "customer_base"],
  "intent_signals_to_capture": ["form_fill", "dark_social_mention", "branded_search_lift"]
}
```

## Outputs

```json
{
  "channel_mix": [
    { "channel": "string", "format": "string", "owner": "string", "t_plus_days": "int", "expected_reach": "int", "cost": "int" }
  ],
  "atomization_plan": [
    { "derivative": "e.g. LinkedIn carousel", "source_timestamp_or_section": "string", "publish_by": "date" }
  ],
  "dark_social_instrumentation": {
    "self_reported_attribution_question": "string (form field)",
    "branded_search_baseline": "int (weekly impressions)",
    "podcast_mention_tracking": "manual log | Podscan | Listen Notes",
    "community_mention_tracking": "common-room | manual | N/A"
  },
  "sales_enablement_routing": {
    "snippet_for_sdrs": "string (≤80 words)",
    "one_line_for_ae_followup": "string",
    "relevant_icp_segments": ["string"]
  },
  "success_criteria": {
    "leading": ["impressions", "engaged-views", "saves/shares", "SDR-reuse count"],
    "lagging": ["branded search lift", "self-reported attribution %", "pipeline-influenced $"]
  }
}
```

## Protocol

1. **Classify the asset.** ToFu/MoFu/BoFu + format → determines default channel mix.
2. **Pick 3–5 channels** across POEM. One must be dark-social-native (LinkedIn post, podcast, community AMA). One must be owned (newsletter/customer base). Reject mixes that are all paid or all organic.
3. **Atomize (1:N).** Every hero asset spawns ≥5 derivatives: LinkedIn post, Twitter/X thread, newsletter section, SDR snippet, sales-deck slide. Each has its own owner and publish date.
4. **Instrument dark social.** Add self-reported-attribution field to forms ("How did you hear about us?"). Baseline branded search. Log podcast/community mentions weekly.
5. **Route to sales.** Give SDRs an 80-word snippet and AEs a one-liner for followup. If sales can't use it in a conversation within 7 days, the content is probably too generic.
6. **Define success.** Leading indicators must be measurable within 14 days (engaged views, saves, SDR reuse). Lagging indicators within 90 days (branded search, self-reported attribution, influenced pipeline).

## Anti-patterns

- **Publish-and-pray.** No named channel mix = don't ship.
- **Pageview theatre.** Measuring raw traffic without engagement or downstream pipeline.
- **Forgetting internal amplifiers.** Employees' LinkedIn audiences often dwarf the company account.
- **Attribution nihilism.** "Dark social is unmeasurable" → so we give up. Self-reported attribution + branded search lift are both real, cheap, and directional.

## Rubric gate

`rubrics/skill.yaml` with criteria: channel-mix diversity (0–10), atomization completeness (0–10), dark-social instrumentation (0–10), sales-enablement clarity (0–10). Pass bar 8.

## Output file

`clients/{id}/content/distribution/{asset-slug}.md`
