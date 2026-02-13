# CHANGELOG

13.02.2026:

* ENH: Initiale Version der Metadata Viewer Extension für CKAN 2.11.2
* ENH: Erweiterte Metadatenanzeige für Datasets und Ressourcen
* ENH: Template-Überschreibungen für Dataset- und Ressourcen-Ansichten (`read.html`, `read_base.html`, `resource_read.html`)
* ENH: Erweiterte Zusatzinformationen (`additional_info.html`)
* ENH: Übersichtliche Darstellung der Metadaten in Rubriken:
  - **Metadaten**: Dataset-URL, Autor, Maintainer, Lizenz
  - **RDF/JSON-LD Export**: Download-Links für Metadaten (bei installiertem DCAT-Plugin)
* ENH: Internationalisierung (i18n) mit deutscher Übersetzung
* ENH: Asset-Management mit CSS und JavaScript
* ENH: Implementierte CKAN-Interfaces:
  - `IConfigurer` - Konfiguration von Templates, Assets und öffentlichen Verzeichnissen
  - `ITranslation` - Unterstützung für mehrsprachige Inhalte
* TECH: Kompatibel mit CKAN Version 2.11.2
* TECH: Python 3 Unterstützung
* TECH: Babel-Integration für Übersetzungs-Extraktion
