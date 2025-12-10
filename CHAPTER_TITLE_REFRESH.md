# CHAPTER TITLE REFRESH - Quote-Based Titles

## Concept

Replace generic chapter titles with **memorable quotes from the chapters themselves**. Ideally dialogue that has dual meaning: literal in context, thematic when isolated.

**Exceptions:** Prologue and Epilogue keep their names.

---

## Part 1: Lost and Found (16 chapters after Prologue extraction)

### Current Structure:
- **Prologue** ? Moved to `Prologue_The_Ritual.md` (separate file)
- P1-01: Prologue (OLD) ? **DELETED**
- P1-02: Resonance ? **Becomes P1-01**
- P1-03-17 ? **Renumber to P1-02-16**

### Renumbering Plan:

| Old File | New File | Suggested Quote Title |
|----------|----------|----------------------|
| ~~P1-01_Prologue.md~~ | *Extracted* | Prologue - The Ritual |
| P1-02_Resonance.md | **P1-01** | *"What if I was meant to, and never will?"* |
| P1-03_The_Archive.md | **P1-02** | *"Some records aren't meant to be found"* |
| P1-04_No_Plans_No_Pressure.md | **P1-03** | *"No plans, no pressure"* ? (already good!) |
| P1-05_First_Practice.md | **P1-04** | *"Start with something already broken"* |
| P1-06_Integration.md | **P1-05** | *"This is permanent, Jason"* |
| P1-07_Night_Thoughts.md | **P1-06** | *"What if I'm not enough?"* |
| P1-08_Small_Changes.md | **P1-07** | *"Small, careful changes"* ? |
| P1-09_Questions.md | **P1-08** | *"Why me?"* |
| P1-10_First_Contact.md | **P1-09** | *"Consent precedes action"* |
| P1-11_Progress.md | **P1-10** | *"You're learning faster than I expected"* |
| P1-12_Digital_Ghosts.md | **P1-11** | *"Mirror.Vox doesn't exist"* |
| P1-13_The_Meeting.md | **P1-12** | *"I'm Milo. And you're real."* |
| P1-14_Thresholds.md | **P1-13** | *"Yellow means caution, not stop"* |
| P1-15_Watchers.md | **P1-14** | *"Someone's paying attention"* |
| P1-16_Marker_at_Home.md | **P1-15** | *"They marked my door"* |
| P1-17_The_Storm.md | **P1-16** | *"Run. Now."* |

---

## Part 3: Negotiation & Revelation (15 chapters)

### Duplicate Title Issue:
- **P3-15: New Equilibrium** 
- **P4-14: New Equilibrium** ? DUPLICATE!

### Suggested Renames:

| Current Title | Suggested Quote Title | Rationale |
|--------------|----------------------|-----------|
| P3-15: New Equilibrium | **"Partnership can work better than control"** | Malvek's realization, thematic |
| P4-14: New Equilibrium | **"This is what we were meant for"** | Jason/RAE reflecting on purpose |

---

## Part 4: Expansion & Responsibility (15 chapters)

### Current Titles to Refresh:

| Chapter | Current Title | Suggested Quote Title |
|---------|--------------|----------------------|
| P4-01 | New Beginning | **"We're going to teach"** |
| P4-02 | First Student & Learning | **"You're not me. You need your own path."** |
| P4-03 | Lina & Jason | **"RAE comes with the package"** |
| P4-04 | Graduation | **"To competence over power"** |
| P4-05 | International Contact | **"Some things cannot be reformed"** |
| P4-06 | Cultural Exchange | **"Or because I'm broken enough to say yes"** |
| P4-07 | The Warning | **"This isn't containment. This is combat."** |
| P4-08 | Tokyo Underground | **"There's no reforming this"** |
| P4-09 | Confrontation | **"Some things must be unmade"** |
| P4-10 | Aftermath | **"Changed, but okay"** |
| P4-11 | Building Legacy | **"That requires more than good intentions"** |
| P4-12 | Integration Milestone | **"I'm not losing myself. I'm becoming more."** |
| P4-13 | The Proposal | **"Family. Yeah. That's what we are."** |
| P4-14 | New Equilibrium | **"This is what we were meant for"** |
| P4-15 | Epilogue | **Epilogue** ? (exception) |

---

## Implementation Plan

### Option A: Rename Files (Complex)
- Rename all Part 1 files (P1-02 ? P1-01, etc.)
- Update all cross-references in outlines
- Risk: Git history confusion

### Option B: Update Markdown Titles Only (Simpler)
- Keep file names as-is (P1-02_Resonance.md)
- Change **only** the `# Chapter Title` inside each file
- Update outlines to reference new titles
- Advantage: Clean Git history, easier to track

### Recommendation: **Option B**

Keep filenames stable, update internal chapter titles with quotes.

---

## Example Implementation (P1-02 ? P1-01 after Prologue extraction)

### File: `P1-02_Resonance.md` (will be considered Chapter 01 after Prologue extraction)

**OLD:**
```markdown
# Ch. 02 - Resonance
```

**NEW:**
```markdown
# Ch. 01 - "What if I was meant to, and never will?"

[Rest of content unchanged]
```

---

## Duplicate Resolution

### P3-15 & P4-14 both titled "New Equilibrium"

**P3-15_New_Equilibrium.md:**
```markdown
# Ch. 15 - "Partnership can work better than control"
```
*Malvek's quote when offering permanent truce*

**P4-14_New_Equilibrium.md:**
```markdown
# Ch. 14 - "This is what we were meant for"
```
*Jason-RAE reflecting on teaching purpose*

---

## Next Steps

1. ? Extract Prologue (DONE)
2. ? Delete old P1-01_Prologue.md (DONE)
3. ? Update Part 1 chapter numbers (Ch. 02?01, etc.)
4. ? Replace chapter titles with quotes
5. ? Update all outlines to reflect changes
6. ? Update MASTER_SUMMARY.md
7. ? Git commit with clear message

---

## Benefits of Quote-Based Titles

? **More memorable** - Readers recall quotes  
? **Thematic resonance** - Title hints at chapter's core  
? **Professional touch** - Common in literary fiction  
? **Contextual depth** - Quote means more after reading  
? **Unique identity** - No more generic "Chapter 5"  

---

**Status:** Plan created, awaiting implementation  
**Priority:** Medium (enhances experience, not critical)  
**Complexity:** Low (markdown title changes only)