# Lighthouse CI Cron Spec — CostSage.ai

> Daily Lighthouse CI run on the marketing-claude-soc server (Ubuntu, `51.222.11.168:8448` per memory). 18 sitemap URLs. Output JSON to `clients/costsage/feeds/lighthouse-daily-YYYY-MM-DD.json`. Slack alert on > 10pt week-over-week drop in performance score on any URL.

## 1. URL list (18 sitemap URLs)

```
https://costsage.ai/
https://costsage.ai/aws
https://costsage.ai/azure
https://costsage.ai/pricing
https://costsage.ai/compare/cloudzero-vs-costsage
https://costsage.ai/compare/nops-vs-costsage
https://costsage.ai/blog/aws-cost-optimisation-best-practices
https://costsage.ai/blog/ri-vs-savings-plans
https://costsage.ai/about
https://costsage.ai/contact
https://costsage.ai/security
https://costsage.ai/privacy
https://costsage.ai/terms
https://costsage.ai/blog
https://costsage.ai/customers
https://costsage.ai/integrations
https://costsage.ai/aws/marketplace
https://costsage.ai/login
```

`[TBD-OPERATOR]` Confirm exact 18 URLs vs `sitemap.xml`. Replace any 404s.

## 2. Cron entry (Ubuntu user `marketing-ops`)

```
# /etc/cron.d/costsage-lighthouse
SHELL=/bin/bash
PATH=/usr/local/bin:/usr/bin:/bin
30 03 * * * marketing-ops /opt/lighthouse-runner/run.sh >> /var/log/costsage-lighthouse.log 2>&1
```

Runs 03:30 UTC daily.

## 3. `/opt/lighthouse-runner/run.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

DATE=$(date -u +%F)
OUTDIR="/opt/lighthouse-runner/out/${DATE}"
URLLIST="/opt/lighthouse-runner/urls.txt"
REPO_FEED="/opt/lighthouse-runner/repo/clients/costsage/feeds"
SLACK_HOOK="${SLACK_LIGHTHOUSE_WEBHOOK}"   # set in /etc/default/costsage-lighthouse

mkdir -p "${OUTDIR}"

declare -a RESULTS
while IFS= read -r URL; do
  [ -z "${URL}" ] && continue
  SAFE=$(echo "${URL}" | sed 's|https\?://||; s|/|_|g; s|_$||')
  OUT="${OUTDIR}/${SAFE}.json"
  npx --yes lighthouse "${URL}" \
    --quiet \
    --chrome-flags="--headless=new --no-sandbox --disable-gpu" \
    --output=json \
    --output-path="${OUT}" \
    --only-categories=performance,accessibility,best-practices,seo \
    --form-factor=mobile \
    --throttling-method=simulate
  RESULTS+=("${OUT}")
done < "${URLLIST}"

# Aggregate into single feed file
node /opt/lighthouse-runner/aggregate.js "${OUTDIR}" "${REPO_FEED}/lighthouse-daily-${DATE}.json"

# Commit feed (read-only PR workflow handles repo write — adapt as needed)
cd /opt/lighthouse-runner/repo
git pull --ff-only
git add "clients/costsage/feeds/lighthouse-daily-${DATE}.json"
git commit -m "chore(costsage): lighthouse daily ${DATE}" || echo "nothing to commit"
git push origin main || echo "push failed — alert ops"

# Run alert check
node /opt/lighthouse-runner/alert.js "${REPO_FEED}" "${DATE}" "${SLACK_HOOK}"
```

## 4. Aggregate output schema

`clients/costsage/feeds/lighthouse-daily-YYYY-MM-DD.json`:

```json
{
  "date": "2026-04-28",
  "form_factor": "mobile",
  "results": [
    {
      "url": "https://costsage.ai/",
      "perf": 0.92,
      "a11y": 0.95,
      "bp": 0.93,
      "seo": 1.00,
      "lcp_ms": 1840,
      "tbt_ms": 110,
      "cls": 0.02,
      "inp_ms": 180,
      "fcp_ms": 1200
    }
  ]
}
```

## 5. Alert spec — Slack webhook payload

When any URL's `perf` drops > 0.10 (10 points) vs the same weekday last week:

```json
{
  "blocks": [
    {
      "type": "header",
      "text": { "type": "plain_text", "text": "⚠️ CostSage Lighthouse perf regression" }
    },
    {
      "type": "section",
      "fields": [
        { "type": "mrkdwn", "text": "*URL*\n<https://costsage.ai/aws|/aws>" },
        { "type": "mrkdwn", "text": "*Perf today*\n0.74 (was 0.88, -0.14)" },
        { "type": "mrkdwn", "text": "*LCP*\n3,200 ms (was 1,840 ms)" },
        { "type": "mrkdwn", "text": "*TBT*\n420 ms (was 110 ms)" }
      ]
    },
    {
      "type": "context",
      "elements": [
        { "type": "mrkdwn", "text": "Feed: `lighthouse-daily-2026-04-28.json` | Compared to `2026-04-21`" }
      ]
    }
  ]
}
```

POST to `${SLACK_LIGHTHOUSE_WEBHOOK}` (channel `#marketing-perf-alerts`).

## 6. Edge cases handled
- URL returns 5xx: alert separately (Slack with `:rotating_light:` block).
- URL returns 404: alert + remove from URL list with operator review.
- Missing prior-week data (cold start): only alert on absolute thresholds (perf < 0.50, LCP > 4,000ms).
- Run fails entirely: cron emails `marketing-ops` via mail.

## 7. Operator deps
- `[TBD-OPERATOR]` SSH access for crontab setup.
- `[TBD-OPERATOR]` Slack webhook URL stored in `/etc/default/costsage-lighthouse` (chmod 600).
- `[TBD-OPERATOR]` Confirm 18 URLs match live sitemap.
- `[TBD-OPERATOR]` Git push credentials for the runner (deploy key).
