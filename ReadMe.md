# INDUSTRIAL-LIMS: Laboratory Information Management System

A comprehensive, modular, and scalable LIMS built with Flask, designed for industrial laboratories with a focus on flexibility and data integrity.

## 🚀 Features

- **Modular Architecture**: Each functional area is a self-contained module
- **RESTful API**: Fully documented API for system integration
- **User Authentication & Authorization**: Role-based access control
- **Data Validation**: Robust input validation and sanitization
- **File Management**: Secure file upload and storage
- **Reporting**: Built-in reporting and data export capabilities
- **Audit Logging**: Comprehensive activity tracking
- **Responsive UI**: Mobile-friendly interface

## 🏗 Project Structure

```
INDUSTRIAL-LIMS/
│
├── app/                            # Main application package
│   ├── __init__.py                 # Application factory
│   ├── config.py                   # Configuration settings
│   ├── extensions.py               # Flask extensions
│   │
│   ├── api/                      # API endpoints
│   │   └── v1/                     # API version 1
│   │       ├── __init__.py
│   │       ├── auth.py             # Authentication endpoints
│   │       ├── samples.py          # Sample management endpoints
│   │       └── ...
│   │
│   ├── auth/                     # Authentication package
│   │   ├── __init__.py
│   │   ├── models.py              # User and role models
│   │   ├── routes.py              # Auth routes
│   │   └── services.py            # Auth business logic
│   │
│   ├── models/                   # Database models
│   │   ├── __init__.py
│   │   ├── core/                  # Core models
│   │   └── modules/               # Module-specific models
│   │
│   ├── controllers/             # Request handlers
│   │   ├── __init__.py
│   │   ├── core/                  # Core controllers
│   │   └── modules/               # Module controllers
│   │
│   ├── services/                # Business logic
│   │   ├── __init__.py
│   │   ├── core/                  # Core services
│   │   └── modules/               # Module services
│   │
│   ├── static/                  # Static files
│   │   ├── css/                   # Stylesheets
│   │   ├── js/                    # JavaScript files
│   │   ├── images/                # Image assets
│   │   └── fonts/                 # Web fonts
│   │
│   └── templates/              # Jinja2 templates
│       ├── base/                  # Base templates
│       ├── auth/                  # Auth templates
│       ├── modules/               # Module templates
│       └── errors/                # Error pages
│
├── modules/                        # Application modules
│   │
│   ├── task-manager/               # MODULO GESTIONE TASK E TIMESHEET (App 1 & 1.1)
│   │   ├── tasks/                  # Sottomodulo gestione attività principali
│   │   │   ├── html/
│   │   │   │   ├── task-calendar.html        # Visualizzazione calendario settimanale
│   │   │   │   ├── task-grid.html            # Visualizzazione griglia attività
│   │   │   │   ├── task-create-edit.html     # Creazione/Modifica task
│   │   │   │   ├── task-detail.html          # Dettaglio task (con sotto-task)
│   │   │   │   └── task-filters.html         # UI per filtri (priorità, ricorrenza, status)
│   │   │   ├── js/
│   │   │   │   ├── task-scheduler.js         # Logica calendario e griglia
│   │   │   │   ├── task-crud.js              # Operazioni CRUD per task
│   │   │   │   ├── task-filter-manager.js    # Gestione filtri
│   │   │   │   ├── subtask-handler.js        # Gestione sotto-task dinamiche
│   │   │   │   └── task-template-linker.js   # Collegamento a Checklist
│   │   │   ├── css/
│   │   │   │   ├── task-main.css
│   │   │   │   └── task-calendar.css
│   │   │   ├── python/
│   │   │   │   ├── task_processor.py         # Logica task, status, priorità, ricorrenze
│   │   │   │   ├── task_model.py             # Modello DB per task e sotto-task
│   │   │   │   └── task_export.py            # Export CSV task filtrate
│   │   │   ├── data/                         # Dati specifici task (e.g., definizioni task standard)
│   │   │   ├── config/                       # Configurazione task (e.g., tipi priorità, status)
│   │   │   └── docs/                         # Documentazione modulo task
│   │   │       ├── README.txt
│   │   │       └── README.html
│   │   │
│   │   ├── timesheets/             # Sottomodulo gestione timesheet collaboratori
│   │   │   ├── html/
│   │   │   │   ├── timesheet-user.html       # Compilazione timesheet settimanale per utente
│   │   │   │   ├── timesheet-admin-view.html # Visualizzazione e validazione timesheet (admin)
│   │   │   │   └── timesheet-report.html     # Reportistica timesheet
│   │   │   ├── js/
│   │   │   │   ├── timesheet-entry.js        # Logica inserimento ore e collegamento task
│   │   │   │   ├── timesheet-validator.js    # Validazione e gestione alerts sovrapposizioni
│   │   │   │   └── timesheet-export.js       # Esportazione timesheet (CSV, formati UE)
│   │   │   ├── css/
│   │   │   │   └── timesheet-main.css
│   │   │   ├── python/
│   │   │   │   ├── timesheet_processor.py    # Logica timesheet, collegamento a task
│   │   │   │   ├── timesheet_model.py        # Modello DB per timesheet
│   │   │   │   └── timesheet_report_generator.py # Generazione reportistica avanzata
│   │   │   ├── data/                         # Dati specifici timesheet
│   │   │   ├── config/                       # Configurazione timesheet (e.g., tag attività)
│   │   │   └── docs/                         # Documentazione modulo timesheet
│   │   │       ├── README.txt
│   │   │       └── README.html
│   │   │
│   │   ├── uploads/                # Directory upload generale del modulo (e.g., allegati task)
│   │   └── exports/                # Directory export generale del modulo
│   │
│   ├── checklist-manager/          # MODULO GESTIONE CHECKLIST (App 2)
│   │   ├── html/
│   │   │   ├── checklist-compiler.html       # Compilazione checklist da template
│   │   │   ├── checklist-template-creator.html # Creazione/Modifica template (admin)
│   │   │   ├── checklist-history.html        # Archivio checklist compilate
│   │   │   ├── checklist-detail.html         # Visualizzazione checklist compilata
│   │   │   └── checklist-list.html           # Lista template/checklist
│   │   ├── js/
│   │   │   ├── checklist-form-handler.js     # Gestione compilazione form checklist
│   │   │   ├── template-builder.js           # UI per creazione template (admin)
│   │   │   ├── checklist-linker.js           # Collegamento a Task, RStatus, DataAnalysis
│   │   │   └── checklist-validator.js        # Validazione input checklist
│   │   ├── css/
│   │   │   ├── checklist-main.css
│   │   │   └── checklist-forms.css
│   │   ├── python/
│   │   │   ├── checklist_processor.py        # Logica checklist, precompilazione da Task/DB
│   │   │   ├── template_manager.py         # Gestione CRUD template (admin)
│   │   │   ├── checklist_model.py            # Modello DB per checklist e template
│   │   │   └── checklist_data_extractor.py   # Estrazione dati per DataAnalysis (massa, vol, etc.)
│   │   ├── uploads/                # Allegati a checklist
│   │   ├── exports/                # Export checklist compilate (PDF, CSV)
│   │   ├── data/                   # JSON dei template, BatchExpRecord archive
│   │   │   ├── templates/
│   │   │   │   ├── methanol-synthesis-checklist.json
│   │   │   │   ├── ammonia-synthesis-checklist.json
│   │   │   │   └── ammonia-cracking-checklist.json
│   │   │   └── archives/
│   │   │       └── BatchExpRecord.sqlite
│   │   ├── config/                 # Configurazione tipi di campo per template
│   │   └── docs/                   # Documentazione modulo checklist
│   │       ├── README.txt
│   │       └── README.html
│   │
│   ├── reactor-event-logger/     # MODULO REGISTRAZIONE EVENTI REATTORE (App 3 - RStatus)
│   │   ├── html/
│   │   │   ├── reactor-event-input.html    # Interfaccia per input vocale/manuale eventi
│   │   │   ├── reactor-event-log.html      # Visualizzazione log eventi per reattore/campagna
│   │   │   └── reactor-selection.html      # Selezione reattore per log/visualizzazione
│   │   ├── js/
│   │   │   ├── voice-input-handler.js      # Gestione API riconoscimento vocale
│   │   │   ├── manual-event-entry.js       # Logica form inserimento manuale
│   │   │   └── event-display.js            # Visualizzazione e filtro log eventi
│   │   ├── css/
│   │   │   └── reactor-event-main.css
│   │   ├── python/
│   │   │   ├── reactor_event_processor.py  # Processa e salva eventi, collega a campagne DataAnalysis
│   │   │   ├── reactor_event_model.py      # Modello DB per eventi reattore
│   │   │   └── speech_to_text_service.py   # Servizio (stub) per conversione audio->testo
│   │   ├── uploads/                # Eventuali file audio registrati (se non processati real-time)
│   │   ├── exports/                # Export log eventi
│   │   ├── data/                   # Log eventi strutturati
│   │   ├── config/                 # Configurazione tipi di evento, reattori
│   │   └── docs/                   # Documentazione modulo RStatus
│   │       ├── README.txt
│   │       └── README.html
│   │
│   ├── experimental-data-analysis/ # MODULO ANALISI DATI SPERIMENTALI (App 4)
│   │   ├── base/                   # Funzionalità base comuni a tutte le analisi
│   │   │   ├── html/
│   │   │   │   ├── campaign-list-base.html
│   │   │   │   ├── campaign-create-edit-base.html # Form base creazione/modifica campagna
│   │   │   │   ├── data-upload-base.html     # UI base per upload files (LV, GC)
│   │   │   │   └── graph-view-base.html      # Contenitore base per grafici Plotly
│   │   │   ├── js/
│   │   │   │   ├── campaign-manager-base.js  # CRUD base campagne
│   │   │   │   ├── data-uploader-base.js     # Logica base upload e validazione file
│   │   │   │   ├── plotly-wrapper.js       # Wrapper per Plotly per grafici standard
│   │   │   │   └── data-interpolator.js    # Logica interpolazione dati GC/LV
│   │   │   ├── python/
│   │   │   │   ├── base_data_processor.py    # Logica base processamento dati, step generation
│   │   │   │   ├── base_campaign_model.py    # Modello DB base per campagne
│   │   │   │   └── base_file_parser.py       # Parser base per LV, GC
│   │   │
│   │   ├── methanol-synthesis/     # Sottomodulo Analisi Sintesi Metanolo
│   │   │   ├── html/                   # Estende/usa html/base
│   │   │   │   └── methanol-dashboard.html
│   │   │   ├── js/                     # Estende/usa js/base
│   │   │   │   └── methanol-charts.js      # Grafici specifici metanolo
│   │   │   ├── css/
│   │   │   │   └── methanol-analysis.css
│   │   │   ├── python/                 # Estende/usa python/base
│   │   │   │   ├── methanol_data_processor.py # Calcoli specifici MeOH
│   │   │   │   └── methanol_campaign_model.py
│   │   │   ├── uploads/                # Dati LV/GC per MeOH
│   │   │   ├── exports/                # Report, CSV processati per MeOH
│   │   │   ├── data/                   # Cache o dati intermedi specifici MeOH
│   │   │   ├── config/                 # Parametri specifici analisi MeOH
│   │   │   └── docs/
│   │   │       ├── README.txt
│   │   │       └── README.html
│   │   │
│   │   ├── ammonia-synthesis/      # Sottomodulo Analisi Sintesi Ammoniaca
│   │   │   ├── html/
│   │   │   │   └── ammonia-syn-dashboard.html
│   │   │   ├── js/
│   │   │   │   └── ammonia-syn-charts.js   # Grafici: Overall, Produttività, Conversione, Selettività, Bilancio Massa, Profilo T, H2/N2
│   │   │   ├── css/
│   │   │   │   └── ammonia-syn-analysis.css
│   │   │   ├── python/
│   │   │   │   ├── ammonia_syn_data_processor.py # Calcoli NH3 (prod., conv., sel., etc.)
│   │   │   │   └── ammonia_syn_campaign_model.py
│   │   │   ├── uploads/
│   │   │   ├── exports/
│   │   │   ├── data/
│   │   │   ├── config/                 # Costanti NH3 (densità, PM), parametri calcolo
│   │   │   └── docs/
│   │   │       ├── README.txt
│   │   │       └── README.html
│   │   │
│   │   ├── ammonia-cracking/       # Sottomodulo Analisi Cracking Ammoniaca
│   │   │   ├── html/
│   │   │   │   └── ammonia-crack-dashboard.html # "Coming Soon" se non implementato
│   │   │   ├── js/
│   │   │   │   └── ammonia-crack-charts.js
│   │   │   ├── css/
│   │   │   │   └── ammonia-crack-analysis.css
│   │   │   ├── python/
│   │   │   │   ├── ammonia_crack_data_processor.py
│   │   │   │   └── ammonia_crack_campaign_model.py
│   │   │   ├── uploads/
│   │   │   ├── exports/
│   │   │   ├── data/
│   │   │   ├── config/
│   │   │   └── docs/
│   │   │       ├── README.txt
│   │   │       └── README.html
│   │   │
│   │   ├── autoclave-tests/        # Sottomodulo Analisi Test Autoclave
│   │   │   ├── html/
│   │   │   │   └── autoclave-dashboard.html # "Coming Soon" o struttura base
│   │   │   ├── js/
│   │   │   ├── css/
│   │   │   ├── python/
│   │   │   │   ├── autoclave_data_processor.py
│   │   │   │   └── autoclave_campaign_model.py
│   │   │   ├── uploads/
│   │   │   ├── exports/
│   │   │   ├── data/
│   │   │   ├── config/
│   │   │   └── docs/
│   │   │       ├── README.txt
│   │   │       └── README.html
│   │   │
│   │   └── fertilizer-tests/       # Sottomodulo Analisi Test Fertilizzanti (Serra)
│   │       ├── html/
│   │       │   └── fertilizer-dashboard.html # "Coming Soon" o struttura base
│   │       ├── js/
│   │       ├── css/
│   │       ├── python/
│   │       │   ├── fertilizer_data_processor.py
│   │       │   └── fertilizer_campaign_model.py
│   │       ├── uploads/
│   │       ├── exports/
│   │       ├── data/
│   │       ├── config/
│   │       └── docs/
│   │           ├── README.txt
│   │           └── README.html
│   │
│   ├── gas-cylinder-manager/       # MODULO GESTIONE BOMBOLE GAS (App 5)
│   │   ├── html/
│   │   │   ├── cylinder-scan-input.html    # UI per OCR da fotocamera
│   │   │   ├── cylinder-manual-entry.html  # Form inserimento manuale dati bombola
│   │   │   ├── cylinder-stock.html         # Visualizzazione e filtro stock bombole
│   │   │   ├── cylinder-return.html        # UI per restituzione bombole
│   │   │   └── cylinder-log-view.html      # Visualizzazione log entrate/uscite
│   │   ├── js/
│   │   │   ├── ocr-scanner-cylinder.js     # Logica OCR per codici bombola (separatore 7563)
│   │   │   ├── cylinder-stock-manager.js   # Gestione UI stock
│   │   │   ├── cylinder-crud.js            # Operazioni CRUD bombole
│   │   │   └── cylinder-log-export.js      # Export log
│   │   ├── css/
│   │   │   └── cylinder-main.css
│   │   ├── python/
│   │   │   ├── gas_cylinder_processor.py   # Logica OCR, validazione, gestione stock, log
│   │   │   ├── gas_cylinder_model.py       # Modello DB bombole e log
│   │   │   └── ocr_service_cylinder.py     # Servizio OCR (integrazione)
│   │   ├── uploads/                # Immagini bombole per OCR (se non dirette da stream)
│   │   ├── exports/                # Export CSV stock, log
│   │   ├── data/                   # Database bombole, storico pressioni
│   │   ├── config/                 # Tipi gas, stati fisici, parametri OCR
│   │   └── docs/                   # Documentazione modulo bombole
│   │       ├── README.txt
│   │       └── README.html
│   │
│   ├── lab-coat-manager/           # MODULO GESTIONE CAMICI (App 6)
│   │   ├── html/
│   │   │   ├── labcoat-scan-input.html     # UI per OCR etichette camici
│   │   │   ├── labcoat-manual-entry.html   # Form inserimento manuale
│   │   │   ├── labcoat-stock.html          # Visualizzazione stock camici
│   │   │   ├── labcoat-laundry.html        # Gestione invio/ritorno lavaggio
│   │   │   └── labcoat-log-view.html       # Log movimenti camici
│   │   ├── js/
│   │   │   ├── ocr-scanner-labcoat.js      # Logica OCR per etichette camici
│   │   │   ├── labcoat-stock-manager.js    # Gestione UI stock
│   │   │   ├── labcoat-status.js           # Gestione stato sporco/pulito
│   │   │   └── labcoat-crud.js
│   │   ├── css/
│   │   │   └── labcoat-main.css
│   │   ├── python/
│   │   │   ├── lab_coat_processor.py       # Logica OCR, gestione stock, stato pulizia
│   │   │   ├── lab_coat_model.py           # Modello DB camici e log
│   │   │   └── ocr_service_labcoat.py      # Servizio OCR
│   │   ├── uploads/                # Immagini etichette per OCR
│   │   ├── exports/                # Export CSV stock, storico lavaggi
│   │   ├── data/                   # Database camici
│   │   ├── config/                 # Taglie, stati pulizia
│   │   └── docs/                   # Documentazione modulo camici
│   │       ├── README.txt
│   │       └── README.html
│   │
│   ├── laboratory-inventory/       # MODULO INVENTARIO LABORATORIO (App 7)
│   │   ├── html/
│   │   │   ├── inventory-dashboard.html    # Panoramica inventario
│   │   │   ├── item-create-edit.html       # Aggiunta/Modifica articolo
│   │   │   ├── item-list-filter.html       # Lista articoli con filtri (codice, stanza, etc.)
│   │   │   ├── item-detail.html            # Dettaglio articolo con allegati
│   │   │   └── attach-document.html        # UI per allegare bolle (immagini, PDF)
│   │   ├── js/
│   │   │   ├── inventory-manager.js        # Logica CRUD e filtri UI
│   │   │   ├── item-location-tracker.js    # Gestione collocazione spaziale
│   │   │   └── document-attacher.js        # Logica upload allegati
│   │   ├── css/
│   │   │   └── inventory-main.css
│   │   ├── python/
│   │   │   ├── lab_inventory_processor.py  # Logica gestione stock, filtri, allegati
│   │   │   ├── lab_inventory_model.py      # Modello DB inventario
│   │   │   └── file_handler_inventory.py   # Gestione salvataggio allegati
│   │   ├── uploads/                # Bolle di consegna, schede tecniche
│   │   │   ├── delivery-notes/
│   │   │   └── item-specs/
│   │   ├── exports/                # Export CSV inventario filtrato
│   │   ├── data/                   # Database inventario
│   │   ├── config/                 # Categorie articoli, fornitori, formati codici locazione
│   │   └── docs/                   # Documentazione modulo inventario
│   │       ├── README.txt
│   │       └── README.html
│   │
│   ├── patent-manager/             # MODULO GESTIONE BREVETTI (Nuovo)
│   │   ├── html/
│   │   │   ├── patent-list.html            # Lista brevetti con filtri
│   │   │   ├── patent-create-edit.html     # Creazione/Modifica brevetto
│   │   │   ├── patent-detail.html          # Dettaglio brevetto (dati, scadenze, documenti)
│   │   │   └── patent-document-upload.html # Upload documenti relativi al brevetto
│   │   ├── js/
│   │   │   ├── patent-crud.js              # Operazioni CRUD brevetti
│   │   │   ├── patent-document-handler.js  # Gestione UI upload documenti
│   │   │   └── patent-reminder.js          # Logica per notifiche scadenze (UI)
│   │   ├── css/
│   │   │   └── patent-main.css
│   │   ├── python/
│   │   │   ├── patent_processor.py         # Logica gestione dati brevetti, scadenze
│   │   │   ├── patent_model.py             # Modello DB brevetti e documenti associati
│   │   │   └── patent_notification_service.py # Servizio per gestione notifiche (e.g., email)
│   │   ├── uploads/                # Documenti brevettuali (PDF, etc.)
│   │   ├── exports/                # Export lista brevetti, report scadenze
│   │   ├── data/                   # Database brevetti
│   │   ├── config/                 # Tipi di brevetto, stati, tipi scadenze
│   │   └── docs/                   # Documentazione modulo brevetti
│   │       ├── README.txt
│   │       └── README.html
│   │
│   └── samples/                    # MODULO CAMPIONI (Mantenuto da ReadMe.md originale, se applicabile e non sovrapposto)
│       ├── html/                   # Interfacce HTML del modulo
│       │   ├── samples-list.html             # Lista campioni (READ)
│       │   ├── sample-create.html            # Creazione campione (CREATE)
│       │   ├── sample-edit.html              # Modifica campione (UPDATE)
│       │   ├── sample-detail.html            # Dettaglio campione (READ)
│       │   ├── sample-delete-confirm.html    # Conferma eliminazione (DELETE)
│       │   ├── sample-registry.html          # Registro campioni
│       │   ├── sample-tracking.html          # Tracciamento campioni
│       │   ├── sample-chain-custody.html     # Catena di custodia
│       │   └── sample-upload.html            # Upload dati campioni
│       │
│       ├── js/                     # JavaScript del modulo
│       │   ├── samples-crud.js               # Operazioni CRUD
│       │   ├── sample-manager.js             # Gestione campioni
│       │   ├── sample-tracking.js            # Tracciamento
│       │   ├── chain-custody.js              # Catena custodia
│       │   ├── sample-upload.js              # Gestione upload
│       │   └── sample-export.js              # Gestione export
│       │
│       ├── css/                    # Stili del modulo
│       │   ├── samples-main.css              # Stili principali
│       │   ├── sample-tracking.css           # Stili tracciamento
│       │   ├── sample-registry.css           # Stili registro
│       │   └── chain-custody.css             # Stili catena custodia
│       │
│       ├── python/                 # Processori Python del modulo
│       │   ├── sample_processor.py           # Processore principale
│       │   ├── sample_crud.py                # Operazioni CRUD
│       │   ├── sample_tracker.py             # Tracciamento campioni
│       │   ├── custody_manager.py            # Gestione custodia
│       │   ├── sample_uploader.py            # Gestione upload
│       │   └── sample_exporter.py            # Export dati
│       │
│       ├── uploads/                # Directory upload del modulo
│       │   ├── sample-data/                  # Dati campioni
│       │   ├── analysis-results/             # Risultati analisi
│       │   ├── certificates/                 # Certificati
│       │   └── temp/                         # File temporanei
│       │
│       ├── exports/                # Directory export del modulo
│       │   ├── csv/                          # Export CSV
│       │   │   ├── samples-registry.csv
│       │   │   ├── sample-tracking.csv
│       │   │   ├── chain-custody.csv
│       │   │   └── analysis-results.csv
│       │   ├── reports/                      # Report generati
│       │   └── archive/                      # Archivio export
│       │
│       ├── data/                   # Dati del modulo
│       │   ├── active-samples/               # Campioni attivi
│       │   ├── analyzed-samples/             # Campioni analizzati
│       │   ├── archived-samples/             # Campioni archiviati
│       │   └── templates/                    # Template campioni
│       │
│       ├── config/                 # Configurazioni del modulo
│       │   ├── sample-types.json
│       │   ├── analysis-methods.json
│       │   └── custody-protocols.json
│       └── docs/                   # Documentazione modulo campioni
│           ├── README.txt
│           └── README.html
│
├── tests/                      # Test suite
│   ├── unit/                     # Unit tests
│   ├── integration/              # Integration tests
│   └── fixtures/                 # Test fixtures
│
├── migrations/                  # Database migrations
├── instance/                    # Instance-specific files
├── requirements/                # Dependencies
│   ├── base.txt                # Core requirements
│   ├── dev.txt                 # Development requirements
│   └── prod.txt                # Production requirements
├── docs/                       # Documentation (generale, oltre a quella nei moduli)
│   ├── api/                    # API documentation
│   ├── development/            # Development guides
│   └── deployment/             # Deployment guides
├── .env.example               # Example environment variables
├── .gitignore                 # Git ignore file
├── config.py                  # Configuration settings (potrebbe essere deprecato se tutto è in app/config.py)
└── wsgi.py                    # WSGI entry point
```

