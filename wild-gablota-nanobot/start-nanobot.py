import json
import os
import shutil


CONFIG_DIR = "/root/.nanobot"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")
TEMPLATE_FILE = "/opt/nanobot-umbrel/config.template.json"
PROMPTS_FILE = os.path.join(CONFIG_DIR, "prompts.md")
MCP_FILE = os.path.join(CONFIG_DIR, "mcp_servers.json")


def ensure_file(path: str, content: str) -> None:
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)


def main() -> None:
    os.makedirs(CONFIG_DIR, exist_ok=True)

    if not os.path.exists(CONFIG_FILE):
        shutil.copyfile(TEMPLATE_FILE, CONFIG_FILE)
        print(f"[nanobot-umbrel] Created {CONFIG_FILE} from template.", flush=True)
        print(
            "[nanobot-umbrel] Edit and restart: "
            "~/umbrel/app-data/wild-gablota-nanobot/data/nanobot/config.json",
            flush=True,
        )
    else:
        # Basic sanity check so syntax errors surface in logs before starting NanoBot.
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            json.load(f)

    ensure_file(PROMPTS_FILE, "# NanoBot prompts\n")
    ensure_file(MCP_FILE, "{}\n")

    os.execvp("nanobot", ["nanobot", "gateway"])


if __name__ == "__main__":
    main()
