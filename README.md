# Nexhouse – gemeinsame Entwicklungsumgebung

Dieses Repository stellt Python, Django, PostgreSQL und Entwicklungswerkzeuge bereit.
Es enthält **kein Django-Projekt, keine Benutzerverwaltung, keine Startseite und keine
Fachmodule**. Die Projektstruktur legen wir später gemeinsam im Team fest.

Eine Übersicht steht in [Erklärung der verschiedenen Module](Erklärung%20der%20verschiedenen%20Module.md).

## Windows: installieren und prüfen

1. [Git](https://git-scm.com/downloads/win) und [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/)
   installieren. Die WSL-2-Einrichtung abschließen und Docker Desktop starten (Linux-Container).
2. PowerShell öffnen:

   ```powershell
   git clone https://github.com/Can-2002/nexhouse-dockertest.git
   cd nexhouse-dockertest
   powershell -NoProfile -ExecutionPolicy Bypass -File .\start.ps1
   ```

   Bei einem vorhandenen Klon nur das Startskript im Projektordner ausführen.
   `ExecutionPolicy Bypass` gilt hier nur für diesen Prozess.
3. Das Skript erstellt bei Bedarf `.env`, baut die Umgebung und prüft die Installation
   sowie die Datenbankverbindung. Erfolg: **Entwicklungsumgebung bereit**.
4. Ein Terminal in der Umgebung öffnen:

   ```sh
   docker compose exec dev bash
   ```

Python und PostgreSQL müssen nicht lokal installiert werden. Der erste Aufbau benötigt
Internetzugang und kann einige Minuten dauern. Eine lokale `.venv` ist nicht erforderlich.
**Es läuft noch keine Website; im Browser gibt es deshalb keine Startseite.**

## macOS / Linux

Git und Docker mit Compose v2 installieren und starten, Repository klonen und im
Projektordner ausführen:

```sh
sh start.sh
```

## VS Code lokal

1. VS Code und die Erweiterung **Dev Containers** (`ms-vscode-remote.remote-containers`) installieren.
2. Projektordner öffnen und **Dev Containers: Reopen in Container** über die Befehlspalette auswählen.
3. Nach dem Aufbau im VS-Code-Terminal prüfen:

   ```sh
   python scripts/check_environment.py
   ```

Das Terminal läuft bereits im Container. Der Projektordner ist eingebunden; Änderungen
bleiben auf dem Rechner gespeichert. Python und Ruff sind im Container eingerichtet.

## GitHub Codespaces

1. Auf GitHub **Code → Codespaces → Create codespace on main** auswählen.
2. Den Aufbau abwarten. Docker muss auf dem eigenen Rechner dafür nicht installiert sein.
3. Im Codespaces-Terminal ausführen:

   ```sh
   python scripts/check_environment.py
   ```

Das zeigt die Python-/Django-Version und prüft die PostgreSQL-Verbindung, ohne Tabellen
oder ein Django-Projekt anzulegen. Es wird kein Browser-Port benötigt.
Jeder Codespace hat seine eigene Datenbank. Verfügbarkeit und Kosten hängen vom GitHub-Konto ab.

**Bei einem bereits bestehenden Codespace:** Zunächst bei sauberem Arbeitsstand `git pull`
aufrufen. Weil der Compose-Dienst von `web` zu `dev` geändert wurde, für diesen Wechsel
am einfachsten einen neuen Codespace auf `main` öffnen; ungesicherte Arbeit vorher sichern.
Für spätere Änderungen an Dockerfile oder Requirements reicht normalerweise **Rebuild Container**.

## Befehle für den Alltag

Im lokalen Terminal im Projektordner:

| Aufgabe | Befehl |
| --- | --- |
| Starten | `docker compose up -d --wait` |
| Nach Requirements-Änderung neu bauen | `docker compose up --build -d --wait` |
| Umgebung prüfen | `docker compose exec dev python scripts/check_environment.py` |
| Container-Terminal öffnen | `docker compose exec dev bash` |
| Code prüfen | `docker compose exec dev ruff check .` |
| Code formatieren | `docker compose exec dev ruff format .` |
| Logs ansehen | `docker compose logs` |
| Stoppen, Daten behalten | `docker compose down` |

In VS Code im Dev Container oder in Codespaces das Präfix `docker compose exec dev`
weglassen. Der Container wartet im Hintergrund, bis ihr darin Befehle ausführt.

## Einstellungen und Daten

- Versionen: Python 3.12.14, Django 5.2.18, PostgreSQL 17.11 und Ruff 0.17.2.
- `.env.example` beschreibt die Datenbankeinstellungen. Die Einrichtung erzeugt daraus
  eine persönliche `.env` mit zufälligem Passwort und erhält vorhandene Dateien.
- `.env` gehört nicht ins Git-Repository. Alte Django-Einträge aus der früheren
  Einrichtung werden nicht mehr verwendet und können aus der persönlichen `.env` entfernt werden.
- PostgreSQL speichert Daten in einem Docker-Volume und veröffentlicht keinen Host-Port.
- `docker compose down` erhält Daten. **`docker compose down --volumes` löscht die
  lokale Datenbank** und ist nur für einen bewusst gewünschten Reset gedacht.
- Änderungen am Passwort in `.env` ändern kein Passwort einer bereits angelegten Datenbank.
- Ein Git-Push überträgt Code, keine Datenbankinhalte. Ein Docker-Volume ist kein Backup.

## Automatische Prüfungen und Stand

GitHub Actions baut die Container, prüft Formatierung und Paketabhängigkeiten und führt
`check_environment.py` gegen PostgreSQL aus. Es gibt noch keine Anwendungstests, weil
noch keine Anwendung existiert.

Auf dem Einrichtungsrechner ist Docker nicht verfügbar: Der Containerstart und der
Codespaces-Aufbau müssen daher auf GitHub beziehungsweise in Codespaces geprüft werden.
Lokale Syntax-/Formatprüfungen ersetzen diese Prüfung nicht.

## Zusammenarbeit

Änderungen in eigenen Branches entwickeln und über Pull Requests zusammenführen.
Neue Pakete mit festen Versionen in den Requirements ergänzen und das Image neu bauen.
Das Django-Projekt und seine Datenbankanbindung richten wir erst nach der Teamabsprache ein.
Hosting, Deployment und eine gemeinsame Testwebsite sind noch nicht Bestandteil dieses Repositories.

## Bei Problemen

- `docker info` und `docker compose version` müssen lokal funktionieren; gegebenenfalls Docker Desktop starten.
- Bei Startfehlern `docker compose logs` ansehen und Internetzugang prüfen.
- Bei unveränderten Paketversionen trotz bearbeiteter Requirements das Image neu bauen.
- Wenn VS Code keine Dateien schreiben kann, Benutzer-/Dateirechte des eingebundenen Ordners prüfen.
