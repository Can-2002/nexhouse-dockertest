# Nexhouse – so richtest du deinen Arbeitsplatz ein

Diese Anleitung richtet sich auch an Personen ohne Programmiererfahrung.
Du musst noch keinen Code schreiben und keine Programmiersprache kennen.

**Ziel:** Am Ende hast du dieselben vorbereiteten Werkzeuge wie die anderen im Team
und kannst mit einem Befehl prüfen, ob die Einrichtung funktioniert.

**Wichtig:** Unsere Immobiliensoftware wurde noch nicht begonnen. Hier werden nur
Werkzeuge bereitgestellt. Es gibt deshalb noch keine Website, keinen Login und
keine Oberfläche zur Objektverwaltung. Das ist beabsichtigt.

## 1. Wähle einen Weg – du brauchst nur einen

| Weg | Was brauchst du? | Für wen passt das? |
| --- | --- | --- |
| **A: Im Browser mit GitHub Codespaces** | GitHub-Konto, Internet und Zugriff auf unser Repository | Einfachster Einstieg zum Ausprobieren, ohne lokale Installation |
| **B: Auf dem eigenen Windows-Rechner** | Git, Docker Desktop und optional VS Code | Wenn du lokal arbeiten möchtest |
| **C: Auf einem Mac oder Linux-Rechner** | Git und Docker mit Compose | Lokale Alternative zu Windows |

Für den ersten Versuch ohne IT-Erfahrung empfehlen wir **Weg A**.
Alle Wege verwenden dieselbe vorbereitete Umgebung. Du musst sie nicht nacheinander durchgehen.

## 2. Einige Begriffe vorab

| Begriff | Einfach erklärt |
| --- | --- |
| GitHub | Die Website, auf der unser gemeinsamer Code liegt. |
| Repository / Repo | Unser Projektordner auf GitHub, einschließlich der Änderungshistorie. |
| Git | Das Werkzeug, mit dem Änderungen am Code gespeichert und ausgetauscht werden. |
| Codespace | Dein eigener Arbeitsrechner bei GitHub, den du im Browser bedienst. |
| VS Code | Ein Programm zum Öffnen und Bearbeiten von Projektdateien. |
| Terminal / PowerShell | Ein Fenster, in das du Befehle eingibst, statt auf Schaltflächen zu klicken. |
| Docker / Container | Docker startet eine vorbereitete Arbeitsumgebung mit den vereinbarten Werkzeugen. Diese Umgebung nennt man Container. |
| Python / Django | Die Programmiersprache und ein Werkzeug für die spätere Webanwendung. |
| PostgreSQL | Die Datenbank, in der später Daten gespeichert werden können. |

**Befehle eingeben:** Kopiere nur den Text aus dem grauen Codekasten, füge ihn in das
angegebene Terminal ein und drücke die Eingabetaste (**Enter**). Die Bezeichnungen
wie `powershell` oder `sh` und die Umrandung gehören nicht zum Befehl.
Warte nach jedem Befehl, bis wieder eine Eingabe möglich ist. Terminaltexte wie
`PS C:\...>` oder `app@...$` musst du nicht mit eingeben.

## Weg A: Im Browser mit Codespaces

### A1. GitHub öffnen und Zugriff prüfen

