import pandas as pd
import random
from typing import Dict, List, Tuple, Optional

# Comprehensive Character Spark Tables
SPARK_TABLES = {
    "evocative_adjectives": [
        "Brooding", "Flamboyant", "Calculating", "Restless", "Enigmatic", "Weathered", "Graceful", "Haunted",
        "Boisterous", "Methodical", "Impulsive", "Serene", "Fierce", "Melancholic", "Whimsical", "Stoic",
        "Ambitious", "Cautious", "Rebellious", "Wise", "Naive", "Cynical", "Optimistic", "Paranoid",
        "Charming", "Gruff", "Elegant", "Rustic", "Scholarly", "Primal", "Refined", "Wild",
        "Mysterious", "Transparent", "Complex", "Simple", "Dramatic", "Understated", "Bold", "Timid",
        "Ancient", "Youthful", "Experienced", "Fresh", "Battle-worn", "Untested", "Legendary", "Forgotten",
        "Noble", "Common", "Exotic", "Familiar", "Dangerous", "Harmless", "Intense", "Laid-back",
        "Passionate", "Detached", "Loyal", "Fickle", "Honest", "Deceptive", "Generous", "Selfish",
        "Patient", "Hasty", "Gentle", "Harsh", "Humble", "Proud", "Curious", "Indifferent",
        "Brave", "Cowardly", "Clever", "Foolish", "Lucky", "Cursed", "Blessed", "Doomed",
        "Radiant", "Shadow-touched", "Storm-blessed", "Earth-bound", "Fire-hearted", "Ice-cold", "Star-kissed", "Moon-touched",
        "Raven-haired", "Golden", "Silver-tongued", "Iron-willed", "Diamond-hard", "Silk-soft", "Thunder-voiced", "Whisper-quiet",
        "Sword-sworn", "Spell-touched", "God-marked", "Demon-scarred", "Angel-blessed", "Fey-touched", "Dragon-blooded", "Giant-born",
        "Tide-turned", "Wind-walked", "Stone-hearted", "Flame-kissed", "Frost-born", "Lightning-struck", "Earthquake-shaken", "Volcano-forged"
    ],
    
    "backgrounds_origins": [
        "Exiled Noble", "Guild Apprentice", "Bastard Heir", "Caravan Guard", "Street Orphan", "Temple Acolyte",
        "Merchant's Child", "Soldier's Offspring", "Tavern Keeper", "Blacksmith's Apprentice", "Scholar's Student", "Sailor's Mate",
        "Forest Hermit", "Mountain Dweller", "Desert Nomad", "Swamp Witch", "Cave Dweller", "Tower Scholar",
        "Royal Spy", "Rebel Fighter", "Cult Survivor", "Plague Doctor", "War Refugee", "Lost Explorer",
        "Circus Performer", "Gladiator Slave", "Pirate's Heir", "Smuggler's Child", "Thief Lord", "Assassin's Shadow",
        "Beast Tamer", "Dragon Rider", "Demon Hunter", "Ghost Whisperer", "Relic Seeker", "Tomb Robber",
        "Court Jester", "Royal Guard", "Diplomatic Envoy", "Foreign Ambassador", "Traveling Judge", "Bounty Hunter",
        "Plague Survivor", "Disaster Witness", "Miracle Child", "Prophesy Bearer", "Chosen One", "Marked Child",
        "Time Traveler", "Dimension Walker", "Plane Shifter", "Reality Bender", "Fate Weaver", "Destiny Changer",
        "Storm Caller", "Earth Shaker", "Fire Bringer", "Water Walker", "Wind Rider", "Shadow Dancer",
        "Light Bearer", "Dark Walker", "Void Toucher", "Star Reader", "Moon Singer", "Sun Worshipper",
        "Ancient Bloodline", "Lost Kingdom", "Hidden Village", "Secret Society", "Forgotten Order", "Banned Brotherhood",
        "Cursed Family", "Blessed Lineage", "Marked Clan", "Chosen House", "Sacred Tribe", "Damned Dynasty",
        "Foreign Land", "Distant Shore", "Unknown Realm", "Hidden Valley", "Lost City", "Forgotten Empire",
        "Sky Island", "Underground Kingdom", "Floating Castle", "Moving City", "Vanished Village", "Timeless Tower",
        "Dream Walker", "Nightmare Survivor", "Vision Seeker", "Oracle's Child", "Seer's Apprentice", "Prophet's Heir",
        "God's Champion", "Devil's Bargain", "Angel's Gift", "Demon's Mark", "Spirit's Chosen", "Ghost's Vengeance"
    ],
    
    "distinctive_traits": [
        "never removes their gloves", "speaks only in questions", "counts everything twice", "always knows true north",
        "can't cross running water without praying", "tastes food before anyone else eats", "sleeps with one eye open",
        "never sits with their back to a door", "always carries exactly seven coins", "speaks to animals like people",
        "draws maps of everywhere they go", "collects interesting stones", "knows a song for every occasion",
        "remembers every face they've ever seen", "can predict weather by joint pain", "never breaks a promise",
        "always tells the truth, even when it hurts", "laughs at their own jokes", "quotes dead philosophers",
        "carves their initials in new places", "always pays their debts immediately", "never gambles with money",
        "reads everything backwards first", "knocks three times before entering", "never eats meat on certain days",
        "whispers to their weapons", "names all their possessions", "keeps a detailed journal", "draws portraits of strangers",
        "never travels the same path twice", "always helps lost children", "feeds stray animals", "lights candles for the dead",
        "never lies to children", "always shares food with the hungry", "gives coins to beggars", "helps strangers in need",
        "remembers everyone's birthday", "knows the names of all the stars", "can find water in any desert",
        "always knows what time it is", "never gets lost in cities", "can sleep anywhere", "wakes at exactly dawn",
        "never forgets a kindness", "always repays cruelty", "keeps their word no matter the cost", "protects the innocent",
        "challenges bullies", "stands up for the weak", "never abandons a friend", "keeps others' secrets",
        "sees good in everyone", "trusts too easily", "forgives too quickly", "loves too deeply",
        "fears commitment", "avoids crowds", "distrusts authority", "questions everything", "believes in luck",
        "sees omens everywhere", "follows ancient customs", "respects old traditions", "honors the ancestors"
    ],
    
    "secret_motivations": [
        "seeks redemption for a terrible mistake", "hunts the one who killed their family", "protects a dangerous secret",
        "searches for their true parentage", "aims to restore their family's honor", "tries to break an ancient curse",
        "wants to prove their worth to a parent", "seeks to avenge a betrayed mentor", "hopes to find a lost love",
        "dreams of building a perfect kingdom", "plans to overthrow a tyrant king", "works to prevent a prophecy",
        "tries to save their homeland from disaster", "seeks immortality to protect others", "wants to become a god",
        "hopes to resurrect a dead friend", "tries to forget a traumatic past", "seeks to master forbidden knowledge",
        "wants to unite warring tribes", "hopes to find a legendary artifact", "tries to close a demon portal",
        "seeks to cure a magical disease", "wants to explore unknown lands", "hopes to make their mark on history",
        "tries to escape their dark destiny", "seeks to fulfill a sacred vow", "wants to earn a place in legend",
        "hopes to find meaning in existence", "tries to understand their strange dreams", "seeks to control their powers",
        "wants to protect future generations", "hopes to right an ancient wrong", "tries to heal the world's wounds",
        "seeks to bridge different worlds", "wants to transcend mortal limitations", "hopes to achieve perfect balance",
        "tries to preserve dying knowledge", "seeks to create something eternal", "wants to inspire others to greatness",
        "hopes to find their true calling", "tries to escape a binding oath", "seeks to free enslaved people",
        "wants to establish a new religion", "hopes to discover new magic", "tries to map the entire world",
        "seeks to commune with the gods", "wants to tame wild beasts", "hopes to sail uncharted seas",
        "tries to climb impossible peaks", "seeks to solve ancient mysteries", "wants to write the perfect song",
        "hopes to paint ultimate beauty", "tries to craft legendary weapons", "seeks to brew perfect potions",
        "wants to grow magical gardens", "hopes to train perfect warriors", "tries to teach wisdom to fools"
    ],
    
    "notable_possessions": [
        "a locket that won't open", "a sword with a chipped blade", "a map to nowhere", "a key without a lock",
        "a book written in unknown language", "a compass that points to lost things", "a mirror that shows truth",
        "a coin that always lands heads", "a feather that never falls", "a stone that feels warm",
        "a ring that changes color with mood", "a pendant that glows at midnight", "a bracelet of silver bells",
        "a hat that's seen better days", "a cloak that never gets wet", "boots that never wear out",
        "gloves that never come off", "a mask with no eye holes", "a blindfold that helps you see",
        "spectacles that reveal magic", "a monocle that magnifies truth", "a pipe that never needs tobacco",
        "a flask that refills itself", "a purse that's always nearly empty", "a bag that holds impossible things",
        "a rope that never tangles", "a hammer that sings when it strikes", "a chisel that carves memories",
        "a paintbrush that paints the future", "a quill that writes by itself", "ink that changes color daily",
        "a candle that never burns out", "a lantern that shows hidden paths", "a torch that burns cold",
        "a blanket that brings good dreams", "a pillow that prevents nightmares", "a teddy bear with button eyes",
        "a wooden horse on wheels", "a set of dice that feel lucky", "a deck of cards missing the ace",
        "a chess set with living pieces", "a music box that plays lullabies", "a snow globe with moving figures",
        "a telescope that sees yesterday", "a sundial that works at night", "an hourglass that runs backwards",
        "a weather vane that predicts hearts", "a door knocker that answers back", "a bell that rings for danger",
        "a horn that calls the wind", "a drum that thunders like storms", "a flute that charms wild beasts"
    ],
    
    "fears_weaknesses": [
        "terrified of deep water", "cannot stand the sight of blood", "freezes when confronted with spiders",
        "loses speech when nervous", "becomes violently ill on boats", "faints at the sight of needles",
        "cannot sleep in complete darkness", "panics in enclosed spaces", "trembles at loud noises",
        "cannot lie convincingly", "trusts everyone immediately", "falls in love too easily",
        "always sees the best in people", "cannot say no to requests", "gives away money freely",
        "believes every sob story", "thinks everyone deserves redemption", "refuses to harm children",
        "won't fight on holy ground", "cannot break their word", "must help anyone in need",
        "compulsively tells the truth", "cannot ignore injustice", "always pays their debts",
        "haunted by recurring nightmares", "hears voices from the past", "sees ghosts of the dead",
        "cursed with prophetic dreams", "remembers other people's memories", "feels others' emotions",
        "cannot touch iron with bare skin", "weakened by running water", "burned by holy symbols",
        "loses power during eclipses", "strength fades in sunlight", "magic fails near churches",
        "allergic to silver", "poisoned by certain foods", "sickened by beautiful music",
        "ages rapidly when angry", "shrinks when afraid", "becomes invisible when embarrassed",
        "speaks only truth when drunk", "compelled to rhyme when excited", "cannot stop dancing to music",
        "must count everything they see", "organizes everything by color", "straightens crooked pictures",
        "washes hands obsessively", "checks locks multiple times", "counts steps while walking"
    ],
    
    "distinctive_mannerisms": [
        "drums fingers when thinking", "chews on their hair when nervous", "always sits facing the door",
        "taps their foot to unheard music", "speaks with their hands constantly", "never makes eye contact",
        "stares intensely when listening", "nods at everything said", "repeats the last word of sentences",
        "starts every sentence with 'Well...'", "ends questions with 'yes?'", "whispers when excited",
        "shouts when whispering would do", "laughs at inappropriate times", "cries during happy moments",
        "hums while working", "sings under their breath", "whistles complex melodies",
        "clicks their tongue when annoyed", "snorts when amused", "giggles nervously",
        "clears throat before speaking", "coughs to get attention", "sneezes when lying",
        "blushes when complimented", "turns pale when angry", "sweats when nervous",
        "twirls their hair around fingers", "braids and unbraids constantly", "adjusts their clothing obsessively",
        "polishes their weapons daily", "sharpens things when bored", "carves wood while talking",
        "draws in the dirt with sticks", "makes shadow puppets", "juggles random objects",
        "balances on narrow ledges", "climbs things unnecessarily", "always takes the high ground",
        "walks in perfect straight lines", "never steps on cracks", "avoids walking under things",
        "opens every door they pass", "looks behind every curtain", "investigates every noise",
        "tastes everything before eating", "smells books before reading", "touches textures compulsively",
        "collects shiny objects", "hoards useful items", "never throws anything away"
    ],
    
    "relationships_connections": [
        "owes a life debt to a stranger", "promised their dying mother something impossible", "sworn enemy of a childhood friend",
        "secretly related to a famous villain", "was engaged to someone they've never met", "has a twin they've never known",
        "trained by a legendary master", "betrayed their best friend for gold", "saved a prince in disguise",
        "shared a cell with a notorious criminal", "learned magic from a dying wizard", "inherited a cursed bloodline",
        "bound by oath to a mysterious order", "seeking revenge for a murdered sibling", "protecting the identity of a hero",
        "carrying a message for a dead man", "searching for their lost mentor", "fleeing from their own wedding",
        "hunting the beast that killed their village", "following clues left by their father", "guided by their grandmother's ghost",
        "competing with their perfect sibling", "trying to impress their disappointed parent", "living up to their ancestor's legend",
        "making amends to their former victim", "repaying kindness shown by a beggar", "fulfilling a promise to a dying enemy",
        "secretly funding an orphanage", "anonymously helping their hometown", "protecting their younger cousin",
        "corresponding with a foreign spy", "allied with an unlikely companion", "indebted to a crime lord",
        "blackmailed by someone from their past", "knows a terrible secret about a leader", "witnessed something they shouldn't have",
        "carrying letters for forbidden lovers", "smuggling refugees to safety", "hiding a political fugitive",
        "harboring a magical creature", "protecting an ancient artifact", "guarding a dangerous secret",
        "member of a secret society", "initiate of a mystery cult", "student of forbidden arts",
        "chosen champion of a minor god", "cursed by a spurned lover", "blessed by a grateful parent"
    ]
}

