# Verification Report — Seven-Pass Repair Operation

**Date:** 2026-05-17
**Wiki files audited:** 238 markdown files across `wiki/`
**Method:** Source-PDF spot-checks via `extract.py` (pdfplumber), dead-link audit via Python crawler, format sampling, naming-collision grep.

---

## Overall: **GREEN with one RED ITEM**

One critical file truncation found (Sepulchre adventure). Everything else holds up. Recommend the user fix the Sepulchre file before treating the repair operation as complete.

---

## A. Source Spot-Checks

| # | Pass | File checked | Source verified | Result |
|---|---|---|---|---|
| 1 | Classes | `wiki/classes/Fanged Deserter.md` | Bare Bones pp.46–47 | PASS |
| 2 | Tables | `wiki/tables/Adventure Seeds.md` | Bare Bones p.69 (Who d20 + Why d100 entries 13–20, 1–22) | PASS |
| 3 | Cosmic NPC | `wiki/npcs/Verhu.md` | Bare Bones p.69–70 (seed 21–22 and seed 69–70 cited in file both verified verbatim in source) | PASS |
| 4 | Per-entry fix | `wiki/npcs/Lesdy.md` | Rotblack Sludge | PASS with minor drift |
| 5 | Dungeon | `wiki/adventures/Sepulchre of the Swamp Witch.md` | MBC Sepulchre pp.2–13 | **FAIL — TRUNCATED** |
| 6 | GLW | `wiki/creatures/Übertaker.md` | Graves Left Wanting p.17 | PASS |
| 7a | EPK creature | `wiki/creatures/Antideer.md` | Eat-Prey-Kill p.4 | PASS |
| 7b | EPK creature | `wiki/creatures/Skelelk.md` | Eat-Prey-Kill p.5 | PASS |
| 7c | EPK creature | `wiki/creatures/Übertaker.md` (verify it is NOT EPK) | EPK p.13 confirms only Überwolf exists in EPK | PASS — naming decision correct |

### Detail per spot-check

**1. Fanged Deserter** — All Abilities verified verbatim (3d6+2 STR, 3d6−1 AGI/PRE, dr14 Agility tests, illiterate). Gear table d6 fully matches source — Brown Scimitar (sepsis 1-in-6, 10 min), Wizard Teeth (4 dice, max dmg on 6), Old Sigûrd's Sling (2d4), gore-hound (dr10/dr12/10hp), shoe of Death's Horse (dr10, d4, 1-in-6 instakill). Bite attack, HP formula, starting Omens — all correct.

**2. Adventure Seeds** — Who d20 entries 13–20 verified verbatim against source p.69. Why d100 entries 1–22 verified — including `Verhu's prophecy is false!` at 21–22 and `Children missing at Lake Onda` at 9–10. Where d12 not re-verified but structure intact.

**3. Verhu cosmic NPC** — The two adventure-seed cross-references in the file body (`adventure seed 69–70: "HE demands a gift. See it delivered"` and `seed 21–22: "Verhu's prophecy is false!"`) both exist in source verbatim. Bare Bones p.10–11 framing of Verhu as Prophecy head and 7:7 misery reference are accurate to canon.

**4. Lesdy** — Stat blocks correct: HP 5, Morale 4, No armor for Lesdy; HP 7, Morale —, Long knives d6 for the three hosts. Greenhouse description, brew/hallucination trigger, host chant ("Lesdy… Lusi… Lesdy… the chosen, the delightful!") all accurate. **Minor drift:** wiki says Lesdy "carries no listed weapon — she fights through her hosts," but source gives her *"Unarmed attack d4"*. The wiki's narrative framing is correct (she slinks away on violence) but the d4 unarmed line was dropped.

**5. Sepulchre** — **FAIL.** File is only 2,319 bytes / 27 lines. After header, rumours table, cult intro, and the EV path notation, it terminates mid-sentence inside Chamber 1: `- Stone gate standing in 5` and ends. Chambers 2–11, the Dead Root Altar payoff, the Ueth stat block, and the cult finale are all missing. The source PDF has 11 chambers across pp.4–13. **This is the most serious finding in the repair operation.** Likely a write/truncation error during pass 5.

**6. Übertaker (GLW)** — d4 action table verified verbatim against Graves Left Wanting p.17:
- 1 SCOURGE TAKE YOU (d4 melee)
- 2 BEHOLD THE POWER (max dmg)
- 3 NO REPROACH ANSWERS (random creature, DR14 def, d6)
- 4 REST IS NOW (DR14 STR or d8 + prone)

HP 27, Morale −, Barrier (palefire) −d4 all correct. Unclean Scroll mechanic and healing-inverts-damage clause both present and accurate.

