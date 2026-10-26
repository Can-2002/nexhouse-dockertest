# Erklärung der verschiedenen Module

Das Repository enthält sowohl die gemeinsame Entwicklungsumgebung als auch ein
erstes Django-Anwendungsgerüst. Für eine reine Entwicklungsumgebung wären die
vorbereiteten Anwendungsmodule noch nicht notwendig.

| Ordner / Datei | Aufgabe |
| --- | --- |
| `Dockerfile` | Definiert die Entwicklungsumgebung: Python-Version, Werkzeuge und Installation der Requirements. |
| `compose.yaml` | Startet Django und PostgreSQL gemeinsam. Die Datenbankdaten bleiben in einem Docker-Volume erhalten. |
| `.devcontainer/` | Verbindet VS Code und GitHub Codespaces mit dieser Docker-Umgebung, einschließlich gemeinsamer Editor-Erweiterungen. |
| `requirements.txt` / `requirements-dev.txt` | Legen die Python-Pakete und ihre Versionen fest. Die zweite Datei ergänzt Entwicklungswerkzeuge wie Ruff. |
| `.env` / `.env.example` | Enthalten lokale Einstellungen wie Datenbankzugang; `.env.example` ist die teilbare Vorlage. Die echte `.env` wird bei der Einrichtung erzeugt und nicht zu GitHub hochgeladen. |
| `scripts/`, `start.ps1`, `start.sh`, `compose.setup.yaml` | Vereinfachen den ersten Start: Einstellungen erzeugen, Container bauen und Anwendung starten. Diese Dateien sind Komforthelfer. |
| `config/` und `manage.py` | Bilden das eigentliche Django-Projekt: Einstellungen, URLs und Verwaltungsbefehle. Das geht über die reine Entwicklungsumgebung hinaus. |
| `accounts/` | Enthält ein vorbereitetes eigenes Django-Benutzermodell. Das ist bereits Anwendungsentwicklung. |
| `core/` | Enthält die Ansicht für eine Startseite, eine Datenbank-Verbindungsprüfung und sechs Tests. Ebenfalls bereits Anwendungscode. |
| `templates/` | Enthält das HTML der einfachen Startseite. |
| `.github/` | Enthält automatische Prüfungen, die bei Pushes und Pull Requests auf GitHub laufen sollen. |
| `pyproject.toml`, `.editorconfig`, `.gitattributes` | Regeln Codeformatierung, Einrückungen und Zeilenenden, damit alle einheitlich arbeiten. |
| `.gitignore` / `.dockerignore` | Verhindern, dass lokale Geheimnisse und unnötige Dateien in Git beziehungsweise ins Docker-Image gelangen. |
| `README.md` / `docs/` | Enthalten die Startanleitung und die Dokumentation der bisherigen Prüfungen. |
| `.venv/` / `.ruff_cache/` | Sind die lokale Python-Testumgebung und ein Werkzeug-Cache auf dem Einrichtungsrechner. Für den Docker-Start sind beide unnötig und werden nicht mit hochgeladen. |
| `.git/` | Speichert die lokale Git-Verwaltung und die Verbindung zum GitHub-Repository. Dieser Ordner wird von Git selbst verwaltet. |

## Brauchen wir eine `.venv`?

Für die Entwicklung mit Docker braucht ihr keine zusätzliche lokale `.venv`.
Sie wurde auf dem Einrichtungsrechner ausschließlich zum Prüfen des Django-Codes
angelegt, weil dort Docker noch nicht verfügbar war. In Docker und Codespaces
werden die Requirements bereits im Container installiert.

## Wo fangen neue Teammitglieder an?

Die [README](README.md) beschreibt den Start unter Windows, macOS/Linux, VS Code
und GitHub Codespaces. Der [Prüfstand](docs/VALIDATION.md) unterscheidet bereits
bestandene Prüfungen von noch ausstehenden Container- und Codespaces-Tests.
