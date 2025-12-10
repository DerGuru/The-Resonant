# RENUMBERING & TITLE REFRESH - STATUS

## ? COMPLETED

### Part 1: Renumbering (After Prologue Extraction)
- ? Prologue extracted to `Prologue_The_Ritual.md`
- ? P1-01_Prologue.md deleted
- ? All files renumbered P1-01 through P1-16
- ? Duplicates resolved

**Final Structure (16 chapters):**
1. P1-01_Resonance.md
2. P1-02_Resonant_Recognition.md
3. P1-03_No_Plans_No_Pressure.md
4. P1-04_Routine_Noise.md
5. P1-05_Echoes.md
6. P1-06_Night_Thoughts.md
7. P1-07_Steam_and_Smalltalk.md
8. P1-08_Unspoken.md
9. P1-09_First_Contact.md
10. P1-10_Learning_Curve.md
11. P1-11_Digital_Ghosts.md
12. P1-12_The_Meeting.md
13. P1-13_Grey_Mornings.md
14. P1-14_Marker_at_Home.md
15. P1-15_Watchers.md
16. P1-16_The_Storm.md

---

## ? REMAINING TASKS

### 1. Update Chapter Titles with Quotes

**Inside each markdown file**, replace chapter titles with quote-based versions.

**Example (P1-01_Resonance.md):**
```markdown
# Ch. 01 - "What if I was meant to, and never will?"
```

**Full list:** See CHAPTER_TITLE_REFRESH.md

### 2. Resolve P3-15 & P4-14 Duplicate Titles

Both are currently titled "New Equilibrium" - needs differentiation.

**Recommended:**
- P3-15: Keep filename, update title ? **"Partnership can work better than control"**
- P4-14: Keep filename, update title ? **"This is what we were meant for"**

### 3. Update All Outlines

Files to update:
- PART1_OUTLINE.md (16 chapters now)
- PART3_OUTLINE.md (note title change)
- PART4_OUTLINE.md (note title change)
- MASTER_SUMMARY.md (16 chapters Part 1)

### 4. Final Git Commit

After all changes:
```sh
git add .
git commit -m "Major restructure: Prologue extracted, Part 1 renumbered (17?16 chapters), quote-based titles planned

CHANGES:
- Prologue extracted to separate file (Prologue_The_Ritual.md)
- Part 1: P1-01 deleted, P1-02?P1-17 renumbered to P1-01?P1-16
- Duplicates resolved (P1-12, P1-15)
- Chapter title refresh planned (quote-based)
- P3-15 & P4-14 duplicate titles identified

STRUCTURE:
- Prologue: 1 file (separate)
- Part 1: 16 chapters (was 17)
- Part 2: 18 chapters (unchanged)
- Part 3: 15 chapters (unchanged)
- Part 4: 15 chapters (unchanged)
- Total: 64 chapters + Prologue

STATUS: Files renamed, titles to be updated in next step"

git push origin main
```

---

## QUOTE-BASED TITLES - Quick Reference

### Part 1 (16 chapters)
1. "What if I was meant to, and never will?"
2. "Some records aren't meant to be found"
3. "No plans, no pressure"
4. "Start with something already broken"
5. "This is permanent, Jason"
6. "What if I'm not enough?"
7. "Small, careful changes"
8. "Why me?"
9. "Consent precedes action"
10. "You're learning faster than I expected"
11. "Mirror.Vox doesn't exist"
12. "I'm Milo. And you're real."
13. "Yellow means caution, not stop"
14. "They marked my door"
15. "Someone's paying attention"
16. "Run. Now."

### Part 3 Title Change
- P3-15: "Partnership can work better than control" (was: New Equilibrium)

### Part 4 Title Change  
- P4-14: "This is what we were meant for" (was: New Equilibrium)

---

## Next Steps

**Option A: Update titles manually**
- Open each file
- Change `# Ch. XX - [Title]` to quote-based version
- Time: ~30 minutes for all files

**Option B: Script-based update**
- Create PowerShell script to update all titles
- Faster but requires testing

**Option C: Do in next session**
- Commit current file renaming
- Update titles in fresh session

---

**Recommendation:** Commit file renaming NOW, update titles in next session (cleaner Git history)

---

**Status:** Files renumbered ? | Titles pending ? | Ready for commit