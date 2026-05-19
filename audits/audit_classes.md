# Classes Audit — Wiki vs. Source PDFs

**Date:** 2026-05-17
**Scope:** All 11 player-class entries in `/wiki/classes/`, audited against the source PDFs in `/source/`.
**Method:** Wiki entry compared to text extracted with `pdfplumber` (which recovered table contents that `pdftotext` could not). Severity reflects how much canonical, mechanically-load-bearing content is missing — not stylistic gaps.

## Severity legend

- **HIGH** — Mechanically required content is missing or so truncated the class cannot be played as written from the wiki. Whole tables (gear, abilities, gifts) absent.
- **MED** — Significant lore or flavor missing; class is partially playable but flavor table(s) or origin entries truncated.
- **LOW** — Minor truncation; one entry incomplete or a small detail missing.

---

## Bare Bones Six

The Bare Bones PDF lays out each class as a typographic spread (pp. 46–57). The wiki's "plaintext source" caveat is accurate — naive `pdftotext` strips most table content. But `pdfplumber` recovers the full text, so the canon content does exist and the wiki entries are demonstrably under-filled vs. source.

### Fanged Deserter — HIGH

**Source:** `MÖRK BORG BARE BONES EDITION.pdf`, pp. 46–47.

Missing from wiki:

- **Earliest memories #4 (d6):** wiki marks "(unwritten in plaintext source)" but source reads: *"Sleeping with dogs in the corner of an inn, waiting for someone to return."*
- **Abilities block — entirely absent from wiki.** Source: *"built like a bull, roll 3d6+2 for Strength. not a bright spark, roll 3d6-1 for Agility and Presence. Normal Agility tests are dr14 instead of dr12, excluding defence. illiterate; you are incapable of understanding scrolls. If you begin with one then reroll, eat it or use it as toilet paper."*
- **"You also begin with one of the following (d6)" gear table — five of six entries missing.** Wiki has only #5 (Gore-hound). Source has the other five:
  - 1. *"crumpled monster mask: Strikes primitive fear into lesser creatures like goblins, gnoums and children. While worn, they check Morale every round."*
  - 2. *"the brown scimitar of galgenbeck: A stinking sword you pulled from a military shit-ditch. D6 damage. dr10 attack and defence while you wield it. 1 in 6 chance a wounded enemy is smitten with potent sepsis, dying in 10 minutes."*
  - 3. *"wizard teeth: Four weird teeth rattle within a blackened pouch. Before battle roll a d6 for each one. For every 6 one of your attacks deals maximum damage."*
  - 4. *"old sigûrd's sling: ... Woven from his long grey hair, this sling has never failed you. 2d4 damage, requires fist-sized rocks..."*
  - 6. *"the shoe of death's horse: ... In your hands it hits with dr10, d4 damage. 1 in 6 chance the shoe smashes the skull, instantly killing small-to-medium sized creatures. The shoe returns to your hand like a boomerang."*

The wiki's "expansion notes" disclaimer is incorrect: this content is canon, not a gap.

---

### Gutterborn Scum — HIGH

**Source:** `MÖRK BORG BARE BONES EDITION.pdf`, pp. 48–49.

Missing from wiki:

- **Bad Birth (d6) — entries 2–6 all blank in wiki.** Source has:
  - 2. *"Mother hanged from a tree outside of Galgenbeck, you fell from the corpse."*
  - 3. *"Raised by rats in the gutters of Grift."*
  - 4. *"Kicked and beaten beneath a baker's table in Schleswig."*
  - 5. *"Escaped the Tvelandian orphanarium."*
  - 6. *"Educated by outlaws in a hovel south of Alliáns."*
- **Abilities block — absent.** Source: *"small, roll 3d6−2 for Strength. stealthy, all Presence and Agility tests have their dr reduced by 2 (normal tests are dr10 instead of dr12). Roll d6 on the weapon table and d2 on the armor table."*
- **"You also begin with one specialty (d6)" — all six entries missing.** Wiki only references the existence of the mechanic. Source:
  - 1. *"coward's jab: When attacking by surprise test Agility dr10. On a success you automatically hit once with a light one-handed weapon, dealing normal damage +3."*
  - 2. *"filthy fingersmith: Your snaky little digits get into pockets and pick locks with a dr8 Agility test. You also begin with lockpicks!"*
  - 3. *"abominable gob lobber: Your phlegm is viscous, lumpy, vile and ballistically accurate at short range. You can spit d2 times during a fight. Roll a dr8 Presence test for accuracy. Targets are blinded, retching and vomiting for d4 rounds. ..."*
  - 4. *"escaping fate: Every time you use an omen there is a 50% chance it is not spent."*
  - 5. *"excretal stealth: ... astounding, almost preternatural ability to hide in muck, debris and filth. ... a dr16 Presence test is required to notice you."*
  - 6. *"dodging death: ... On death, if there is even the slightest possibility that you survived, there is a 50% chance that you did. If successful, after 10 rounds you pop back up with d4 hp..."*

