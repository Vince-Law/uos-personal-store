# NanoBot on Umbrel (Cloudflare Tunnel Ready)

## 0) Build and publish your patched NanoBot image first (multi-arch for Umbrel ARM)

This Umbrel package is now designed for a **custom image built from patched `HKUDS/NanoBot` source** (not `jerryin/nanobot`).

Required upstream fixes:

- `nanobot gateway` supports `--host`
- gateway starts an HTTP listener exposing `GET /health`

Build and push a multi-arch image from the patched upstream checkout (example for Docker Hub):

```bash
cd _nanobot_upstream
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t <your-user>/nanobot-hostfix:0.1.4.post2-umbrel1 \
  --push \
  .
```

Or for GHCR:

```bash
cd _nanobot_upstream
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t ghcr.io/<your-user>/nanobot-hostfix:0.1.4.post2-umbrel1 \
  --push \
  .
```

Then edit `wild-gablota-nanobot/docker-compose.yml` and replace:

- `ghcr.io/REPLACE_ME/nanobot-hostfix:0.1.4.post2-umbrel1`

with your published image.

If you see `no matching manifest for linux/arm64/v8`, the pushed image tag does not include an ARM64 manifest. Re-push with `docker buildx build --platform ... --push` as shown above.

## 1) Edit NanoBot config after first start

First app start creates the NanoBot config here:

`~/umbrel/app-data/wild-gablota-nanobot/data/nanobot/config.json`

Update at least:

- `providers.openai.apiKey` -> your provider API key (or configure another provider under `providers`)
- `agents.defaults.model` -> model id matching your provider (example: `openai/gpt-4o-mini`, `openrouter/anthropic/claude-sonnet-4`)
- `channels.telegram.enabled` -> `true`
- `channels.telegram.token` -> your Telegram bot token
- `channels.telegram.allowFrom` -> your Telegram chat/user IDs (strings)

Notes:

- The app bootstrap still auto-rewrites the older invalid template format to NanoBot's current `providers`-based format on startup.
- The patched image is expected to include `curl` (Umbrel legacy installer healthcheck requirement).
- Umbrel on Raspberry Pi requires an image manifest that includes `linux/arm64` (or `linux/arm64/v8`).

## 2) Restart the app

Restart from Umbrel UI after editing the config.

## 3) Cloudflare Tunnel route (public internet)

Create/point a Cloudflare Tunnel hostname to:

`http://<your-umbrel-lan-ip>:1210`

Notes:

- This app is exposed through Umbrel `app_proxy` (recommended), not a direct container port.
- `PROXY_AUTH_ADD=false` is already set so webhook/callback routes are not broken by Umbrel auth injection.
- If you use Cloudflare Access, bypass/allow provider callbacks for NanoBot callback routes.

## 4) Useful endpoints (through Umbrel or your Cloudflare hostname)

- `GET /health`
- `POST /v1/chat/completions` (if/when implemented by your NanoBot build)
- `POST /v1/callback/telegram` (if you configure webhook mode)

## 5) Telegram callback URL example (if you choose webhook mode)

`https://<your-public-hostname>/v1/callback/telegram`

Use the public Cloudflare hostname, not localhost.
