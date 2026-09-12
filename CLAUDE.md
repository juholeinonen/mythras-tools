# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Python-based helper application for Mythras RPG Game Masters. The project includes character sheet generators (both standard Mythras and d20 Classic Fantasy variants), a PyQt5-based GUI for NPC visualization, and PDF text extraction utilities for working with Mythras rulebooks.

## Technology Stack

- **Language**: Python 3.9
- **GUI Framework**: PyQt5 (for NPC visualization)
- **Excel Generation**: openpyxl (for character sheet generators)
- **PDF Processing**: pdfminer.six, mutool
- **Data Format**: JSON for NPC data storage

## Environment Setup

The project uses a Python virtual environment:

```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies (inferred from imports)
pip install PyQt5 openpyxl pdfminer.six
```

## Running the Tools

### Character Sheet Generators

```bash
# Generate standard Mythras character sheet
python bin/mythras_python_generator.py
# Output: Mythras_Character_Sheet_Enhanced.xlsx

# Generate d20 Classic Fantasy variant
python bin/mythras_d20_generator.py
# Output: Mythras_d20_Classic_Fantasy_Character_Sheet.xlsx
```

### NPC Visualization GUI

```bash
# Launch GUI with NPC data
cd bin
python gui.py
```

The GUI reads NPC data from `data/efar.json` and displays:
- Character hitpoints on body locations
- Skill values organized by type (standard, magic, professional, custom, combat styles)
- SVG-based character visualization with color-coded hit locations

### PDF Text Extraction

```bash
# Extract text using pdfminer.six
python bin/pdfminer_six.py <path_to_pdf>

# mutool_txt_json.py contains spell parsing logic (incomplete implementation)
```

## Code Architecture

### Character Sheet Generators (`mythras_python_generator.py`, `mythras_d20_generator.py`)

Both generators create Excel-based character sheets with automated calculations:

- **Characteristics System**: STR, CON, SIZ, DEX, INT, POW, CHA stored in column O (python) or S (d20)
- **Skills**: Standard skills pre-populated with characteristic-based formulas
- **Point Pools**: Cultural (100), Career (50-100), Class (75, d20 only), Free (25-50)
- **Automatic Calculations**:
  - Base skill values from characteristics (e.g., Athletics = STR + DEX)
  - Total skill = Base + Cultural Points + Career Points + Free Points (+ Class Points for d20)
  - Point tracking with conditional formatting for overspending
  - d20 conversion: `d20 Value = skill ÷ 5 (rounded down)`, `Bonus = remainder`

Key differences:
- `mythras_d20_generator.py` adds Class point pool and d20 conversion columns (O, P)
- Both use `get_base_formula()` helper to generate Excel formulas from characteristic pairs

### GUI Application (`gui.py`)

PyQt5-based NPC sheet viewer:

- **NpcWindow**: Main window class displaying NPC data
- **Components**:
  - `init_image()`: SVG character visualization using `QSvgWidget`
  - `init_hitpoints()`: Hit location display using `QGraphicsScene` with editable text items
  - `init_skills()`: Grid layout of skill spinboxes organized by type
- **Hit Location Positioning**: Dictionary maps body parts to (x, y) coordinates
- **SVG Color Manipulation**: `change_color()` uses ElementTree to modify SVG element fill colors
- **Data Source**: Reads from `data/*.json` files

### Data Format

NPC JSON structure (see `data/efar.json`):

```json
{
    "name": "Character Name",
    "hp_image_path": "../images/stick_figure.jpg",
    "color_image_path": "../images/stick_figure.svg",
    "hitpoints": {
        "right_leg": 5,
        "left_leg": 5,
        "abdomen": 6,
        "chest": 7,
        "right_arm": 4,
        "left_arm": 4,
        "head": 5
    },
    "standard_skills": {},
    "magic_skills": {},
    "professional_skills": {},
    "custom_skills": {},
    "combat_styles": {}
}
```

### PDF Processing Utilities

- `pdfminer_six.py`: Command-line tool for basic PDF text extraction
- `mutool_txt_json.py`: Incomplete spell parsing logic for extracting structured spell data from Mythras rulebooks

## Important Notes

- The GUI uses relative paths (`../images/`, `../data/`) and should be run from the `bin/` directory
- Character sheet generators are standalone scripts that create Excel files in the current directory
- SVG manipulation in `gui.py` directly modifies the SVG file on disk (line 39)
- Both character generators include reference sheets explaining Mythras/d20 rules
- The project contains Mythras rulebook PDFs in `data/` (check copyright/licensing before distribution)
