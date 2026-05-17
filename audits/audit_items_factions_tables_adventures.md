# Wiki Audit — Items, Factions, Tables, Adventures

**Scope:** four wiki sub-folders compared against the source PDFs in `/source`.
**Methodology:** PDFs were converted to plaintext with `pdftotext -layout`; counts and named entries were compared against the wiki Markdown. Quotations are taken from the source PDFs (or noted where the plaintext extractor truncated them — many Bare Bones tables are typographically chaotic and not all rows survive extraction).
**Diagnose only.** No fixes performed.

---

## 1. ITEMS

### `wiki/items/Equipment.md`
- **Issue:** The starting **Armor table (d4)** from Bare Bones p.22 is missing entirely. The wiki Equipment.md never lists starting armor — only repair and prices.
- **Source:** Bare Bones p.22. Plaintext is mostly blank for this table (typographic glyphs lost), but the four tiers are recoverable from the Rules Reference card: *"ARMOR TIERS 1. light 2. medium\* 3. heavy\*\* −d2 / −d4 / −d6. \*+2 DR Agility tests. \*\*+4 DR Agility tests (Defence +2 DR)."* That gives the d4 outcome set (1: no armor; 2: light −d2; 3: medium −d4; 4: heavy −d6).
- **Missing details:** starting-armor roll table; starting-weapon prices marked with **cost** but no **die** in wiki (wiki currently has both, OK). Also the starting **Backpack / Sack / Wagon / Donkey d6** table from p.20 (rope, torches, lantern, magnesium strip, scroll, sharp needle, etc.) is not in any wiki file.
- **Severity:** MED

### `wiki/items/Powers.md`
- **Issue:** Bare Bones Unclean Powers (d10) and Sacred Powers (d10) tables are blank in plaintext source. Wiki correctly flags this. Bare Bones p.34: only Unclean #8 is readable in plaintext (*"1–3 d4 skeletons / 4–6 d4 zombies"*) and Sacred #1 begins with *"G"*. The wiki notes this gap. **The 20-entry Powers list is therefore 95% absent.**
- **Arcane Catastrophes (Bare Bones p.43–44):** another d20 table; only entry **19 (Cube-Violet)** survives plaintext extraction (*"Slay riddling Kulvan… three colorless pearls… Poison a close friend with crumbled Sict-Shroom… Reach up through the fire to the golden key above. d4 fingers burn to ash… The cube is perfect, and empty…"*). Wiki references Cube-Violet only.
- **Source:** Bare Bones p.34–35 (Powers), p.43–44 (Arcane Catastrophes).
- **Severity:** HIGH — these are referenced rules tables a GM needs at the table; the gap is the biggest mechanical hole in the wiki.

### `wiki/items/Merchant Inventory.md`
- **Wästland mislabel:** Wiki labels region 2 as "Western Kingdom Wares"; source PDF (The Merchant, p.5) heading is **"Wästland"**. Wiki body links `[[Western Kingdom]]` rather than `[[Wästland]]`.
- All 24 items (4 regions × 6) present.
- **Source:** MBC_Merchant.pdf, p.4–7.
- **Severity:** LOW (correctness, not truncation).

### `wiki/items/Tablets of Ochre Obscurity.md`
- All **10 of 10** tablets present and faithful to source. Complete.
- **Severity:** NONE.

### `wiki/items/Forlorn Philosopher Gifts.md`
- All **6 of 6** gifts present. Complete.
- **Severity:** NONE.

### `wiki/items/Songbird Instruments.md`
- All **6 of 6** instruments present. Complete.
- **Severity:** NONE.

### `wiki/items/Calumny Pearl.md`, `Croaking Trident.md`, `Elixir Vitalis.md`, `Emerald Venom.md`, `Goblin Cure.md`, `Gourmand's Cutlery.md`, `Icon of St Largoth.md`, `Lunar Zweihänder.md`, `Sict-Shroom.md`, `Spiral Crown.md`
- Each is a focused single-item entry with stats and flavor extracted faithfully from its parent adventure or rule section.
- Minor: **Lunar Zweihänder** — wiki has *"Damage d12 + radiance"* but does not specify two-handed (implied by *"longer than the Swamp Witch herself"*). Croaking Trident entry: damage *"d10 regular + d4 pandemonic"* matches Sepulchre PDF.
- **Severity:** LOW.

