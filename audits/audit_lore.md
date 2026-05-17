# Lore Category Audit

Diagnostic pass over `wiki/lore/` against the source PDFs. Findings only — no fixes applied. Severities: **HIGH** = canonical text/named entity missing or wrong; **MED** = a real gap that affects play or cross-reference; **LOW** = wording or polish issue.

Source pages referenced are from the page numbers printed in the PDFs themselves (which already match the wiki's own page citations).

---

## Misery Table

**Entry:** `wiki/lore/Misery Table.md`
**Source:** MÖRK BORG BARE BONES EDITION, pp. 17–20 (The Calendar of Nechrubel — The Nameless Scriptures)

### Structural finding — the table is COMPLETE, not truncated

The brief flagged a possible "49 prophecies" expectation. Canon is **37 prophecies**: Psalm I–VI each contain 6 verses (1:1–1:6, 2:1–2:6, … 6:1–6:6), plus the singular Psalm VII = 7:7. The wiki's structure matches the source exactly. The lookup is d66 (two d6 read as tens/ones), not d100 or d49.

| Psalm | Source verses | Wiki verses | Status |
|---|---|---|---|
| I | 1:1–1:6 | 1:1–1:6 | complete |
| II | 2:1–2:6 | 2:1–2:6 | complete |
| III | 3:1–3:6 | 3:1–3:6 | complete |
| IV | 4:1–4:6 | 4:1–4:6 | complete |
| V | 5:1–5:6 | 5:1–5:6 | complete |
| VI | 6:1–6:6 | 6:1–6:6 | complete |
| VII | 7:7 only | 7:7 only | complete |

### Wording deviations (LOW)

These do not change meaning but the wiki claims to quote canon, so they are flagged:

- **Heading.** Wiki: "Misery Table — Roll d66 when a Misery wakes." Source heading reads `The Calendar of Nechrubel — The Nameless Scriptures. Transcribed by Anuk Schleger the monk.` The wiki should at minimum preserve that attribution line — it's the in-fiction frame for the whole table.
- **4:1.** Wiki: *"mothers' flesh shall be the cloak of demons."* Source: *"mothers flesh shall be the cloak of demons."* (No apostrophe in source — likely a deliberate stylistic choice of the layout.) LOW.
- **Psalm headings.** Source uses Roman numerals as standalone headers (`PSALM I`, `PSALM II`, … `PSALM VII THE LAST`). Wiki uses "## Psalm I" through "## Psalm VII — The Last" — fine, but worth noting the source style for fidelity.
- **5:5.** Both texts match: *"The sky shall weep fire and a great stone shall plummet as a city fallen from heaven. Its gift is Death and madness is its herald."* No issue.

### Procedural canon NOT captured on the Misery Table page (MED)

The Bare Bones text on p. 17 contains procedural canon adjacent to the verses themselves that the wiki places only on `Calendar of Nechrubel.md`. Some of this belongs on the Misery Table for in-play use:

- *"The world trembles. One can feel it in ways sharp and subtle, mysterious and clear. One by one, inevitable events demand their place."* — the opening flavor.
- *"The gm then rolls d66 to determine which Misery occurs. The same Misery will not befall the world twice."* — wiki Misery Table says only "Roll d66 when a Misery wakes" — the "no repeats" rule is lore-critical and not on the table page.
- *"The seventh Misery will always be 7:7, and the world finally dies. The seventh seal is broken for the seventh and final time. The game and your lives end here. Burn the book."* — the wiki Calendar entry paraphrases this; the literal closing line *"Burn the book."* appears verbatim in source and is one of the most-quoted lines in Mörk Borg canon.
- The "Years of pain" subscript (d100 / d20 / d10 / d6 / d2 — die-size selection for the daily Misery roll) is on the same page and is gameplay-critical. Wiki `Calendar of Nechrubel.md` mentions "the smaller the die, the faster the world bleeds out" but does not show the canonical die ladder.

**Severity:** MED — Misery Table is correct in content, but missing the procedural framing that makes it usable at the table without consulting two files.

---

## Calendar of Nechrubel

**Entry:** `wiki/lore/Calendar of Nechrubel.md`
**Source:** MÖRK BORG BARE BONES EDITION, pp. 16–20

### Missing canonical text (MED)

The opening of p. 16 in source:
> *"The world trembles. One can feel it in ways sharp and subtle, mysterious and clear. One by one, inevitable events demand their place."*

This is the *Calendar*'s prologue line — not currently quoted in the wiki entry. The entry paraphrases the mechanism well but loses the source's framing.

### Missing die ladder (MED)

Source p. 16 lists the die options for "Years of pain": d100 / d20 / d10 / d6 / d2. Wiki says "the smaller the die, the faster the world bleeds out" — true, but the canonical ladder is not shown. The d2 option in particular (a near-immediate apocalypse) is not obvious from the paraphrase.

### Missing "Burn the book." (LOW–MED)

The literal closing instruction `Burn the book.` (Bare Bones p. 16) is omitted from the wiki entry, which says only *"the world dies, and the players' lives end with it. Burn the book."* — italicised in passing. The original is given its own line in the source, after a paragraph break, with weight equal to the rule itself. Worth elevating.

### Sepulchre of the Swamp Witch interaction NOT captured (MED)

Sepulchre of the Swamp Witch, p. 13 ("Wishes" table) contains canon directly tied to the Calendar:

> *"Asking for the world not to end only delays the inevitable; do not roll on The Calendar of Nechrubel the next time a Misery is supposed to activate."*

And entry **5** of the Wishes table:
> *"Time slows down in the dungeon: the GM rolls until a Misery occurs. A number of days passes equal to the number of rolls made…"*

And entry **2**:
> *"A Misery instantly activates."*

These are the only published canonical mechanics for *interfering with* the Calendar. The wiki Calendar entry says mechanical edge cases are "GM-judgment in the source" — that is now incorrect; the Swamp Witch altar gives concrete rules. Cross-reference is missing from both `Calendar of Nechrubel.md` and `Sepulchre of the Swamp Witch.md` (lore side).

**Severity:** MED (cosmology mechanic exists in canon, wiki claims it doesn't).

---

## Nameless Scriptures

**Entry:** `wiki/lore/Nameless Scriptures.md`
**Source:** Bare Bones pp. 10–11 (`What Was Written Must Be Known`, sections I–II), pp. 17–20 (the text itself).

### Coverage is good. Minor finding:

The wiki cites "p.10, 17–20." Source section II on p. 11 also contains the key sentence the wiki paraphrases:
> *"The bAsilisks Are two And two-heAded. The four heads have argued for hundreds of years. Verhu predicts inexorable annihilation and, since he's always right, has become utterly full of himself. His is also the head worshipped most."*

The wiki captures the Scriptures' content but does not quote the source's two-paragraph framing ("Since then all events described within have come to pass. The prophecies are absolutely, factually true and have, thus, supplanted all other Scripture."). The first half ("absolutely, factually true") is paraphrased; the second half ("supplanted all other Scripture") is the actual reason older Creton orthodoxy was overwritten and is not in the wiki.

**Severity:** LOW.

---

## Nechrubel

**Entry:** `wiki/lore/Nechrubel.md`
**Source:** Bare Bones p. 12 (Galgenbeck section), p. 19 (Psalm 6:6).

### Coverage is good. Minor findings:

The wiki captures the canonical sentence:
> *"Nechrubel: the shadow that covers all. Nechrubel is melancholy, crop failure, conflict and war. It is said he whispered the apocalyptic prophecies in Verhu's ear."*

It correctly flags the "right underling" as unnamed in canon (only Daejmon, the left, is named at 6:6).

The wiki's "Gaps" section says Nechrubel's form and cult are blank. True in Bare Bones, but the adventure-seed table on p. 71 entry **2** lists *"Nechrubel-worshipping lich with a skeletal court"* — the only canonical hint that Nechrubel has direct worshippers. Worth surfacing into the Nechrubel entry's connections or notes.

**Severity:** LOW.

---

## HE, SHE, Verhu, Gorgh, Arkh, Lusi, Two-Headed Basilisks

All six basilisk-related entries cross-checked against Bare Bones pp. 10–11 (sections I–III, "What Was Written Must Be Known").

### Findings:

- **HE.md**, **SHE.md**, **Verhu.md** — all quote canon accurately. No missing content.
- **Gorgh.md** — captures the Envy framing and the gold-piled-faithful. Complete.
- **Arkh.md** — captures Deception and 4:4 verse. Complete.
- **Lusi.md** — captures Denial and *"yet all shall be well."* Complete. Source p. 11 line *"many walk her twin paths"* is also captured (via Arkh entry).
- **Two-Headed Basilisks.md** — complete. Connects all four heads, the Galgenbeck mortal cult, Josilfa, Inquisition, Akünh.

### One LOW finding across all of these:

The source consistently styles the basilisks' names (Verhu, Lusi, Arkh, Gorgh, HE, SHE) and the opening word of each section as drop-caps / small-caps (`The bAsilisks Are`, `she bears`, `he survived`, etc.). The wiki preserves the meaning but loses the typographic emphasis on **HE** and **SHE** which is *canonical orthography in source*. The current wiki already bolds **HE** and **SHE** in body text; this is on-spec. Note only — no action needed.

---

## Yetsabu-Nech

**Entry:** `wiki/lore/Yetsabu-Nech.md`
**Source:** Bare Bones p. 19 (Psalm VII, verse 7:7).

### Coverage is complete.

Wiki captures the full canonical line:
> *"All praise Yetsabu-Nech, the underworld's nightmare, the black disk which stands before the sun! All praise Verhu, beaming with delight! All praise the fire which burns all! And the darkness shall swallow the darkness."*

The "fire which burns all" line is captured. The wiki notes this is end-of-game, which is correct.

**Severity:** none.

---

## Daejmon

**Entry:** `wiki/lore/Daejmon.md`
**Source:** Bare Bones p. 19 (Psalm 6:6).

### Coverage is complete; the gap is in canon, not the wiki.

Wiki correctly notes Daejmon is one sentence of canon:
> *"And the unnamed enter the earth, passing through the Veil as it is sundered by Daejmon, the left underling of Nechrubel."*

The "right underling" is genuinely never named anywhere in any of the source PDFs.

**Severity:** none.

---

## The Dying World

**Entry:** `wiki/lore/The Dying World.md`
**Source:** Bare Bones pp. 7, 11 (sections II, III, IV of "What Was Written Must Be Known"), p. 16.

### Coverage is good. One missing canonical passage (LOW):

Source p. 11 section IV reads in part:
> *"The world dies even now. Reality decays, truth becomes dream and dream, truth. Cracks grow in the once-stable structures of the past, allowing things misshapen and vile to worm through, emerging into day's wan light."*

Wiki captures this nearly verbatim ("Reality decays. Truth becomes dream and dream truth."). Good.

The wiki's geography summary skips the canonical phrase from p. 7:
> *"The Wind from the west. From the sundered land. Rot rides it, and the stench of blood. Cursed walker, will you travel there? To the Valley of the Unfortunate Undead?"*

— wiki has the first sentence but not the address-to-the-reader continuation. Minor.

The phrase *"Life locked and failing in a DARK FORT"* is captured and translated. Good.

**Severity:** LOW.

---

## Shimmering Fields

**Entry:** `wiki/lore/Shimmering Fields.md`
**Source:** Bare Bones p. 12.

### Coverage is good.

Wiki accurately captures the canon from p. 12:
> *"To take one's own life is considered sinful cowardice. The road to salvation lies through mortification of the flesh; the apocalypse is to be met with eyes wide open. Only then can the soul be allowed passage to the Shimmering Fields."*

Sigfúm the Kind connection is preserved.

**Severity:** none.

---

## Heedless Creation

**Entry:** `wiki/lore/Heedless Creation.md`
**Source:** The Death Ziggurat, p. 6 (Spiral Chapel section).

### Coverage is good.

Wiki captures the canonical line:
> *"Dedicated to the spiraling cosmic force of Heedless Creation. The ceiling inside is a painted night sky with a spiral galaxy in the center."*

And the Spiral Crown effect:
> *"the wearer becomes a cosmic vessel, seeing strange and nightmarish visions of the infinite, collapsing Cosmos."*

The wiki note that this is older than the Two-Headed Basilisks is consistent with the source's framing of "forgotten even by the oldest scribes in Galgenbeck" (re: Akünh's binding).

**Severity:** none.

---

## Death Realm

**Entry:** `wiki/lore/Death Realm.md`
**Source:** The Death Ziggurat, pp. 2, 6.

### Coverage is good.

Wiki captures the canonical lineage:
> *"a spawn of SHE — conceived in the unholy bonding between the basilisk and a demonic being from a parallel world filled with undeath and torment. Shut out from the world of the living by ancient covenant, but always gazing hungrily upon it…"*

The wiki note about Akünh's "channeling" as a tornado-cloud of power drawn from her demonic parent matches source p. 6 (`a whirlwind of clouds at its top, ever pulling from a point in the sky`).

**Severity:** none.

---

## The Dark Spider, Harbinger of the End

**Entry:** `wiki/lore/The Dark Spider.md`
**Source:** The Merchant, p. 2.

### Coverage is complete; the gap is in canon.

Wiki accurately captures the only canonical reference:
> *"Repent for the sins of your family and be forgiven by the Dark Spider, Harbinger of the end."*

Said by the unnamed "foul priestess" who saved Mikhael. That is the entire canon for the Dark Spider across all surveyed PDFs.

**Severity:** none.

---

## Goddess of Fat and Plenty

**Entry:** `wiki/lore/Goddess of Fat and Plenty.md`
**Source:** Bloat (MBC), p. 1–2.

### Coverage is good.

Source describes the labyrinth as *"once the home of an obscure cult of bacchanalian priests dedicated to a goddess of fat and plenty"* and the statue as *"an imposing, corpulent woman with opal eyes"* — wiki captures both. The Gourmand's Cutlery as relic is implied in source, not stated outright — wiki notes "presumably," which is honest.

**Severity:** none.

---

## Cube-Violet

**Entry:** `wiki/lore/Cube-Violet.md`
**Source:** Bare Bones p. 45 (Arcane Catastrophes table); p. 70 (Adventure Seed 55–56).

### Coverage appears complete.

Four trials, Sict-Shroom poisoning, golden key fire trial, the "wait for another fool" final ordeal — all present. Adventure seed 55–56 cross-referenced.

**Severity:** none.

---

## Goblin Curse

**Entry:** `wiki/lore/Goblin Curse.md`
**Source:** Bare Bones p. 58; The Goblin Grinder.

### Coverage is good.

The d6-day transformation, attack-on-attack contagion, the "ruined mind watching its body-prison" framing — all present. The Goblin Cure / Nagel Krat connection is preserved.

**Severity:** none. (Note: Goblin Curse arguably belongs in `creatures/` not `lore/`, but that's a categorisation question, not a content gap.)

---

## Cross-cutting findings

### 1. Missing lore entry: "Forgotten Mind-Cult" / Tablets cosmology (MED)

`MÖRK BORG CULT: FERETORY — The Tablets of Ochre Obscurity`, p. 64 introduces:

> *"Made from the clay of the Valley of the Unfortunate Undead, these Ochre Tablets are Relics of a forgotten mind-cult so rare they can be sold for 100 silver."*

This **forgotten mind-cult** is a named-but-unnamed cosmic entity:
- It is canonically older than the Two-Headed Basilisks.
- Its Tablets are made of clay from the **Valley of the Unfortunate Undead** — connecting it to **HE**, **SHE**'s lair geography, and possibly the same dust-and-clay primordium the basilisks crawled from.
- The Forlorn Philosopher class (`MÖRK BORG Forlorn Philosopher.pdf`) is canonically the only class that can wield the Tablets without Presence +3 — implying the Philosopher tradition has some unspoken connection to the cult.

No wiki entry covers this. `wiki/items/Tablets of Ochre Obscurity.md` exists (items side) but there is no `wiki/lore/Mind-Cult.md` or equivalent. The README index does not list it.

**Recommendation:** new lore entry, severity MED. Currently the only mention of an entire forgotten cult and its clay-relic cosmology lives on an items page.

### 2. Missing lore entry: The 10 dead gods of the Dead God's Prophet (MED → HIGH for category completeness)

`MBC_Dead_Gods_Prophet.pdf` p. 1 contains a 3d10 / d10×2 table of slain god-names. These are *named cosmic entities*:

> 1 Acrophoe — Beacon of blood
> 2 Elioch — Bearer of death
> 3 Ekk — Bride of decay
> 4 Ghzat — Child of flies
> 5 Gnost — Herald of impotence
> 6 Häil — King of panic
> 7 Kvera — Lady of rot
> 8 Malais — Prince of rust
> 9 Varkka — Queen of unease
> 10 Öde — Song of the flesh

Canon says **all of these were slain by SHE within the Bergen Chrypt**:

> *"You are the prophet of a god; only your god is dead, slain by the Basilisk SHE within the wretched peaks of the Bergen Chrypt."*

The wiki's `SHE.md` mentions this fact in a connections line, and `Dead God's Prophet.md` exists under `classes/`. But the lore folder has **no entry for the dead pantheon itself** — these are 10 named entities whose murder is a foundational cosmology event. Currently they exist only as a class-creation flavor roll.

**Recommendation:** new lore entry `Dead Gods.md` or `Slain Pantheon.md`. Severity MED.

### 3. Missing lore entry: Sagsobuth, interdimensional being (LOW–MED)

`MÖRK BORG ROTBLACK SLUDGE.pdf` p. III introduces:

> *"Bazaar from a distorted dimension — Sagsobuth manifests. An interdimensional trader…"*
> *"Sagsobuth — Shapeless and ethereal. Her face a vortex of light. Cannot be harmed but will not attack unless provoked."*

This is a named cosmic entity from a "distorted dimension" — i.e., another extradimensional realm parallel to (or distinct from) the Death Realm. It currently lives in `wiki/creatures/Sagsobuth.md` (creature stat block). There is no lore-side entry connecting it to the cosmology of parallel worlds / extradimensional bazaars.

**Severity:** LOW–MED, classification-dependent.

### 4. Anuk Schleger and Creton Order — out of scope but flagged

`wiki/lore/README.md` does not list Anuk Schleger or the Creton Order; both exist in `wiki/npcs/` and `wiki/factions/` respectively. As the prophet-author of the Nameless Scriptures and the order from which the orthodox Two-Headed Basilisks broke, they are arguably cosmological lore. Currently lore/Nameless Scriptures links to them but lore/README does not surface them in any sub-list.

**Severity:** LOW, structural.

---

## Summary table

| Severity | Count | Items |
|---|---|---|
| HIGH | 0 | (Misery Table is complete; no canonical verses missing.) |
| MED | 5 | Calendar procedural canon on Misery Table; die ladder on Calendar; Swamp-Witch wish interaction with Calendar; missing Forgotten Mind-Cult lore entry; missing Dead Gods (10 names) lore entry. |
| LOW | 6 | 4:1 apostrophe; missing prologue line on Calendar; "Burn the book." styling; Dying World address-to-reader passage; Nameless Scriptures' "supplanted all other Scripture" line; Nechrubel-worshipping lich seed not connected. |

The Misery Table itself — the brief's primary concern — is intact. The canon is 37 prophecies (not 49), Psalms I–VI × 6 + 7:7, and every verse is present in the wiki. The structural risks lie elsewhere: procedural canon scattered across two files, a forgotten mind-cult and a slain pantheon of 10 gods both absent from lore/, and a Calendar-interaction mechanic in the Swamp Witch source that contradicts the wiki's "no canonical mechanics" claim.
