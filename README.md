# Nexhouse – gemeinsame Django-Entwicklungsumgebung

Dieses Repository ist das technische Grundgerüst für unsere Immobilienverwaltung.
Es enthält eine Startseite, eine Datenbank-Verbindungsprüfung und die Django-Verwaltung.
Objektverwaltung, Buchhaltung, Tickets und Mandantentrennung sind noch nicht implementiert.

Eine Übersicht der Dateien und Ordner steht in
[Erklärung der verschiedenen Module](Erklärung%20der%20verschiedenen%20Module.md).

## Schnellstart zum Ausprobieren (Windows)

1. [Git für Windows](https://git-scm.com/downloads/win) und
   [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/) installieren.
   Bei Docker die Einrichtung mit WSL 2 abschließen und gegebenenfalls neu starten.
2. Docker Desktop öffnen und warten, bis die Engine läuft. Linux-Container verwenden.
3. PowerShell öffnen und das Repository herunterladen:

   ```powershell
   git clone https://github.com/Can-2002/nexhouse-dockertest.git
   cd nexhouse-dockertest
   powershell -NoProfile -ExecutionPolicy Bypass -File .\start.ps1
   ```

   Wer das Repository bereits hat, öffnet PowerShell im vorhandenen Projektordner
   und führt nur den letzten Befehl aus. Nicht ein zweites Repository hinein klonen.
   Die ExecutionPolicy-Option gilt nur für diesen Prozess und verändert keine
   dauerhafte Systemeinstellung.

4. Nach der Erfolgsmeldung [http://localhost:8000](http://localhost:8000) öffnen.
5. Für den Zugang zur Verwaltung einmal einen eigenen Administrator anlegen:

   ```powershell
   docker compose exec web python manage.py createsuperuser
   ```

   Benutzername, optionale E-Mail und Passwort eingeben. Beim Passwort werden keine
   Zeichen angezeigt. Danach unter [http://localhost:8000/admin/](http://localhost:8000/admin/)
   anmelden. Es gibt kein gemeinsames Standardpasswort.

Python und PostgreSQL müssen nicht auf dem Rechner installiert werden. Docker lädt
die benötigten Images und installiert die Python-Pakete beim ersten Start; das dauert
einige Minuten und benötigt Internetzugang. Spätere Starts sind schneller.

## macOS und Linux

Git und Docker mit Compose v2 installieren, Docker starten, Repository klonen und
im Projektordner ausführen:

```sh
sh start.sh
docker compose exec web python manage.py createsuperuser
```

## Entwickeln mit VS Code auf dem eigenen Rechner

1. [VS Code](https://code.visualstudio.com/) und die Erweiterung
   **Dev Containers** (`ms-vscode-remote.remote-containers`) installieren.
2. Den geklonten Projektordner in VS Code öffnen.
3. `Strg+Umschalt+P` → **Dev Containers: Reopen in Container** auswählen.
4. Die Einrichtung erzeugt bei Bedarf `.env`, baut die Umgebung und startet Django
   sowie PostgreSQL. Der erste Aufbau benötigt Internetzugang.
5. Im VS-Code-Terminal läuft man bereits im Anwendungscontainer. Dort Befehle ohne
   `docker compose exec web` verwenden:

   ```sh
   python manage.py createsuperuser
   python manage.py test
   ruff check .
   ruff format .
   ```

Der Quellcode bleibt im Projektordner und wird in den Container eingebunden.
Django lädt Python-Änderungen automatisch neu. Das gilt auch, wenn man die Umgebung
über das Startskript startet und den Ordner normal in VS Code bearbeitet.

## Entwickeln mit GitHub Codespaces

Voraussetzung: Die Dateien dieses Grundgerüsts wurden in das GitHub-Repository gepusht.

1. Im Repository auf **Code → Codespaces → Create codespace** klicken und den
   gewünschten Branch wählen.
2. Codespaces verwendet `.devcontainer/devcontainer.json` und baut dieselbe
   Django-/PostgreSQL-Grundlage wie lokal. Auf dem eigenen Rechner ist Docker dafür
   nicht erforderlich. Codespaces-Verfügbarkeit und Kosten hängen vom GitHub-Konto ab.
3. Nach dem Aufbau im Bereich **Ports** den Port **8000** im Browser öffnen.
   Den Port privat lassen. Die konkrete Codespace-Adresse wird für Django erlaubt.
4. Im Terminal `python manage.py createsuperuser` ausführen und anschließend den
   Pfad `/admin/` öffnen.

Jeder Codespace hat seine eigene Entwicklungsdatenbank. Codespaces sind keine
gemeinsame Testwebsite. Beim Löschen des Codespaces gehen seine lokalen Daten verloren.
Nach Änderungen an Dockerfile oder Requirements den Container neu bauen.

## Häufige Befehle auf dem eigenen Rechner

Alle Befehle im Projektordner ausführen:

| Aufgabe | Befehl |
| --- | --- |
| Start nach der Einrichtung | `docker compose up -d --wait` |
| Images nach Requirements-Änderung neu bauen | `docker compose up --build -d --wait` |
| Stoppen, Daten behalten | `docker compose down` |
| Protokolle ansehen | `docker compose logs -f web` |
| Laufende Dienste anzeigen | `docker compose ps` |
| Tests mit PostgreSQL | `docker compose exec web python manage.py test` |
| Django-Konfiguration prüfen | `docker compose exec web python manage.py check` |
| Code prüfen | `docker compose exec web ruff check .` |
| Code formatieren | `docker compose exec web ruff format .` |
| Migrationen nach Modelländerung erstellen | `docker compose exec web python manage.py makemigrations` |
| Migrationen anwenden | `docker compose exec web python manage.py migrate` |

Im Dev-Container-Terminal die Befehle jeweils ohne `docker compose exec web` ausführen.
Django wendet vorhandene Migrationen zusätzlich bei jedem Containerstart an.
Neue Migrationsdateien immer zusammen mit den Modelländerungen committen.

## Wie die Umgebung aufgebaut ist

- **Python 3.12.14**, **Django 5.2.18 LTS**, **PostgreSQL 17.11**, **Ruff 0.17.2**.
- `Dockerfile`: Entwicklungsimage inklusive Git, Python-Paketen und Ruff;
  Anwendung läuft als Benutzer `app`, nicht als root.
- `compose.yaml`: Anwendung und Datenbank mit Bereitschaftsprüfungen.
- `compose.setup.yaml` / `scripts/setup.py`: Erstellt `.env` mit zufälligen lokalen
  Schlüsseln. Vorhandene `.env` bleibt unverändert.
- `requirements.txt`: Anwendungsabhängigkeiten mit festen Versionen;
  `requirements-dev.txt`: zusätzliche Entwicklungswerkzeuge.
- `config/`: Django-Einstellungen und URLs; `accounts/`: eigenes Benutzermodell.
- `core/`: Startseite, `/health/` inklusive Datenbankprüfung und Grundlagentests.
- `.editorconfig`, `.gitattributes`, `pyproject.toml`: gemeinsame Formatierungsregeln.
- `.github/workflows/ci.yml`: Baut auf GitHub die Container, prüft Code, Migrationen,
  Tests mit PostgreSQL und den HTTP-Zugang bei Pushes und Pull Requests.

Versionen werden bewusst gemeinsam aktualisiert und mit CI geprüft. Feste Versions-Tags
sind keine unveränderlichen Image-Digests; Basisimages können unter demselben Tag
neu gebaut werden. Betriebssystem-/Architekturunterschiede können weiterhin bestehen.

## Einstellungen und Daten

`.env.example` beschreibt die Einstellungen. `.env` enthält persönliche Werte und
gehört nicht ins Git-Repository. Die Dateien werden durch `.gitignore` und
`.dockerignore` ausgeschlossen. Django erhält Einstellungen über die Container-Umgebung.

Die Datenbank liegt im Docker-Volume `postgres_data`. Ein normaler Neustart, ein
Image-Neubau oder `docker compose down` löscht ihre Daten nicht. **`docker compose down
--volumes` löscht dagegen die lokale Datenbank.** Diesen Befehl nur für einen bewusst
gewünschten vollständigen Reset verwenden. Ein Volume ersetzt kein Backup.

Das PostgreSQL-Passwort wird beim ersten Anlegen des Datenbank-Volumes gesetzt.
Eine spätere Änderung in `.env` ändert kein Passwort in einer bestehenden Datenbank.

## Zusammenarbeit zu dritt

1. Vor Arbeitsbeginn Änderungen des Teams holen (`git pull`, bei sauberem Arbeitsstand).
2. Für die Aufgabe einen Branch anlegen, beispielsweise `git switch -c feature/objekte`.
3. Entwickeln, formatieren und testen.
4. Änderungen einschließlich Migrationen committen und den Branch pushen.
5. Pull Request erstellen und von einer anderen Person prüfen lassen.

Der GitHub-Workflow liefert Prüfungen, aber eine verpflichtende Freigabe und verpflichtende
CI-Prüfungen müssen zusätzlich in den GitHub-Branch-Regeln eingerichtet werden.
Ein Push überträgt Code, keine lokalen Datenbankinhalte.

Für gemeinsame Vorführungen wird später eine separate Testwebsite mit eigener
Testdatenbank eingerichtet. Produktivbetrieb bekommt eine getrennte Datenbank.
Dieses Repository enthält noch kein Hosting und keinen automatischen Deployment-Ablauf.

## Probleme beim Start

- **Docker nicht gefunden / keine Verbindung:** Docker Desktop starten und Terminal
  neu öffnen. `docker info` und `docker compose version` müssen funktionieren.
- **Port 8000 belegt:** In `.env` `WEB_PORT=8001` setzen, erneut starten und
  `http://localhost:8001` öffnen.
- **Fehler beim Download:** Internetzugang, Proxy und GitHub-Zugriff prüfen, dann erneut starten.
- **Migration oder Anmeldung scheitert:** `docker compose logs web db` ansehen.
  Nicht einfach das Datenbank-Volume löschen.
- **CSRF-Fehler bei anderer Testadresse:** Exakte Adresse inklusive `https://` in
  `DJANGO_CSRF_TRUSTED_ORIGINS`, Hostname ohne Protokoll in `DJANGO_ALLOWED_HOSTS`
  eintragen und Container neu erstellen. Keine pauschalen Wildcards verwenden.
- **Geänderte Requirements wirken nicht:** Image neu bauen; im Dev Container
  **Dev Containers: Rebuild Container** verwenden.

## Entwicklungsumgebung, keine Produktionsinstallation

Der Django-Entwicklungsserver und `DEBUG=true` sind für Entwicklung gedacht.
Vor einem Kundenbetrieb fehlen unter anderem Produktionsserver, HTTPS-Konfiguration,
Backups, Monitoring und die fachlichen Berechtigungs-/Mandantenregeln. Nur fiktive
Testdaten verwenden. Die Anwendung ist lokal an `127.0.0.1` gebunden; PostgreSQL
veröffentlicht keinen Port auf dem Rechner.

## Validierung dieses Grundgerüsts

Die lokalen Prüfungen sind in `docs/VALIDATION.md` dokumentiert. Die maßgebliche
Container-/PostgreSQL-Prüfung übernimmt der GitHub-Workflow beim ersten Push.

Offizielle Grundlagen: [Django](https://docs.djangoproject.com/en/5.2/),
[Dev Containers](https://code.visualstudio.com/docs/devcontainers/create-dev-container),
[Codespaces](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/adding-a-dev-container-configuration/introduction-to-dev-containers).