**7. EPK creatures** —
- **Antideer** — HP 7, Morale 6, Tough skin −d2, Antlers d6, DR12 Presence test on consumption, −1 PRE on fail. Verbatim.
- **Skelelk** — HP 9, Morale 8, Exoskeleton −d6, Antlers d6, blunt weapons max-dmg rule. Verbatim. Group size d4 verified.
- **Übertaker vs Überwolf** — EPK Bergen Chrypt entry on p.13 is the **Überwolf** (HP 18, Thick fur −d2, Bite/Claws d8, with d6+ regular wolves). No EPK Übertaker exists. The naming decision is correct.

---

## B. Dead-Link Audit

**Total files with dead links:** 66
**Total unique dead link targets:** 112

These are pre-existing AND newly-introduced. Crawler treats `[[X]]` as dead unless `wiki/**/X.md` exists by basename. Obsidian's loose H1-title matching saves a handful (e.g., `[[The Übertaker]]` resolves to `Übertaker.md` via H1), but most listed below are genuinely unresolved.

### Per-entry-fix-introduced links (the prompt's focus group)

All listed by the prompt are unresolved:

| Target | Files | Status |
|---|---|---|
| `Klefunheim` | `wiki/locations/Galgenbeck.md`, `wiki/locations/Tveland.md` | UNRESOLVED |
| `Jota Klefunheim` | `wiki/locations/Galgenbeck.md`, `wiki/locations/Tveland.md` | UNRESOLVED |
| `Tongue-shaped Knife` | `wiki/npcs/Silas the Fattened King.md` | UNRESOLVED |
| `Urgrip Wikt` | `wiki/locations/Galgenbeck.md` | UNRESOLVED |
| `Arga` | `wiki/locations/Galgenbeck.md`, `wiki/npcs/The Deadn't.md`, `wiki/npcs/The Undertaker.md` | UNRESOLVED |
| `Benzen` | `wiki/npcs/The Deadn't.md`, `wiki/npcs/The Undertaker.md` | UNRESOLVED |
| `Stein` | `wiki/npcs/The Deadn't.md`, `wiki/npcs/The Undertaker.md` | UNRESOLVED |
| `The Undertaker's Hut` / `Undertaker's Hut` | 5 files | UNRESOLVED |
| `The Übertaker` | 4 files | Resolves to `Übertaker.md` via H1 (technically OK) |

### Dead links by source file (selected — full list above in conversation log)

**Adventures**
- `Death Ziggurat.md` → `Frozen Lake`
- `Devil's Tomb.md` → `Angelic Choir`, `Madman`, `Pit to Hell`
- `Eat-Prey-Kill.md` → `Earthbound`
- `Graves Left Wanting.md` → `Rotted Skeleton`, `Widow-wraith`
- `Rotblack Sludge.md` → `Distraught Spirit`, `Tired Crystal Demon`
- `Sepulchre of the Swamp Witch.md` → `Dead Root Altar` (file truncated — incomplete content also expected)

**Classes** (all class gear/companion links — these are expected expansion seeds, not bugs)
- `Esoteric Hermit.md` → 4 links (Berserker-Slayers, Book of Boiling Blood, Cliffs of Terion, Invisible College)
- `Fanged Deserter.md` → 6 links (Brown Scimitar, Old Sigûrd's Sling, Shoe of Death's Horse, Sigûrd, Wizard Teeth, Wästland)
- `Forlorn Philosopher.md` → 5 links
- `Heretical Priest.md` → 4 links
- `Occult Herbmaster.md` → 6 links
- `Sacrilegious Songbird.md` → 6 links
- `Wretched Royalty.md` → 9 links

**Creatures** — mostly thematic expansion seeds. Notable: 6 separate creatures link to `Wästland` (not a wiki page; canon spelling is `Wästland` — check if there should be a stub location page).

**Locations**
- `Galgenbeck.md` → `Arga`, `Jota Klefunheim`, `Klefunheim`, `Urgrip Wikt` (newly introduced by per-entry fix)
- `Graven-Tosk.md` → `Undertaker's Hut`
- `Tveland.md` → `Jota Klefunheim`, `Klefunheim`

