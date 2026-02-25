FROM jerryin/nanobot:latest

USER root

RUN set -eux; \
    if command -v apk >/dev/null 2>&1; then \
      apk add --no-cache curl; \
    elif command -v apt-get >/dev/null 2>&1; then \
      apt-get update; \
      apt-get install -y --no-install-recommends curl; \
      rm -rf /var/lib/apt/lists/*; \
    elif command -v microdnf >/dev/null 2>&1; then \
      microdnf install -y curl; \
      microdnf clean all; \
    elif command -v dnf >/dev/null 2>&1; then \
      dnf install -y curl; \
      dnf clean all; \
    else \
      echo "No supported package manager found to install curl" >&2; \
      exit 1; \
    fi
