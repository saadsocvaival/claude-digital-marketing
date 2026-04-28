---
client_id: costsage
sprint: 2
gap: G2
artifact: wikidata-q-item-payload
date: 2026-04-27
priority: P0
audience: operator
---

# G2 — Wikidata Q-item submission payload

> **Why this is P0:** Wikidata is the single highest-leverage entity-grounding source for LLMs (ChatGPT, Claude, Gemini, Perplexity all retrieve from it). A clean Q-item gives CostSage a canonical entity LLMs can cite with confidence. Cost: free. Time to submit: ~10 min.

## Submission steps (operator)

1. Sign in at https://www.wikidata.org/ (any account; create one if needed — confirm email).
2. Click **Special:NewItem** → https://www.wikidata.org/wiki/Special:NewItem
3. **Label (English):** `CostSage`
4. **Description (English):** `AI FinOps platform for cloud cost optimisation` (≤250 chars; keep concise — Wikidata enforces uniqueness vs sibling entities, so this disambiguates from "Sage" / "Sage Group plc" / "Sage Intacct")
5. **Aliases (English):** `CostSage AI`, `costsage.ai`
6. Save → you'll get a Q-number like `Q123456789`. Record it.
7. Add the **statements** below (use "Add statement" on the item page).

## Statements (Wikidata properties)

| Property | ID | Value | Notes |
|---|---|---|---|
| instance of | P31 | `business` (Q4830453) | or `software company` (Q1058914) — pick the better fit |
| instance of | P31 | `software` (Q7397) | second instance-of for the platform itself |
| industry | P452 | `cloud computing` (Q483639) | |
| industry | P452 | `financial technology` (Q5167028) | |
| official website | P856 | `https://costsage.ai/` | |
| inception | P571 | `TBD-CONFIRM-WITH-OPERATOR` | founding date — must be exact YYYY-MM-DD |
| country | P17 | `TBD-CONFIRM-WITH-OPERATOR` | HQ country (if Vaival Technologies parent: confirm Pakistan or UAE) |
| headquarters location | P159 | `TBD` | city Q-item |
| founded by | P112 | `TBD-CONFIRM-WITH-OPERATOR` | founder names — Q-items if they exist, or just plain text |
| parent organization | P749 | `Vaival Technologies` (search Wikidata for Q-item; create one if missing — see G3a below) | |
| social media followers | P8687 | (skip until ≥1000 followers somewhere) | |
| LinkedIn ID | P4264 | `costsage` | URL fragment from `linkedin.com/company/costsage` |
| Crunchbase organization ID | P2087 | `TBD-AFTER-CRUNCHBASE-CREATED` (see G3) | |
| G2 product ID | (no formal property; use "described at URL" P973) | `https://www.g2.com/products/costsage` | |
| AWS Marketplace ID | (use P973) | `https://aws.amazon.com/marketplace/pp/prodview-l7gymco6bhnxg` | confirm slug |
| logo image | P154 | (skip until logo uploaded to Wikimedia Commons under appropriate license) | |

## Sitelinks (low priority)
Add the costsage.ai homepage as a sitelink to the English Wikipedia entry IF a Wikipedia article exists. (None today — Wikipedia is gated behind notability and likely Sprint-3+.)

## Reciprocity hook (after Q-item is live)
Once the Q-number is known, update the homepage Organization JSON-LD `sameAs[]` array to include the Wikidata URL:
```
"sameAs": [
  ...,
  "https://www.wikidata.org/wiki/Q<NUMBER>"
]
```
Also re-deploy via the bind-mount overlay (no source-repo PR needed).

## Operator-confirmation TBDs

Need confirmed before submitting:
- [ ] Founding date (YYYY-MM-DD)
- [ ] HQ country + city
- [ ] Founder names (and whether to list them publicly)
- [ ] Parent-company line: "Vaival Technologies" — confirm legal entity name + jurisdiction
- [ ] Logo: where can we host the logo file under a free license (CC-BY-SA 4.0 or similar) so we can upload to Wikimedia Commons?

## Verification (after submission)
1. WebSearch `"CostSage" wikidata` — Q-item should surface within 24h.
2. Within 7d: search Google for `CostSage` and look for a Knowledge Panel or rich-org card. Wikidata is the upstream feeder for that panel.
3. Within 30d: re-run Track-3 LLM citation baseline; compare brand-prompt and category-prompt mention rates.
