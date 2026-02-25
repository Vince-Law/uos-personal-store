# NanoBot on Umbrel (Cloudflare Tunnel Ready)

## 1) Edit NanoBot config after first start

First app start creates the NanoBot config here:

`~/umbrel/app-data/wild-gablota-nanobot/data/nanobot/config.json`

Update at least:

- `providers.openai.apiKey` -> your provider API key (or configure another provider under `providers`)
- `agents.defaults.model` -> model id matching your provider (example: `openai/gpt-4o-mini`, `openrouter/anthropic/claude-sonnet-4`)
- `channels.telegram.enabled` -> `true`
- `channels.telegram.token` -> your Telegram bot token
- `channels.telegram.allowFrom` -> your Telegram chat/user IDs (strings)

Image note:

- This package currently uses `jerryin/nanobot:latest` (Docker Hub mirror) because some Umbrel installs receive `403 denied` when pulling `ghcr.io/hkuds/nanobot`.
- If you already installed an older package revision, this app now auto-rewrites the old invalid template format to NanoBot's current `providers`-based format on startup.

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
- `POST /v1/chat/completions`
- `POST /v1/callback/telegram`

## 5) Telegram callback URL example (if you choose webhook mode)

`https://<your-public-hostname>/v1/callback/telegram`

Use the public Cloudflare hostname, not localhost.
