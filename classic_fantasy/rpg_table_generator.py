import pandas as pd
import json
from typing import Dict, List, Tuple

# Configuration for races and classes
RPG_CONFIG = {
    "races": {
        "Human": {
            "weight": 40,
            "subtypes": {
                "Civilized": 50,  # Most common
                "Barbarian": 30,
                "Nomad": 15,
                "Primitive": 5
            }
        },
        "Halfling": {
            "weight": 25,
            "subtypes": {}  # No subtypes, evenly divided means just one entry
        },
        "Dwarf": {
            "weight": 15,
            "subtypes": {
                "Hill Dwarf": 50,
                "Mountain Dwarf": 50
            }
        },
        "Half-Orc": {
            "weight": 10,
            "subtypes": {}
        },
        "High Elf": {"weight": 3},
        "Wood Elf": {"weight": 3},
        "Dark Elf": {"weight": 2},
        "Drow": {"weight": 1},
        "Gnome": {
            "weight": 1,
            "subtypes": {}
        }
    },
    
    "classes": {
        "Fighter": {
            "weight": 1,
            "subtypes": {
                "Sword & Board": 25,
                "Two-handed Specialist": 25,
                "Dual-wielding": 20,
                "Ranged Fighter": 20,
                "Weapon Master": 10
            }
        },
        "Magic User": {
            "weight": 1,
            "subtypes": {
                "Generalist": 40,
                "Evocation Specialist": 15,
                "Necromancy Specialist": 10,
                "Illusion Specialist": 10,
                "Divination Specialist": 10,
                "Enchantment Specialist": 8,
                "Conjuration Specialist": 7
            }
        },
        "Cleric": {
            "weight": 1,
            "subtypes": {
                "War Priest": 30,
                "Healer": 30,
                "Death Domain": 15,
                "Nature Domain": 15,
                "Knowledge Domain": 10
            }
        },
        "Thief": {
            "weight": 1,
            "subtypes": {
                "Burglar": 40,
                "Scout": 30,
                "Spy": 20,
                "Treasure Hunter": 10
            }
        },
        "Thief-Acrobat": {"weight": 1},
        "Ranger": {
            "weight": 1,
            "subtypes": {
                "Beast Master": 35,
                "Tracker": 35,
                "Archer": 30
            }
        },
        "Paladin": {"weight": 1},
        "Arcane Bard": {"weight": 1},
        "Druidic Bard": {"weight": 1},
        "Druid": {
            "weight": 1,
            "subtypes": {
                "Nature's Warden": 50,
                "Shapeshifter": 30,
                "Weather Caller": 20
            }
        },
        "Berserker": {"weight": 1},
        "Monk": {
            "weight": 1,
            "subtypes": {
                "Way of the Open Hand": 40,
                "Way of the Shadow": 30,
                "Way of the Elements": 30
            }
        }
    }
}

def calculate_probability_ranges(config: Dict, total_range: int = 100) -> List[Tuple[str, str, str]]:
    """
    Calculate d100 ranges for races or classes based on weights.
    Returns list of tuples: (range_string, main_type, subtype)
    """
    results = []
    current_start = 1
    
    # First, calculate total weight
    total_weight = sum(item.get('weight', 0) for item in config.values())
    
    for main_type, data in config.items():
        weight = data.get('weight', 0)
        main_range_size = int((weight / total_weight) * total_range)
        
        # Handle subtypes
        subtypes = data.get('subtypes', {})
        if subtypes:
            subtype_start = current_start
            subtype_total_weight = sum(subtypes.values())
            
            for subtype, subtype_weight in subtypes.items():
                subtype_size = int((subtype_weight / subtype_total_weight) * main_range_size)
                if subtype_size == 0:
                    subtype_size = 1  # Ensure at least 1
                
                range_end = subtype_start + subtype_size - 1
                range_str = f"{subtype_start:02d}-{range_end:02d}" if subtype_start != range_end else f"{subtype_start:02d}"
                
                results.append((range_str, main_type, subtype))
                subtype_start = range_end + 1
            
            current_start = subtype_start
        else:
            # No subtypes
            range_end = current_start + main_range_size - 1
            range_str = f"{current_start:02d}-{range_end:02d}" if current_start != range_end else f"{current_start:02d}"
            
            results.append((range_str, main_type, ""))
            current_start = range_end + 1
    
    return results

