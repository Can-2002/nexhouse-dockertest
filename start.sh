#!/bin/sh
set -eu
cd "$(dirname "$0")"
command -v docker >/dev/null 2>&1 || { echo 'Bitte Docker installieren und starten.'; exit 1; }
docker info >/dev/null
docker compose -f compose.setup.yaml run --rm setup
docker compose up --build --wait --wait-timeout 180
docker compose exec -T dev python scripts/check_environment.py
echo 'Entwicklungsumgebung bereit. Terminal oeffnen: docker compose exec dev bash'