def create_spark_table(table_name: str, items: List[str]) -> pd.DataFrame:
    """Create a d100 table from a list of items."""
    # Pad or trim to exactly 100 items
    if len(items) > 100:
        items = items[:100]
    elif len(items) < 100:
        # Repeat items to fill 100 slots, cycling through
        while len(items) < 100:
            items.extend(items[:min(100-len(items), len(items))])
    
    # Create range strings
    ranges = [f"{i+1:02d}" for i in range(100)]
    
    df = pd.DataFrame({
        'd100 Roll': ranges,
        table_name.replace('_', ' ').title(): items
    })
    
    return df

def generate_character_spark(num_traits: int = 3) -> str:
    """Generate a random character spark by combining multiple tables."""
    spark_parts = []
    
    # Always include an adjective and background
    adjective = random.choice(SPARK_TABLES["evocative_adjectives"])
    background = random.choice(SPARK_TABLES["backgrounds_origins"])
    spark_parts.append(f"You are a **{adjective} {background}**")
    
    # Add random traits
    available_traits = ["distinctive_traits", "secret_motivations", "notable_possessions", 
                       "fears_weaknesses", "distinctive_mannerisms", "relationships_connections"]
    
    selected_traits = random.sample(available_traits, min(num_traits, len(available_traits)))
    
    for trait_type in selected_traits:
        trait = random.choice(SPARK_TABLES[trait_type])
        trait_name = trait_type.replace('_', ' ').title()
        spark_parts.append(f"**{trait_name}**: {trait}")
    
    return "\\n".join(spark_parts)