def create_dataframe(data: List[Tuple[str, str, str]], table_type: str) -> pd.DataFrame:
    """Create a pandas DataFrame from the probability data."""
    if table_type.lower() == "race":
        columns = ['d100 Roll', 'Race', 'Cultural Background/Subrace']
    else:
        columns = ['d100 Roll', 'Class', 'Specialization/Kit']
    
    df = pd.DataFrame(data, columns=columns)
    return df

def generate_latex_table(df: pd.DataFrame, table_title: str) -> str:
    """Generate LaTeX table code from DataFrame."""
    latex_code = df.to_latex(
        index=False,
        escape=False,
        column_format='|c|l|l|',
        caption=table_title,
        label=f"tab:{table_title.lower().replace(' ', '_')}"
    )
    
    # Add some LaTeX formatting improvements
    latex_code = latex_code.replace('\\toprule', '\\hline')
    latex_code = latex_code.replace('\\midrule', '\\hline') 
    latex_code = latex_code.replace('\\bottomrule', '\\hline')
    
    return latex_code

def save_tables(race_df: pd.DataFrame, class_df: pd.DataFrame, base_filename: str = "classic_fantasy_tables"):
    """Save tables in multiple formats."""
    
    # Save to Excel with multiple sheets
    with pd.ExcelWriter(f"{base_filename}.xlsx", engine='openpyxl') as writer:
        race_df.to_excel(writer, sheet_name='Race Table', index=False)
        class_df.to_excel(writer, sheet_name='Class Table', index=False)
    
    # Save individual CSV files
    race_df.to_csv(f"{base_filename}_races.csv", index=False)
    class_df.to_csv(f"{base_filename}_classes.csv", index=False)
    
    # Generate and save LaTeX
    race_latex = generate_latex_table(race_df, "Character Race Table")
    class_latex = generate_latex_table(class_df, "Character Class Table")
    
    with open(f"{base_filename}_latex.tex", "w") as f:
        f.write("% Classic Fantasy RPG Tables\n")
        f.write("% Generated automatically\n\n")
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage[utf8]{inputenc}\n")
        f.write("\\usepackage{booktabs}\n")
        f.write("\\usepackage{array}\n")
        f.write("\\begin{document}\n\n")
        f.write("\\section{Character Creation Tables}\n\n")
        f.write(race_latex)
        f.write("\n\\newpage\n\n")
        f.write(class_latex)
        f.write("\n\\end{document}")
    
    print(f"Tables saved as:")
    print(f"  - {base_filename}.xlsx (Excel with multiple sheets)")
    print(f"  - {base_filename}_races.csv")
    print(f"  - {base_filename}_classes.csv") 
    print(f"  - {base_filename}_latex.tex (Complete LaTeX document)")

# Generate the tables
def main():
    print("Generating Classic Fantasy RPG Tables...")
    print("="*50)
    
    # Generate race table
    race_data = calculate_probability_ranges(RPG_CONFIG["races"])
    race_df = create_dataframe(race_data, "race")
    
    # Generate class table  
    class_data = calculate_probability_ranges(RPG_CONFIG["classes"])
    class_df = create_dataframe(class_data, "class")
    
    # Display preview
    print("\nRACE TABLE PREVIEW:")
    print(race_df.head(10))
    print(f"... ({len(race_df)} total entries)")
    
    print("\nCLASS TABLE PREVIEW:")
    print(class_df.head(10)) 
    print(f"... ({len(class_df)} total entries)")
    
    # Save all formats
    save_tables(race_df, class_df)
    
    return race_df, class_df

if __name__ == "__main__":
    race_df, class_df = main()