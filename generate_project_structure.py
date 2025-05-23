#!/usr/bin/env python3
"""
This script generates the full directory and file structure for the INDUSTRIAL-LIMS project based on Architect.md and ReadMe.md examples.
"""

import os

# Define the project structure as a nested dictionary.
# Keys with dictionary values represent directories, whereas keys with string values represent files with their content.

structure = {
    "INDUSTRIAL-LIMS": {
        "app": {
            "__init__.py": "# Application factory initialization\n",
            "config.py": "# Configuration settings\n",
            "extensions.py": "# Flask extensions initialization\n"
        },
        "modules": {
            "task-manager": {
                "tasks": {
                    "html": {
                        "task-calendar.html": "<!-- Task Calendar HTML -->\n",
                        "task-grid.html": "<!-- Task Grid HTML -->\n",
                        "task-create-edit.html": "<!-- Task Create/Edit HTML -->\n",
                        "task-detail.html": "<!-- Task Detail HTML -->\n",
                        "task-filters.html": "<!-- Task Filters HTML -->\n"
                    },
                    "js": {
                        "task-scheduler.js": "// Task Scheduler JS\n",
                        "task-crud.js": "// Task CRUD JS\n",
                        "task-filter-manager.js": "// Task Filter Manager JS\n",
                        "subtask-handler.js": "// Subtask Handler JS\n",
                        "task-template-linker.js": "// Task Template Linker JS\n"
                    },
                    "css": {
                        "task-main.css": "/* Task Main CSS */\n",
                        "task-calendar.css": "/* Task Calendar CSS */\n"
                    },
                    "python": {
                        "task_processor.py": "# Task processor logic\n",
                        "task_model.py": "# Task model definition\n",
                        "task_export.py": "# Task export utilities\n"
                    },
                    "data": {},
                    "config": {},
                    "docs": {
                        "README.txt": "Task Manager Tasks Documentation\n",
                        "README.html": "<html><body><h1>Task Manager Tasks</h1></body></html>\n"
                    }
                },
                "timesheets": {
                    "html": {
                        "timesheet-user.html": "<!-- Timesheet User HTML -->\n",
                        "timesheet-admin-view.html": "<!-- Timesheet Admin View HTML -->\n",
                        "timesheet-report.html": "<!-- Timesheet Report HTML -->\n"
                    },
                    "js": {
                        "timesheet-entry.js": "// Timesheet Entry JS\n",
                        "timesheet-validator.js": "// Timesheet Validator JS\n",
                        "timesheet-export.js": "// Timesheet Export JS\n"
                    },
                    "css": {
                        "timesheet-main.css": "/* Timesheet Main CSS */\n"
                    },
                    "python": {
                        "timesheet_processor.py": "# Timesheet processing logic\n",
                        "timesheet_model.py": "# Timesheet DB model\n",
                        "timesheet_report_generator.py": "# Report generator for timesheets\n"
                    },
                    "data": {},
                    "config": {},
                    "docs": {
                        "README.txt": "Timesheet Documentation\n",
                        "README.html": "<html><body><h1>Timesheet Docs</h1></body></html>\n"
                    }
                },
                "uploads": {},
                "exports": {}
            },
            "checklist-manager": {
                "html": {
                    "checklist-compiler.html": "<!-- Checklist Compiler HTML -->\n",
                    "checklist-template-creator.html": "<!-- Checklist Template Creator HTML -->\n",
                    "checklist-history.html": "<!-- Checklist History HTML -->\n",
                    "checklist-detail.html": "<!-- Checklist Detail HTML -->\n",
                    "checklist-list.html": "<!-- Checklist List HTML -->\n"
                },
                "js": {
                    "checklist-form-handler.js": "// Checklist Form Handler JS\n",
                    "template-builder.js": "// Template Builder JS\n",
                    "checklist-linker.js": "// Checklist Linker JS\n",
                    "checklist-validator.js": "// Checklist Validator JS\n"
                },
                "css": {
                    "checklist-main.css": "/* Checklist Main CSS */\n",
                    "checklist-forms.css": "/* Checklist Forms CSS */\n"
                },
                "python": {
                    "checklist_processor.py": "# Checklist processor logic\n",
                    "template_manager.py": "# Template manager for checklists\n",
                    "checklist_model.py": "# Checklist DB model\n",
                    "checklist_data_extractor.py": "# Extractor for checklist data\n"
                },
                "uploads": {},
                "exports": {},
                "data": { "templates": {} },
                "config": {},
                "docs": {
                    "README.txt": "Checklist Manager Documentation\n",
                    "README.html": "<html><body><h1>Checklist Manager</h1></body></html>\n"
                }
            },
            "reactor-event-logger": {
                "html": {
                    "reactor-event-input.html": "<!-- Reactor Event Input HTML -->\n",
                    "reactor-event-log.html": "<!-- Reactor Event Log HTML -->\n",
                    "reactor-selection.html": "<!-- Reactor Selection HTML -->\n"
                },
                "js": {
                    "voice-input-handler.js": "// Voice Input Handler JS\n",
                    "manual-event-entry.js": "// Manual Event Entry JS\n",
                    "event-display.js": "// Event Display JS\n"
                },
                "css": {
                    "reactor-event-main.css": "/* Reactor Event Main CSS */\n"
                },
                "python": {
                    "reactor_event_processor.py": "# Reactor event processor\n",
                    "reactor_event_model.py": "# Reactor event model\n",
                    "speech_to_text_service.py": "# Speech to text service stub\n"
                },
                "uploads": {},
                "exports": {},
                "data": {},
                "config": {},
                "docs": {
                    "README.txt": "Reactor Event Logger Documentation\n",
                    "README.html": "<html><body><h1>Reactor Event Logger</h1></body></html>\n"
                }
            },
            "experimental-data-analysis": {
                "base": {
                    "html": {
                        "campaign-list-base.html": "<!-- Campaign List Base HTML -->\n",
                        "campaign-create-edit-base.html": "<!-- Campaign Create/Edit Base HTML -->\n",
                        "data-upload-base.html": "<!-- Data Upload Base HTML -->\n",
                        "graph-view-base.html": "<!-- Graph View Base HTML -->\n"
                    },
                    "js": {
                        "campaign-manager-base.js": "// Campaign Manager Base JS\n",
                        "data-uploader-base.js": "// Data Uploader Base JS\n",
                        "plotly-wrapper.js": "// Plotly Wrapper JS\n",
                        "data-interpolator.js": "// Data Interpolator JS\n"
                    },
                    "python": {
                        "base_data_processor.py": "# Base data processor\n",
                        "base_campaign_model.py": "# Base campaign model\n",
                        "base_file_parser.py": "# Base file parser\n"
                    }
                },
                "methanol-synthesis": {
                    "html": {
                        "methanol-dashboard.html": "<!-- Methanol Dashboard HTML -->\n"
                    },
                    "js": {
                        "methanol-charts.js": "// Methanol Charts JS\n"
                    },
                    "css": {
                        "methanol-analysis.css": "/* Methanol Analysis CSS */\n"
                    },
                    "python": {
                        "methanol_data_processor.py": "# Methanol data processor\n",
                        "methanol_campaign_model.py": "# Methanol campaign model\n"
                    },
                    "uploads": {},
                    "exports": {},
                    "data": {},
                    "config": {},
                    "docs": {
                        "README.txt": "Methanol Synthesis Documentation\n",
                        "README.html": "<html><body><h1>Methanol Synthesis</h1></body></html>\n"
                    }
                },
                "ammonia-synthesis": {
                    "html": {
                        "ammonia-syn-dashboard.html": "<!-- Ammonia Syn Dashboard HTML -->\n"
                    },
                    "js": {
                        "ammonia-syn-charts.js": "// Ammonia Syn Charts JS\n"
                    },
                    "css": {
                        "ammonia-syn-analysis.css": "/* Ammonia Syn Analysis CSS */\n"
                    },
                    "python": {
                        "ammonia_syn_data_processor.py": "# Ammonia Syn data processor\n",
                        "ammonia_syn_campaign_model.py": "# Ammonia Syn campaign model\n"
                    },
                    "uploads": {},
                    "exports": {},
                    "data": {},
                    "config": {},
                    "docs": {
                        "README.txt": "Ammonia Synthesis Documentation\n",
                        "README.html": "<html><body><h1>Ammonia Synthesis</h1></body></html>\n"
                    }
                },
                "ammonia-cracking": {
                    "html": {
                        "ammonia-crack-dashboard.html": "<!-- Ammonia Crack Dashboard HTML (Coming Soon) -->\n"
                    },
                    "js": {
                        "ammonia-crack-charts.js": "// Ammonia Crack Charts JS\n"
                    },
                    "css": {
                        "ammonia-crack-analysis.css": "/* Ammonia Crack Analysis CSS */\n"
                    },
                    "python": {
                        "ammonia_crack_data_processor.py": "# Ammonia Crack data processor\n",
                        "ammonia_crack_campaign_model.py": "# Ammonia Crack campaign model\n"
                    },
                    "uploads": {},
                    "exports": {},
                    "data": {},
                    "config": {},
                    "docs": {
                        "README.txt": "Ammonia Cracking Documentation\n",
                        "README.html": "<html><body><h1>Ammonia Cracking</h1></body></html>\n"
                    }
                },
                "autoclave-tests": {
                    "html": {
                        "autoclave-dashboard.html": "<!-- Autoclave Dashboard HTML (Coming Soon) -->\n"
                    },
                    "js": {},
                    "css": {},
                    "python": {
                        "autoclave_data_processor.py": "# Autoclave data processor\n",
                        "autoclave_campaign_model.py": "# Autoclave campaign model\n"
                    },
                    "uploads": {},
                    "exports": {},
                    "data": {},
                    "config": {},
                    "docs": {
                        "README.txt": "Autoclave Tests Documentation\n",
                        "README.html": "<html><body><h1>Autoclave Tests</h1></body></html>\n"
                    }
                },
                "fertilizer-tests": {
                    "html": {
                        "fertilizer-dashboard.html": "<!-- Fertilizer Dashboard HTML (Coming Soon) -->\n"
                    },
                    "js": {},
                    "css": {},
                    "python": {
                        "fertilizer_data_processor.py": "# Fertilizer data processor\n",
                        "fertilizer_campaign_model.py": "# Fertilizer campaign model\n"
                    },
                    "uploads": {},
                    "exports": {},
                    "data": {},
                    "config": {},
                    "docs": {
                        "README.txt": "Fertilizer Tests Documentation\n",
                        "README.html": "<html><body><h1>Fertilizer Tests</h1></body></html>\n"
                    }
                }
            },
            "gas-cylinder-manager": {
                "html": {
                    "cylinder-scan-input.html": "<!-- Cylinder Scan Input HTML -->\n",
                    "cylinder-manual-entry.html": "<!-- Cylinder Manual Entry HTML -->\n",
                    "cylinder-stock.html": "<!-- Cylinder Stock HTML -->\n",
                    "cylinder-return.html": "<!-- Cylinder Return HTML -->\n",
                    "cylinder-log-view.html": "<!-- Cylinder Log View HTML -->\n"
                },
                "js": {
                    "ocr-scanner-cylinder.js": "// OCR Scanner for Cylinder JS\n",
                    "cylinder-stock-manager.js": "// Cylinder Stock Manager JS\n",
                    "cylinder-crud.js": "// Cylinder CRUD JS\n",
                    "cylinder-log-export.js": "// Cylinder Log Export JS\n"
                },
                "css": {
                    "cylinder-main.css": "/* Cylinder Main CSS */\n"
                },
                "python": {
                    "gas_cylinder_processor.py": "# Gas Cylinder processor\n",
                    "gas_cylinder_model.py": "# Gas Cylinder model\n",
                    "ocr_service_cylinder.py": "# OCR service for cylinder\n"
                },
                "uploads": {},
                "exports": {},
                "data": {},
                "config": {},
                "docs": {
                    "README.txt": "Gas Cylinder Manager Documentation\n",
                    "README.html": "<html><body><h1>Gas Cylinder Manager</h1></body></html>\n"
                }
            },
            "lab-coat-manager": {
                "html": {
                    "labcoat-scan-input.html": "<!-- Lab Coat Scan Input HTML -->\n",
                    "labcoat-manual-entry.html": "<!-- Lab Coat Manual Entry HTML -->\n",
                    "labcoat-stock.html": "<!-- Lab Coat Stock HTML -->\n",
                    "labcoat-laundry.html": "<!-- Lab Coat Laundry HTML -->\n",
                    "labcoat-log-view.html": "<!-- Lab Coat Log View HTML -->\n"
                },
                "js": {
                    "ocr-scanner-labcoat.js": "// OCR Scanner for Lab Coat JS\n",
                    "labcoat-stock-manager.js": "// Lab Coat Stock Manager JS\n",
                    "labcoat-status.js": "// Lab Coat Status JS\n",
                    "labcoat-crud.js": "// Lab Coat CRUD JS\n"
                },
                "css": {
                    "labcoat-main.css": "/* Lab Coat Main CSS */\n"
                },
                "python": {
                    "lab_coat_processor.py": "# Lab Coat processor\n",
                    "lab_coat_model.py": "# Lab Coat model\n",
                    "ocr_service_labcoat.py": "# OCR service for lab coat\n"
                },
                "uploads": {},
                "exports": {},
                "data": {},
                "config": {},
                "docs": {
                    "README.txt": "Lab Coat Manager Documentation\n",
                    "README.html": "<html><body><h1>Lab Coat Manager</h1></body></html>\n"
                }
            },
            "laboratory-inventory": {
                "html": {
                    "inventory-dashboard.html": "<!-- Inventory Dashboard HTML -->\n",
                    "item-create-edit.html": "<!-- Item Create/Edit HTML -->\n",
                    "item-list-filter.html": "<!-- Item List Filter HTML -->\n",
                    "item-detail.html": "<!-- Item Detail HTML -->\n",
                    "attach-document.html": "<!-- Attach Document HTML -->\n"
                },
                "js": {
                    "inventory-manager.js": "// Inventory Manager JS\n",
                    "item-location-tracker.js": "// Item Location Tracker JS\n",
                    "document-attacher.js": "// Document Attacher JS\n"
                },
                "css": {
                    "inventory-main.css": "/* Inventory Main CSS */\n"
                },
                "python": {
                    "lab_inventory_processor.py": "# Lab Inventory Processor\n",
                    "lab_inventory_model.py": "# Lab Inventory Model\n",
                    "file_handler_inventory.py": "# File handler for Inventory uploads\n"
                },
                "uploads": { "delivery-notes": "", "item-specs": "" },
                "exports": {},
                "data": {},
                "config": {},
                "docs": {
                    "README.txt": "Laboratory Inventory Documentation\n",
                    "README.html": "<html><body><h1>Laboratory Inventory</h1></body></html>\n"
                }
            },
            "patent-manager": {
                "html": {
                    "patent-list.html": "<!-- Patent List HTML -->\n",
                    "patent-create-edit.html": "<!-- Patent Create/Edit HTML -->\n",
                    "patent-detail.html": "<!-- Patent Detail HTML -->\n",
                    "patent-document-upload.html": "<!-- Patent Document Upload HTML -->\n"
                },
                "js": {
                    "patent-crud.js": "// Patent CRUD JS\n",
                    "patent-document-handler.js": "// Patent Document Handler JS\n",
                    "patent-reminder.js": "// Patent Reminder JS\n"
                },
                "css": {
                    "patent-main.css": "/* Patent Main CSS */\n"
                },
                "python": {
                    "patent_processor.py": "# Patent processor logic\n",
                    "patent_model.py": "# Patent DB model\n",
                    "patent_notification_service.py": "# Patent notification service\n"
                },
                "uploads": {},
                "exports": {},
                "data": {},
                "config": {},
                "docs": {
                    "README.txt": "Patent Manager Documentation\n",
                    "README.html": "<html><body><h1>Patent Manager</h1></body></html>\n"
                }
            },
            "samples": {
                "html": {
                    "samples-list.html": "<!-- Samples List HTML -->\n",
                    "sample-create.html": "<!-- Sample Create HTML -->\n",
                    "sample-edit.html": "<!-- Sample Edit HTML -->\n",
                    "sample-detail.html": "<!-- Sample Detail HTML -->\n",
                    "sample-delete-confirm.html": "<!-- Sample Delete Confirm HTML -->\n",
                    "sample-registry.html": "<!-- Sample Registry HTML -->\n",
                    "sample-tracking.html": "<!-- Sample Tracking HTML -->\n",
                    "sample-chain-custody.html": "<!-- Sample Chain Custody HTML -->\n",
                    "sample-upload.html": "<!-- Sample Upload HTML -->\n"
                },
                "js": {
                    "samples-crud.js": "// Samples CRUD JS\n",
                    "sample-manager.js": "// Sample Manager JS\n",
                    "sample-tracking.js": "// Sample Tracking JS\n",
                    "chain-custody.js": "// Chain Custody JS\n",
                    "sample-upload.js": "// Sample Upload JS\n",
                    "sample-export.js": "// Sample Export JS\n"
                },
                "css": {
                    "samples-main.css": "/* Samples Main CSS */\n",
                    "sample-tracking.css": "/* Sample Tracking CSS */\n",
                    "sample-registry.css": "/* Sample Registry CSS */\n",
                    "chain-custody.css": "/* Chain Custody CSS */\n"
                },
                "python": {
                    "sample_processor.py": "# Sample processor logic\n",
                    "sample_crud.py": "# Sample CRUD operations\n",
                    "sample_tracker.py": "# Sample tracking logic\n",
                    "custody_manager.py": "# Custody manager logic\n",
                    "sample_uploader.py": "# Sample uploader logic\n",
                    "sample_exporter.py": "# Sample exporter logic\n"
                },
                "uploads": { "sample-data": "", "analysis-results": "", "certificates": "", "temp": "" },
                "exports": { "csv": "", "reports": "", "archive": "" },
                "data": {},
                "config": { "sample-types.json": "", "analysis-methods.json": "", "custody-protocols.json": "" },
                "docs": {
                    "README.txt": "Samples Module Documentation\n",
                    "README.html": "<html><body><h1>Samples Module</h1></body></html>\n"
                }
            }
        },
        "tests": {},
        "migrations": {},
        "instance": {},
        "requirements": {},
        "docs": {},
        "backup": {
            "system": {},
            "data": {},
            "scripts": {},
            "logs": {},
            "config": {}
        },
        "database": {
            "sqlite": {},
            "migrations": {},
            "converters": {},
            "schema": {}
        },
        "config": {},
        "logs": {}
    }
}

def create_structure(base_path, struct):
    """
    Recursively creates directories and files from the structure dictionary.
    """
    for name, content in struct.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # Create directory if it does not exist
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")
            create_structure(path, content)
        elif isinstance(content, str):
            # Create file with the given content
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Created file: {path}")


def main():
    base_dir = os.getcwd()  # Use the current directory as the base
    create_structure(base_dir, structure)


if __name__ == "__main__":
    main() 