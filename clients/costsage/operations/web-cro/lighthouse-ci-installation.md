# Lighthouse CI Installation Plan — costsage.ai

**Status:** Plan, awaiting eng to execute
**Goal:** Catch CWV regressions on every overlay deploy. Tie into G12 (sprint-2 perf hardening).

---

## 1. Why

Pages are getting added quickly during Sprint-2 (5 net-new this batch). Without automated CWV tracking we'll discover regressions only after they hit Search Console or live users. Lighthouse CI runs on every deploy and fails the build if budgets are breached.

## 2. Architecture

- Run on the existing soc-server (Ubuntu 22.04, 51.222.11.168) as a cron job, not in CI/CD — costsage.ai has no Git CI today
- Triggered post-deploy by the same script that runs `nginx -s reload`
- Stores reports in `/opt/costsage-sprint1/lighthouse/` with date-stamped folders
- Optionally pushes summary JSON to a small static dashboard at `/internal/perf/` (basic-auth-protected)

## 3. Install

```bash
# On soc-server, as root
apt-get install -y nodejs npm chromium-browser
npm install -g @lhci/cli@0.13.x
mkdir -p /opt/costsage-sprint1/lighthouse
```

## 4. Config — `/opt/costsage-sprint1/lighthouse/lighthouserc.json`

```json
{
  "ci": {
    "collect": {
      "url": [
        "https://costsage.ai/",
        "https://costsage.ai/pricing",
        "https://costsage.ai/aws",
        "https://costsage.ai/azure",
        "https://costsage.ai/multi-cloud",
        "https://costsage.ai/finops-for-ai-workloads",
        "https://costsage.ai/azure-cost-optimization",
        "https://costsage.ai/compare/cloudzero-vs-costsage",
        "https://costsage.ai/compare/nops-vs-costsage",
        "https://costsage.ai/alternatives/vantage",
        "https://costsage.ai/alternatives/prosperops"
      ],
      "numberOfRuns": 3,
      "settings": {
        "preset": "desktop",
        "chromePath": "/usr/bin/chromium-browser",
        "chromeFlags": "--headless --no-sandbox --disable-gpu"
      }
    },
    "assert": {
      "assertions": {
        "categories:performance": ["error", {"minScore": 0.85}],
        "categories:accessibility": ["error", {"minScore": 0.9}],
        "categories:best-practices": ["warn", {"minScore": 0.9}],
        "categories:seo": ["error", {"minScore": 0.95}],
        "largest-contentful-paint": ["error", {"maxNumericValue": 2500}],
        "cumulative-layout-shift": ["error", {"maxNumericValue": 0.1}],
        "interaction-to-next-paint": ["warn", {"maxNumericValue": 200}]
      }
    },
    "upload": {
      "target": "filesystem",
      "outputDir": "/opt/costsage-sprint1/lighthouse/reports"
    }
  }
}
```

## 5. Run hook

Append to the deploy script:
```bash
cd /opt/costsage-sprint1/lighthouse && lhci autorun --config=./lighthouserc.json || \
  echo "[$(date -u +%FT%TZ)] LHCI assertions failed — see reports" >> /opt/costsage-sprint1/lighthouse/regressions.log
```

`|| echo` keeps deploy non-blocking initially (warn-only mode). Flip to `|| exit 1` after 2 weeks of clean runs.

## 6. Mobile budget (separate run)

After desktop is green, add a parallel mobile profile (preset: "mobile", same URLs). Mobile budgets:
- LCP ≤ 4000 ms
- CLS ≤ 0.1
- INP ≤ 500 ms

## 7. Alerting

Phase 1: log file only.
Phase 2 (after 2 weeks): if regressions.log is non-empty in last 24h, send Slack/email via the existing alerting webhook — `[TBD-OPERATOR]` confirm webhook URL.

## 8. Verification

- [ ] Node + Chromium installed on soc-server
- [ ] Config in place
- [ ] First run completes and produces 11 reports
- [ ] Reports retained for 30 days, then rotated
- [ ] Hook tied into deploy script
- [ ] One intentional regression (e.g. unoptimised hero image) demonstrates the assertion catch