def create_all_spark_tables():
    """Create DataFrames for all spark tables."""
    tables = {}
    
    for table_name, items in SPARK_TABLES.items():
        tables[table_name] = create_spark_table(table_name, items)
    
    return tables

def save_spark_tables(base_filename: str = "character_spark_tables"):
    """Save all spark tables in multiple formats."""
    
    tables = create_all_spark_tables()
    
    # Save to Excel with multiple sheets
    with pd.ExcelWriter(f"{base_filename}.xlsx", engine='openpyxl') as writer:
        for table_name, df in tables.items():
            sheet_name = table_name.replace('_', ' ').title()[:31]  # Excel sheet name limit
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    # Generate LaTeX document with all tables
    latex_content = generate_spark_latex(tables)
    
    with open(f"{base_filename}_latex.tex", "w") as f:
        f.write(latex_content)
    
    # Save individual CSV files
    for table_name, df in tables.items():
        df.to_csv(f"{base_filename}_{table_name}.csv", index=False)
    
    print(f"Spark tables saved as:")
    print(f"  - {base_filename}.xlsx (Excel with {len(tables)} sheets)")
    print(f"  - {base_filename}_latex.tex (Complete LaTeX document)")
    print(f"  - Individual CSV files for each table")
    
    return tables

def generate_spark_latex(tables: Dict[str, pd.DataFrame]) -> str:
    """Generate a complete LaTeX document with all spark tables."""
    
    latex_header = r"""
\documentclass[11pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{fancyhdr}

\pagestyle{fancy}
\fancyhf{}
\rhead{Classic Fantasy Character Spark Tables}
\lfoot{\thepage}

\title{Character Spark Tables for Classic Fantasy RPG}
\author{Randomly Generated Inspiration}
\date{\today}

\begin{document}

\maketitle

\tableofcontents
\newpage

\section{Introduction}

These tables are designed to spark character inspiration rather than define complete personalities. Roll on one or more tables to generate interesting character concepts, background details, or roleplay hooks.

Each table contains 100 entries for d100 rolls. Mix and match results from different tables to create unique character concepts.

\section{How to Use These Tables}

\begin{itemize}
\item Roll on individual tables for specific inspiration
\item Combine results from multiple tables for complex characters  
\item Use as writing prompts for character backstories
\item Let results guide character development during play
\item Ignore results that don't fit your character concept
\end{itemize}

\newpage
"""
    
    latex_content = latex_header
    
    for table_name, df in tables.items():
        section_name = table_name.replace('_', ' ').title()
        latex_content += f"\n\\section{{{section_name}}}\n\n"
        
        # Create a more compact table format for the spark tables
        latex_table = df.to_latex(
            index=False,
            escape=False,
            longtable=True,
            column_format='|c|p{4in}|'
        )
        
        # Clean up LaTeX formatting
        latex_table = latex_table.replace('\\toprule', '\\hline')
        latex_table = latex_table.replace('\\midrule', '\\hline')
        latex_table = latex_table.replace('\\bottomrule', '\\hline')
        latex_table = latex_table.replace('longtable', 'longtable')
        
        latex_content += latex_table + "\n\\newpage\n"
    
    latex_content += "\n\\end{document}"
    
    return latex_content

