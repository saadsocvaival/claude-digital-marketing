---
name: answer-engine-brief
description: Produces a content brief optimized for answer engines (ChatGPT/Claude/Gemini/Perplexity/Google AI Overview) — not just SEO. Specifies structure, schema markup, canonical answer blocks, entity grounding, and factual density requirements that LLMs preferentially cite.
invoked_by: head-of-content, head-of-seo-geo-aeo
frameworks:
  - GEO (Generative Engine Optimization) — Aggarwal et al. 2024
  - Schema.org structured data
  - EEAT (Experience, Expertise, Authority, Trust)
---

## Why a separate skill (vs classic SEO brief)

Classic SEO optimizes for clicks from blue links. Answer engines consume content and *answer without sending clicks*. The winning structure is different:

| Blue-link SEO | Answer-engine SEO |
|---|---|
| Long-form, narrative | Answer-first, TL;DR up top |
| Keyword density | Entity density + factual density |
| Meta description for click-through | Canonical-answer block for citation |
| Backlinks | Being in Wikidata + authoritative mentions |
| Featured-snippet optimization | Direct-citation optimization |

## Inputs

```json
{
  "target_query": "string",
  "query_intent": "informational | commercial-investigation | comparison | branded",
  "target_engines": ["chatgpt", "claude", "gemini", "perplexity", "google_aio"],
  "competing_citations": ["urls currently cited for this query"],
  "primary_entity": "string (our brand or product)",
  "word_count_target": "int (usually 1200-2000 for answer-engine content)"
}
```

## Outputs

```json
{
  "content_structure": {
    "canonical_answer_block": "string (50-80 words, self-contained, will-be-cited)",
    "tldr_bullets": ["3-5 bullets directly answering the query"],
    "h2_sections": [{ "heading": "string", "answer_paragraph": "string", "evidence": "string" }],
    "faq_schema": [{ "q": "string", "a": "string" }]
  },
  "schema_markup": {
    "types": ["Article", "FAQPage", "HowTo", "Product", "Organization"],
    "json_ld_template": "string"
  },
  "entity_grounding": {
    "primary_entity": "string",
    "wikidata_id": "string if exists",
    "authoritative_mentions_to_secure": ["Wikipedia", "G2", "Gartner Peer Insights", "Wikidata"]
  },
  "factual_density_targets": {
    "citations_per_1000_words": ">=8",
    "named_entities_per_1000_words": ">=15",
    "date_stamps": "required (LLMs trust date-stamped claims more)"
  },
  "anti_patterns": ["vague adjectives", "unsourced superlatives", "keyword-stuffed intros", "thin FAQ blocks"]
}
```

## Protocol

1. **Reverse-engineer competing citations.** For each URL currently cited by target engines, extract: canonical answer paragraph, schema types, entity grounding, factual density.
2. **Design canonical answer block.** 50–80 words, self-contained (readable without surrounding context), answers the query directly, contains primary entity + 2–3 named secondary entities.
3. **Build TL;DR bullets.** 3–5 items, each a standalone answer fragment citable alone.
4. **Structure H2 sections.** Each H2 = one sub-question. Each sub-section starts with a 2–3 sentence answer paragraph, then evidence.
5. **Specify schema markup.** Minimum: `Article` + `FAQPage`. Add `HowTo` for procedural, `Product` for product pages, `Organization` in site-wide schema.
6. **Entity grounding checklist.**
   - Is brand in Wikidata? If not, queue Wikidata submission.
   - Does Wikipedia mention brand? If not, queue notable-source mentions first.
   - Are G2/Gartner Peer Insights pages canonical and up to date?
7. **Factual density targets.** Citations ≥8 per 1000 words, named entities ≥15 per 1000 words, date stamps on all claims.
8. **Anti-pattern check.** Remove weasel words, unsourced superlatives, keyword-stuffed openers.

## Failure modes

- **Writing for humans, not for retrieval.** An answer block that reads like marketing copy won't be cited. It needs to read like an encyclopedia entry.
- **Over-rotating on one engine.** Optimize for 3+ engines; each weights signals differently.
- **Forgetting entity hygiene.** Best content in the world won't be cited if the LLM doesn't know your brand is a real entity.
- **Writing when you're not expert-adjacent.** EEAT matters. If your content isn't rooted in first-party experience, it gets demoted.

## Rubric gate
`rubrics/seo-brief.yaml` with AEO-criterion additions: canonical-answer-block quality (0–10), entity-grounding completeness (0–10), factual-density compliance (0–10). Pass bar 8.

## Output file
`clients/{id}/seo-cluster/{query-slug}-aeo-brief.md`
