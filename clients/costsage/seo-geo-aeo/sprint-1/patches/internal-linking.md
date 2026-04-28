# Internal-linking patches — F12

Goal: route authority to the pillar piece (`/finops-agent-vs-dashboard`) and
the new commercial-intent landing pages, while ensuring every page has at
least 3 contextually relevant internal outbound links.

## Link insertions

### 1. Home `/` — hero or "Built for teams that take cloud spend seriously" section
Insert a contextual link to the pillar:
```html
…built for teams that take cloud spend seriously. Read why
<a href="/finops-agent-vs-dashboard">an agent beats a dashboard</a>
for closing the loop on cloud waste.
```

### 2. Home `/` — features grid item descriptions
Each H3 (AI Rightsizing, RI/SP Optimisation, etc.) should link out to the
matching anchor on `/features` or to the relevant blog post once shipped.

### 3. `/features` — first body paragraph
```html
CostSage operates across <a href="/aws">AWS</a> and <a href="/azure">Azure</a>.
Every recommendation includes a reasoning trace — see
<a href="/finops-agent-vs-dashboard">why agentic FinOps beats dashboard FinOps</a>.
```

### 4. `/pricing` — final CTA block
```html
Still comparing? See how CostSage stacks up against
<a href="/nops-alternative">nOps</a> and
<a href="/cloudzero-alternative">CloudZero</a>.
```

### 5. `/nops-alternative` — body
Add reciprocal link to `/cloudzero-alternative`:
```html
Also evaluating CloudZero?
<a href="/cloudzero-alternative">See the CloudZero comparison</a>.
```

### 6. `/cloudzero-alternative` — body
Reciprocal link to `/nops-alternative`:
```html
Also evaluating nOps?
<a href="/nops-alternative">See the nOps comparison</a>.
```

### 7. `/azure` — "How CostSage Works" section
Add cross-link to AWS counterpart (once `/aws` ships):
```html
Running AWS too? See <a href="/aws">CostSage on AWS</a>.
```

### 8. `/aws` (new) — already includes link to `/azure` and `/finops-agent-vs-dashboard`.

### 9. `/about` — "Built on FinOps principles" section
```html
…the agent that puts FinOps principles into practice — see
<a href="/finops-agent-vs-dashboard">how the execution loop works</a>
or the <a href="/data-access">exact permissions we request</a>.
```

### 10. `/data-access` — final CTA
```html
Once you're comfortable with our access model, see
<a href="/aws">how CostSage runs on AWS</a> or
<a href="/azure">on Azure</a>.
```

### 11. `/finops-agent-vs-dashboard` — final CTA
Already strong; ensure links to:
- `/features` (capabilities)
- `/pricing` (commercial)
- `/aws` and `/azure` (cloud-specific landings)

### 12. Footer — site-wide
Add `/aws` next to existing `/azure` link in the cloud-coverage footer column.

## Anchor-text discipline

- Avoid "click here" / "learn more" — use descriptive phrases that match the
  target page's H1 or a target keyword.
- One internal link per ~150 words of body copy is healthy. Don't over-link.
- Pillar (`/finops-agent-vs-dashboard`) should receive ≥4 inbound links from
  other pages by end of Sprint 1.

## Verification

After deploy, run:
```bash
for url in / /features /pricing /aws /azure /nops-alternative /cloudzero-alternative /about /data-access /blog; do
  echo "=== $url ==="
  curl -sL "https://costsage.ai$url" | grep -oE 'href="(/[^"]*)"' | sort -u
done
```
Confirm each page has ≥3 internal outbound links and the pillar receives ≥4
inbound links.
