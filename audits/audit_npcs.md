# NPC Wiki Audit — Source vs. Wiki

Auditor pass over `wiki/npcs/*.md` against source PDFs in `source/`.
Diagnosis only. Each entry lists what is missing or under-quoted from
the source, with severity. Severity scale:

- **HIGH** — canonical stat block, named ability, or load-bearing relationship omitted.
- **MED** — flavor phrasing, secondary item, or named link omitted; wiki is broadly correct but thin.
- **LOW** — minor tonal phrase, page anchor, or cross-reference omitted.

Quoted phrases below are verbatim from source PDFs (with original
typos/capitalization preserved where present).

---

## Entries with missing or truncated content

### Aldon — `wiki/npcs/Aldon.md`

Source: **MÖRK BORG ROTBLACK SLUDGE.pdf** (room 13, Son's Room).

Wiki captures the Son's-Room scene, the bullwhip, and Fletcher/Seer setup. Reasonable, but:

- **Bullwhip damage notation is wrong.** Source: *"A bullwhip with cryptic runes (d4 + necro-plasmic shock, d4 damage) hangs on the wall."* — i.e. **d4 base + d4 necro-plasmic shock**. Wiki collapses both into "d4 + necro-plasmic shock," losing the second d4. Severity: **MED**.
- **Statue / King Lenard II eye-puzzle omitted.** Aldon's room is sealed by a hereditary puzzle: *"Black statue of the one-eyed King Lenard II. Obvious cavity where the eye would be. Investigation reveals bloodstains in the socket … Place an eye in the king's socket: the door to the Son's room opens with a loud crack."* This is the only access to Aldon and it is gory; the wiki doesn't mention Lenard II or the eye-socket key at all. Severity: **HIGH** (this is the named connection to a prior Shadow King).
- **The Son's-Room contents beyond the whip** are omitted: *"Bookshelf with a large iron hook, a mirror and a crossbow with four bolts. Bowls with water and food."* These objects characterize Aldon's captivity. Severity: **LOW**.
- **No stat block** for Aldon in source — wiki correctly flags this gap.

---

### Anthelia — `wiki/npcs/Anthelia.md`

Source: **MÖRK BORG BARE BONES EDITION.pdf**, p.15.

Wiki is faithful to the Anthelia passage and quotes Misery 6:3 and adventure seed 37–38. Notes:

- **Page reference is slightly off.** Source quote *"Countess Anthelia. North, where the wind is born, lies Alliáns, a storm-piercing spire-city of black glass."* sits on the Kergüs spread, p.14–15 in source (index lists Anthelia at p.15). Wiki cites p.15; acceptable. Severity: **LOW**.
- **Misery 6:3 wording.** Source: *"6:3 Anthelia shall have her will and drink all colour from the world."* Wiki has it correct.
- No omissions in lore content; the gulls-cry phrasing, the "dreams of the Countess" line, and the "court life entails grey opulence, excitement and fear" beat are all present.

Overall **CLEAN.**

---

### Anuk Schleger — `wiki/npcs/Anuk Schleger.md`

Source: **MÖRK BORG BARE BONES EDITION.pdf**, p.10.

Wiki is faithful but loses one small detail:

- **The Two-Headed Basilisks discovery context.** Source: *"300 years later, while working on a new Cathedral, The Two-Headed Basilisks, an orthodox branch of the Creton order uncovered Schlegers tomb and with it the Scriptures."* Wiki says *"masons … broke ground for a new Cathedral"* — source says the basilisks themselves uncovered the tomb *while working on* the Cathedral, not *while breaking ground*. Minor phrasing drift. Severity: **LOW**.
- **The Calendar attribution line is uncited.** Source p.17 reads *"The Calendar of Nechrubel – The Nameless Scriptures. Transcribed by Anuk Schleger the monk."* Wiki doesn't quote this transcription credit. Worth pulling. Severity: **LOW**.

Overall **CLEAN.**

---

### Belpheduk — `wiki/npcs/Belpheduk.md`

Source: **Devils Tomb.pdf** (Traitor's Den room).

Wiki has stat block correctly: *"HP 5 Morale 3 Scales −d2 Claws d4"*. Notes:

- **Wiki adds detail not in source.** Wiki says *"this cell — a muddy, cramped cave with her severed arm nailed to the wall — is her punishment."* Source says *"Muddy, cramped cave. A severed arm is nailed to the wall."* and separately *"Belpheduk killed a fellow drowned and this cell is her punishment."* The wiki's *"her severed arm"* is an inference — source doesn't say whose arm. Could be a CANON CHECK. Severity: **MED**.
- **Drowned faction context is thin.** Source establishes the Drowned worship the Plant of Life *and* its "angelic children"; Belpheduk's betrayal is against worshippers of that Plant. Wiki could note she is a Plant-worship apostate, not just "a traitor." Severity: **LOW**.
- **Pronoun.** Source uses "her"/"she" — wiki uses "she" consistently. Good.

---

### Fathmu IX — `wiki/npcs/Fathmu IX.md`

Source: **MÖRK BORG BARE BONES EDITION.pdf**, p.15–16, 61 (the zombie cure note); **MBC_Sepulchre-of-the-Swamp-Witch.pdf** (the murdered messenger).

Wiki captures all three citations. Notes:

- **Zombie passage quote.** Source p.61 *Nodh, zombie*: *"The only cure or vaccine is said to be found at the peak of a pale mountain within an infinitely-miserable forest of dark leaves. king fAthmu ix of wästlAnd in particular seeks this cure and knows the name and location of the forest which the mountain overlooks."* Wiki paraphrases correctly.
- **Swamp Witch trigger phrasing.** Source: *"You stumbled on these forbidden words on a murdered messenger wearing mad King Fathmu IX's crest in a ditch."* Wiki gets the spirit but doesn't quote the *"mad"* descriptor (source applies it as a fixed epithet — Fathmu is *"mad King Fathmu IX"* in Sepulchre). Severity: **LOW**.
- **No stat block** in source — wiki correctly flags.

Overall **CLEAN.**

---

### Fletcher — `wiki/npcs/Fletcher.md`

Source: **MÖRK BORG ROTBLACK SLUDGE.pdf** (room 15, Forge/slaughterhouse).

Wiki has full stat block, all three Powers, his origin story, and sympathy-rain. Verified against source line-by-line. Minor:

- **Setting context.** Source places Fletcher's hearths-and-meat-hooks room: *"Sooty and very hot, sulfuric haze from Rotblack Sludge … Lit by two large hearths. Used as smelters and ovens for preparing meals … Chunks of meat hang on ceiling hooks. Largely human flesh—adults and children."* Wiki doesn't quote the *"largely human flesh — adults and children"* line, which is the cannibalism evidence. Severity: **MED** (the wiki calls him "cannibal warlock" but never quotes the source's reason).
- **Pump room ladder.** Source: *"west: stepladder to a hatch in the Pump room."* Adds a secondary egress not in wiki. Severity: **LOW**.

---

### Josilfa Migol — `wiki/npcs/Josilfa Migol.md`

Source: **MÖRK BORG BARE BONES EDITION.pdf**, p.12.

Wiki is brief but accurate. Notes:

- **Nechrubel context omitted.** Source: *"Nechrubel: the shadow that covers all. Nechrubel is melancholy, crop failure, conflict and war. It is said he whispered the apocalyptic prophecies in Verhu's ear."* Josilfa's bargain is with this entity — wiki names Nechrubel but doesn't relay what Nechrubel *is*. Severity: **LOW** (probably belongs in `wiki/factions/Nechrubel.md` or similar, not here).
- **Inquisition link.** Source on same page: *"Heretics and apostates are hunted down and corrected, in public and at length, by the Inquisition."* Wiki links to `[[Inquisition]]` in Connections but doesn't note Josilfa's authority over it. The Inquisition serves the Two-Headed Basilisks; Josilfa, as arch-priestess of Galgenbeck, presumably commands it. Worth flagging in expansion notes. Severity: **LOW**.
- **No stat block** in source — correctly flagged.

Overall **CLEAN.**

---

### Klopstock — `wiki/npcs/Klopstock.md`

Source: **MBC_Sepulchre-of-the-Swamp-Witch.pdf**, p.7 (Worship Hall).

Wiki captures the ring, the price markup, the unnamed surviving family member. Notes:

- **Source phrasing on the markup.** Source: *"Among them is a ruby ring inscribed with the name Klopstock—worth 200 silver to most merchants, but if brought to Schleswig, the only surviving Klopstock family member pays five times as much."* Wiki says 1000s (5× of 200s = 1000s). Math is right; the *"five times as much"* phrasing is in source, not the numeric 1000. Severity: **LOW** (numeric inference is fine).
- The wiki notes the cult took the ring. Source doesn't say the cult took it — it says the ring is *among the stained blankets of the Worship Hall*. Likely the cult had it, but this is wiki inference. Severity: **LOW**.

Overall **CLEAN.**

---

### Kulvan — `wiki/npcs/Kulvan.md`

Source: **MÖRK BORG BARE BONES EDITION.pdf**, p.45 (Cube-Violet trial list).

Wiki accurately notes Kulvan has no dedicated stat block — source only says *"Slay riddling Kulvan (strong goblin, page 58) who holds three colorless pearls."* and the page-58 reference points at the generic `Seth, Goblin` stat block (*"HP 6 Morale 7 Ropy skin -d2 Knife/shortbow d4 Special: Quick, attacks and defence are dr14."*). Notes:

- **Pearls' significance is undefined in source.** Wiki flags this as a gap correctly.
- **The other three trials are absent from Kulvan's page.** Source lists four trials to escape Cube-Violet; Kulvan is one of four. The other three (Sict-Shroom poisoning, the golden key in fire, empty-cube ending) are relevant to Kulvan's environment. Wiki could cross-link these as `[[Cube-Violet]]` content. Severity: **LOW**.

Overall **CLEAN** (correctly skeletal because source is skeletal).

---

### Lesdy — `wiki/npcs/Lesdy.md`

Source: **MÖRK BORG ROTBLACK SLUDGE.pdf** (room 11, Greenhouse).

Wiki has stat block (HP 5 Morale 4 No armor), the three hosts, the Greenhouse description, her sludge-and-Gutworm plan. Notes:

- **The 3 hosts' stat block is omitted.** Source: *"3 hosts. Young, dressed in rags. Zealous. HP 7 Morale – No armor. Long knives d6."* Wiki mentions them narratively but doesn't include the block, even though they fight alongside Lesdy and have **no morale** (will not flee). Severity: **HIGH** (combat-load-bearing).
- **Lesdy's *Morale 4*** is the lowest morale of any boss-tier NPC in canon — she will break on the slightest pressure. Worth flagging in the "she begs to be allies" interpretation. Severity: **LOW**.
- **No weapon on Lesdy herself.** Source gives her *no* listed weapon — she fights through her hosts. Wiki implies this but doesn't make it explicit.

---

### Mikhael the Merchant — `wiki/npcs/Mikhael the Merchant.md`

Source: **MBC_Merchant.pdf**.

Wiki has stat block (HP 6 Morale 9, Staff d4, Eternal Unlife) and the soul-cost trading mechanic. Notes:

- **Regional inventory tables are flattened to `[[Merchant Inventory]]`.** Source breaks Mikhael's wares into **three named regional lists**: **Tveland** (Stone Dagger, Tongue of a False Prophet, Two-headed Silver Ring, Vial of Goblin Ichor, Wickhead Brain, Galgenbeck Deathmask), **Wästland** (Pouch of Valley Vapors, Jar of Troll Piss, Fine but Gaudy Clothing, Pilgrim's Compass, Peasant's Kuksa, Lucky Fishing Spear), and **Kergüs** (Vibrant Red Ribbon, Vial of Glowing Blue Blood, Gleaming Golden Scalpel, Pleasing Green Cloak, One-eyed One-legged One-winged Gull, Bright Yellow Flower). Wiki defers all of this to an unbuilt link. Severity: **HIGH** (the wares ARE Mikhael — his region-roving is mechanical, not flavor).
- **"Foul priestess"** is named exactly that in source — wiki notes she is unnamed. Correct.
- **The Dark Spider** is mentioned only once in source as *"the Dark Spider, Harbinger of the end"* (capitalized in source). Wiki correctly flags as expansion seed.
- **White-eyed mule** is canon: *"frequently found alone or with a wagon drawn by a white eyed mule."* Wiki captures.

---

### Nagel Krat — `wiki/npcs/Nagel Krat.md`

Source: **MBC_Goblin Grinder.pdf**.

Wiki has the full scheme, stat block, smoke-bomb, silver-in-apron mechanic, key info. Notes:

- **Smoke-bomb full effect.** Source: *"Smoke bomb DR14 Presence or Nagel gets away. Creates a brilliant flash as likely to blind you. Anyone within attacks and defence are rolled at −2 until a [period not extracted cleanly]."* Wiki says *"DR14 Presence or Nagel gets away"* — the **flash-blind effect (−2 attacks/defence)** is in source and missing from wiki. Severity: **MED**.
- **The "spare key on Urvan's body in the basement"** is in source and in wiki. Good.
- **Apron-silver chase rule.** Wiki has it correctly.

---

### Qarg — `wiki/npcs/Qarg.md`

Source: **MBC_Goblin Grinder.pdf**.

Wiki has stat block, the 50s/body and 10s/hour fees, the bribe DR8, the dragged-blood trail. Verified line-by-line against source. **CLEAN.**

---

### Sarku — `wiki/npcs/Sarku.md`

Source: **MBC_The-Death-Ziggurat.pdf**.

Wiki has stat block (HP 15 Morale 8, Blood-sucking tongue d4, Ethereal), the upside-down corpses, the heart-knowledge. Notes:

- **Stretches their tongues.** Source: *"a long, sharp tongue that sucks the blood of his victims and stretches their tongues."* Wiki captures *"stretches their tongues."* Good.
- **Once Akünh's closest advisor.** Source confirms wiki's phrasing.
- **Location detail.** Source says corpses *"hang upside down from the trees"* — wiki adds *"around the Death Ziggurat depression"* (correct inference from the depression context, but not literally a tree-around-depression quote). Severity: **LOW**.
- **Random-encounter entries.** Source has Sarku appear in encounters: *"9. Stalked by Sarku, who accidentally makes some noise before [attacking]"* and *"10. Approached by Sarku, curious."* This indicates Sarku is wandering the depression, sometimes hostile, sometimes curious. Wiki doesn't mention this dual behavior. Severity: **MED**.

---

### Shadow King — `wiki/npcs/Shadow King.md`

Source: **MÖRK BORG BARE BONES EDITION.pdf**, p.13; **MÖRK BORG ROTBLACK SLUDGE.pdf**.

Wiki captures the hereditary line, the imbecile brother, Aldon's kidnapping, the masked Seer. Notes:

- **The Palace context.** Source p.13: *"A gothic black castle, like a mirror to the Cathedral of the Two-Headed Basilisk in Galgenbeck. Most of the palace lies in crumbling ruins, home to unfortunate souls sheltering beneath its broken halls. None dare dream what might lie under the rubble covered catacombs and cellars. Tunnels sprawl beneath like writhing roots, digging deeper into the cold earth like cancerous veins. The inner wing still stands, acting as the home of the Shadow King."* Wiki refers to *[[Palace of the Shadow King]]* but doesn't quote the catacombs-and-tunnels description in the Shadow King entry. Severity: **LOW** (belongs in the Palace entry, not here).
- **Princes-as-tricksters legend.** Wiki captures: *"It's whispered Princes of that line disguise themselves as ordinary men wandering the ruins engaging in games and tricking travelers, multiplying the miseries of their people."* Good.
- **King Lenard II** is named on a black statue in Rotblack Sludge's Statue Room — *"Black statue of the one-eyed King Lenard II"* — and is the access-key to Aldon's prison cell. **No wiki entry** for Lenard II exists, and the Shadow King page doesn't note him as a presumed-prior Shadow King. Severity: **HIGH**. Lenard II is a hereditary anchor for the line.

---

### Sigfúm the Kind — `wiki/npcs/Sigfúm the Kind.md`

Source: **MÖRK BORG BARE BONES EDITION.pdf**, p.14.

Wiki captures the calendars-of-despair, the Terion march, the Inquisition disapproval, adventure seed 57–58. Notes:

- **Source uses present tense and adds context.** Source: *"King Sigfúm the Kind is mocked in the street."* (Note the present tense — Sigfúm is *currently* mocked, not "once mocked." The wiki says *"Once mocked"* which mistakenly implies he's no longer mocked.) Severity: **MED** (canon drift).
- **Source phrasing on the bridges.** Source: *"Each night the bridges scream and roar like great ships grinding upon rocks. Sigfúm is defeated."* Wiki doesn't quote the *"bridges scream and roar"* line nor *"Sigfúm is defeated"* — both are characterizing details. Severity: **LOW**.
- **Múr.** Source: *"Cut from the world by the bottomless Múr, the thriving city state can be reached only by three bridges of such might and cyclopean size it is said that only enslaved giants could have raised them."* Wiki doesn't link `[[Múr]]` (the bottomless chasm) or `[[the three bridges]]`. Severity: **LOW** (these belong on the Grift page; cross-link from Sigfúm).
- **No stat block** in source — correctly flagged.

---

### Silas the Fattened King — `wiki/npcs/Silas the Fattened King.md`

Source: **MBC_Bloat.pdf**.

Wiki has stat block (HP 20 Morale 9, Cutlery d4 + Engulf, Flatulence), the Goddess of Fat and Plenty cult, the automaton compulsion. Notes:

- **Tongue-shaped knife in the sewage pit.** Source: *"The only thing Silas can't digest is metal: beneath the sludge are d6 silver and a long, curved knife shaped like a tongue (d6 damage, on a hit makes the target ravenously hungry and desperately thirsty, must eat and drink within the hour or die)."* This is a unique cursed weapon tied to Silas's chamber. **Not mentioned in wiki.** Severity: **HIGH** (relic).
- **Opal-eyed statue in Chapel of Filth.** Source: *"Look into the opal eyes: DR14 Presence test or be compelled to visit Silas in room 6 and offer yourself for dinner."* This is the statue that compelled Silas himself in the backstory; the wiki references the statue but doesn't quote the DR14 compulsion mechanic. Severity: **MED**.
- **Ratbadger.** Source: *"The ratbadger is still here: HP 5, Morale 9, Tough hide –d2, Nasty bite d4."* This is the creature whose burrow Silas crawled into — narrative anchor for the discovery story. Severity: **LOW**.

---

### Srolki & Yaoxl — `wiki/npcs/Srolki & Yaoxl.md`

Source: **MBC_Sepulchre-of-the-Swamp-Witch.pdf** (room 11, Downward Spiral).

Wiki has both stat blocks, Slimespeed, Croak, Drain, the Powers list, the cities-below note. Notes:

- **Trident object name discrepancy.** Source says *"They are willing to do almost anything to get their hands on the Croaking Trident."* — but Yaoxl actually wields the **Ranseur of the Maelström** (not the Croaking Trident). The Croaking Trident is what they *want*; the Ranseur is what Yaoxl *has*. Wiki captures both names but doesn't explicitly say the Croaking Trident is **not yet in their possession**. Severity: **MED** (the GM needs this to run the encounter).
- **Where the Croaking Trident actually is** — source does not say. This is a true gap in canon. Wiki should flag.
- **Page 50' below the ledge.** Source places them *"hidden 50' below"* the ledge entrance — wiki has "fifty feet below the Downward Spiral." Good.

---

### Swamp Witch — `wiki/npcs/Swamp Witch.md`

Source: **MBC_Sepulchre-of-the-Swamp-Witch.pdf** (room 9).

Wiki has stat block (HP 30 Morale −, Ethereal barrier −d4, Lunar Zweihänder d12 + radiance), Radiance, Eternal. Notes:

- **Lunar Zweihänder placement.** Source: *"On her back is a shining greatsword longer than she. She floats 2' above the ground."* Wiki has *"longer than she is"* — accurate. Good.
- **Telepathy.** Source: *"She communicates telepathically with either whispers or screeches."* Wiki captures.
- **The wish-mechanic is on the altar entry, not the witch.** Source has the Swamp Witch *instructing* PCs how to make a wish at the Dead Root Altar — *"would all members of the party truly be missed in this world?"* Wiki captures this beat.
- **Strange Serpent Drug Cult relationship.** Source: *"At first the cult is unaware of the Swamp Witch or her tomb but know plenty about an altar [further in]."* Wiki notes this in Connections but phrases it parenthetically. Severity: **LOW**.

Overall **CLEAN.**

---

### Tergol — `wiki/npcs/Tergol.md`

Source: **MÖRK BORG BARE BONES EDITION.pdf**, p.7, 72.

Wiki correctly identifies Tergol as a deliberate blank slate. The two source mentions are: opening invocation (*"Our young ones are taken by the child-thief Tergol, known for his vile crimes and alchemy of flesh"*) and Bedeviled Dungeons table entry 10 (*"Tergol's escaped experiment"*). Wiki captures both.

Overall **CLEAN.**

---

### The Bastard — `wiki/npcs/The Bastard.md`

Source: **MBC_Goblin Grinder.pdf**.

Wiki has stat block (HP 10 Morale 6, Mutant hide −d4, Knife d4, Goblin overlord trait). Verified against source. **CLEAN.**

---

### Ueth — `wiki/npcs/Ueth.md`

Source: **MBC_Sepulchre-of-the-Swamp-Witch.pdf**.

Wiki has stat block (HP 20 Morale 6, Gatorskin robe −d4, Jagged spear d8 + bleed), the gospel scroll, Slithering Strangulation. Notes:

- **Three large snakes upside-down on his chamber ceiling.** Source: *"There are three large snakes slithering upside down on the ceiling. They do not wish to be disturbed and respond to threats by attacking twice the same round for D4 damage and then disappear."* Visible only on Emerald Venom. Wiki doesn't mention these. Severity: **MED** (encounter-load-bearing — these are *in his room*).
- **The chamber visibility.** Source: *"The small openings leading to Ueth's chamber are only visible for those on Emerald Venom."* Wiki doesn't note the access requires the drug. Severity: **MED**.
- **Slithering Strangulation full effect.** Source: *"D4 rainbow colored, ethereal boa constrictors emerge from the ground and capture one creature each for D8 rounds, dealing D2 damage each round. Attacking a constricted creature in melee comes with a 50% risk of the snake changing target to the attacker."* Wiki links the Power but doesn't quote its mechanics. Severity: **LOW** (belongs on the Power entry, not Ueth).

---

### Urvan Krat — `wiki/npcs/Urvan Krat.md`

Source: **MBC_Goblin Grinder.pdf**.

Wiki has the corpse description, the body's loot (yellow vial, spare Grinder key in boot), the mill-ownership backstory. Verified against source. **CLEAN.**

---

## Named NPCs in source PDFs with NO wiki entry

The following named characters appear in canon and are not covered by `wiki/npcs/`. They are real omissions, not just background mentions.

### From MÖRK BORG BARE BONES EDITION

- **Arkh** (p.11) — *"Her twin Arkh, Head of Deception, claims to be the first prophet of truths now prostituted by Verhu."* One of the four basilisk heads. No wiki entry. Severity: **HIGH** (named deity-tier figure). *Note: may belong under `wiki/factions/` or `wiki/creatures/Basilisks` rather than NPCs.*
- **Lusi** (p.11) — *"she bears the head of Denial, Lusi, who looks up and down. Yet all shall be well."* The first basilisk; oldest. Severity: **HIGH**.
- **Gorgh** (p.11) — *"The head Gorgh is bitter, rank with envy that only his twin Verhu knows the damned truth."* Severity: **HIGH**.
- **Verhu** (p.10–11) — wiki links `[[Verhu]]` from multiple entries but `wiki/npcs/Verhu.md` does not exist. The single most-referenced canon entity besides Nechrubel. Severity: **CRITICAL** (this is the prophet-basilisk; everything in the wiki cross-references him). *Categorization note: deity/creature, but the wiki uses [[Verhu]] inline everywhere — the broken link will surface in every other entry.*
- **Nechrubel** (p.12) — *"Nechrubel: the shadow that covers all. Nechrubel is melancholy, crop failure, conflict and war. It is said he whispered the apocalyptic prophecies in Verhu's ear."* Same status as Verhu. Severity: **CRITICAL**.
- **Daejmon** (Misery psalm) — *"as it is sundered by Daejmon, the left underling of Nechrubel."* Named once, in a Misery. Severity: **MED**.
- **HE / The Basilisk in the Valley** (p.16) — *"Rumors whisper the basilisk HE is coiled within its crypts."* Also referenced in adventure seed 69–70 (*"HE demands a gift. See it delivered"*). Same entity as Gorgh? Source is ambiguous. Severity: **HIGH**.

### From MBC_The-Death-Ziggurat

- **Akünh** — the demon spawn at the ziggurat's center. Wiki README mentions `[[Akünh]]` as "five-eyed demon spawn (also creature entry)" but there is **no `wiki/npcs/Akünh.md`**. Source has full stat block: *"HP 20, Morale 11, No armor. Death scream … Claws and devouring … Dark rays … Separated heart … Teleport."* Severity: **CRITICAL**.

### From MBC_Graves_left_wanting

- **Fela Maus** — *"The legendary bard-made-noble Fela Maus was cursed by a bog hag after neglecting to fulfill her part of a long-forgotten occult enterprise."* Dead, but her bones float in the Vomatorium and her family's skulls bedeck the **Roseate Baritona** horn. Severity: **HIGH** (named, historied, item-bearing).
- **Erhard** — Erhard's Tomb in Graven-Tosk contains his odorless waxy corpse with an iron skeleton and a fist-sized ruby in the ribcage. *"a man's odorless corpse in near perfect condition, wearing fine silk clothes. The skin is waxy, malleable like dough and very flammable."* Named only by tomb-association, no first-person info, but worth a stub. Severity: **MED**.
- **The Roach Herder** — *"a graverobber made hermit, sits on his throne, roach whip in grubby hand."* HP 4 Morale 5, Bite d4 + special, Barbed Roach Whip d6. Recruitable. Severity: **HIGH** (statted, named, recruitable companion).
- **The Undertaker** (a.k.a. dead form **The Übertaker**) — *"The Undertaker dug graves and made coffins. She buried corpses and left them to rot. Some refused to do so quietly. Some, she silenced herself."* HP 27 (Übertaker form), Barrier (palefire) −d4, four powers. Killed by the Deadn't, returns as a fiery skeletal entity. Severity: **HIGH**.
- **Stein** — Grift merchant. HP 2 Morale 8, Shortsword d4, 50s purse. One of the Deadn't. Severity: **MED**.
- **Benzen** — Schleswig guard. HP 3 Morale 9, Leather −d2, Crossbow d8, 10 bolts. One of the Deadn't. Severity: **MED**.
- **Arga** — Galgenbeck priest. HP 4 Morale 10, Scale −d4, Staff d4, carries a random sacred scroll. One of the Deadn't. Severity: **MED**.
- **The Deadn't** (collective) — three living people who killed the Undertaker and got trapped in the cemetery. *"They're friendly enough and invite the PCs to join them in settling down."* Severity: **HIGH** (collective entry; named members above could either each get a stub or be folded here).

### From Devils Tomb

- **The Madman** — *"Former graverobber, mad with spore-fever. Naked and unarmed. Cannot remember his name. Scared to death of The Angelic Choir."* HP 2 Morale −, Bite d2. Stops PCs from entering. Severity: **MED** (un-named in source but distinct character role).
- **St Largoth** — *"The Eyes of the Icon of St Largoth have been stolen."* Named saint; source provides only the name and the existence of the icon (and its eyes, which see hidden things). Severity: **LOW** (referent only).

### From MÖRK BORG BARE BONES EDITION — creature stat blocks with proper names

Source treats these as creature *types* (representative individuals named for the entry), not as unique NPCs. Auditor view: they read as named NPCs and could each have a wiki entry, but they're better filed under `wiki/creatures/` than `wiki/npcs/`. Listing here for completeness — none has an entry anywhere in the wiki:

- **Belze** (blood-drenched skeleton, p.59 — uses piercing rules and mimics voices)
- **Arbint** (Troll, p.60 — *"They grow larger during the healing process and will definitely come back, stronger than before."*)
- **Nodh** (zombie, p.61 — the cure-mountain mention sits in this entry)
- **Lady Porcelain** (undead doll, p.61 — *"In Tveland relic thieves, defamers and corrupt clerks suffer a punishment of exquisite and deeply impractical cruelty."*)
- **Thinx** (Grotesque, p.61)
- **Aland** (Wickhead knife-wielder, p.61)
- **Seth** (Goblin, p.58 — the generic goblin block Kulvan inherits from)
- **Bent** (Scum, p.58 — slum cutpurse)
- **Zukuma** (berserker, p.58)
- **Wrat** (Wraith, p.59)
- **Eulotha** (Wyvern, p.62 — *"Where the wyvern fly crops die"*)

These are creature-archetype names rather than unique individuals (any encounter spawns a "Seth" or a "Bent"). Probably belong in `wiki/creatures/` rather than `wiki/npcs/`. Severity: **N/A for NPC index**; flagged so they aren't lost.

### From MBC_Goblin Grinder

- The "unsavory royals" whose torturer-corpse became The Bastard are unnamed in source. Already flagged in Bastard entry.
- The assassin who killed Urvan is unnamed in source. Already flagged in Urvan entry.

### From Rotblack Sludge

- **King Lenard II** — *"Black statue of the one-eyed King Lenard II"* in the Statue Room of the Accursed Den. Presumed prior Shadow King (the statue's eye is the key to the Son's Room where Aldon is held). No wiki entry. Severity: **HIGH** (named historical Shadow King; mechanically load-bearing for the Aldon rescue).
- **The desperate necromancers** who raised Fletcher — unnamed. Already flagged in Fletcher entry.

### From MBC_Bloat

- **Goddess of Fat and Plenty** — *"bacchanalian priests dedicated to a goddess of fat and plenty."* Unnamed proper noun. Severity: **MED** (deity reference, no wiki entry; could be `wiki/factions/` material).

### From MBC_Merchant

- **The foul priestess** who cursed Mikhael — unnamed in source. Already flagged in Mikhael entry.

### From MBC_The-Death-Ziggurat

- **Rot priests** / **Cultist** — the 25 cultists from Tveland are statted but the rot-priests are statted *and* named as a faction. Could be a wiki entry for the rot-priest order. Severity: **LOW**.

---

## Cross-cutting issues

1. **Broken wiki links.** The wiki uses `[[Verhu]]`, `[[Nechrubel]]`, `[[Akünh]]`, `[[Daemon of Capillaries]]`, `[[Nine Violet Signs Unknot the Storm]]`, `[[Ich-bin-luft]]`, `[[Metzhuotl Blind Your Eye]]`, `[[Roskoe's Consuming Glare]]`, `[[Slithering Strangulation]]`, `[[Two-Headed Basilisks]]`, `[[Calendar of Nechrubel]]`, `[[Gutworm]]`, `[[Emerald Serpent]]`, `[[Cube-Violet]]`, `[[Goblin Curse]]`, `[[Goblin Cure]]`, `[[Goblin Grinder]]`, `[[Gourmand's Cutlery]]`, `[[Fleshy Automaton]]`, `[[Plant of Life]]`, `[[Lunar Zweihänder]]`, `[[Ranseur of the Maelström]]`, `[[Dead Root Altar]]`, `[[Croaking Trident]]`, `[[Emerald Venom]]`, `[[Strange Serpent Drug Cult]]`, `[[Drowned]]`, `[[Nameless Scriptures]]`, `[[Creton Order]]`, `[[Inquisition]]`, `[[Sarkash]]`, `[[Galgenbeck]]`, `[[Graven-Tosk]]`, `[[Bergen Chrypt]]`, `[[Schleswig]]`, `[[Kergüs]]`, `[[Alliáns]]`, `[[Wästland]]`, `[[Grift]]`, `[[Terion]]`, `[[Nechdorf]]`, `[[Lake Onda]]`, `[[Shimmering Fields]]`, `[[Cathedral of the Two-Headed Basilisks]]`, `[[Palace of the Shadow King]]`, `[[Valley of the Unfortunate Undead]]`, `[[Sepulchre of the Swamp Witch]]`, `[[Accursed Den]]`, `[[Derelict Mill]]`, `[[Medickal Shoppe]]`, `[[Death Ziggurat]]`, `[[Devil's Tomb]]`, `[[Rotblack Sludge]]`, `[[Merchant Inventory]]`, `[[The Dark Spider]]`. The npcs/README.md also references `[[Akünh]]`. Confirm which of these have target entries; this audit only covers `wiki/npcs/` so cross-link integrity is out of scope but worth flagging the volume of dependencies.

2. **README.md gap.** `wiki/npcs/README.md` lists `[[Akünh]]` but no Akünh.md exists in wiki/npcs/. Either remove the listing or build the entry. Severity: **MED**.

3. **Page references are inconsistent.** Some entries cite source PDFs by scenario name only (e.g. "Source: Rotblack Sludge"), others give page numbers (e.g. "p.15"). Page numbers in source PDFs sometimes drift by ±1 due to cover-page numbering. Recommend a single convention.

4. **The "Verhu, Nechrubel, Akünh" trio** is the highest-priority gap. These are *not* in `wiki/npcs/` and they are *the* most referenced figures in canon. Categorization (deity vs creature vs NPC) is a content-architecture question, but the wiki currently has dead `[[Verhu]]` and `[[Nechrubel]]` links across at least eight NPC entries.

---

## Severity rollup

| Severity | Count |
|---|---|
| HIGH (missing stat block, named ability, or load-bearing relationship) | 11 |
| MED (flavor phrasing, secondary item, named link omitted) | 13 |
| LOW (minor tonal phrase or cross-reference omitted) | 18 |

HIGH-severity items (consolidated):
- Aldon: King Lenard II eye-puzzle access mechanic.
- Lesdy: 3 hosts stat block missing.
- Mikhael the Merchant: full three-region inventory tables flattened to a placeholder link.
- Shadow King: King Lenard II unmentioned.
- Silas: tongue-shaped knife relic missing.
- No wiki entries for: **Verhu, Nechrubel, Akünh, Arkh, Lusi, Gorgh, HE, Fela Maus, The Roach Herder, The Undertaker / Übertaker, The Deadn't, King Lenard II**.
