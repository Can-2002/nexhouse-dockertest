# Prüfstand vom 26.10.2026

## Erfolgreich lokal geprüft

- Python 3.12.14 mit den festgelegten Django-/Psycopg-/Ruff-Versionen installiert.
- `ruff check .` und `ruff format --check .`.
- `python manage.py check` mit den regulären PostgreSQL-Einstellungen
  (dies prüft noch keine PostgreSQL-Verbindung).
- Keine fehlenden Migrationen laut `makemigrations --check --dry-run`.
- Alle sechs Django-Tests mit `config.test_sqlite`: Startseite, Datenbank-Healthcheck,
  Fehlerantwort ohne interne Details, Admin-Anmeldepflicht, Ausschluss normaler
  Benutzer und Zugang für Superuser inklusive Passwortprüfung.
- Initiale Migrationen einschließlich des eigenen Benutzermodells mit SQLite angewendet.
- JSON-/YAML-Dateien lesbar; PowerShell-Startskript syntaktisch geprüft.
- Die festgelegten Image-Tags für Python und PostgreSQL sind bei Docker Hub verfügbar.
- Einrichtung erzeugt `.env`; eine Wiederholung erhält die vorhandenen Werte.

## Noch praktisch zu prüfen

Auf dem Einrichtungsrechner wurde keine Docker-Installation gefunden. Deshalb wurden
Docker-Build, Compose-Start, PostgreSQL-Integration, Persistenz nach Neustart und
Dev-Container-/Codespaces-Aufbau noch nicht ausgeführt. Die SQLite-Tests ersetzen
keine PostgreSQL-Integrationstests.

Der GitHub-Workflow prüft nach dem Push den Docker-Build, Anwendungsstart inklusive
Migrationen, sechs Tests mit PostgreSQL und die HTTP-Erreichbarkeit. Ein erfolgreicher
Workflow allein bestätigt noch nicht den VS-Code-/Codespaces-Aufbau.

## Abnahme auf einem Rechner mit Docker

1. `start.ps1` oder `sh start.sh` ausführen; Startseite und `/health/` öffnen.
2. Mit `createsuperuser` einen Administrator anlegen und `/admin/` prüfen.
3. `docker compose exec web python manage.py test` ausführen.
4. `docker compose down`, danach `docker compose up -d --wait`; derselbe Administrator
   muss sich weiterhin anmelden können.
5. VS Code: **Dev Containers: Reopen in Container**; Datei bearbeiten, automatisches
   Neuladen und `python manage.py test` im Container prüfen.
6. Frischen Codespace öffnen; Port 8000 privat öffnen, Administrator anlegen und
   die Anmeldung inklusive CSRF-Prüfung testen.

Die `.venv` auf dem Einrichtungsrechner dient nur der lokalen Validierung, ist von
Git und Docker-Build ausgeschlossen und wird für den Teamstart nicht benötigt.