**Items**
- `Merchant Inventory.md` → 25+ inventory-item dead links (Bright Yellow Flower, Chip the Rat, Galgenbeck Deathmask, Pilgrim's Compass, Tongue of a False Prophet, Wickhead Brain, etc.) — these mirror Mikhael's inventory and form a single expansion pool.

**NPCs**
- `Erhard.md` → `Erhard's Tomb`, `The Plague Pit`
- `Fela Maus.md` → 4 links
- `Fletcher.md` → 3 Power-name links (Daemon of Capillaries, Ich-bin-luft, Nine Violet Signs Unknot the Storm)
- `Mikhael the Merchant.md` → 11 inventory item links
- `Silas the Fattened King.md` → `Tongue-shaped Knife` (per-entry fix)
- `Srolki & Yaoxl.md` → 5 Power/item links
- `Swamp Witch.md` → `Dead Root Altar`
- `The Deadn't.md` / `The Undertaker.md` → `Arga`, `Benzen`, `Stein` (the trio's three named members)
- `Ueth.md` → `Slithering Strangulation`

**Wästland repeated dead link** appears in 9 files (Bautaboar, Feather Fox, Filth-crow, Liar-bird, Three-thirds-pheasant, Schleswig Bog-feeder, Wretched Royalty, Fanged Deserter, Fela Maus, Merchant Inventory, Mikhael). Strong candidate for a stub location page.

**Powers as dead links** — Several class gear/spell entries link to specific Powers (Daemon of Capillaries, Nine Violet Signs Unknot the Storm, Roskoe's Consuming Glare, Metzhuotl Blind Your Eye, Ich-bin-luft, Slithering Strangulation). Source has these as Powers in the rules. A `wiki/powers/` directory may be missing entirely.

---

## C. Format Check

Sampled: `Dead Gods.md`, `Forgotten Mind-Cult.md`, `Antideer.md`, `Gorgh.md`, `Troubling Tales.md`, `Skelelk.md`, `Übertaker.md`, `King Lenard II.md`, `HE.md`.

| Requirement | Status |
|---|---|
| `# Name` H1 | All compliant |
| `**Type:**` line | All compliant |
| `**Source:** [PDF, page]` | All compliant; cosmic NPCs and tables use compound source citations consistently |
| Stat block (creatures) | Correct format `HP X, Morale X, [armor], [attack]` matching source convention |
| `**Connections:**` section | Present on all sampled files |
| `**Gaps/Expansion Notes:**` section | Present on all sampled files |
| Mörk Borg voice | Consistent. No clean fantasy language detected. Tone is fragmented, doomy, gallows-humor — e.g., "meat sits in the gut like a confession," "the cemetery is consuming itself," "his stenographer, dead 300 years and counting." |
| Cross-linking density | High, appropriate. New pages link both upward (lore) and outward (locations, factions). |

**No format defects found.**

---

## D. Naming Collision Check

The **Übertaker vs Überwolf** decision is consistently reflected:

- `wiki/creatures/Übertaker.md` — contains explicit "Naming note" clarifying Übertaker = GLW possessed undead, Überwolf = EPK Bergen Chrypt wolf. Confirms there is no EPK Übertaker.
- `wiki/creatures/Überwolf.md` — mirror naming note pointing back to Übertaker.
- `wiki/locations/Bergen Chrypt.md` — references `[[Überwolf]]` (not Übertaker). Correct.
- `wiki/npcs/The Deadn't.md` — links `[[The Übertaker]]`. Correct.
- `wiki/npcs/The Undertaker.md` — links `[[The Übertaker]]` throughout, never Überwolf. Correct.

Source verification: EPK p.13 confirms Bergen Chrypt entry 5 is **ÜBERWOLF** (HP 18, Thick fur −d2, Bite/Claws d8, regular wolf HP 6 Morale 8 Bite d6). The wiki Überwolf entry matches source verbatim. No collision risk.

**Status:** CLEAN.

---

## E. Summary

| Category | Status |
|---|---|
| Source accuracy (8 spot-checks) | 7 PASS, 1 FAIL (Sepulchre truncated), 1 minor drift (Lesdy unarmed d4 omitted) |
| Dead links (per-entry-fix focus group) | All 9 unresolved as expected — expansion seeds |
| Dead links (other) | 112 unique dead targets across 66 files — mix of expansion seeds and a missing `wiki/powers/` directory |
| Format compliance | CLEAN |
| Mörk Borg voice | CLEAN |
| Naming collision (Übertaker/Überwolf) | CLEAN |

### **Verdict: GREEN with one RED item to fix**

**Single critical issue:** `wiki/adventures/Sepulchre of the Swamp Witch.md` is truncated at 2,319 bytes / 27 lines, terminating mid-sentence in Chamber 1. Chambers 2–11 plus the Dead Root Altar resolution and Ueth stat block are missing. The source PDF (pp.2–13) supports a full 11-chamber dungeon write-up.

**Minor drift:** Lesdy's source-listed `Unarmed attack d4` was rephrased to "carries no listed weapon" — narratively defensible but technically removed a canon stat. One-line fix if desired.

**Expansion gaps (not bugs):** ~112 unresolved `[[wiki links]]` are working as designed — Mörk Borg expansion hooks for future passes. The largest blocs are:
1. Class-specific named gear and companions (50+ links across 7 class files) — these are the "Gaps/Expansion Notes" the project plan calls for.
2. Mikhael/Merchant Inventory items (25+ links) — single expansion sweep would close it.
3. Powers (~6 links) — no `wiki/powers/` directory exists; likely a future pass.
4. `Wästland` — referenced from 9+ pages without a stub. Recommend a stub location page.
5. Per-entry-fix introduced names (Klefunheim, Jota Klefunheim, Arga, Benzen, Stein, Urgrip Wikt, Tongue-shaped Knife, Undertaker's Hut) — these were *introduced* by the repair operation and would normally be created in the same pass. Worth a follow-up pass.

The wiki is in solid shape. Fix the Sepulchre truncation, optionally restore Lesdy's `Unarmed d4`, and the repair operation is complete.
