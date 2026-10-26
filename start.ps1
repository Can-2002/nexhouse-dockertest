$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    throw 'Docker fehlt. Bitte Docker Desktop installieren, starten und das Terminal neu oeffnen.'
}
docker info --format '{{.ServerVersion}}'
if ($LASTEXITCODE -ne 0) { throw 'Docker Desktop starten und auf die Bereitschaft warten.' }
docker compose -f compose.setup.yaml run --rm setup
if ($LASTEXITCODE -ne 0) { throw 'Einrichtung fehlgeschlagen.' }
docker compose up --build --wait --wait-timeout 180
if ($LASTEXITCODE -ne 0) { throw 'Start fehlgeschlagen. Diagnose: docker compose logs' }
docker compose exec -T dev python scripts/check_environment.py
if ($LASTEXITCODE -ne 0) { throw 'Umgebungspruefung fehlgeschlagen.' }
Write-Host 'Entwicklungsumgebung bereit. Terminal oeffnen: docker compose exec dev bash'
