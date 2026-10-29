# Fork Frankfurt

## Funktionen
- Restaurant-Entdeckung aus OpenStreetMap per Overpass API
- Persönliche Want-to-go-Liste, Bewertungen von 1 bis 5 und Notizen
- Filter nach Küche, Suche, Karte, manuelle Restaurants und JSON-Backup

## Datenquelle und Grenzen
Der Restaurant-Katalog wird live vom öffentlichen Overpass-Server geladen. Keine erfundenen Bewertungen, Öffnungszeiten oder Qualitätsversprechen. Die API kann gelegentlich überlastet sein; eigene Einträge und zuletzt geladene Orte funktionieren weiter. Ein Restaurant hat nur dann einen Kartenmarker, wenn Koordinaten vorliegen.

## Installation über GitHub Pages

1. ZIP entpacken. **Für jede App ein eigenes GitHub-Repository** anlegen (öffentlich, wenn GitHub Pages kostenlos genutzt werden soll).
2. Den **Inhalt des entpackten App-Ordners** in das Repo-Root hochladen oder via Git pushen. Die versteckte `.github`-Struktur muss mit übernommen werden, falls vorhanden.
3. Unter **Repository → Settings → Pages** einstellen: für Market Pulse und Frankfurt Radar **Source: GitHub Actions**; bei den vier anderen **Deploy from a branch**, Branch `main`, `/(root)`.
4. Nach dem Deployment die bereitgestellte Pages-URL auf dem iPhone in Safari öffnen und unter Teilen **Zum Home-Bildschirm** wählen.
5. Falls Updates zunächst nicht sichtbar sind: Seite neu laden und ggf. den Homescreen-Link schließen und neu öffnen. Die Service-Worker-Datei nutzt bei Internetzugang eine Network-first-Strategie.

### Lokal ausprobieren

Im jeweiligen Ordner ausführen:

```sh
python3 -m http.server 8000
```

Dann `http://localhost:8000` im Browser öffnen. Für RSS-Apps muss zuvor das jeweilige `scripts/fetch_*.py` ausgeführt werden, um Online-Schlagzeilen abzurufen.

### Datenschutz

Persönliche Daten werden im lokalen Browser-Speicher gespeichert (bei Bildern IndexedDB). Es gibt keine Anmeldung und keine Synchronisierung. Der Quellcode eines öffentlichen GitHub-Repositorys ist öffentlich, **deine lokal eingegebenen Daten jedoch nicht im Repo enthalten**. Drittanbieter-Dienste für Karten, Wetter und RSS können übliche Verbindungsdaten erhalten. Import/Export von persönlichen Daten ist in den App-Einstellungen verfügbar (Bilder gesondert beachten).

### Technische Details

- Reines HTML/CSS/JavaScript, keine Build-Pipeline, keine bezahlten Dienste oder verpflichtenden API-Keys
- Responsiv für iPhone und Desktop, Hell-/Dunkelmodus, PWA-Manifest und Service Worker
- API-/Netzwerkzugriff erforderlich für aktuelle Feeds und externe Karten/Wetter
- **Prototypen:** vor produktivem Einsatz oder Veröffentlichung mit echten Daten bitte weitere Tests durchführen
