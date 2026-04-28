# PostHog Self-Host Install — CostSage.ai

> Self-hosted PostHog OSS via Docker on `marketing-claude-soc` host (or alternate ops host). Append to existing `/opt/wordpress/docker-compose.yml`. **Do not** edit that file from here — this doc supplies the YAML and operator applies.

## 1. Add to `/opt/wordpress/docker-compose.yml`

```yaml
# ===== PostHog (added 2026-Q3) =====
# Single-host OSS deployment. Suitable for ≤ 1M events/month.
# Source: https://posthog.com/docs/self-host (per public docs)

services:
  posthog-postgres:
    image: postgres:15-alpine
    container_name: posthog-postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: posthog
      POSTGRES_PASSWORD: ${POSTHOG_PG_PASSWORD}
      POSTGRES_DB: posthog
    volumes:
      - posthog_postgres_data:/var/lib/postgresql/data
    networks:
      - posthog_net

  posthog-redis:
    image: redis:7-alpine
    container_name: posthog-redis
    restart: unless-stopped
    volumes:
      - posthog_redis_data:/data
    networks:
      - posthog_net

  posthog-clickhouse:
    image: clickhouse/clickhouse-server:23.12-alpine
    container_name: posthog-clickhouse
    restart: unless-stopped
    ulimits:
      nofile:
        soft: 262144
        hard: 262144
    volumes:
      - posthog_clickhouse_data:/var/lib/clickhouse
    networks:
      - posthog_net

  posthog-kafka:
    image: bitnami/kafka:3.6
    container_name: posthog-kafka
    restart: unless-stopped
    environment:
      KAFKA_CFG_NODE_ID: 1
      KAFKA_CFG_PROCESS_ROLES: controller,broker
      KAFKA_CFG_LISTENERS: PLAINTEXT://:9092,CONTROLLER://:9093
      KAFKA_CFG_ADVERTISED_LISTENERS: PLAINTEXT://posthog-kafka:9092
      KAFKA_CFG_CONTROLLER_QUORUM_VOTERS: 1@posthog-kafka:9093
      KAFKA_CFG_CONTROLLER_LISTENER_NAMES: CONTROLLER
      ALLOW_PLAINTEXT_LISTENER: "yes"
    volumes:
      - posthog_kafka_data:/bitnami/kafka
    networks:
      - posthog_net

  posthog-web:
    image: posthog/posthog:latest
    container_name: posthog-web
    restart: unless-stopped
    depends_on:
      - posthog-postgres
      - posthog-redis
      - posthog-clickhouse
      - posthog-kafka
    environment:
      DATABASE_URL: postgres://posthog:${POSTHOG_PG_PASSWORD}@posthog-postgres:5432/posthog
      REDIS_URL: redis://posthog-redis:6379
      CLICKHOUSE_HOST: posthog-clickhouse
      KAFKA_HOSTS: posthog-kafka:9092
      SECRET_KEY: ${POSTHOG_SECRET_KEY}        # 50-char random
      SITE_URL: https://posthog.costsage.ai
      DISABLE_SECURE_SSL_REDIRECT: "false"
      IS_BEHIND_PROXY: "true"
      TRUSTED_PROXIES: "172.16.0.0/12,10.0.0.0/8,127.0.0.1"
    ports:
      - "127.0.0.1:8000:8000"
    networks:
      - posthog_net

  posthog-worker:
    image: posthog/posthog:latest
    container_name: posthog-worker
    restart: unless-stopped
    command: ./bin/docker-worker
    depends_on:
      - posthog-postgres
      - posthog-redis
      - posthog-clickhouse
      - posthog-kafka
    environment:
      DATABASE_URL: postgres://posthog:${POSTHOG_PG_PASSWORD}@posthog-postgres:5432/posthog
      REDIS_URL: redis://posthog-redis:6379
      CLICKHOUSE_HOST: posthog-clickhouse
      KAFKA_HOSTS: posthog-kafka:9092
      SECRET_KEY: ${POSTHOG_SECRET_KEY}
    networks:
      - posthog_net

volumes:
  posthog_postgres_data:
  posthog_redis_data:
  posthog_clickhouse_data:
  posthog_kafka_data:

networks:
  posthog_net:
    driver: bridge
```

