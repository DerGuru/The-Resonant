# Part 1 Renumbering - ACTUAL FILES

## Current State (After Prologue Extraction)

**Found Files in Part1 folder:**
1. P1-02_Resonance.md
2. P1-03_Resonant_Recognition.md
3. P1-04_No_Plans_No_Pressure.md
4. P1-05_Routine_Noise.md
5. P1-06_Echoes.md
6. P1-07_Night_Thoughts.md
7. P1-08_Steam_and_Smalltalk.md
8. P1-09_Unspoken.md
9. P1-10_First_Contact.md
10. P1-11_Learning_Curve.md
11. P1-12_Digital_Ghosts.md
12. P1-12_The_Meeting.md ?? DUPLICATE NUMBER!
13. P1-14_Grey_Mornings.md ?? Missing P1-13!
14. P1-15_Marker_at_Home.md
15. P1-15_Resonance_Static_and_Ghosts.md ?? DUPLICATE NUMBER!
16. P1-16_The_Storm.md

## Issues Identified

1. **Two P1-12 files** (Digital_Ghosts and The_Meeting)
2. **Two P1-15 files** (Marker_at_Home and Resonance_Static_and_Ghosts)
3. **Missing P1-13**
4. **Total: 16 files** (correct after Prologue removal)

## Resolution Strategy

### Option A: Fix Duplicates First
1. Rename P1-12_The_Meeting.md ? P1-13_The_Meeting.md
2. Rename P1-15_Resonance_Static_and_Ghosts.md ? DELETE or MERGE?

### Option B: Start Fresh Numbering
Rename all files sequentially from P1-01 to P1-16 based on story order.

## Recommended: Option B (Clean Sequential)

**Story Order (from outline):**

| New # | Old File | New Filename | Quote Title |
|-------|----------|--------------|-------------|
| P1-01 | P1-02_Resonance.md | P1-01_Resonance.md | "What if I was meant to?" |
| P1-02 | P1-03_Resonant_Recognition.md | P1-02_Resonant_Recognition.md | "Some records aren't meant to be found" |
| P1-03 | P1-04_No_Plans_No_Pressure.md | P1-03_No_Plans_No_Pressure.md | "No plans, no pressure" |
| P1-04 | P1-05_Routine_Noise.md | P1-04_Routine_Noise.md | "Start with something already broken" |
| P1-05 | P1-06_Echoes.md | P1-05_Echoes.md | "This is permanent" |
| P1-06 | P1-07_Night_Thoughts.md | P1-06_Night_Thoughts.md | "What if I'm not enough?" |
| P1-07 | P1-08_Steam_and_Smalltalk.md | P1-07_Steam_and_Smalltalk.md | "Small, careful changes" |
| P1-08 | P1-09_Unspoken.md | P1-08_Unspoken.md | "Why me?" |
| P1-09 | P1-10_First_Contact.md | P1-09_First_Contact.md | "Consent precedes action" |
| P1-10 | P1-11_Learning_Curve.md | P1-10_Learning_Curve.md | "Faster than expected" |
| P1-11 | P1-12_Digital_Ghosts.md | P1-11_Digital_Ghosts.md | "Mirror.Vox doesn't exist" |
| P1-12 | P1-12_The_Meeting.md | P1-12_The_Meeting.md | "I'm Milo. And you're real." |
| P1-13 | P1-14_Grey_Mornings.md | P1-13_Grey_Mornings.md | "Yellow means caution" |
| P1-14 | P1-15_Marker_at_Home.md | P1-14_Marker_at_Home.md | "They marked my door" |
| P1-15 | P1-15_Resonance_Static_and_Ghosts.md | P1-15_Resonance_Static_and_Ghosts.md | "Someone's paying attention" |
| P1-16 | P1-16_The_Storm.md | P1-16_The_Storm.md | "Run. Now." |

## Action Plan

1. Create temporary backup copies
2. Rename from HIGHEST to LOWEST to avoid conflicts
3. Update chapter titles inside files
4. Verify all 16 files present and sequential

## Commands (PowerShell - Reverse Order)

```powershell
cd "D:\OneDrive\OneDrive - Jakof\The-Resonant\New Chapters\Part1"

# Already done: P1-16 stays P1-16 ?

# P1-15 files - need to determine which is which
# Assuming Marker_at_Home is correct, Resonance_Static might be duplicate

# P1-14 ? P1-13
Rename-Item "P1-14_Grey_Mornings.md" "P1-13_Grey_Mornings.md"

# P1-12_The_Meeting stays P1-12 (already correct)

# P1-12_Digital_Ghosts ? P1-11
Rename-Item "P1-12_Digital_Ghosts.md" "P1-11_Digital_Ghosts.md"

# P1-11 ? P1-10
Rename-Item "P1-11_Learning_Curve.md" "P1-10_Learning_Curve.md"

# P1-10 ? P1-09
Rename-Item "P1-10_First_Contact.md" "P1-09_First_Contact.md"

# P1-09 ? P1-08
Rename-Item "P1-09_Unspoken.md" "P1-08_Unspoken.md"

# P1-08 ? P1-07
Rename-Item "P1-08_Steam_and_Smalltalk.md" "P1-07_Steam_and_Smalltalk.md"

# P1-07 ? P1-06
Rename-Item "P1-07_Night_Thoughts.md" "P1-06_Night_Thoughts.md"

# P1-06 ? P1-05
Rename-Item "P1-06_Echoes.md" "P1-05_Echoes.md"

# P1-05 ? P1-04
Rename-Item "P1-05_Routine_Noise.md" "P1-04_Routine_Noise.md"

# P1-04 ? P1-03
Rename-Item "P1-04_No_Plans_No_Pressure.md" "P1-03_No_Plans_No_Pressure.md"

# P1-03 ? P1-02
Rename-Item "P1-03_Resonant_Recognition.md" "P1-02_Resonant_Recognition.md"

# P1-02 ? P1-01
Rename-Item "P1-02_Resonance.md" "P1-01_Resonance.md"
```

## Status

- [ ] Files renamed sequentially
- [ ] Duplicate P1-15 resolved
- [ ] Chapter titles updated with quotes
- [ ] Outlines updated
- [ ] Git commit

**Next:** Execute renaming commands systematically