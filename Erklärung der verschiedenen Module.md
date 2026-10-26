# Erklärung der verschiedenen Module

Dieses Repository enthält nur die gemeinsame Entwicklungsumgebung. Django ist
installiert, aber es wurde kein Django-Projekt angelegt. Die Architektur und die
Anwendungsmodule werden erst gemeinsam im Team festgelegt.

| Ordner / Datei | Aufgabe |
| --- | --- |
| `Dockerfile` | Legt Python und die installierten Werkzeuge fest. Der Container bleibt als Arbeitsumgebung aktiv und startet keine Anwendung. |
| `compose.yaml` | Startet die Entwicklungsumgebung und PostgreSQL. Daten bleiben in einem Docker-Volume erhalten. |
| `.devcontainer/` | Bindet dieselbe Umgebung in VS Code und GitHub Codespaces ein und legt Editor-Erweiterungen fest. |
| `requirements.txt` | Legt Django, den PostgreSQL-Treiber und ihre Abhängigkeiten mit festen Versionen fest. |
| `requirements-dev.txt` | Ergänzt Ruff als Werkzeug für Formatierung und Codeprüfung. |
| `.env` / `.env.example` | Enthalten persönliche Datenbankeinstellungen beziehungsweise deren teilbare Vorlage. Die echte `.env` wird nicht gepusht. |
| `scripts/setup.py` / `compose.setup.yaml` | Erzeugen bei der ersten Einrichtung eine `.env` mit zufälligem Datenbankpasswort. Vorhandene Einstellungen bleiben erhalten. |
| `scripts/check_environment.py` | Zeigt Python-/Django-Versionen und prüft die PostgreSQL-Verbindung. Es legt keine Tabellen oder Anwendung an. |
| `start.ps1` / `start.sh` | Fassen Einrichtung, Containerstart und Umgebungsprüfung für Windows beziehungsweise macOS/Linux zusammen. |
| `.github/` | Prüft die Entwicklungsumgebung nach Pushes und bei Pull Requests automatisch. |
| `pyproject.toml`, `.editorconfig`, `.gitattributes` | Vereinheitlichen Codeformatierung, Einrückungen und Zeilenenden. |
| `.gitignore` / `.dockerignore` | Schließen lokale Geheimnisse und unnötige Dateien aus Git beziehungsweise Docker-Builds aus. |
| `README.md` | Erklärt Installation, Codespaces und die wichtigsten Befehle. |
| `.git/` | Wird von Git verwaltet und enthält die lokale Versionshistorie sowie die GitHub-Verbindung. |

## Was ist notwendig, was ist Komfort?

Dockerfile, Requirements und Compose bilden die technische Grundlage inklusive
PostgreSQL. Die Dev-Container-Konfiguration ermöglicht den vereinbarten Einstieg
über VS Code und Codespaces. Startskripte, automatische Prüfungen und gemeinsame
Formatierungsregeln erleichtern Einrichtung und Zusammenarbeit.

## Was wurde entfernt?

Das vorzeitig angelegte Django-Projekt (`config`, `manage.py`), die Benutzerverwaltung
(`accounts`), die Startseite und Anwendungstests (`core`, `templates`) sowie das
Django-Startskript wurden entfernt. Die alte Prüfdokumentation wurde durch den aktuellen
Prüfstand in der README ersetzt. Django selbst bleibt als installiertes Paket erhalten.

## Brauchen wir eine `.venv`?

Nein. Docker und Codespaces installieren die Pakete im Container. Eine eventuell
noch vorhandene lokale `.venv` und `.ruff_cache` stammen von lokalen Prüfungen,
sind nicht im Repository und können bei Nichtgebrauch gelöscht werden.