`.env` additions (operator-managed):
```
POSTHOG_PG_PASSWORD=<32-char random>
POSTHOG_SECRET_KEY=<50-char random>
```

## 2. Cloudflare reverse-proxy notes

PostHog is exposed at `127.0.0.1:8000` only. Front it with the existing Nginx that already serves WordPress, and tunnel it via Cloudflare:

```nginx
server {
  listen 443 ssl http2;
  server_name posthog.costsage.ai;

  # Cloudflare-Origin TLS — use existing wildcard or run certbot for the subdomain.
  ssl_certificate     /etc/letsencrypt/live/costsage.ai/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/costsage.ai/privkey.pem;

  # WebSocket support (PostHog uses WS for realtime).
  location / {
    proxy_pass http://127.0.0.1:8000;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_read_timeout 600s;
  }

  client_max_body_size 50m;
}
```

Cloudflare DNS:
- A `posthog.costsage.ai` → SOC server IP (51.222.11.168 if hosted there per memory; otherwise `[TBD-OPERATOR]`).
- Proxy: **DNS only (grey cloud)** until WS-through-CF tested. Re-enable orange cloud after verifying realtime works (Cloudflare proxies WS on Pro plans, free has caveats).
- Page Rules: cache "Bypass" for `/api/*` and `/decide/*`.

## 3. Capacity / sizing estimate

Assumptions for CostSage Y1:
- Sessions/mo (paid + organic + app): grow from ~10K → 80K over 12 months.
- Events per session: avg 8 (page_view + scroll_75 + cta_click + occasional form_*).
- Identify events: 1 per logged-in app-session × ~30K mo by Y1-end.
- → Y1 total events: roughly 12M (back-of-envelope; conservative 20M).

| Resource | Y1 estimate | Y1 with 50% headroom |
|----------|-------------|----------------------|
| ClickHouse on-disk (compressed, ~100B/event) | ~1.2 GB/M events × 20M = 24 GB | **40 GB** |
| Postgres metadata | < 5 GB | **10 GB** |
| Kafka short-term buffer | 10 GB | **20 GB** |
| **Total disk** | ~50 GB | **80 GB** (provision SSD) |
| RAM | ClickHouse 4G + Kafka 2G + PG 1G + Web/Worker 2G + Redis 0.5G = **9–10G** baseline | **16 GB host** |
| CPU | 2 vCPU baseline; bursts during ingest | **4 vCPU host** |

Verify SOC server (`51.222.11.168`) capacity per `reference_soc_server.md` memory entry — `[TBD-OPERATOR]`.

## 4. JS snippet for site (already referenced in `tag-plan.md`)

```html
<script>
!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){...});</script>
<script>
posthog.init('[TBD-OPERATOR-PROJECT-API-KEY]', {
  api_host: 'https://posthog.costsage.ai',
  capture_pageview: false, // we manage page_view via GTM
  autocapture: false,       // we manage events explicitly
  persistence: 'localStorage+cookie'
});
</script>
```

## 5. Backup
- ClickHouse: nightly `clickhouse-backup` to S3 bucket `[TBD-OPERATOR]`.
- Postgres: nightly `pg_dump` → S3.
- Retention: 30 days rolling.

## 6. Operator deps
- `[TBD-OPERATOR]` Confirm SOC host has 16 GB RAM / 80 GB SSD free.
- `[TBD-OPERATOR]` DNS record + TLS cert for `posthog.costsage.ai`.
- `[TBD-OPERATOR]` `.env` secrets set.
- `[TBD-OPERATOR]` S3 backup target.