---

### Esoteric Hermit — HIGH

**Source:** `MÖRK BORG BARE BONES EDITION.pdf`, pp. 50–51.

Missing from wiki:

- **Eldritch Origins (d6) — entirely absent.** Source:
  - 1. *"Awakening, adult, in a ritual circle underneath the northern bridge to Grift."*
  - 2. *"Wandered, memoryless, from the mouth of a cavern at the cliffs of Terion."*
  - 3. *"Single child survivor of an incident in the Valley of the Unfortunate Undead."*
  - 4. *"Dying of plague in a Bergen Chrypt hovel, you touched something from outside."*
  - 5. *"An average individual until you encountered something in a dim glade in Sarkash."*
  - 6. *"Raised on a lonely island in Lake Onda. No one else has ever heard of this island and you can't return."*
- **Abilities block — absent.** Source: *"wise, roll 3D6+2 for Presence. weak, roll 3D6−2 for Strength. Ordinary starting equipment plus one random scroll (sacred or unclean). Roll a D4 on the weapons table and D2 on the armor table."*
- **"You also begin with one of the following (d6)" — all six absent.** Source:
  - 1. *"master of fate: ... You know the right way with a dr8 Presence test."*
  - 2. *"book of boiling blood: ... D2 Berserker-slayers ... appear from the depths of a forgotten dimension of blood. ... On a 5–6 they turn on you, attempting to kill you and destroy the book."*
  - 3. *"speaker of truths: Twice per day use your wisdom ... The dr of the next test they undertake is lowered by 4."*
  - 4. *"initiate of the invisible college: Once per day you may summon D2 scrolls ... Roll a d4, on a 1–2 the scrolls are sacred, on a 3–4, unclean. If the scrolls are not used before sunrise they turn to ash."*
  - 5. *"bard of the undying: ... The music of your Harp gives +D4 on reaction rolls."*
  - 6. *"hawk as weapon: ... Attacks/defence dr10 (claws/bite D4) HP 8."*

Wiki connection to `Bergen Chrypt` is plausible but the canonical origins also cover Grift, Terion, Valley of the Unfortunate Undead, Sarkash, and Lake Onda — all should be cross-linked.

---

### Wretched Royalty — HIGH

**Source:** `MÖRK BORG BARE BONES EDITION.pdf`, pp. 52–53.

Missing from wiki:

- **"Things were going so well, until... (d6)" — entirely absent.** Wiki has no origin table at all. Source:
  - 1. *"your Wästland palace was reduced to rubble."*
  - 2. *"your caravan kingdom of Tveland fell into penury."*
  - 3. *"King Fathmu IX's brother Zigmund, your father, was murdered."*
  - 4. *"the southern empire of Südglans sank into the sea."*
  - 5. *"Anthelia demanded a gift of noble blood."*
  - 6. *"two young princes were kidnapped west of Bergen Chrypt and disappeared into the black crevasse of the eastern slopes."*
- **Abilities block — absent.** Source: *"painfully average, you adjust no abilities. Roll a d8 on the weapons table. Roll a d4 on the armor table but reroll if you receive heavy armor."* (Wiki implies but does not state the no-modifier rule, weapon-d8, armor-d4 with reroll.)
- **"You begin with two of the following (d6)" — all six absent.** Source:
  - 1. *"the blade of your ancestors: This magnificent and clearly magical talking sword is foppish, unreliable and quietly despises you. ... Deals d6+1 damage. Attack/Defence dr is 10."*
  - 2. *"'poltroon' the court jester: ... For the first two rounds you and your allies get +2 on attack/defence."*
  - 3. *"barbarister the incredible horse: Barbarister is magical, intelligent, arrogant and vain. He can also talk. ... occasionally adds +2 to Presence tests involving logic and intellect."*
  - 4. *"hamfund the squire: ... guardian for the scabbard of the cursed sword Eurekia. ... The sword does 2d6 damage, and for every swing of Eurekia roll a d6. On a 1 the squire is slain and Eurekia vanishes forever."*
  - 5. *"the snake-skin gift: An expensive sandalwood box bound in snakeskin. It contains a seemingly ordinary dagger ... on a 1 the target dies immediately of deadly poison weeping from the blade."*
  - 6. *"horn of the schleswig lords! Once per day release a blare from this dented old trumpet and test Presence dr12. One creature may make their next non-combat test an automatic success."*