def interactive_spark_generator():
    """Interactive character spark generator."""
    print("=== CHARACTER SPARK GENERATOR ===")
    print()
    
    while True:
        print("Options:")
        print("1. Generate random character spark")
        print("2. Roll on specific table")  
        print("3. Generate multiple sparks")
        print("4. Save all tables to files")
        print("5. Exit")
        
        choice = input("\nChoose option (1-5): ").strip()
        
        if choice == '1':
            num_traits = int(input("How many additional traits? (1-6): ") or "3")
            spark = generate_character_spark(num_traits)
            print(f"\n{spark}\n")
            
        elif choice == '2':
            print("\nAvailable tables:")
            for i, table_name in enumerate(SPARK_TABLES.keys(), 1):
                print(f"{i}. {table_name.replace('_', ' ').title()}")
            
            table_choice = int(input("Choose table number: ")) - 1
            table_name = list(SPARK_TABLES.keys())[table_choice]
            roll = random.randint(1, 100)
            result = SPARK_TABLES[table_name][roll-1]
            print(f"\nRolled {roll}: {result}\n")
            
        elif choice == '3':
            num_sparks = int(input("How many character sparks? ") or "5")
            for i in range(num_sparks):
                print(f"\n--- CHARACTER SPARK #{i+1} ---")
                spark = generate_character_spark(3)
                print(spark)
            print()
            
        elif choice == '4':
            save_spark_tables()
            
        elif choice == '5':
            break
        
        input("Press Enter to continue...")
        print()

if __name__ == "__main__":
    # Run the interactive generator
    interactive_spark_generator()