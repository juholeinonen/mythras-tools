# Provided correct format content
correct_format_content = """
Spiritshield
Concentration, Resist (Willpower), Touch
This spell creates a shield around the recipient which deters spirits 
from entering. Any spirit wishing to attack or possess the recipient 
must overcome the spell by winning an opposed test of their Will-
power against the caster’s Folk Magic skill.
...
Witchsight
Ranged, Resist (Willpower)
Witchsight allows the caster to see active magic, enchanted items, 
and invisible entities (although such things are simply shadowy 
representations) that lie within range and line of sight. It can also 
penetrate illusions or discern the true guise of shapeshifted crea-
tures. Beings which wish to remain hidden or disguised must win an 
opposed test of their Willpower versus the casting roll.
"""

def extract_spells_from_correct_format(content: str) -> list:
    """
    Extracts spell information from the provided correct format and structures it into a JSON format.

    Args:
    - content (str): Text content in the correct format.

    Returns:
    - list: List of dictionaries containing structured spell information.
    """
    # Split the content into lines and initialize variables
    lines = content.strip().split("\n")
    spells = []
    current_spell = {}
    
    for line in lines:
        if not line.strip():
            continue
        # Check for spell name (title-like structure)
        if line[0].isupper() and line[-1].islower() and not current_spell:
            current_spell["name"] = line
        # Check for attributes (comma-separated values)
        elif "," in line and "name" in current_spell and "attributes" not in current_spell:
            current_spell["attributes"] = line.split(", ")
        # Remaining lines are part of the description
        elif "name" in current_spell and "attributes" in current_spell:
            current_spell["description"] = current_spell.get("description", "") + line + " "
            # If the next line is a spell name or the end of content, add the current spell to the list
            if lines.index(line) == len(lines) - 1 or (lines.index(line) + 1 < len(lines) and lines[lines.index(line) + 1][0].isupper()):
                spells.append(current_spell)
                current_spell = {}
                
    return spells

# Extract spell information from the correct format content
spells_from_correct_format = extract_spells_from_correct_format(correct_format_content)

# Convert the list of spell dictionaries into a JSON string
spells_from_correct_format_json = json.dumps(spells_from_correct_format, indent=4)

spells_from_correct_format_json[:1000]  # Displaying the first 1000 characters for readability

