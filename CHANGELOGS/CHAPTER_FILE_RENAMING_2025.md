# Chapter File Renaming - December 2025

## Summary
Renamed all Prologue and Part 1 chapter files to include their quote-based titles in the filename.

## New Naming Convention

**Format:** `[Part]-[Chapter#]-[Quote_Title].md`

Where:
- `[Part]` = `00-Prolog` or `01-Part1`
- `[Chapter#]` = Two-digit number (01, 02, etc.)
- `[Quote_Title]` = Chapter quote title with spaces replaced by underscores, special characters removed/replaced

---

## Prologue Files Renamed

| Old Filename | New Filename |
|--------------|--------------|
| `Prologue-01_The_Ritual.md` | `00-Prolog-01-Not_you_Not_this_Wrong_pattern_Wrong_time.md` |
| `Prologue-02_The_Observation.md` | `00-Prolog-02-I_want_to_understand_it_before_it_decides_we_dont_matter.md` |
| `Prologue-03_Awakening_and_Escape.md` | `00-Prolog-03-Youre_not_broken_Youre_filtered.md` |

**Directory:** `New Chapters\00 Prologue\`

---

## Part 1 Files Renamed

| Old Filename | New Filename |
|--------------|--------------|
| `P1-01_Resonance.md` | `01-Part1-01-I_really_need_to_go_to_bed.md` |
| `P1-02_Resonant_Recognition.md` | `01-Part1-02-Do_not_overwrite.md` |
| `P1-03_No_Plans_No_Pressure.md` | `01-Part1-03-Youre_not.md` |
| `P1-04_Routine_Noise.md` | `01-Part1-04-And_then_what.md` |
| `P1-05_Echoes.md` | `01-Part1-05-This_time_he_listened.md` |
| `P1-06_Night_Thoughts.md` | `01-Part1-06-What_if_I_was_meant_to_and_never_did.md` |
| `P1-07_Steam_and_Smalltalk.md` | `01-Part1-07-Learning_to_fly.md` |
| `P1-08_Unspoken.md` | `01-Part1-08-Some_doors_stay_locked_for_a_reason.md` |
| `P1-09_First_Contact.md` | `01-Part1-09-Choice_is_sacred.md` |
| `P1-10_Learning_Curve.md` | `01-Part1-10-I_merely_guided.md` |
| `P1-11_Digital_Ghosts.md` | `01-Part1-11-Found_or_found_by.md` |
| `P1-12_The_Meeting.md` | `01-Part1-12-A_question_thats_still_alive.md` |
| `P1-13_Grey_Mornings.md` | `01-Part1-13-Something_that_matters.md` |
| `P1-14_Marker_at_Home.md` | `01-Part1-14-I_wont_let_them.md` |
| `P1-15_Watchers.md` | `01-Part1-15-Do_you_trust_me.md` |
| `P1-16_The_Storm.md` | `01-Part1-16-Me_too.md` |
| `P1-17_Between_Storm_and_Step.md` | `01-Part1-17-Because_knowing_who_were_hiding_from_is_kind_of_important.md` |

**Directory:** `New Chapters\01 - Part1\`

---

## Part 2 Files Renamed

| Old Filename | New Filename |
|--------------|--------------|
| `P2-01_Kettle_Lessons.md` | `02-Part2-01-Red_stops_No_exceptions.md` |
| `P2-02_Scaffold_and_Consequences.md` | `02-Part2-02-You_saved_them_but_you_almost_died.md` |
| `P2-03_Recovery_and_Rules.md` | `02-Part2-03-Smart_choices_not_heroic_ones.md` |
| `P2-04_Scouting_the_Mill.md` | `02-Part2-04-She_knows_something_we_dont.md` |
| `P2-05_First_Lessons_with_Elyra.md` | `02-Part2-05-Integration_is_permanent.md` |
| `P2-06_The_Whisper_Clips.md` | `02-Part2-06-Max_three_channels_Thats_the_limit.md` |
| `P2-07_Resonogram_Cluster.md` | `02-Part2-07-Green_to_yellow_never_to_red.md` |
| `P2-08_Forbidden_Maps.md` | `02-Part2-08-Precision_over_power.md` |
| `P2-09_Malveks_Agent.md` | `02-Part2-09-Were_offering_protection.md` |
| `P2-10_Archive_Sabotage.md` | `02-Part2-10-Destroy_everything.md` |
| `P2-11_Resonance_Market.md` | `02-Part2-11-Theyre_watching_now.md` |
| `P2-12_Convergence.md` | `02-Part2-12-Every_choice_has_weight.md` |
| `P2-13_Into_the_Network.md` | `02-Part2-13-This_is_Mill-4.md` |
| `P2-14_Acceleration.md` | `02-Part2-14-Forty_percent_Thats_permanent.md` |
| `P2-15_The_Reckoning.md` | `02-Part2-15-Containment_teams_are_coming.md` |

**Directory:** `New Chapters\02 - Part2\`

**Additional fixes:**
- Corrected chapter numbers in headers (Ch. 04-15) to match filename numbers
- Fixed P2-12 title from "Destroy everything" to "Every choice has weight"

---

## Character Replacements

Special characters were handled as follows:
- **Spaces** ? Underscore (`_`)
- **Apostrophes** (`'`) ? Removed or replaced with empty string
- **Commas** (`,`) ? Removed
- **Question marks** (`?`) ? Removed  
- **Periods** (`.`) ? Removed
- **Quotes** (`"`) ? Removed

**Examples:**
- `"You're not"` ? `Youre_not`
- `"What if I was meant to, and never did?"` ? `What_if_I_was_meant_to_and_never_did`
- `"I won't let them"` ? `I_wont_let_them`

---

## Benefits

? **Self-documenting:** Filename immediately shows chapter content
? **Consistent format:** All files follow same pattern
? **Sortable:** Files sort correctly by part and chapter number
? **Searchable:** Can search by quote keywords in filename
? **Professional:** Clear, organized structure

---

## Verification

**Prologue:**
```powershell
Get-ChildItem "New Chapters\00 Prologue" -Filter "*.md" | Measure-Object
# Count: 3 ?
```

**Part 1:**
```powershell
Get-ChildItem "New Chapters\01 - Part1" -Filter "*.md" | Measure-Object
# Count: 17 ?
```

**Part 2:**
```powershell
Get-ChildItem "New Chapters\02 - Part2" -Filter "*.md" | Measure-Object
# Count: 15 ?
```

**Total renamed:** 35 files

---

## Files NOT Renamed

The following remain unchanged (not chapter files):
- Feedback files in `Feedbacks\` directory
- Documentation files in `General\` and `CHANGELOGS\`

---

## Summary

**Total files renamed:** 35
- Prologue: 3 files
- Part 1: 17 files  
- Part 2: 15 files

**Additional fixes:**
- Part 2 chapter numbers corrected in file headers (Ch. 04-15)
- Part 2 Ch. 12 title corrected from "Destroy everything" to "Every choice has weight"

---

**Date:** December 2025  
**Files Renamed:** 35 (3 Prologue + 17 Part 1 + 15 Part 2)  
**Status:** Complete and verified  
**Format:** `[Part]-[Chapter#]-[Quote_Title].md`