1. Öffne [github.com](https://github.com/) im Browser und melde dich an (**Sign in**).
   Falls du kein Konto hast, lege über **Sign up** eines an und bestätige deine E-Mail-Adresse.
2. Öffne [unser Repository nexhouse-dockertest](https://github.com/Can-2002/nexhouse-dockertest).
3. Du solltest Dateien wie `README.md`, `Dockerfile` und `requirements.txt` sehen.
   Bei einer Fehlermeldung oder „404“ prüfe dein angemeldetes Konto und bitte Can um Zugriff.
   Eine Einladung zum Repository musst du zuerst annehmen.

### A2. Deinen Arbeitsplatz erstellen

1. Prüfe auf der Repository-Seite, dass der ausgewählte Branch **main** heißt.
2. Klicke auf **Code**, dann auf den Reiter **Codespaces**.
3. Lies den Hinweis zur Abrechnung. Codespaces kann je nach Konto, Freikontingent und
   Nutzung Kosten verursachen. Bei Unklarheit vor dem Start mit dem Team absprechen.
4. Klicke auf **Create codespace on main** beziehungsweise die entsprechende Schaltfläche
   zum Erstellen eines Codespaces.
5. Warte, bis der Editor geöffnet und die Einrichtung abgeschlossen ist. Beim ersten
   Aufbau müssen Pakete heruntergeladen werden; das kann mehrere Minuten dauern.

**Erwartetes Ergebnis:** Links siehst du unsere Projektdateien. Der Codespace darf nicht
nur im Wiederherstellungsmodus („Recovery Mode“) geöffnet sein. In diesem Fall ist
der Aufbau fehlgeschlagen; siehe den Abschnitt „Wenn etwas nicht funktioniert“.

Offizielle Hilfe: [Codespace erstellen](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository).

### A3. Prüfen, ob alles funktioniert

1. Öffne im Editor das Menü **Terminal → New Terminal** beziehungsweise **Neues Terminal**.
   Bei schmalem Fenster findest du die Menüs eventuell hinter dem Symbol mit drei Strichen.
2. Unten erscheint ein Eingabefenster. Klicke hinein und führe diesen Befehl aus:

   ```sh
   python scripts/check_environment.py
   ```

3. Du solltest Versionsangaben für Python, Django und PostgreSQL sehen. Am Ende steht:

   ```text
   Entwicklungsumgebung bereit. Datenbankverbindung erfolgreich.
   ```

**Dann hat die Prüfung funktioniert.** Der Befehl legt weder ein Django-Projekt noch
Tabellen an. Einen Browser-Port oder eine Website musst du nicht öffnen.

### A4. Optional: Prüfen, ob du Dateien speichern kannst

1. Klicke links im Dateibereich auf „Neue Datei“ und nenne sie `mein-test.txt`.
2. Schreibe `Hallo Nexhouse` hinein und speichere mit **Strg+S** (Mac: **Cmd+S**).
3. Öffne die Datei erneut. Wenn der Text noch vorhanden ist, kannst du Dateien bearbeiten.
4. Lösche anschließend nur diese Testdatei wieder über das Kontextmenü.

### A5. Pause machen und später weiterarbeiten

Öffne [deine Codespaces](https://github.com/codespaces). Über das Menü mit den drei
Punkten beim passenden Codespace kannst du ihn stoppen (**Stop codespace**).
Nur den Browser-Tab zu schließen beendet die laufende Sitzung nicht unbedingt sofort.
Später kannst du denselben Codespace dort wieder öffnen. Auch gestoppter Speicher
kann auf dein Kontingent angerechnet werden.

**Stoppen und Löschen sind verschieden:** Löschen entfernt den Codespace samt dortigen
ungesicherten Dateien und lokaler Datenbank. Eigene Arbeit vorher mit dem Team sichern.

## Weg B: Auf dem eigenen Windows-Rechner

### B1. Die benötigten Programme herunterladen

Du installierst die Programme einmal. **Python, Django und PostgreSQL brauchst du
nicht einzeln herunterzuladen:** Das erledigt anschließend Docker.

| Programm | Offizieller Download | Aufgabe |
| --- | --- | --- |
| Git | [Git für Windows](https://git-scm.com/downloads/win) | Holt unsere Dateien von GitHub |
| Docker Desktop | [Docker für Windows](https://docs.docker.com/desktop/setup/install/windows-install/) | Startet die gemeinsame Umgebung |
| VS Code (optional zum ersten Test) | [VS Code herunterladen](https://code.visualstudio.com/download) | Bearbeitet später den Code |

Lade die Installationsdatei passend zu deinem Windows-Rechner herunter. Bei Unsicherheit
über „x64/AMD64“ oder „ARM64“ schaue unter **Windows-Einstellungen → System → Info →
Systemtyp** nach oder frage im Team nach.

### B2. Git installieren

1. Öffne die heruntergeladene Git-Installationsdatei im Ordner **Downloads**.
2. Folge dem Installationsassistenten. Für diesen Einstieg sind die vorgeschlagenen
   Standardeinstellungen ausreichend.
3. Schließe nach der Installation bereits geöffnete Terminalfenster und öffne sie später neu.

### B3. Docker Desktop installieren und starten

1. Öffne die heruntergeladene Docker-Installationsdatei und folge dem Assistenten.
2. Wenn eine Auswahl angeboten wird, verwende **WSL 2**. Das ist die Linux-Unterstützung
   von Windows, die Docker für unsere Umgebung nutzt.
3. Führe einen angeforderten Neustart durch. Öffne danach **Docker Desktop** über das Startmenü.
4. Warte, bis Docker meldet, dass die Engine läuft. Docker muss während der lokalen Arbeit laufen.

Wenn Docker meldet, dass WSL fehlt oder aktualisiert werden muss, folge dem angezeigten
Einrichtungslink. Die [offizielle Windows-Anleitung](https://docs.docker.com/desktop/setup/install/windows-install/)
führt die Voraussetzungen und WSL-Schritte auf. Bei fehlenden Administratorrechten oder
Virtualisierungsfehlern hole dir Hilfe im Team; ändere nicht auf Verdacht BIOS-Einstellungen.

### B4. PowerShell öffnen und Installationen prüfen

1. Öffne das Windows-Startmenü und tippe **PowerShell**.
2. Öffne **Windows PowerShell**. Für die folgenden Projektbefehle brauchst du normalerweise
   kein Fenster mit Administratorrechten.
3. Gib diese Befehle einzeln ein:

   ```powershell
   git --version
   ```

   Erwartet wird eine Ausgabe, die mit `git version` beginnt.

   ```powershell
   docker compose version
   ```

   Erwartet wird eine Versionsangabe von Docker Compose.

   ```powershell
   docker info
   ```

   Erwartet wird eine längere Liste mit Docker-Informationen, keine Meldung, dass der
   Docker-Server nicht erreichbar ist. Die genaue Versionsnummer muss nicht bei allen gleich sein.

### B5. Projekt herunterladen

**Falls du das Repository bereits auf dem Rechner hast:** Überspringe den Download.
Öffne den vorhandenen Ordner im Windows-Explorer, klicke oben in die Adressleiste,
tippe `powershell` und drücke Enter. Fahre mit B6 fort.

Für einen neuen Download führen wir dich in einen eigenen Ordner unter deinem Windows-Benutzer:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\Projekte" | Out-Null
```

Das erstellt den Ordner `Projekte`, falls er noch nicht existiert.

```powershell
Set-Location "$env:USERPROFILE\Projekte"
```

Das wechselt in diesen Ordner.

```powershell
git clone https://github.com/Can-2002/nexhouse-dockertest.git
```

Das lädt das Repository in den neuen Unterordner `nexhouse-dockertest`. Falls ein
GitHub-Anmeldedialog erscheint, melde dich mit deinem berechtigten Konto an.

```powershell
Set-Location nexhouse-dockertest
```

Du befindest dich jetzt im Projektordner. Mit `Get-ChildItem` kannst du prüfen, ob unter
anderem `README.md` und `start.ps1` angezeigt werden. Lade das Projekt nicht noch einmal
in einen bereits vorhandenen Projektordner herunter.

### B6. Umgebung starten

Führe im Projektordner aus:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\start.ps1
```

Die Option `ExecutionPolicy Bypass` erlaubt dieses Skript für den gestarteten Prozess;
sie ändert keine dauerhafte Windows-Einstellung.

Das Skript erledigt automatisch:

- persönliche Datenbankeinstellungen erzeugen, sofern sie noch fehlen;
- die Container herunterladen beziehungsweise bauen und die Python-Pakete installieren;
- PostgreSQL und den Arbeitscontainer starten;
- Python, Django und die Datenbankverbindung prüfen.

Viele Textzeilen während des Downloads sind normal. Warte auf die Erfolgsmeldung:

```text
Entwicklungsumgebung bereit. Datenbankverbindung erfolgreich.
```

Danach erscheint noch ein Hinweis zum Öffnen des Container-Terminals.
**Die Einrichtung ist damit geprüft. Es öffnet sich keine Website.**

### B7. Optional: Den Ordner in VS Code öffnen

1. Installiere VS Code über den oben verlinkten Download und starte es.
2. Wähle **File → Open Folder / Datei → Ordner öffnen** und deinen Ordner
   `nexhouse-dockertest`. Bei einem bereits vorhandenen Klon kann er anders heißen.
3. Bestätige eine Vertrauensabfrage nur für den bewusst geöffneten Team-Projektordner.
4. Öffne links **Extensions / Erweiterungen** (Symbol mit den kleinen Quadraten).
5. Suche nach **Dev Containers**, Herausgeber **Microsoft**, Kennung
   `ms-vscode-remote.remote-containers`, und klicke auf **Install**.
6. Drücke **Strg+Umschalt+P**. Das öffnet die Befehlssuche.
7. Suche nach **Dev Containers: Reopen in Container** und wähle den Eintrag aus.
8. Warte auf den Aufbau. Öffne dann **Terminal → New Terminal** und führe aus:

   ```sh
   python scripts/check_environment.py
   ```

Dieses Terminal läuft jetzt im Container. Es verwendet die dort installierten Werkzeuge.
Die Dateien liegen weiterhin in deinem lokalen Projektordner.
Weitere Hilfe: [Offizielle Dev-Containers-Anleitung](https://code.visualstudio.com/docs/devcontainers/tutorial).

## Weg C: macOS oder Linux

Der Browser-Weg A funktioniert auch hier. Für die lokale Installation:

1. Installiere [Git](https://git-scm.com/downloads) und Docker mit Compose.
   Für Mac gibt es [Docker Desktop für Mac](https://docs.docker.com/desktop/setup/install/mac-install/),
   für Linux die [Docker-Installationsübersicht](https://docs.docker.com/engine/install/).
   Unter Linux unterscheiden sich Installation und Benutzerrechte je nach Distribution;
   gehe die Einrichtung bei fehlender Erfahrung gemeinsam mit jemandem aus dem Team durch.
2. Starte Docker. Öffne unter macOS die App **Terminal**, unter Linux das Terminal deiner Oberfläche.
3. Prüfe einzeln `git --version`, `docker compose version` und `docker info`.
4. Lade das Projekt herunter und starte es (jede Zeile einzeln ausführen):

   ```sh
   mkdir -p ~/Projekte
   cd ~/Projekte
   git clone https://github.com/Can-2002/nexhouse-dockertest.git
   cd nexhouse-dockertest
   sh start.sh
   ```

   Bei einem bestehenden Klon nur in dessen Ordner wechseln und `sh start.sh` ausführen.
5. Warte auf die gleiche Erfolgsmeldung wie unter B6. Für VS Code folge B7;
   auf einem Mac öffnet **Cmd+Umschalt+P** die Befehlssuche.

## Beim nächsten Mal

**Codespaces:** Deinen bestehenden Arbeitsplatz unter [github.com/codespaces](https://github.com/codespaces)
öffnen. Für eine erneute Prüfung im dortigen Terminal `python scripts/check_environment.py` eingeben.

**Lokal:** Docker Desktop starten, Projektordner öffnen und das Startskript erneut
aufrufen. Vorhandene Einstellungen und Daten bleiben erhalten. Wer VS Code im Container
nutzt, kann stattdessen den Projektordner wieder im Dev Container öffnen.

**Lokal beenden:** Im normalen Terminal auf deinem Rechner im Projektordner eingeben:

```sh
docker compose down
```

Das stoppt die Container und erhält die Datenbank. Im VS-Code-Container-Terminal ist
dieser Docker-Befehl nicht vorgesehen; öffne dafür ein separates lokales Terminal.

## Wenn etwas nicht funktioniert

| Meldung / Problem | Was du tun kannst |
| --- | --- |
| GitHub zeigt „404“ oder verweigert Zugriff | Angemeldetes Konto prüfen, Einladung annehmen und Can um Zugriff bitten. |
| Codespaces fehlt oder verlangt Zahlungsangaben | Mit dem Team Kontoberechtigung und Abrechnung klären; alternativ lokal arbeiten. |
| Codespace meldet „Recovery Mode“ | Der Aufbau ist fehlgeschlagen. Das Einrichtungsprotokoll öffnen und die Fehlermeldung mit dem Team prüfen. |
| `git` oder `docker` wird nicht erkannt | Installation prüfen. Terminal und gegebenenfalls VS Code schließen und neu öffnen. |
| Docker-Server nicht erreichbar | Docker Desktop starten, Bereitschaft abwarten und `docker info` erneut ausführen. |
| `start.ps1` oder `scripts/check_environment.py` nicht gefunden | Du bist wahrscheinlich im falschen Ordner. Öffne den Ordner, der die README und diese Dateien enthält. |
| `No module named django` | Du verwendest vermutlich Python auf deinem Rechner. Im Dev Container arbeiten oder lokal `docker compose exec dev python scripts/check_environment.py` ausführen. |
| `destination path ... already exists` | Das Repository wurde schon heruntergeladen. Den vorhandenen Ordner öffnen, nicht noch einmal hinein klonen. |
| Datenbankverbindung fehlgeschlagen | Lokal im Projektordner `docker compose logs db` ausführen und die Ausgabe mit dem Team prüfen. |
| „Permission denied“ beim Speichern | Auf Linux kann die Benutzerzuordnung im Container abweichen. Das Team sollte die Dateirechte und Container-Benutzer-ID prüfen. |
| Keine Website erreichbar | Das ist aktuell richtig: Es gibt nur die Entwicklungsumgebung, noch keine Anwendung. |

Wenn du Hilfe brauchst, schicke dem Team den **genauen Befehl**, den **Wortlaut der
Fehlermeldung** und ob du **Codespaces, Windows, Mac oder Linux** verwendest.
Keine Inhalte der `.env` oder Passwörter mitschicken. Bei Downloads können längere
Wartezeiten vorkommen; bei einer Fehlermeldung nicht wahllos weitere Befehle ausprobieren.

## Was du vorerst nicht ändern oder löschen solltest

- `.env` enthält deine lokalen Datenbankzugangsdaten. Sie wird automatisch erstellt
  und nicht zu GitHub hochgeladen. Das Datenbankpasswort vorerst unverändert lassen.
- Die Datenbank liegt in einem Docker-Volume, einem getrennten Speicherbereich.
  `docker compose down` erhält diesen Speicher; der Zusatz `--volumes` würde ihn löschen.
- Ein gelöschter Codespace verliert seine dort gespeicherten Daten. GitHub speichert
  nicht automatisch jede Dateiänderung oder den Inhalt deiner Datenbank.
- `.venv` und `.ruff_cache` sind für unseren Docker-Start nicht nötig. Falls von früheren
  lokalen Prüfungen vorhanden, können sie bei Nichtgebrauch entfernt werden.

## Für Teammitglieder mit Entwicklungserfahrung

### Welche Befehle gehören in welches Terminal?

| Aufgabe | Lokales Terminal im Projektordner | Terminal in Codespaces / Dev Container |
| --- | --- | --- |
| Umgebung prüfen | `docker compose exec dev python scripts/check_environment.py` | `python scripts/check_environment.py` |
| Code prüfen | `docker compose exec dev ruff check .` | `ruff check .` |
| Code formatieren | `docker compose exec dev ruff format .` | `ruff format .` |
| Pakete prüfen | `docker compose exec dev python -m pip check` | `python -m pip check` |

Nach Requirements-Änderungen lokal `docker compose up --build -d --wait` ausführen;
im Dev Container beziehungsweise Codespace **Rebuild Container** verwenden.
Versionsänderungen gemeinsam abstimmen. Es sind Python 3.12.14, Django 5.2.18,
PostgreSQL 17.11 und Ruff 0.17.2 festgelegt.

Die Container-Umgebung ist noch nicht mit Django-Einstellungen verbunden, weil es
kein Django-Projekt gibt. Den Projektaufbau legen wir gemeinsam fest. Später werden
Änderungen in eigenen Branches entwickelt und über Pull Requests zusammengeführt.
Hosting und eine gemeinsame Testwebsite gehören noch nicht zu dieser Einrichtung.

### Vorhandene Codespaces aus dem alten Anwendungsgerüst

Der Compose-Dienst wurde von `web` auf `dev` umbenannt. Eigene Änderungen zuerst sichern,
dann für diesen Wechsel am einfachsten einen neuen Codespace auf `main` erstellen.
Nicht ungesicherte Arbeit durch das Löschen des alten Codespaces verlieren.

### Bisheriger Prüfstand

GitHub Actions ist so eingerichtet, dass es Container baut, Codeformatierung und
Paketabhängigkeiten prüft und die PostgreSQL-Verbindung testet. Das ist keine Prüfung
einer fertigen Anwendung. Den Status des jeweiligen Commits findest du im Repository
unter **Actions**; ein grüner Lauf bestätigt die dort ausgeführten Prüfungen.

Auf dem Einrichtungsrechner war Docker nicht verfügbar. Ein erfolgreicher lokaler
Syntaxcheck ist deshalb kein Nachweis, dass Docker und Codespaces auf jedem Rechner
funktionieren. Geht die Anleitung einmal auf euren tatsächlichen Geräten durch,
einschließlich des Speichertests. Damit prüfen wir die Einrichtung für unser Team.
