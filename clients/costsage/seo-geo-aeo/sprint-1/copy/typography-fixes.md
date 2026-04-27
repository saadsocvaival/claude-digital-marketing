# Typography fixes — F7

5 visible-in-HTML heading concatenations. Apply in CMS source. If the joining
is intentional CSS line-break styling (likely a styled `<br>` collapsed during
HTML extraction), wrap the joined fragments in distinct spans with explicit
whitespace so crawlers and LLMs see clean tokens.

## Recommended source pattern

```html
<!-- BEFORE -->
<h1>Your cloud bill is hiding<br>thousands. We find them.</h1>

<!-- AFTER -->
<h1>
  <span class="line-1">Your cloud bill is hiding thousands.</span>
  <span class="line-2">We find them.</span>
</h1>
```

CSS handles the line break (`.line-1, .line-2 { display: block; }`); the raw
HTML reads as proper sentences.

## The 5 fixes

| Page | Element | Before (raw HTML) | After (raw HTML) |
|---|---|---|---|
| `/` | H1 | `Your cloud bill is hidingthousands. We find them.` | `Your cloud bill is hiding thousands. We find them.` |
| `/` | H2 (#1) | `From connected to savingin under 60 seconds` | `From connected to saving in under 60 seconds` |
| `/` | H2 (last) | `Your cloud bill is hidingthousands. Let the agent find them.` | `Your cloud bill is hiding thousands. Let the agent find them.` |
| `/features` | H1 | `Built to reason, plan,and execute` | `Built to reason, plan, and execute` |
| `/pricing` | H1 | `We only winwhen you save.` | `We only win when you save.` |

## Verification

After fix, re-run:
```bash
curl -sL https://costsage.ai/ | grep -oE '<h[12][^>]*>[^<]*</h[12]>'
```
Each heading should read as a complete sentence with proper spacing.
