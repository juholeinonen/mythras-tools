#!/usr/bin/env python3
"""
Mythras d20 Classic Fantasy Character Sheet Generator

This script creates an enhanced Excel character sheet for Mythras d20 Classic Fantasy
with automatic calculations, point tracking, and d20 conversion formulas.

Requirements: pip install openpyxl
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.formatting.rule import CellIsRule

def create_mythras_d20_character_sheet():
    """Create a comprehensive Mythras d20 Classic Fantasy character sheet with automation."""
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Character Sheet"
    
    # Define styles
    header_font = Font(bold=True, size=14, color="FFFFFF")
    subheader_font = Font(bold=True, size=12)
    bold_font = Font(bold=True)
    
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    culture_fill = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")
    professional_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
    class_fill = PatternFill(start_color="F2E6FF", end_color="F2E6FF", fill_type="solid")  # Light purple for class
    
    center_align = Alignment(horizontal="center", vertical="center")
    left_align = Alignment(horizontal="left", vertical="center")
    
    thin_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    
    # Set column widths
    column_widths = {
        'A': 25,  # Skill names
        'B': 12,  # Cultural
        'C': 12,  # Career
        'D': 12,  # Class
        'E': 12,  # Char 1
        'F': 8,   # Char 1 Value
        'G': 12,  # Char 2
        'H': 8,   # Char 2 Value
        'I': 10,  # Base
        'J': 12,  # Cult Pts
        'K': 12,  # Career Pts
        'L': 12,  # Class Pts
        'M': 12,  # Free Pts
        'N': 10,  # Total
        'O': 8,   # d20 Value
        'P': 8,   # d20 Bonus
        'Q': 3,   # Space
        'R': 18,  # Characteristics
        'S': 10,  # Values
    }
    
    for col, width in column_widths.items():
        ws.column_dimensions[col].width = width
    
    # Title
    ws.merge_cells('A1:P1')
    ws['A1'] = "MYTHRAS d20 CLASSIC FANTASY CHARACTER SHEET"
    ws['A1'].font = Font(bold=True, size=16, color="FFFFFF")
    ws['A1'].fill = PatternFill(start_color="203764", end_color="203764", fill_type="solid")
    ws['A1'].alignment = center_align
    
    # Character Info Section (Left side)
    char_info_row = 3
    ws[f'A{char_info_row}'] = "CHARACTER INFO"
    ws[f'A{char_info_row}'].font = subheader_font
    
    char_fields = ["Name:", "Culture:", "Career:", "Class:", "Age:"]
    for i, field in enumerate(char_fields):
        ws[f'A{char_info_row + 1 + i}'] = field
        ws[f'A{char_info_row + 1 + i}'].font = bold_font
    
    # Point Pools Section (Middle)
    ws[f'E{char_info_row}'] = "POINT POOLS"
    ws[f'E{char_info_row}'].font = subheader_font
    
    ws[f'E{char_info_row + 1}'] = "Cultural Points:"
    ws[f'F{char_info_row + 1}'] = 100
    ws[f'E{char_info_row + 2}'] = "Career Points:"
    ws[f'F{char_info_row + 2}'] = 50
    ws[f'E{char_info_row + 3}'] = "Class Points:"
    ws[f'F{char_info_row + 3}'] = 75
    ws[f'E{char_info_row + 4}'] = "Free Points:"
    ws[f'F{char_info_row + 4}'] = 25
    
    # Points Used tracking - Sum entire columns
    ws[f'E{char_info_row + 6}'] = "POINTS USED"
    ws[f'E{char_info_row + 6}'].font = subheader_font
    
    ws[f'E{char_info_row + 7}'] = "Cultural Used:"
    ws[f'F{char_info_row + 7}'] = '=SUM(J:J)'
    ws[f'E{char_info_row + 8}'] = "Career Used:"
    ws[f'F{char_info_row + 8}'] = '=SUM(K:K)'
    ws[f'E{char_info_row + 9}'] = "Class Used:"
    ws[f'F{char_info_row + 9}'] = '=SUM(L:L)'
    ws[f'E{char_info_row + 10}'] = "Free Used:"
    ws[f'F{char_info_row + 10}'] = '=SUM(M:M)'
    
    # Remaining Points
    ws[f'E{char_info_row + 12}'] = "REMAINING"
    ws[f'E{char_info_row + 12}'].font = subheader_font
    
    ws[f'E{char_info_row + 13}'] = "Cultural Left:"
    ws[f'F{char_info_row + 13}'] = f'=F{char_info_row + 1}-F{char_info_row + 7}'
    ws[f'E{char_info_row + 14}'] = "Career Left:"
    ws[f'F{char_info_row + 14}'] = f'=F{char_info_row + 2}-F{char_info_row + 8}'
    ws[f'E{char_info_row + 15}'] = "Class Left:"
    ws[f'F{char_info_row + 15}'] = f'=F{char_info_row + 3}-F{char_info_row + 9}'
    ws[f'E{char_info_row + 16}'] = "Free Left:"
    ws[f'F{char_info_row + 16}'] = f'=F{char_info_row + 4}-F{char_info_row + 10}'
    
    # Characteristics Section (Right side)
    ws[f'R{char_info_row}'] = "CHARACTERISTICS"
    ws[f'R{char_info_row}'].font = subheader_font
    
    characteristics = [
        ("STR:", 10), ("CON:", 10), ("SIZ:", 10), ("DEX:", 10),
        ("INT:", 10), ("POW:", 10), ("CHA:", 10)
    ]
    
    char_cells = {}  # Store characteristic cell references
    for i, (char_name, default_val) in enumerate(characteristics):
        row = char_info_row + 1 + i
        ws[f'R{row}'] = char_name
        ws[f'R{row}'].font = bold_font
        ws[f'S{row}'] = default_val
        char_cells[char_name.rstrip(':')] = f'S{row}'
    
    # Skills Section Header
    skills_start_row = 20
    headers = ["SKILL", "CULTURAL", "CAREER", "CLASS", "CHAR 1", "VAL 1", "CHAR 2", "VAL 2", "BASE", "CULT PTS", "CAREER PTS", "CLASS PTS", "FREE PTS", "TOTAL", "d20 VALUE", "d20 BONUS"]
    
    for col, header in enumerate(headers, 1):
        cell = ws.cell(row=skills_start_row, column=col, value=header)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border
    
    # Standard Skills
    current_row = skills_start_row + 2
    ws[f'A{current_row}'] = "STANDARD SKILLS"
    ws[f'A{current_row}'].font = Font(bold=True, size=12, color="FFFFFF")
    ws[f'A{current_row}'].fill = PatternFill(start_color="70AD47", end_color="70AD47", fill_type="solid")
    current_row += 1
    
    # Define skills with their characteristics and special formulas
    standard_skills = [
        ("Athletics", "STR", "DEX", None),
        ("Boating", "STR", "CON", None),
        ("Brawn", "STR", "SIZ", None),
        ("Conceal", "DEX", "POW", None),
        ("Customs", "INT", "", "INT*2+40"),
        ("Dance", "DEX", "CHA", None),
        ("Deceit", "INT", "CHA", None),
        ("Drive", "DEX", "POW", None),
        ("Endurance", "CON", "CON", None),
        ("Evade", "DEX", "DEX", None),
        ("First Aid", "INT", "DEX", None),
        ("Influence", "CHA", "CHA", None),
        ("Insight", "INT", "POW", None),
        ("Locale", "INT", "INT", None),
        ("Native Tongue", "INT", "CHA", "INT+CHA+40"),
        ("Perception", "INT", "POW", None),
        ("Ride", "DEX", "POW", None),
        ("Sing", "CHA", "POW", None),
        ("Stealth", "DEX", "INT", None),
        ("Swim", "STR", "CON", None),
        ("Unarmed", "STR", "DEX", None),
        ("Willpower", "POW", "POW", None),
        ("Combat Style", "STR", "DEX", None),
    ]
    
    def get_base_formula(char1, char2, special_formula):
        """Generate the base skill formula."""
        if special_formula:
            if special_formula == "INT*2+40":
                return f"={char_cells['INT']}*2+40"
            elif special_formula == "INT+CHA+40":
                return f"={char_cells['INT']}+{char_cells['CHA']}+40"
        
        if char1 == char2:  # Same characteristic twice
            return f"={char_cells[char1]}*2"
        elif char2:  # Two different characteristics
            return f"={char_cells[char1]}+{char_cells[char2]}"
        else:  # Single characteristic (shouldn't happen with current skills)
            return f"={char_cells[char1]}"
    
    # Add standard skills
    for skill_name, char1, char2, special in standard_skills:
        ws[f'A{current_row}'] = skill_name
        # Leave Cultural, Career, and Class columns empty for user to mark
        ws[f'E{current_row}'] = char1
        ws[f'F{current_row}'] = f"={char_cells[char1]}" if char1 else ""
        ws[f'G{current_row}'] = char2 if char2 else ""
        ws[f'H{current_row}'] = f"={char_cells[char2]}" if char2 else ""
        
        # Base calculation
        if special:  # Special formula
            ws[f'I{current_row}'] = get_base_formula(char1, char2, special)
        elif char2:  # Has second characteristic
            ws[f'I{current_row}'] = get_base_formula(char1, char2, None)
        else:  # Single characteristic
            ws[f'I{current_row}'] = f"={char_cells[char1]}"
        
        # Points columns default to 0
        ws[f'J{current_row}'] = 0
        ws[f'K{current_row}'] = 0
        ws[f'L{current_row}'] = 0
        ws[f'M{current_row}'] = 0
        
        # Total calculation
        ws[f'N{current_row}'] = f"=I{current_row}+J{current_row}+K{current_row}+L{current_row}+M{current_row}"
        
        # d20 conversion formulas
        ws[f'O{current_row}'] = f"=ROUNDDOWN(N{current_row}/5,0)"  # d20 value (divided by 5, rounded down)
        ws[f'P{current_row}'] = f"=MOD(N{current_row},5)"  # d20 bonus (remainder when divided by 5)
        
        current_row += 1
    
    # Professional Skills Section
    current_row += 2
    ws[f'A{current_row}'] = "PROFESSIONAL SKILLS"
    ws[f'A{current_row}'].font = Font(bold=True, size=12, color="FFFFFF")
    ws[f'A{current_row}'].fill = PatternFill(start_color="FFC000", end_color="FFC000", fill_type="solid")
    current_row += 1
    
    ws[f'A{current_row}'] = "(Add your chosen professional skills below)"
    ws[f'A{current_row}'].font = Font(italic=True)
    current_row += 1
    
    # Add empty professional skill rows for user to fill
    for i in range(8):  # 8 empty rows for professional skills
        # Leave all fields empty except for default point values and formulas
        ws[f'J{current_row}'] = 0
        ws[f'K{current_row}'] = 0
        ws[f'L{current_row}'] = 0
        ws[f'M{current_row}'] = 0
        ws[f'N{current_row}'] = f"=I{current_row}+J{current_row}+K{current_row}+L{current_row}+M{current_row}"
        ws[f'O{current_row}'] = f"=ROUNDDOWN(N{current_row}/5,0)"
        ws[f'P{current_row}'] = f"=MOD(N{current_row},5)"
        
        # Apply professional skill styling
        for col in range(1, 17):  # A to P
            ws.cell(row=current_row, column=col).fill = professional_fill
        
        current_row += 1
    
    # Instructions section
    current_row += 2
    ws[f'A{current_row}'] = "INSTRUCTIONS:"
    ws[f'A{current_row}'].font = Font(bold=True, size=12, color="C5504B")
    current_row += 1
    
    instructions = [
        "1. Fill in your characteristics (STR, CON, etc.) in column S",
        "2. Mark Cultural skills: type 'x' in column B for skills from your cultural background",
        "3. Mark Career skills: type 'x' in column C for skills from your chosen career",
        "4. Mark Class skills: type 'x' in column D for skills from your character class",
        "5. Add skill points in columns J (Cultural), K (Career), L (Class), M (Free)",
        "6. For Professional skills: Add skill name in column A, characteristics in E & G",
        "7. Professional skill base formulas: Add in column I (e.g., =S4+S7 for STR+DEX)",
        "8. d20 VALUE = skill ÷ 5 (rounded down), d20 BONUS = remainder",
        "9. Point tracking and totals calculate automatically!",
        "10. Yellow rows = Professional skills section"
    ]
    
    for instruction in instructions:
        ws[f'A{current_row}'] = instruction
        current_row += 1
    
    # Add conditional formatting for point tracking
    # Highlight cells red if overspent
    ws.conditional_formatting.add(
        f'F{char_info_row + 13}:F{char_info_row + 16}',
        CellIsRule(operator='lessThan', formula=[0], 
                  fill=PatternFill(start_color='FF6B6B', end_color='FF6B6B', fill_type='solid'))
    )
    
    # Create a reference sheet
    ref_ws = wb.create_sheet("Reference")
    
    # Reference data
    ref_data = [
        ["MYTHRAS d20 CLASSIC FANTASY REFERENCE"],
        [""],
        ["d20 CONVERSION SYSTEM"],
        ["Mythras uses percentile dice (d100), d20 Classic Fantasy converts to d20"],
        ["Formula: d20 Value = Skill ÷ 5 (rounded down)"],
        ["Bonus: Remainder when dividing by 5"],
        ["Example: Skill 43 → d20 Value 8, Bonus +3"],
        [""],
        ["SKILL CHARACTERISTIC COMBINATIONS"],
        ["Skill", "Char 1", "Char 2", "Formula", "Notes"],
        *[
            [skill[0], skill[1], skill[2] if skill[2] else "", 
             skill[3] if skill[3] else f"{skill[1]}+{skill[2]}" if skill[2] else skill[1],
             "Special calculation" if skill[3] else ""]
            for skill in standard_skills
        ],
        [""],
        ["POINT ALLOCATION PHASES"],
        ["Phase", "Typical Points", "Used For"],
        ["Cultural", "100", "Standard skills from cultural background"],
        ["Career", "50-100", "Standard skills from chosen career"],
        ["Class", "75", "Standard skills from character class (NEW for d20)"],
        ["Free Points", "25-50", "Any standard skills + existing professional skills"],
        [""],
        ["PROFESSIONAL SKILLS"],
        ["- Choose based on character concept"],
        ["- Add skill names in column A of Professional Skills section"],
        ["- Each uses two characteristics as base"],
        ["- Can be improved with Career, Class, or Free points if already known"],
        [""],
        ["SKILL CATEGORIES"],
        ["Mark with 'x' in Cultural column for cultural background skills"],
        ["Mark with 'x' in Career column for career skills"],
        ["Mark with 'x' in Class column for character class skills"],
        ["Professional skills go in the yellow section at bottom"],
        [""],
        ["d20 USAGE"],
        ["Roll d20 + Bonus ≤ d20 Value for success"],
        ["Higher d20 Value = better chance of success"],
        ["Bonus adds extra points when close to next threshold"]
    ]
    
    for row_idx, row_data in enumerate(ref_data, 1):
        for col_idx, value in enumerate(row_data, 1):
            ref_ws.cell(row=row_idx, column=col_idx, value=value)
            if row_idx == 1:  # Title
                ref_ws.cell(row=row_idx, column=col_idx).font = Font(bold=True, size=14)
            elif row_idx in [3, 9, 14, 22, 28, 34]:  # Section headers
                ref_ws.cell(row=row_idx, column=col_idx).font = Font(bold=True, size=12)
    
    # Auto-fit columns in reference sheet
    for column in ref_ws.columns:
        max_length = max(len(str(cell.value)) if cell.value else 0 for cell in column)
        ref_ws.column_dimensions[column[0].column_letter].width = min(max_length + 2, 50)
    
    return wb

def main():
    """Generate and save the Mythras d20 Classic Fantasy character sheet."""
    print("🎲 Generating Mythras d20 Classic Fantasy Character Sheet...")
    
    try:
        wb = create_mythras_d20_character_sheet()
        filename = "Mythras_d20_Classic_Fantasy_Character_Sheet.xlsx"
        wb.save(filename)
        
        print(f"✅ Success! Character sheet saved as '{filename}'")
        print("\n📋 Features included:")
        print("  • Automatic characteristic-to-skill calculations")
        print("  • Point tracking for Cultural/Career/Class/Free phases")
        print("  • Culture, Career, and Class skill identification")
        print("  • d20 conversion formulas (skill ÷ 5 + bonus)")
        print("  • Professional skills section with formulas")
        print("  • Reference sheet with d20 rules and formulas")
        print("  • Conditional formatting for overspending alerts")
        print("\n🎯 d20 Classic Fantasy Features:")
        print("  • Added Class phase with separate point pool")
        print("  • d20 Value column (skill ÷ 5, rounded down)")
        print("  • d20 Bonus column (remainder from division)")
        print("  • Point tracking sums entire columns for accuracy")
        print("\n🎮 Usage:")
        print("  1. Open the Excel file")
        print("  2. Enter your characteristics in column S")
        print("  3. Mark skills as 'x' in Cultural/Career/Class columns")
        print("  4. Add skill points in columns J/K/L/M")
        print("  5. Use d20 Value + Bonus for d20 system rolls! ⚄")
        
    except ImportError:
        print("❌ Error: openpyxl not installed")
        print("📦 Install with: pip install openpyxl")
    except Exception as e:
        print(f"❌ Error creating sheet: {e}")

if __name__ == "__main__":
    main()
