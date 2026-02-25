#!/bin/sh
set -eu

CONFIG_DIR="/root/.nanobot"
CONFIG_FILE="$CONFIG_DIR/config.json"
TEMPLATE_FILE="/opt/nanobot-umbrel/config.template.json"
PROMPTS_FILE="$CONFIG_DIR/prompts.md"
MCP_FILE="$CONFIG_DIR/mcp_servers.json"

mkdir -p "$CONFIG_DIR"

if [ ! -f "$CONFIG_FILE" ]; then
  cp "$TEMPLATE_FILE" "$CONFIG_FILE"
  echo "[nanobot-umbrel] Created $CONFIG_FILE from template."
  echo "[nanobot-umbrel] Edit Umbrel app data config, then restart the app:"
  echo "[nanobot-umbrel] ~/umbrel/app-data/wild-gablota-nanobot/data/nanobot/config.json"
fi

if [ ! -f "$PROMPTS_FILE" ]; then
  printf "# NanoBot prompts\n" > "$PROMPTS_FILE"
fi

if [ ! -f "$MCP_FILE" ]; then
  printf "{}\n" > "$MCP_FILE"
fi

exec nanobot gateway