Note: Wiki connections list Anthelia, Sigfúm, Shadow King, Fathmu IX — Tveland, Wästland, Südglans, and "Zigmund" (a previously unnamed royal — expansion seed) are also canonically present and unreferenced.

---

### Heretical Priest — HIGH

**Source:** `MÖRK BORG BARE BONES EDITION.pdf`, pp. 54–55.

Wiki has the Unholy Origins table complete and correct. Missing:

- **Abilities block — absent.** Source: *"insightful, roll 3d6+2 for Presence. frail, roll 3d6-2 for Strength. Roll a d8 on the weapons table and may use Powers while wearing medium armor."* (The medium-armor allowance is mechanically important and missing.)
- **"You begin with one of the following (d6)" — all six absent.** Source:
  - 1. *"sacred shepherd's crook: Its head a hook of human bone inscribed with overlapping anti-prayers. This crook hooks through other worlds. Staff does 2d4 damage except to faithless humans."*
  - 2. *"stolen mitre: ... the priest's vile body fades, becoming hard to hit in combat (Defence dr10). If pulled over the ears outside of battle the priest becomes nearly invisible, testing stealth against dr8."*
  - 3. *"list of sins: A long and accurate document cross-referenced against reality to discover unseen evil-doers. ... A strange light surrounds evil creatures. The list's owner defends with +2 against any being discovered this way."*
  - 4. *"the blasphemous nechrubel bible: So intensely blasphemous even the Priests themselves can only peruse it once per day. ... Even result: ... pcs heal d4 hp after just five minutes of rest. Odd result: ... demonic hallucinations."*
  - 5. *"stones taken from thel-emas' lost temple: Cast the stones on the ground. Their pattern reveals if danger lurks in an adjacent room. The stones can lie."*
  - 6 (rendered "666" in source). *"(wrong jesus) crucifix: ... can be used in encounters with the undead as well as lesser trolls and goblins. Check morale ... to see if the creatures bow and kindly remove themselves."*

The **"Nechrubel Bible"** and **"Thel-emas' lost temple"** are named only here — both are wiki-worthy entities entirely missing from the wiki.

---

### Occult Herbmaster — HIGH

**Source:** `MÖRK BORG BARE BONES EDITION.pdf`, pp. 56–57.

Missing from wiki:

- **"Probably raised in (d8)" — entry 8 blank in wiki.** Source: *"the ruins of the Shadow King's manse, thick with memories of mushrooms and smoke."*
- **Abilities block — absent.** Source: *"tough as wood, roll 3d6+2 Toughness. low in protein, roll 3d6-2 Strength. Roll d6 on the weapons table and d2 on the armor table. You carry a portable laboratory and continually search for frequently expended ingredients. Daily you have the materials to create two randomly determined decoctions and can brew a total of d4 doses. If unused they lose vitality after 24 hours."* (The portable laboratory and the daily two-decoctions / d4 doses mechanic is the entire engine of the class and is missing.)
- **Occult Herbmaster decoctions (d8) — wiki has only first letters (R, E, S, E, S, F, H, B).** Source has all eight:
  - 1. *"red poison: Toughness dr12 or -d10 hp."*
  - 2. *"ezumiels vapor: Pass a dr14 test or severe (and arguably fun) hallucinations for d4 hours."*
  - 3. *"southern frog stew: Vomit for d4 hours, pass a dr14 test or you can do nothing else."*
  - 4. *"elixir vitalis: Heals d6 hp and stops infection. Can be habit-forming."*
  - 5. *"spider-owl soup: See in darkness, climb on walls for 30 minutes."*
  - 6. *"fernor's philtre: Translucent oil, must be dabbed right into the eye. Heals infection and gives +2 on Presence tests for d4 hours."*
  - 7. *"hyphos' enervating snuff: Berserk! Two attacks per round but defend with dr14. Lasts one fight. Must be snorted, causes sneezing."*
  - 8. *"black poison: Toughness dr14 or -d6 hp and blinded for one hour."*

