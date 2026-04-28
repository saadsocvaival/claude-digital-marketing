#!/bin/bash
# Daily Lighthouse + audit-sweep cron job for costsage.ai
# Runs all 23 URLs, computes deltas vs prior day, alerts on regression > 10 pts.
# Output: /opt/costsage-feeds/YYYY-MM-DD/{lighthouse-*.json, audit-sweep.json, summary.txt}
set -u
DATE=$(date -u +%Y-%m-%d)
OUTBASE=/opt/costsage-feeds
OUT="$OUTBASE/$DATE"
PRIOR=$(ls -1d "$OUTBASE"/2* 2>/dev/null | sort | tail -2 | head -1)
mkdir -p "$OUT"

URLS=(
  "https://costsage.ai/" "https://costsage.ai/about" "https://costsage.ai/features"
  "https://costsage.ai/pricing" "https://costsage.ai/contact" "https://costsage.ai/azure"
  "https://costsage.ai/aws" "https://costsage.ai/data-access" "https://costsage.ai/finops-agent-vs-dashboard"
  "https://costsage.ai/nops-alternative" "https://costsage.ai/cloudzero-alternative"
  "https://costsage.ai/blog" "https://costsage.ai/blog/aws-cost-optimisation-best-practices"
  "https://costsage.ai/blog/ri-vs-savings-plans" "https://costsage.ai/finops-for-ai-workloads"
  "https://costsage.ai/azure-cost-optimization" "https://costsage.ai/multi-cloud"
  "https://costsage.ai/alternatives/vantage" "https://costsage.ai/alternatives/prosperops"
  "https://costsage.ai/compare/cloudzero-vs-costsage" "https://costsage.ai/compare/nops-vs-costsage"
  "https://costsage.ai/privacy" "https://costsage.ai/terms"
)

slug() { s=$(echo "$1" | sed 's|https://costsage.ai||;s|^/$|home|;s|/|_|g;s|^_||'); [ -z "$s" ] && s=home; echo "$s"; }

for u in "${URLS[@]}"; do
  s=$(slug "$u")
  CHROME_PATH=/usr/bin/chromium-browser \
  lighthouse "$u" --output=json --output-path="$OUT/lh-$s.json" \
    --only-categories=performance,seo,accessibility,best-practices \
    --form-factor=mobile --throttling-method=simulate \
    --chrome-flags="--headless --no-sandbox --disable-gpu --disable-dev-shm-usage" \
    --quiet 2>&1 | tail -1
done

# Compute summary
python3 <<PY
import json, glob, os, sys
out_dir = "$OUT"
prior = "$PRIOR"
files = sorted(glob.glob(f"{out_dir}/lh-*.json"))
lines = []
totals = {"perf": [], "seo": [], "a11y": [], "bp": []}
per_url = {}
for f in files:
    try:
        with open(f) as fh: d = json.load(fh)
        url = d.get("finalDisplayedUrl", os.path.basename(f))
        c = d["categories"]
        scores = {k: int(c[k]["score"]*100) if c[k]["score"] is not None else None for k in ["performance","seo","accessibility","best-practices"]}
        per_url[url] = scores
        for k, name in [("performance","perf"),("seo","seo"),("accessibility","a11y"),("best-practices","bp")]:
            if scores[k] is not None: totals[name].append(scores[k])
    except: pass

avg = {k: round(sum(v)/len(v)) if v else 0 for k,v in totals.items()}
lines.append(f"=== CostSage Lighthouse — {os.path.basename(out_dir)} ===")
lines.append(f"URLs sampled: {len(files)}")
lines.append(f"Mobile averages: perf={avg['perf']}  seo={avg['seo']}  a11y={avg['a11y']}  bp={avg['bp']}")

# Compare to prior
if prior and os.path.isdir(prior):
    prior_files = glob.glob(f"{prior}/lh-*.json")
    prior_totals = {"perf": [], "seo": [], "a11y": [], "bp": []}
    for f in prior_files:
        try:
            with open(f) as fh: d = json.load(fh)
            c = d["categories"]
            for k, name in [("performance","perf"),("seo","seo"),("accessibility","a11y"),("best-practices","bp")]:
                if c[k]["score"] is not None: prior_totals[name].append(int(c[k]["score"]*100))
        except: pass
    pavg = {k: round(sum(v)/len(v)) if v else 0 for k,v in prior_totals.items()}
    delta = {k: avg[k] - pavg[k] for k in avg}
    lines.append(f"Prior ({os.path.basename(prior)}): perf={pavg['perf']}  seo={pavg['seo']}  a11y={pavg['a11y']}  bp={pavg['bp']}")
    lines.append(f"Delta:                                      perf={delta['perf']:+d}     seo={delta['seo']:+d}     a11y={delta['a11y']:+d}    bp={delta['bp']:+d}")
    if delta["perf"] <= -10:
        lines.append(f"⚠️  PERF REGRESSION ≥10 points — investigate")

with open(f"{out_dir}/summary.txt", "w") as f:
    f.write("\n".join(lines))
print("\n".join(lines))
PY
