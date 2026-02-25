# NanoBot on Umbrel (Cloudflare Tunnel Ready)

## 1) Edit NanoBot config after first start

First app start creates the NanoBot config here:

`~/umbrel/app-data/wild-gablota-nanobot/data/nanobot/config.json`

Update at least:

- `llm_services[0].api_key` -> your provider API key
- `gateway_api_keys[0]` -> strong random API key used by NanoBot gateway clients
- `channels.telegram.enabled` -> `true`
- `channels.telegram.bot_token` -> your Telegram bot token
- `channels.telegram.allow_list` -> your Telegram chat/user IDs (strings)

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
