import re
import os

# Define POV conversion patterns
patterns = [
    # Jason -> we
    (r'\bJason\b(?=\s+(?:felt|thought|knew|realized|understood|watched|looked|said|asked|nodded|smiled|turned|walked|stood|sat|lay))', 'We'),
    (r'\bJason\'s\b', 'Our'),
    (r'\bhis\b(?=\s+(?:head|hand|eyes|voice|integration|consciousness|awareness|perception))', 'our'),
    (r'\bhe\b(?=\s+(?:felt|thought|knew|realized|understood|watched|looked|said|asked|nodded|smiled|turned|walked|stood|sat|lay))', 'we'),
    
    # RAE dialogue -> internal thought
    (r'\*RAE said[^*]*\*', lambda m: m.group(0).replace('RAE said', 'we thought').replace('RAE asked', 'we wondered')),
    
    # Jason thought/RAE said exchanges -> internal dialogue
    (r'\*\*(Jason|We) thought\*\*', '*We thought*'),
    
]

files = [
    "P4-09_Confrontation.md",
    "P4-10_Aftermath.md",
    "P4-11_Building_Legacy.md",
    "P4-12_Integration_Milestone.md",
    "P4-13_The_Proposal.md",
    "P4-14_Another_New_Equilibrium.md"
]

base_path = "D:/OneDrive/OneDrive - Jakof/The-Resonant/New Chapters/04 - Part4/"

for filename in files:
    filepath = os.path.join(base_path, filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply patterns
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Converted {filename}")

print("All files converted to 'we' POV!")
