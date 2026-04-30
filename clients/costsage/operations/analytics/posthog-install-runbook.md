---
artifact: posthog-self-host-runbook
date: 2026-04-30
purpose: 15-step operator runbook to install PostHog self-hosted on marketing-claude-soc
prerequisites: 16GB+ RAM available, 80GB+ disk, docker installed, ports 8000+8001+9000 free
---

# PostHog Self-Host Install Runbook

> Realistic resource needs: PostHog's full stack (postgres + redis + clickhouse + kafka + zookeeper + plugin-server + posthog) wants ~16GB RAM minimum. Server has 196GB free disk; verify RAM with `free -h` before starting.

## Steps

```bash
# 1. SSH in
ssh marketing-claude-soc

# 2. Verify resources
free -h
df -h /opt
docker --version

# 3. Make working directory
mkdir -p /opt/posthog && cd /opt/posthog

# 4. Pull official compose
curl -L https://posthog.com/docker-compose.yml -o docker-compose.yml

# 5. Generate secrets
echo "POSTHOG_SECRET=$(openssl rand -hex 32)" > .env
echo "DOMAIN=ph.costsage.ai" >> .env

# 6. Boot
docker compose up -d

# 7. Wait for postgres + clickhouse migrations (~3 min)
docker compose logs -f posthog | grep -m1 "ready"

# 8. Create initial user (first-run wizard at http://localhost:8000)
#    Default-bind to 127.0.0.1 only; expose later via Cloudflare tunnel if desired.

# 9. Verify
curl http://localhost:8000/_health

# 10. Snapshot the config
tar -czf /opt/costsage-sprint1/backup/posthog-initial-$(date +%Y%m%d).tar.gz /opt/posthog
```

## Add Cloudflare tunnel route (optional)

If exposing publicly at `ph.costsage.ai`:
1. In Cloudflare Zero Trust → Applications → Add tunnel route → `ph.costsage.ai` → `http://localhost:8000`.
2. Bind same Cloudflare Access policy as `admin.costsage.ai` (operator only).

## Snippet to instrument costsage.ai

Add to all HTML pages (after `</title>`):
```html
<script>
!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures getActiveMatchingSurveys getSurveys onSessionId".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
posthog.init('phc_YOUR_PROJECT_API_KEY',{api_host:'https://ph.costsage.ai'})
</script>
```

Replace `phc_YOUR_PROJECT_API_KEY` with the value from PostHog UI → Settings → Project API Key.

## Why we're using a runbook instead of auto-install

PostHog's full stack pulls ~5GB of images and takes 5-8 minutes to converge migrations. Better as an explicit operator-driven step than blind `docker compose up` from an automation. Plus operator should choose whether to expose publicly or keep internal-only.

## Decision tree

| Decision | Choice | Default |
|---|---|---|
| Self-host vs Cloud | Self-host | We have the infra (196GB free) |
| Public vs internal-only | Internal first | Reduces attack surface; expose later if external dashboards needed |
| Postgres bundled vs external | Bundled | Single-node, less ops burden |
| Backup cadence | Daily snapshot | tar of /opt/posthog → /opt/costsage-sprint1/backup/ |

## Operator confirmations needed before this runs

- [ ] RAM check (`free -h`) shows ≥16GB available
- [ ] Disk check (`df -h /opt`) shows ≥80GB free
- [ ] Confirm internal-only vs public
- [ ] Confirm Cloudflare tunnel route addition (if public)
