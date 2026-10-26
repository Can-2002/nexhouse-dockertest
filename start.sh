#!/bin/sh
set -eu
cd "$(dirname "$0")"
command -v docker >/dev/null 2>&1 || { echo 'Bitte Docker installieren und starten.'; exit 1; }
docker info >/dev/null
docker compose -f compose.setup.yaml run --rm setup
docker compose up --build --wait --wait-timeout 180
echo 'Nexhouse ist bereit. Standardadresse: http://localhost:8000 (WEB_PORT in .env beachten).'
