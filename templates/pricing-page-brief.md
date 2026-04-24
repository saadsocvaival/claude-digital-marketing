# Pricing Page Brief — {Client}

## 1. Decision the page must drive
- **Primary action:** start-trial | book-demo | self-serve-purchase
- **Secondary action:** talk-to-sales (Enterprise tier only)
- **Disqualifying action:** filter out non-ICP so they don't waste sales time

## 2. Tier architecture
| Tier | Target segment | Anchor value | Price point | Packaging axis |
|---|---|---|---|---|
| {Free/Starter} | ... | ... | ... | seats / events / MAU |
| {Pro} | ... | ... | ... | ... |
| {Business} | ... | ... | ... | ... |
| {Enterprise} | ... | "Contact us" | — | custom |

**Packaging rule:** one dominant axis; secondary axis (if any) affects add-ons only. Avoid 3-axis grids — conversion drops ~40%.

## 3. Anchoring & decoys
- **Anchor:** most-prominent tier (usually middle) — visually differentiated.
- **Decoy tier** (optional): inferior on price/value to steer to anchor.
- **Annual toggle:** default on, showing savings; monthly available but un-anchored.

## 4. Above-the-fold must-haves
- Headline — one-sentence value, not "Pricing."
- Segment selector (SMB / Mid-Market / Enterprise) if tiers differ by segment.
- Tier cards with: price, 3-bullet value, CTA, "most popular" label on anchor.

## 5. Below-the-fold
- Feature comparison matrix (sortable, collapsible by category).
- Social proof: logos at the tier they buy at.
- FAQ — top 8 objections drawn from sales call transcripts.
- ROI calculator if ACV >$10k.
- Security/compliance badges (SOC2, ISO, GDPR).

## 6. Copy rules
- Prices in customer's currency (geo-detect).
- Benefits phrased as outcomes, not features ("ship 10× faster" not "CI/CD integration").
- No "Contact for pricing" on anything below Enterprise — it kills mid-market conversion.

## 7. Instrumentation
- Events: `pricing_view`, `tier_hover`, `annual_toggle`, `cta_click` (per tier), `faq_open`, `comparison_scroll_depth`.
- Heatmap + session replay on first 30 days post-launch.
- A/B framework wired in (see `experiment-program.skill.md`).

## 8. Testing queue
1. Headline (outcome vs. category language)
2. Anchor tier position (middle vs. left)
3. Feature-matrix default state (collapsed vs. expanded)
4. ROI calculator presence
5. Testimonial placement (per-tier vs. global)

## 9. Kill criteria
- Overall conversion <0.5× industry median after 8 weeks → full rebuild brief.
- Self-serve:sales-touch ratio drifting wrong way for 2 months → packaging review.