## 🛠 Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/industrial-lims.git
   cd industrial-lims
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements/dev.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Initialize the database**
   ```bash
   flask db upgrade
   ```

6. **Run the development server**
   ```bash
   flask run
   ```

## 📚 Documentation

- General documentation is in the main `/docs` folder.
- Each module inside `/modules` also contains its own `docs/` subfolder with:
    - `README.txt`: Detailed operational guide for the module.
    - `README.html`: User-friendly HTML version of the guide, linkable from an "Info" button within each app page.
- [API Documentation](/docs/api/README.md)
- [Development Guide](/docs/development/README.md)
- [Deployment Guide](/docs/deployment/README.md)

## 🤝 Contributing

Contributions are welcome! Please see our [contributing guidelines](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For support or questions, please contact support@example.com

## Architettura Generale (Legacy - To be removed or updated)
The section below shows a previous architectural overview. It should be updated or removed to reflect the new module structure defined under "🏗 Project Structure" which is based on `Architect.md`.

```
INDUSTRIAL-LIMS/
│
├── core/                           # Core del sistema
│   ├── framework/                  # Framework base
│   │   ├── html/
│   │   │   ├── base.html          # Template base
│   │   │   ├── navigation.html    # Navigazione principale
│   │   │   └── error.html         # Pagina errori
│   │   ├── js/
│   │   │   ├── core.js            # Funzioni core JavaScript
│   │   │   ├── crud-base.js       # CRUD operations base
│   │   │   ├── upload-handler.js  # Handler per upload
│   │   │   └── export-handler.js  # Handler per export
│   │   ├── css/
│   │   │   ├── main.css           # Stili principali
│   │   │   ├── forms.css          # Stili per form
│   │   │   ├── tables.css         # Stili per tabelle
│   │   │   └── components.css     # Componenti riutilizzabili
│   │   └── python/
│   │       ├── base_processor.py  # Processore dati base
│   │       ├── crud_operations.py # Operazioni CRUD base
│   │       ├── file_handler.py    # Gestione file e upload
│   │       └── csv_exporter.py    # Export CSV base
│   │
│   ├── api/                        # API centrali
│   │   ├── endpoints/
│   │   │   ├── crud_api.py
│   │   │   ├── upload_api.py
│   │   │   └── export_api.py
│   │   └── middleware/
│   │       ├── auth_middleware.py
│   │       └── validation_middleware.py
│   │
│   └── database/                   # Database centrale
│       ├── models/
│       ├── migrations/
│       └── seeds/
│
├── modules/                        # Moduli dell'applicazione (VECCHIA STRUTTURA - DA RIMUOVERE/SOSTITUIRE)
│   │
│   ├── campaigns/                  # MODULO CAMPAGNE (OBSOLETO)
│   │   ├── ... (contenuto precedente campaigns)
│   │
│   ├── setups/                     # MODULO IMPIANTI (OBSOLETO)
│   │   ├── ... (contenuto precedente setups)
│   │
│   ├── processes/                  # MODULO PROCESSI (OBSOLETO)
│   │   ├── ... (contenuto precedente processes)
│   │
│   ├── samples/                    # MODULO CAMPIONI (MANTENUTO E AGGIORNATO SOPRA)
│   │   ├── ... (contenuto precedente samples - verificare se già coperto dalla nuova struttura)
│   │
│   ├── cylinders/                  # MODULO GESTIONE BOMBOLE (OBSOLETO)
│   │   ├── ... (contenuto precedente cylinders)
│   │
│   ├── inventory/                  # MODULO INVENTARIO LABORATORIO (OBSOLETO)
│   │   ├── ... (contenuto precedente inventory)
│   │
│   ├── gas-consumption/            # MODULO CONSUMI GAS (OBSOLETO, integrare se necessario)
│   │   ├── ... (contenuto precedente gas-consumption)
│   │
│   ├── checklists/                 # MODULO CHECKLIST (OBSOLETO)
│   │   ├── ... (contenuto precedente checklists)
│   │
│   └── analysis-management/        # MODULO GESTIONE ANALISI (OBSOLETO, integrare se necessario)
│       ├── ... (contenuto precedente analysis-management)
│
├── backup/                         # SISTEMA BACKUP
│   ├── system/                     # Backup sistema
│   │   ├── core-backup/                      # Backup core
│   │   ├── modules-backup/                   # Backup moduli
│   │   ├── database-backup/                  # Backup database
│   │   └── config-backup/                    # Backup configurazioni
│   │
│   ├── data/                       # Backup dati
│   │   ├── json-backups/                     # Backup JSON
│   │   │   ├── daily/                        # Backup giornalieri
│   │   │   ├── weekly/                       # Backup settimanali
│   │   │   ├── monthly/                      # Backup mensili
│   │   │   └── yearly/                       # Backup annuali
│   │   │
│   │   ├── uploads-backup/                   # Backup upload
│   │   └── exports-backup/                   # Backup export
│   │
│   ├── scripts/                    # Script backup
│   │   ├── backup_scheduler.py               # Schedulatore backup
│   │   ├── json_backup_manager.py            # Gestore backup JSON
│   │   ├── incremental_backup.py             # Backup incrementale
│   │   ├── restore_manager.py                # Gestore ripristino
│   │   └── backup_validator.py               # Validatore backup
│   │
│   ├── logs/                       # Log backup
│   │   ├── backup-operations.log             # Log operazioni
│   │   ├── restore-operations.log            # Log ripristini
│   │   └── backup-errors.log                 # Log errori
│   │
│   └── config/                     # Configurazioni backup
│       ├── backup-schedule.json              # Programmazione backup
│       ├── retention-policy.json             # Politiche retention
│       └── restore-points.json               # Punti di ripristino
│
├── database/                       # DATABASE E CONVERSIONE
│   ├── sqlite/                     # Database SQLite
│   │   ├── production.db                     # Database produzione
│   │   ├── staging.db                        # Database staging
│   │   └── backup.db                         # Database backup
│   │
│   ├── migrations/                 # Migrazioni database
│   │   ├── json-to-sqlite/                   # Conversione JSON->SQLite
│   │   ├── schema-updates/                   # Aggiornamenti schema
│   │   └── data-migrations/                  # Migrazioni dati
│   │
│   ├── converters/                 # Convertitori dati
│   │   ├── json_to_sqlite.py                 # Convertitore JSON->SQLite
│   │   ├── data_validator.py                 # Validatore dati
│   │   ├── schema_mapper.py                  # Mappatore schema
│   │   └── batch_converter.py                # Convertitore batch
│   │
│   └── schema/                     # Schema database
│       ├── tables.sql                        # Definizioni tabelle
│       ├── indexes.sql                       # Indici
│       ├── views.sql                         # Viste
│       └── triggers.sql                      # Trigger
│
├── config/                         # CONFIGURAZIONI GLOBALI
│   ├── system-config.json                    # Configurazione sistema
│   ├── modules-config.json                   # Configurazione moduli
│   ├── backup-config.json                    # Configurazione backup
│   ├── database-config.json                  # Configurazione database
│   └── security-config.json                  # Configurazione sicurezza
│
├── logs/                           # LOG SISTEMA
│   ├── system/                               # Log sistema
│   ├── modules/                              # Log moduli
│   ├── backup/                               # Log backup
│   ├── database/                             # Log database
│   └── security/                             # Log sicurezza
│
└── docs/                          # DOCUMENTAZIONE (generale, vedi anche sotto "📚 Documentation")
    ├── api/                                  # Documentazione API
    ├── modules/                              # Documentazione moduli (obsoleto se ogni modulo ha la sua)
    ├── installation/                         # Guide installazione
    ├── user-guides/                          # Guide utente
    └── troubleshooting/                      # Risoluzione problemi
```

## Esempi di JSON Generati dai Processori Python

### Esempio: Bombole (gas_cylinder_processor.py - nel modulo gas-cylinder-manager)
```json
{
  "cylinder_id": "CYL-2025-001",
  "gas_type": "nitrogen",
  "pressure": 200,
  "status": "in_storage",
  "location": "A1-001",
  "delivery_date": "2025-01-15",
  "last_inspection": "2025-01-10",
  "supplier": "Air Liquide",
  "ocr_scan_data": {
    "raw_text": "...",
    "extracted_codes": ["7563-XXXXXXXXXXXXXX"]
  },
}
```

### Esempio: Inventario (lab_inventory_processor.py - nel modulo laboratory-inventory)
```json
{
  "item_id": "INV-2025-045",
  "category": "consumables",
  "name": "Syringe 10mL",
  "current_stock": 25,
  "minimum_stock": 10,
  "unit_cost": 2.50,
  "supplier": "VWR",
  "expiration_date": "2026-12-31",
  "storage_location_code": "MAG-B-0-2",
  "room": "Main Lab",
  "zone": "Bench B",
  "shelf": "0",
  "box": "2",
  "entry_date": "2025-01-10",
  "last_modified_date": "2025-01-20",
  "attached_document_path": "uploads/delivery-notes/DN_INV-2025-045.pdf"
}
```

### Sistema di Backup JSON
Il sistema implementa:
- **Backup automatici**: Schedulati giornalmente, settimanalmente, mensilmente
- **Backup incrementiali**: Solo modifiche dall'ultimo backup
- **Versioning**: Mantenimento versioni multiple dei JSON
- **Compressione**: Backup compressi per ottimizzare spazio
- **Validazione**: Controllo integrità dei backup
- **Ripristino selettivo**: Possibilità di ripristinare singoli moduli o file

### Conversione JSON → SQLite
Il sistema prevede:
- **Schema mapping**: Conversione automatica struttura JSON in tabelle SQL (per i database centralizzati)
- **Data validation**: Validazione dati durante conversione
- **Batch processing**: Elaborazione a lotti per grandi volumi
- **Rollback capability**: Possibilità di annullare conversioni
- **Incremental sync**: Sincronizzazione incrementale JSON-DB (dove applicabile, per mantenere coerenza tra eventuali file JSON di data e i DB SQLite)