The wiki's own expansion notes flag this as the highest-priority gap, but **all of it is canon and recoverable**, not invention territory. **Ezumiel, Southern Frog, Spider-Owl, Fernor, Hyphos** are five named entities entirely missing from the wiki.

---

## Cult Five

### Forlorn Philosopher — LOW

**Source:** `MÖRK BORG Forlorn Philosopher.pdf` (1 page, double-sided spread).

Wiki entry is essentially complete: Roots (d8), dejection origins (d6), all six gifts named and summarized, ability scores correct, starting silver/Omens/HP correct.

Minor gaps:

- **Hegelian Owl stat block** is summarized but full source line not quoted: *"HEGELIAN OWL Too quick to hit. Claws/bite d4. Attacks are DR8."*
- **Prism of Ambiguity #3:** wiki says "heal and reduce DRs, or harm on failure" — source specifies *"healing d6 HP. For the next hour one of them lowers all test DRs by -2. If the test is failed they suffer d4 damage and their armor or a weapon is destroyed. You can use the prism twice per day."* (twice-per-day cap missing).
- **Marked by Obscurity #6:** wiki omits *"Roll each morning which tablet it is. The tablet can only be used once per day but automatically succeeds."* — this is the entire mechanical effect.
- Wiki's "weapon table" / "armor table" mention is right but lacks the line *"You begin with one Tablet of Ochre Obscurity and one of the following"* — the tablet is starting gear.

---

### Pale One — LOW

**Source:** `MBC_Pale-one.pdf` (1 page).

Wiki entry is nearly complete. All six origins, all six blessings, ability mods, HP, silver, Omens, weapon/armor dice are correct.

Minor:

- The wiki abbreviates the You-call-yourself name table; the source provides the full 20×20×20 columns. Wiki captures only a sample. Provide full lists (e.g., adjectives include *Abhorred, Beneath, Clad, Errant, Familiar, Giant, Hidden, Lyrical, Maniacal, Nameless, Obscene, Painful, Reposed, Skeletal, Strong, Sudden, Unaware, Unknowing, Vitriolic, Westward*) for at-table usability.
- Wiki says origin 5 is "a bog-witch in a Western Kingdom swamp" — source uses **Wästland** (the in-world name; the wiki appears to use "Western Kingdom" as a translation; consistency check — but other entries in this same wiki use the same convention, so likely intentional).

---

### Cursed Skinwalker — LOW

**Source:** `MBC_Cursed-Skinwalker.pdf` (1 page).

Wiki is essentially complete. All six "First Died" entries, all six creature shapes with stats, abilities, HP, silver, Omens, transformation rules — all present.

Minor:

- Wiki's "Shifting bones occupies a single painful round" matches source but omits the source's explicit framing: *"Give in to the advances of your antithetical other and change your very anatomy into the likeness of its being."* Already captured.
- All correct. The wiki here is in good shape.

---

### Dead God's Prophet — LOW

**Source:** `MBC_Dead_Gods_Prophet.pdf` (1 page).

Wiki is essentially complete. All 8 gifts, the 3d10 god-name table sample, abilities, scrolls/Presence DR12 rule, silver, Omens, HP — all present and accurate.

Minor:

- Wiki shows the 3d10 god-naming table but only as a single column of 10 ("Acrophoe Beacon of blood... Öde Song of the flesh"). Source presents three columns to be rolled separately for 1,000 combinations. The wiki should clarify that each of the three components is rolled on its own d10. (Wiki does say "three columns — adjective + title + dread-domain" so this is borderline; consider this LOW.)

---

### Sacrilegious Songbird — LOW

**Source:** `MBC_Songbird.pdf` (1 page).

Wiki is essentially complete. All six "A deal was struck" entries match source exactly. All six instruments captured with mechanics. Silver, Omens, HP, abilities, weapon/armor dice all correct.

Minor:

