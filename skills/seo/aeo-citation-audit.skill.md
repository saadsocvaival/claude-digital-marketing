---
name: aeo-citation-audit
description: Audits brand presence in LLM/AI-assistant answers (ChatGPT, Claude, Gemini, Perplexity, Google AI Overviews). Produces a citation-share report per target query class and a remediation queue.
invoked_by: head-of-seo-geo-aeo
frameworks:
  - Answer Engine Optimization (AEO) — Rand Fishkin / SparkToro frameworks
  - Generative Engine Optimization (GEO) — Princeton/Georgia Tech 2024 paper
  - Brand-as-entity graph (Google Knowledge Graph + LLM grounding)
---

## Inputs

```json
{
  "client_id": "string",
  "query_set": ["array of target queries — informational, commercial, branded"],
  "engines": ["chatgpt", "claude", "gemini", "perplexity", "google_ai_overview"],
  "competitor_list": ["string"],
  "lookback_days": 30
}
```

## Outputs

```json
{
  "citation_share": { "per_engine": { "brand": "number", "competitor_X": "number" } },
  "answer_presence": { "per_query": { "brand_cited": "bool", "brand_recommended": "bool", "position": "int" } },
  "citation_types": { "direct_quote": "int", "source_link": "int", "paraphrased": "int", "none": "int" },
  "remediation_queue": [ { "query": "string", "gap": "string", "proposed_action": "string", "owner_head": "string" } ]
}
```

## Protocol

1. **Build query set.** Cover 4 classes:
   - Informational ("what is feature flagging")
   - Commercial-investigation ("best feature flag platform for enterprise")
   - Comparison ("LaunchDarkly vs Loopgate")
   - Branded ("is Loopgate SOC2 compliant")
2. **Run queries against each engine.** Log response verbatim + source links. Run 3 times per query (LLM outputs vary) — take the union of citations.
3. **Classify citations.**
   - **Direct quote** — brand text appears verbatim.
   - **Source link** — brand URL in the source list.
   - **Paraphrase** — brand claim appears but unattributed.
   - **None** — absent.
4. **Compute citation-share.** `brand_citations ÷ total_citations_across_all_brands` per engine.
5. **Identify structural gaps.** For queries where competitors cite but we don't:
   - Is our content indexed? (search site:domain.com + query fragment)
   - Does our content have an answer block? (schema markup, TL;DR at top, structured Q&A)
   - Is our entity canonical? (Wikipedia page, Wikidata, LinkedIn company page matching domain)
6. **Remediation queue.** Each gap → action → owner Head → target date.

## Failure modes

- **Single-run sampling.** LLM outputs vary; one query = one sample. Always n≥3.
- **Treating Google AI Overview as stable.** It's not; rerun quarterly.
- **Over-indexing on citation count.** Citation *quality* (direct quote in answer > link in sources) matters more.
- **Ignoring entity hygiene.** If brand isn't in Wikidata, LLMs won't ground on it. This is the #1 structural lever.

## Metric: Brand-Mention-in-LLM (BMI-LLM)

```
BMI-LLM = (direct_quotes × 3 + source_links × 2 + paraphrases × 1) / total_queries_in_set
```

Target BMI-LLM by query class; track weekly.

## Rubric gate
`rubrics/skill.yaml` + `rubrics/seo-brief.yaml` (for remediation-brief outputs).

## Output file
`clients/{id}/feeds/aeo-citation-{yyyy-mm-dd}.md` + `clients/{id}/experiments/aeo-remediation-queue.md`
