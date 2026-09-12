import pandas as pd
import random
from typing import Dict, List, Tuple, Optional

# Import the spark tables from external file
# from spark_tables import SPARK_TABLES

# For this example, I'll include a small subset inline
# In actual use, you'd uncomment the import above and remove this
SPARK_TABLES = {
    "evocative_adjectives": ["Brooding", "Haunted", "Hasty", "Melancholic", "Storm-blessed"],
    "backgrounds_origins": ["Angel's Gift", "Fate Weaver", "Exiled Noble", "Dragon Rider", "Ghost Whisperer"],
    "distinctive_traits": ["always knows true north", "never removes their gloves", "speaks to animals like people"],
    "secret_motivations": ["tries to climb impossible peaks", "hunts the one who killed their family", "seeks redemption"],
    "notable_possessions": ["a quill that writes by itself", "a music box that plays lullabies", "a sword with a chipped blade"],
    "fears_weaknesses": ["strength fades in sunlight", "terrified of deep water", "cannot lie convincingly"],
    "distinctive_mannerisms": ["braids and unbraids constantly", "sweats when nervous", "drums fingers when thinking"],
    "relationships_connections": ["learned magic from a dying wizard", "trained by a legendary master", "owes a life debt"]
}

# Sentence templates for natural flow
SPARK_TEMPLATES = {
    "intro": [
        "Meet {adjective} {background}, who {trait}.",
        "This is {adjective} {background}, someone who {trait}.",
        "Here we have {adjective} {background}, a person who {trait}.",
        "Consider {adjective} {background}, one who {trait}.",
        "Behold {adjective} {background}, they {trait}."
    ],
    
    "possession_connector": [
        "They carry {possession}",
        "In their pack rests {possession}",
        "They never travel without {possession}",
        "Always at their side is {possession}",
        "Their most prized possession is {possession}"
    ],
    
    "motivation_connector": [
        "driven by a desire to {motivation}",
        "secretly working to {motivation}",
        "haunted by the need to {motivation}", 
        "desperately trying to {motivation}",
        "ultimately hoping to {motivation}"
    ],
    
    "relationship_connector": [
        "Their past is marked by having {relationship}",
        "They are bound by the fact that they {relationship}",
        "What defines them is that they {relationship}",
        "A key part of their story is that they {relationship}",
        "They carry the weight of having {relationship}"
    ],
    
    "weakness_connector": [
        "Yet they struggle with being {weakness}",
        "However, they are {weakness}",
        "Their greatest challenge is being {weakness}",
        "Despite their strengths, they are {weakness}",
        "What holds them back is being {weakness}"
    ],
    
    "mannerism_connector": [
        "Others notice how they {mannerism}",
        "You can spot them by the way they {mannerism}",
        "A telltale sign is that they {mannerism}",
        "What gives them away is how they {mannerism}",
        "People remember them because they {mannerism}"
    ]
}

def generate_flowing_spark(num_details: int = 3) -> str:
    """Generate a character spark with natural sentence flow."""
    
    # Core identity
    adjective = random.choice(SPARK_TABLES["evocative_adjectives"])
    background = random.choice(SPARK_TABLES["backgrounds_origins"])
    trait = random.choice(SPARK_TABLES["distinctive_traits"])
    
    # Build the character description
    intro_template = random.choice(SPARK_TEMPLATES["intro"])
    spark_text = intro_template.format(
        adjective=adjective.lower(),
        background=background.lower(),
        trait=trait
    )
    
    # Available detail types
    detail_types = [
        ("notable_possessions", "possession_connector"),
        ("secret_motivations", "motivation_connector"),
        ("relationships_connections", "relationship_connector"),
        ("fears_weaknesses", "weakness_connector"),
        ("distinctive_mannerisms", "mannerism_connector")
    ]
    
    # Randomly select which details to include
    selected_details = random.sample(detail_types, min(num_details, len(detail_types)))
    
    # Add each detail with flowing connectors
    for detail_table, connector_key in selected_details:
        detail = random.choice(SPARK_TABLES[detail_table])
        connector_template = random.choice(SPARK_TEMPLATES[connector_key])
        
        # Format the detail based on its type
        if detail_table == "notable_possessions":
            detail_text = connector_template.format(possession=detail)
        elif detail_table == "secret_motivations":
            detail_text = connector_template.format(motivation=detail)
        elif detail_table == "relationships_connections":
            detail_text = connector_template.format(relationship=detail)
        elif detail_table == "fears_weaknesses":
            detail_text = connector_template.format(weakness=detail)
        elif detail_table == "distinctive_mannerisms":
            detail_text = connector_template.format(mannerism=detail)
        
        # Add to the spark text
        spark_text += f" {detail_text}."
    
    return spark_text

def generate_multiple_sparks(count: int = 5, details_per_spark: int = 3):
    """Generate multiple character sparks."""
    sparks = []
    for i in range(count):
        spark = generate_flowing_spark(details_per_spark)
        sparks.append(f"**Character {i+1}:**\\n{spark}\\n")
    
    return "\\n".join(sparks)


def demo_spark_generator():
    """Demonstrate the improved spark generator."""
    print("=== IMPROVED CHARACTER SPARK GENERATOR ===")
    print("\\nGenerating 5 example character sparks with natural sentence flow:\\n")
    
    for i in range(5):
        spark = generate_flowing_spark(random.randint(2, 4))
        print(f"**Example {i+1}:**")
        print(spark)
        print()
    
    print("\\n" + "="*60)
    print("\\nCompare this to the old choppy format:")
    print("You are a **Haunted Angel's Gift**\\n**Relationships Connections**: learned magic from a dying wizard")
    print("\\nvs. the new flowing format:")
    example = generate_flowing_spark(3)
    print(example)

if __name__ == "__main__":
    demo_spark_generator()