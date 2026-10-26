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
Write-Host 'Nexhouse ist bereit. Standardadresse: http://localhost:8000 (WEB_PORT in .env beachten).'