- **Hurty-Gurdy #2:** wiki says "Presence DR12 or take d2 damage (escalating)" — source clarifies the escalation: *"The first round played, it deals d2 damage, increasing to a d4 and beyond on subsequent rounds."* Mechanically clearer in source.
- **Spinal Husk #3:** wiki bullets the 2d6 outcomes but the natural-12 outcome's wording in source is *"Your ears won't stop ringing; you are deaf for the next 24 hours."* — wiki has "deafen yourself for 24 hours" (close enough but the "ringing" flavor lost).

---

## Cross-Cutting Findings

1. **The Bare Bones six are all HIGH severity for the same reason:** all six wiki entries assume the source PDF was illegible and treated tables as "gaps to fill." In fact the content is fully present in source and recoverable with `pdfplumber`. Each wiki page is missing: Abilities block, full origin table, full gear/specialty table — roughly **70–85% of the canonical playable content per class**.
2. **The Cult five are all LOW severity.** Their PDFs are single-spread layouts that extract cleanly; the wiki author had access to the same text and used it.
3. **Named entities missing from the wiki proper, surfaced only inside class spreads:**
   - **Lake Onda** (Esoteric Hermit origin 6) — never mentioned elsewhere.
   - **Cliffs of Terion** (Esoteric Hermit origin 2) — distinct from the "hermit of Terion" forbidden brew (already in wiki as a Miseries entry).
   - **Zigmund** (Wretched Royalty origin 3) — Fathmu IX's murdered brother, otherwise unnamed.
   - **Tvelandian orphanarium** / **Tveland** caravan kingdom (Gutterborn 5, Wretched Royalty 2) — Tveland is referenced; the orphanarium is new.
   - **Nechrubel Bible / Blasphemous Nechrubel Bible** (Heretical Priest gift 4) — major artifact, no wiki entry.
   - **Thel-emas' lost temple** (Heretical Priest gift 5) — named location, no wiki entry.
   - **Ezumiel** (Herbmaster decoction 2), **Fernor** (decoction 6), **Hyphos** (decoction 7), **Spider-Owl** (decoction 5), **Southern Frog** (decoction 3) — all named entities missing from creatures/items wiki.
   - **Brown Scimitar of Galgenbeck**, **Old Sigûrd's Sling**, **Shoe of Death's Horse**, **Wizard Teeth**, **Crumpled Monster Mask** (Fanged Deserter gear) — all named items missing.
   - **The Blade of Your Ancestors** (talking sword), **Eurekia** (cursed sword), **Barbarister** (talking horse), **Hamfund the Squire**, **Poltroon the Court Jester**, **Horn of the Schleswig Lords**, **Snake-skin Gift** dagger (Wretched Royalty items) — all named NPCs/items missing.
   - **Berserker-slayers** (Hermit gift 2) — named creature, missing from bestiary.
   - **"Invisible College"** (Hermit gift 4) — named faction/concept, missing.
4. **Mechanic disclaimers in wiki are factually wrong.** Several Bare Bones wiki pages say "Source plaintext leaves the class' specialty tables almost entirely blank." This was true of `pdftotext` output but is **not** true of the PDF itself. The audit recommends re-extraction with `pdfplumber` before any expansion work.

---

## Summary Table

| Entry | Severity | Origin table | Abilities | Gear/Gift table | Other |
|---|---|---|---|---|---|
| Fanged Deserter | HIGH | 1/6 entries blank | absent | 5/6 entries missing | — |
| Gutterborn Scum | HIGH | 5/6 entries missing | absent | 6/6 entries missing | — |
| Esoteric Hermit | HIGH | 6/6 entries missing | absent | 6/6 entries missing | — |
| Wretched Royalty | HIGH | 6/6 entries missing | partial | 6/6 entries missing | — |
| Heretical Priest | HIGH | complete | absent | 6/6 entries missing | medium-armor Powers rule missing |
| Occult Herbmaster | HIGH | 1/8 entries missing | absent | 8/8 decoctions truncated to first letter | portable laboratory rule missing |
| Forlorn Philosopher | LOW | complete | complete | complete (minor wording) | owl stat block, prism cap |
| Pale One | LOW | complete | complete | complete | full 20×20×20 name table abbreviated |
| Cursed Skinwalker | LOW | complete | complete | complete | — |
| Dead God's Prophet | LOW | complete | complete | complete | 3d10 god-name presentation |
| Sacrilegious Songbird | LOW | complete | complete | complete | minor wording on Hurty-Gurdy / Spinal Husk |