### Missing items entries (referenced in source but no entry exists)
- **Nostalgia Gruel** — Graves Left Wanting, p.11 (*"NOSTALGIA GRUEL, enough to restore two people to their prime by increasing all abilities +1"*).
- **Healing tincture** — Goblin Grinder, p.13 (alchemical recipe in the laboratory, also stocked at Medickal Shoppe).
- **Vial of Sour Yellow Liquid** — Goblin Grinder basement (*"alchemical pain remedy. Heals D6 + 1 when drunk but dulls the senses (−2 Presence for 1 hour)"*).
- **Spare Key (Urvan's)** — Goblin Grinder basement.
- **Tongue-shaped knife** under Bloat Sewage Pit (*"d6 damage, on a hit makes the target ravenously hungry and desperately thirsty, must eat and drink within the hour or die"*).
- **Drowned Hoard contents** — Devil's Tomb (silver effigy of three-headed basilisk, ten-foot copper rod, two shortswords; partially in [[Drowned]] entry but no dedicated item entry).
- **Goblin two-handed sword (d10+1)** — Devil's Tomb.
- **Severity:** LOW (these are item-level details inside adventures already summarized).

---

## 2. FACTIONS

### `wiki/factions/Inquisition.md`
- **Issue:** Source mentions are sparse but contain at least three concrete operational facts the wiki omits:
  - Bare Bones p.12: *"Heretics and apostates are hunted down and corrected, in public and at length, by the Inquisition."* (wiki has this).
  - Bare Bones p.14: *"The inquisition of the Two-Headed Basilisks is not too keen on the heretical suicide scheme of Sigfúm the Kind."* (wiki has this).
  - Bare Bones p.3 (Contents of Pockets, entry 34): *"Known and liked/despised witch-hunter's face. Flayed."* (wiki has this).
- **Missing:** No named leader (canon implies arch-priestess **Josilfa Migol** of Galgenbeck sits atop the Two-Headed Basilisks; the Inquisition's relationship to her is implicit, not in wiki). No named officers, ranks, or signature methods. **The wiki itself flags this gap.**
- **Source:** Bare Bones p.12, 14.
- **Severity:** LOW — the Inquisition is genuinely lightly written in canon. Wiki is faithful to the thin source.

### `wiki/factions/Creton Order.md` ("Cretun" in Death Ziggurat)
- Wiki flags the **[CANON CHECK]** spelling discrepancy correctly.
- **Source:** Bare Bones p.10 (Creton); MBC_The-Death-Ziggurat.pdf p.3 *("centuries ago, unsung knights of the Cretun order subdued Akünh and bound her")*.
- No named leadership, no member roster, no holdings beyond the Cathedral of the Two-Headed Basilisks (the orthodox splinter) and the implication that the order still hires agents from Galgenbeck. Wiki flags this.
- **Severity:** LOW — canon is genuinely thin.

### `wiki/factions/Death-Obsessed Cultists.md`
- Source (Death Ziggurat p.2): *"a group of 25 cultists from a plague-wracked Tveland hovel"*, *"They have felt the deathly vibrations…"*, *"They are not aware of Akünh or her rot-priests"*. All present in wiki.
- Source p.9 — high-rank Power "Deathlike Silence" — present in wiki.
- **Missing:** Plague-wracked hovel is unnamed (canon gap). No named cult leader, no internal hierarchy beyond "high rank". Wiki flags this.
- **Severity:** LOW.

### `wiki/factions/Drowned.md`
- Source (Devil's Tomb): *"Amphibian creatures exiled from their poisoned, dried out lake. 10 individuals present. 4 more soon back from a raid. They worship The Plant of Life and its angelic children."* All in wiki.
- Stat block in wiki (HP 6, Morale 8, Scales −d2, Spear d6) **matches** source.
- Drowned Hoard d4 table (1: 20+2d10 silver / 2: two shortswords / 3: silver effigy of a three-headed basilisk / 4: a ten-foot copper rod) is **missing** from wiki — wiki mentions "coins, cutlery, chains, nails, horseshoes" (a different flavor list in the Drowned Hoard description) but **does not include the d4 search-yield table**.
- **Severity:** MED — a small but concrete game-table.

### `wiki/factions/Strange Serpent Drug Cult.md`
- Sepulchre p.2 source faithfully extracted. Forked-Tongue Devotees called out. Origin (Ueth's serpent-and-fungus brew, return to Nechdorf) preserved.
- **Severity:** NONE.

### `wiki/factions/Udok Cultists.md`
- Source: Forlorn Philosopher (origin 7) *"Udok cultists captured your family and forced you to debate with them while they devoured your parents alive."* This is the **only** canon mention. Wiki correctly flags it as an expansion seed.
- **Severity:** NONE — wiki captures everything canon says.

### Missing faction entries (referenced in source but no wiki entry)
- **Two-Headed Basilisks** — referenced in factions README but no dedicated faction file in `/wiki/factions/`. Bare Bones p.9–10 has a half-page (*"The basilisks are two and two-headed. The four heads have argued for hundreds of years…"*, the III section on Lusi/Arkh, the descriptions of Verhu and Gorgh, and pp.11–12 on Josilfa Migol and Galgenbeck). Wiki has individual entries for Verhu/Lusi/Arkh/Gorgh in `/wiki/` but no consolidated faction entry.
- **Outcasts** as a faction — Bare Bones p.63 has full text on Outcasts as followers, listing **four types**: Earthbound, Wild Wickhead, Pale One, Prowler — each with HP/Morale/armor/weapon, **Traits (d4), Specialty (d4), Values (d6)** sub-tables. The wiki has individual creature/class entries for Pale One and Wickhead but no consolidated `Outcasts.md` faction. (Bare Bones p.62: *"Money might cross hands but these weirdos don't cost silver to hire."*)
- **Rot Priests** as a sub-faction of the Death-Obsessed grouping — wiki links to them as a creature, not faction. Death Ziggurat lists their stats and medallion requirement.
- **Forked-Tongue Devotees** — linked from Strange Serpent Drug Cult entry; whether a separate file exists in `/wiki/creatures/` is outside this audit's scope but they're referenced as a distinct inner-circle group.
- **Severity:** MED (Two-Headed Basilisks especially — they are the dominant religious faction of canon).

---

## 3. TABLES — **highest-risk category for truncation**

### `wiki/tables/Adventure Seeds.md` (d100)
- **Canonical:** Bare Bones p.67–69 has 4 sub-tables: **Where (d12), Who (d20), Why (d100), and a fourth column the plaintext eats**. The Why column is d100 with entries paired (1–2, 3–4, … 99–00 = 50 paired entries).
- **Wiki entries:**
  - Where (d12): **12 of 12 present**.
  - Who (d20): **5 of 20 readable** in wiki (rows 2, 7, 8, 11, 16). Wiki notes *"other rows blank in plaintext source"*.
  - Why (d100): **47 of 50 paired entries present**. Wiki notes 1–2, 3–4, 43–44 as blank in plaintext source. Source plaintext actually has **3–4** present: *"Thirteen priests are missing"* (Bare Bones p.68). **The wiki entry says 3–4 is blank — this is the only definitively recoverable missing seed.**
- **Source quote (3–4):** *"3–4  Thirteen priests are missing"* (Bare Bones p.68).
- **Severity:** HIGH for the **Who d20** column (15 rows blank in plaintext, fillable from artistic-edition rulebook). MED for **Why** (only 3 truly missing in source plaintext: 1–2, 43–44, and 3–4 which IS in plaintext but wiki misses it).

### `wiki/tables/Names.md`
- All **48 of 48** entries (d6 × d8) present. Complete.
- **Severity:** NONE.

### `wiki/tables/Terrible Traits.md`
- Terrible Traits **20 of 20**. Broken Bodies **20 of 20**. Bad Habits **20 of 20**.
- Wiki's title says *"Terrible Traits, Broken Bodies, Bad Habits"* — matches canon p.38–40.
- **Note:** Bare Bones p.41 has a **"Troubling Tales" d20 table** (referenced in index *"41 Troubling tales"*) that the wiki **does not include**. The plaintext extracted is all blank rows for this table — typographic loss. The table exists in source. Wiki has no entry for it.
- **Source:** Bare Bones p.40 (Troubling Tales heading): *"The whole group can share the same backstory, or groups within the group can share a tale. Or the GM can quickly give history to a seemingly mundane character."* Then rows 1–20 follow, all blank in plaintext.
- **Severity:** MED — a fourth d20 character-creation table the wiki has dropped silently.

### `wiki/tables/Reaction and Morale.md`
- 2d6 Reaction: **5 of 5 ranges**. 2d6 Morale rules: complete. Matches Rules Reference card and Bare Bones p.32. Complete.
- **Severity:** NONE.

### `wiki/tables/Traps.md` (d12)
- **11 of 12** entries present in wiki; row 1 blank in plaintext source. The source PDF artistic version definitely has 12 entries; the plaintext extractor missed row 1.
- **Source:** Bare Bones p.3.
- **Severity:** LOW.

### `wiki/tables/Weather.md` (d12)
- **12 of 12** present. Complete.
- **Severity:** NONE.

### `wiki/tables/d100 Items and Trinkets.md`
- All **100 of 100** entries present. Complete.
- **Severity:** NONE.

### `wiki/tables/Contents of Pockets.md` (d66)
- d66 should be 36 entries (11–16, 21–26, 31–36, 41–46, 51–56, 61–66).
- **Wiki has:** entries 21–26, 31–36, 41–46, 51–56, 61–66 (30 of 36). Entries **11–16 blank in plaintext source** (6 missing). Wiki flags this.
- **Severity:** MED — 6 of 36 (~17%) missing; pulled from the typographic original would close the gap.

### `wiki/tables/Adventure Seeds.md` — already audited above.

### `wiki/tables/Bedeviled Dungeons.md`
- **What is the dungeon? (d12 + d12):** 12 of 12 adj × 12 of 12 noun present.
- **Status:** complete.
- **In what state? (d10):** **1 of 10** entries present (row 3, "Is about to collapse"). Wiki flags 9 rows blank in plaintext source.
- **Who lives there? (d12):** **12 of 12** present. Complete.
- **What did they leave? (d12):** **2 of 12** present (rows 4 and 7). Wiki flags 10 rows blank in plaintext source.
- **Room details (d4 × d6 = 24):** **21 of 24** present (one slot in d4=1's inscriptions list and a few sub-cells are blank in plaintext source).
- **Severity:** HIGH for **In What State (9 missing)** and **What Did They Leave (10 missing)** — these are major canonical content holes.

### `wiki/tables/The Basilisks Demand.md` (d20)
- All **20 of 20** entries present. Complete.
- **Severity:** NONE.

### `wiki/tables/Unheroic Feats.md` (d66 = 36)
- All **36 of 36** feats present with effect summaries. Complete.
- **Severity:** NONE.

### `wiki/tables/Blackpowder Weapons.md`
- All **11 firearms** + 3 ammunition lines + global rules present. Complete.
- **Severity:** NONE.

### `wiki/tables/Overland Travel.md`
- Travel distances: 10 of 10 routes.
- Roads (d8): 8 of 8.
- Events (d20): **all 20** present (wiki notes Adnah/Arbint canon discrepancy correctly).
- Search food/water (d6): 6 of 6.
- Village (d6): 6 of 6.
- Leave the road (d12): **11 of 12** — wiki correctly notes row 9 blank in source. Source plaintext (MBC - Overland travel) genuinely **skips from 8 to 10** (canonical printing gap or typographic loss).
- **Source:** MBC - Overland travel, p.3–4.
- **Severity:** LOW.

### Missing tables (canonical, not in wiki at all)
- **Bare Bones p.41 Troubling Tales d20** — see above.
- **Bare Bones p.39 Broken (0 HP) d4 outcomes** — wiki has these blank/missing. Recoverable from Rules Reference card.
- **Bare Bones p.42–44 Arcane Catastrophes d20** — only entry 19 (Cube-Violet) in wiki; the rest of the d20 table is blank in plaintext source but the table exists in canon.
- **Bare Bones p.21 Starting Item d12 tables (two of them)** — backpack/torches/lantern/strip/scroll/needle… (one column) and the grappling-hook/shield/crowbar/tent column. Mostly blank in plaintext, partly recoverable.
- **Bare Bones p.22 Starting Weapon d10 and Armor d4** — Weapon table 10 of 10 present in wiki Equipment.md. Armor d4 absent.
- **Bare Bones Outcasts d4 type table + per-type Traits/Specialty/Values** (p.63–66) — wiki does not have these tables; they are character-creation companion tables for hireable NPCs.
- **Death Ziggurat: d10 ruin types, d10 search results, d12 random events, d10 minor / d6 major treasures** — all present in source PDF but only mentioned as **a one-line "Tables:" reference** in `wiki/adventures/Death Ziggurat.md`. No dedicated table entries.
- **Eat-Prey-Kill: d10 Hunting Mishaps, d10 In the Belly of the Beast** — both fully readable in source plaintext, neither has a dedicated wiki table file. They are summarized in the adventure entry but not transcribed.
- **Severity:** MED (game-table-ready content missing for active play).

---

## 4. ADVENTURES

### `wiki/adventures/Bloat.md`
- **6 rooms** in source (Vestibule, Rotting Larder, Sewage Pit, Chapel of Filth, Automaton Storage, The Fattened King). All **6 referenced** in wiki paragraph form.
- NPC stats present in source: Silas (HP 20, Morale 9, Cutlery d4 + Engulf), Fleshy Automaton (HP 8, Morale −, Ceramic −d4, Violent Shove d6), Ratbadger (HP 5, Morale 9, Tough hide −d2, Bite d4). **Wiki has no stat blocks**, only narrative summary.
- Hidden treasure: d6 silver + tongue-knife in Sewage Pit (present in wiki).
- **Severity:** MED — narrative summary preserved but stat blocks and room-by-room hooks not transcribed; the published one-pager has the actionable detail wiki lacks.

### `wiki/adventures/Death Ziggurat.md`
- 5 named tables in source (d10 ruin types, d10 search, d12 events, d10 minor / d6 major treasure). Wiki **mentions** them in a single line (*"Tables: d10 ruin types, d10 search results, d12 random events per hex, d10 minor and d6 major treasures"*) but **does not list the entries**.
  - Source minor treasures (worth 3d20s): Blasphemous idol / Charcoal black chalice / Bracelet of teeth / Curved ritual dagger / Poisoned brooch / Blood-stained coins / Obsidian rod / Iron devil mask / (one truncated) / (one truncated).
  - Source major treasures (worth 30+2d20s): Demonic figurine with eyes / Void-black ring / Handful of gemstones / Mummified head of a prophet / Crystal ball / Unclean scroll.
  - Source d10 ruin types: Unholy chapel / Intact tower / Cracked dome / Underground shrine / Fountain plaza / Walled garden / Black monolith / Overgrown ziggurat / Demon statuary / Basalt mausoleum.
  - Source d12 events: 1–2 nothing / 3 thunder / 4 spiral galaxy revealed / 5 sudden cold / 6 d6 moaning undead / 7 d4 rot-priests / 8 d4 rot-priests + 2 horn beasts / 9 Sarku hides / 10 Sarku curious / 11 Akünh resurrecting corpses / 12 Akünh approaches.
- Necropolis room: source has it, wiki has it.
- Spiral Chapel room: source has it, wiki has it. The d12 ruin/event tables are the major canonical loss.
- **Severity:** HIGH — ~40 table entries dropped.

### `wiki/adventures/Devil's Tomb.md`
- One-page dungeon. Wiki captures all named rooms (Madman, Drowned Lair / Altar / Hoard, Pit to Hell, Traitor's Den, Goblins, Angelic Choir, Plant of Life). Source stat blocks: Madman (HP 2, Morale −, No armor, Bite d2), Drowned (HP 6, Morale 8, Scales −d2, Spear d6), Belpheduk (HP 5, Morale 3, Scales −d2, Claws d4), Goblin (HP 6, Morale 7, Ropy skin −d2, Knife d4, DR14 to hit/defend). **Wiki has Drowned stat but not the others.**
- Spores d4 table (visions of death / dizziness / pitch black + red outline / invisibility) — wiki summarizes the four effects; complete.
- Drowned Hoard d4 (silver / shortswords / silver effigy / copper rod) — **wiki paraphrases the contents but does not list the d4 results**.
- **Severity:** MED.

### `wiki/adventures/Eat-Prey-Kill.md`
- **8 regional d6 hunting tables** in source = **48 beasts**: Tveland, Sarkash, Graven-Tosk, Grift, Kergüs, Wästland, Lake Onda, Valley of the Unfortunate Undead, Bergen Chrypt. (That's actually 9 regions in source, totaling **54 beasts**.)
- Wiki names **6 Tveland + 6 Sarkash + 6 Graven-Tosk + ~5 Grift + "other regions" listed by name only** = roughly **23 beasts named, none with stats**.
- Missing entirely from wiki: Lake Onda's 6 beasts (Cursed Trout, Rusty Bass, The Groan, Carcasswan, Unresting Duck, Sursturgeon), Valley of the Unfortunate Undead's 6 (Phantom Rats, Grubstoppers, Tomb Ape, Gravelings, Marrow Sparrow, Bonemare), Bergen Chrypt's 6 (Tunnel Sneak, Nephalix Monkeys, Weakwill'd Whisperbird, Vierwinged Falchon, Überwolf, Ragpie), Kergüs 6 (Flail-Horned Muskox, Tar-Pelted Goats, Molar Bear, Megasloths, Blubber Gulls, False Seal), Wästland 6 (Liar-Bird, Three-Thirds-Pheasant, Feather Fox, Bautaboar, Schleswig Bogfeeder, Gold-Crested Filth-Crow), Grift entries 6 (Múrder Gulls and at least one more).
- Each beast in source has HP / Morale / armor / attack / special — none of these are in wiki.
- d10 Hunting Mishaps and d10 In the Belly of the Beast: present in wiki as run-on summaries; **complete content, format flattened**.
- **Source:** MBC_Eat-Prey-Kill.pdf, pp. 2–13.
- **Severity:** HIGH — by far the largest content gap in adventures; ~30 named beasts dropped, all stat blocks dropped.

### `wiki/adventures/Goblin Grinder.md`
- Source rooms: Basement (−1), Ground floor (entrance, missing from wiki listing), 2nd floor "Fire! Fire!", 3rd floor Laboratory, 4th floor The Goblin Grinder. **Wiki says "four floors plus basement"** which is correct, but rooms not described individually.
- NPC stats in source: Nagel Krat (HP 6, Morale 6, No armor, Knife d4, Smoke bomb), The Bastard (HP 10, Morale 6, Mutant hide −d4, Knife d4), Fresh Goblins (HP 5, Morale 7, Ropy skin −d2, Bite d4, DR14), Archer goblins (HP 6, Morale 7, Ropy skin −d2, Shortbow + flaming arrows d6), Qarg (mentioned but stats not yet pulled), Alchemical Ooze (HP 10, Morale −, Gooey −d2, Acidic splash d8). **Wiki names them all but provides no stat blocks.**
- d4 hooks (PCs afflicted / hired as guards / suspicious noble Jota Klefunheim / worried peasant Urgrip Wikt with Calumny Pearl): all 4 present in wiki.
- d6 alchemy-table spillover (acid / foul / weird / sweet — 4 of 4 sub-entries on d4) — **missing from wiki entirely**.
- Goblin Cure pricing escalation: 40s rising 5/day — present in wiki Goblin Cure entry.
- **Severity:** MED.

### `wiki/adventures/Graves Left Wanting.md`
- Source has **7 named locations**: The Strangly Tree, The Plague Pit, The Origin Fountain, Maus' Vomatorium, The Colander Room, Catacomb Corridor → Erhard's Tomb (wiki misspells as Orerhard's Tomb, source spelling is **Erhard's**), Roach Herder's Lair, The Undertaker's Hut. Plus *Inside the Tree* and *The Jar*.
- Wiki lists 6 locations and flags *"plaintext source is partial — many sub-areas (Orerhard's Tomb, the Colander Room, Maus' Vomatorium, Undertaker's Hut) are not fully extracted here"*. Source plaintext **does** have these — they were extracted, wiki just hasn't pulled them.
- Missing canon details:
  - **The Übertaker** transformation (the Undertaker rises with shovel-as-polearm, HP 27, Morale −, Barrier (palefire) −d4, d4 random actions). Wiki has zero on this.
  - **The Deadn't** (Stein, Benzen, Arga — three living NPCs in the hut, full stat blocks for each).
  - **Encounter d10 + Sensory Strangeness d8**: 8 of 8 sensory entries in source; wiki has none transcribed.
  - **What You Know (d6)** rumors: only 2 of 6 readable in wiki ("magical barrier — false", "growing warmer — true"). Source has all 6 (3: graveyard is full (maybe); 4: dead sleep well to music (false); 5: inescapable (maybe); 6: mist plays tricks (true)).
  - **The Jar — Nostalgia Gruel** (restores two people to prime, +1 all abilities).
  - **The Roach Herder** (HP 4, Morale 5, Bite d4 + special, or Barbed Roach Whip d6; "Recluse of Refuse" lore).
  - **Twice-Grown Corpse Fly** (HP 4, Morale −, Exoskeleton −d4, Bite d4 + special).
  - **Inside The Tree** room treasures (1: 3d10 silver, 2: rations, 3: scrolls, 4: rope, 5: powder, 6: pouch).
- **Severity:** HIGH — most concrete adventure content (NPCs, encounter table, key climax) is absent.

### `wiki/adventures/Rotblack Sludge.md`
- Source: **15 rooms** (Entrance, Dining Hall, [implied room 3], Guard Room, Cells, [room 6], [room 7], Chain Room, Gem Room, Forge/Slaughterhouse at 15, Statue Room at 12, Son's Room at 13, Debris Room at 14). Wiki says **"15 rooms"** but does not name them individually.
- NPCs called out: Fletcher, Lesdy, Aldon, Distraught Spirit, Sagsobuth, Tired Crystal Demon, King Lenard II — all present.
- Power Catalogue: 4 powers in source — Slithering Strangulation, Nine Violet Signs Unknot the Storm, Daemon of Capillaries, Ich-bin-luft — all in wiki (under Powers.md).
- Random encounter d8 + once-per-scenario weird d4-ish: present in source, only summarized in wiki.
- Gutworm stat block (HP 50, Morale −, Thick hide −d6, plus swim hazard d6): **wiki names the Gutworm; no stats**.
- Items found in Cells d6 (bony dog remains, black-stone necklace, 3d10 silver, urn of poison powder, scroll/beetle box, small crossbow): **complete in source, none transcribed in wiki**.
- d8 things the Seer sees: source has the table; wiki summarizes only.
- **Severity:** MED — adventure narrative captured but room-by-room and item tables dropped.

### `wiki/adventures/Sepulchre of the Swamp Witch.md`
- 11 chambers — wiki notes 11 but does not enumerate. Chambers (source): 1 Sunken Entrance, 2 Cult Common Hall, 3 [unnamed], 4 [unnamed], 5–6 [unnamed], 7 Garden, 8 Hidden Ferns (Croaking Trident location), 9 Tomb (Swamp Witch's chamber), 10–11 [unnamed].
- Wish-altar d6 side-effects: source has 6 entries; wiki summarizes them as a range ("from minor cracks in the altar to fully draining maximum HP from everyone in the room") — **specific entries not transcribed**.
- Srolki & Yaoxl stat blocks: source has them; wiki names them but **no stats**.
- Swamp Witch stat block (with Lunar Zweihänder): source has full block; wiki summarizes weapon only.
- **Severity:** HIGH — 11-chamber dungeon with no chamber-by-chamber description in wiki.

### `wiki/adventures/Tenebrous Reliquary.md`
- **d66 = 36 cursed items** in source.
- **Wiki has 12 items.** Wiki itself flags: *"This wiki entry samples the table. A full transcription of all 66 entries is an obvious expansion task."*
- Source PDF contains all 36 items at named numbers 11, 12, 13, 14, 15, 16, 21–26, 31–36, 41–46, 51–56, 61–66.
- Missing from wiki (24 of 36):
  - **31 Volt Thrower** (ancient javelin, d6, on crit lightning +2d10 not reduced by armor; on fumble strikes wielder).
  - **32 The War Starter** (heavy round shield, viewers test Presence DR14 or are provoked to attack wielder).
  - **33 Zodiac Lung** (absorbed organ, breathe in unclean water).
  - **34 Cup of Peace** (drinking = DR16 Toughness or die).
  - **35 Dust of Paradise** (DR14 Presence or visions for d6 minutes).
  - **36 Ebony Tears** (vial of black liquid; DR14 Presence or grief, fail morale).
  - **41 Eye of Horus** (forehead-eye, see grisly death-timeline, overland travel mired in corpses).
  - **42 Finger Paintings of the Insane** (Toughness DR12 or paint heretical imagery; mark scrolls −d4 Presence).
  - **43 Flower of Disease** (poisonous weed seeds; can swallow a village in 2 days).
  - **44 Foehammer** (cursed warhammer 2d6; develops new grudges).
  - **45 Cauldron of Lies** (cooked beverages let imbibers detect lies for a month).
  - **46 Cursed Tongue of the Naga** (placed in skull, runs about screaming).
  - **51 Chaos Blade** (Zweihänder 2d8; on max damage casts Death).
  - **52 Chains of Death** (frigid manacles; if you die wearing them, your killer is dragged to another world).
  - **53 Claw of the Sloth** (dagger d4, on 1 attack/defense DR −2 next round; if DR=0 frozen permanently).
  - **54 Blood of the Serpents** (acidic poison liquid; turns blood neon-green and contagious).
  - **55 Crown of Burning Stars** (omens equal to elapsed Miseries; Miseries on 1 & 2).
  - **56 Book of Oblivion** (sentient tome; permanently transfer memory; on fail it takes extra).
  - **61 Antlers of Lightning** (any scroll on Heads becomes Nine Violet Signs).
  - **62 Eyes and Teeth** (replace missing teeth/eyes; d4 outcome each).
  - **63 Black Candles** (jet-black flame flickers toward greatest threat within 1 mile).
  - **64 Robe of Bones** (once daily, stare at humanoid; DR13 Toughness or random limb bone snaps).
  - **65 Ash of the Mind** (sigil + touch; read thoughts).
  - **66 Bowels of a Baby Killer** (drape entrails; evil creatures DR14 to discern your location).
- **Source:** MBC_Tenebrous_Reliquary.pdf, full PDF.
- **Severity:** HIGH — 24 of 36 (67%) items missing. The largest single gap in the audit.

---

## SEVERITY SUMMARY

### HIGH (significant, recoverable content missing)
1. **`wiki/items/Powers.md`** — Bare Bones d10 Unclean + d10 Sacred Powers tables effectively absent. Source plaintext lost most rows; full art-edition rulebook required. 19+ named scrolls missing.
2. **`wiki/tables/Adventure Seeds.md`** — Who d20 column has 15 of 20 rows blank; Why d100 entry 3–4 ("Thirteen priests are missing") is in plaintext but **not** in wiki.
3. **`wiki/tables/Bedeviled Dungeons.md`** — In What State (9/10 blank) and What Did They Leave (10/12 blank) sub-tables effectively empty.
4. **`wiki/adventures/Eat-Prey-Kill.md`** — ~30 named regional beasts and all stat blocks missing.
5. **`wiki/adventures/Tenebrous Reliquary.md`** — 24 of 36 cursed items missing; wiki itself flags this.
6. **`wiki/adventures/Graves Left Wanting.md`** — The Übertaker climax, The Deadn't NPCs, the Roach Herder, room-by-room contents, Sensory Strangeness d8 table all absent.
7. **`wiki/adventures/Sepulchre of the Swamp Witch.md`** — 11-chamber dungeon described in single paragraph; wish-altar d6 side-effects, Srolki & Yaoxl and Swamp Witch stat blocks dropped.
8. **`wiki/adventures/Death Ziggurat.md`** — d10 ruins, d10 search, d12 events, d10/d6 treasures (~40 entries) referenced but not transcribed.

### MED
1. `wiki/items/Equipment.md` — starting Armor d4 and starting-item d12 tables missing.
2. `wiki/factions/Drowned.md` — Drowned Hoard d4 search-yield table absent.
3. `wiki/factions/` — **no consolidated Two-Headed Basilisks faction entry**; no Outcasts faction entry; both have substantial Bare Bones content.
4. `wiki/tables/Contents of Pockets.md` — entries 11–16 (6 of 36) blank in plaintext.
5. `wiki/tables/` — **Bare Bones Troubling Tales d20 (p.41)** absent entirely.
6. `wiki/tables/` — **Outcasts** d4 type table + per-type Traits/Specialty/Values sub-tables not present.
7. `wiki/adventures/Bloat.md` — narrative only; no stat blocks for Silas / Automaton / Ratbadger.
8. `wiki/adventures/Goblin Grinder.md` — narrative only; no stat blocks for Nagel / Bastard / Goblins / Ooze; d6 alchemy-table spillover (d4 sub) dropped.
9. `wiki/adventures/Rotblack Sludge.md` — 15 rooms not enumerated; Gutworm stats and Cells d6 contents dropped.
10. `wiki/adventures/Devil's Tomb.md` — Drowned Hoard d4 not enumerated; Madman/Belpheduk/Goblin stats absent.

### LOW
1. `wiki/items/Merchant Inventory.md` — labels region 2 "Western Kingdom" instead of source's "Wästland".
2. `wiki/items/Lunar Zweihänder.md` — handedness implied not stated.
3. `wiki/factions/Inquisition.md`, `Creton Order.md`, `Death-Obsessed Cultists.md` — canon is genuinely thin; wiki captures what exists.
4. `wiki/tables/Traps.md` — row 1 blank (1 of 12).
5. `wiki/tables/Overland Travel.md` — leave-the-road row 9 blank (canon also skips it).
6. Missing item entries: Nostalgia Gruel, Healing Tincture, Vial of Sour Yellow Liquid, tongue-knife (under Bloat), etc. — most are summarized inside adventure entries.

### NONE (complete)
- `wiki/tables/Names.md`, `Terrible Traits.md` (all three sub-tables), `Reaction and Morale.md`, `Weather.md`, `d100 Items and Trinkets.md`, `The Basilisks Demand.md`, `Unheroic Feats.md`, `Blackpowder Weapons.md`
- `wiki/items/Tablets of Ochre Obscurity.md`, `Forlorn Philosopher Gifts.md`, `Songbird Instruments.md`
- `wiki/factions/Strange Serpent Drug Cult.md`, `Udok Cultists.md`

---

## NOTES ON PLAINTEXT EXTRACTION LIMITS

The Bare Bones rulebook in particular uses heavy typographic layout — multi-column, scattered glyphs, decorative backgrounds — that `pdftotext` strips. Many rows that appear blank in extraction are likely **printed in the art edition** and could be recovered by:
- using OCR on the relevant page images (`pdfimages` + `tesseract`), or
- referring to community wikis / SRD compilations that have already transcribed Bare Bones into clean text.

Rows the wiki currently labels *"(blank in plaintext source)"* are honest documentation of this limit. They are not author oversight — they're flagged work.

---

## END OF AUDIT
