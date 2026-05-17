# Creatures Audit — Wiki vs. Source PDFs

**Date:** 2026-05-17
**Scope:** All 31 wiki entries in `/wiki/creatures/`, audited against the source PDFs in `/source/`.
**Method:** Each wiki entry was compared line-for-line to text extracted with `pdfplumber` (which recovers table content that naive `pdftotext` strips out). Severity reflects how much canonical content is missing — not stylistic gaps.

## Severity legend

- **HIGH** — No stats at all, or whole stat block / major flavor passage missing.
- **MED** — Stat block present but truncated; abilities, flavor, or named NPCs missing.
- **LOW** — Minor missing detail or specific number/phrasing.

---

# Part I — Existing wiki entries with gaps

## Bare Bones bestiary (`MÖRK BORG BARE BONES EDITION.pdf`, pp. 58–67)

### Goblin (Seth) — LOW
**Source:** Bare Bones p.58.

The wiki entry is accurate against source. Minor notes:
- Source canonical name spelling is **"Seth, Goblin"** (the wiki has this).
- "Strong goblin **Kulvan**" appears in Bare Bones p.44 (Arcane Catastrophes table 19): *"Slay riddling Kulvan (strong goblin, page 58) who holds three colorless pearls."* Wiki notes this but does not state Kulvan holds **three colorless pearls** in its main entry.
- Bedeviled Dungeons p.71 also notes goblin connection: *"Animated suits of armor battling goblins"* (line 1) and *"Tergol's escaped experiment"* (line 10) — Tergol is a parallel child-thief.

### Scum (Bent) — LOW
**Source:** Bare Bones p.58.

Wiki is faithful. Source loot reads **"Captured 50–120s (wanted, serious crime) — Dead 20–70s (wanted, serious crime)"** — the wiki has the silver values but omits the **"(wanted, serious crime)"** qualifier (a flavor detail that explains why corpses fetch more than usual when bounty-eligible).

### Berserker (Zukuma) — none

Wiki matches source verbatim. No gaps detected.

### Wraith (Wrat) — none

Wiki matches source. No gaps.

### Blood-drenched Skeleton (Belze) — none

Wiki matches source. No gaps. (Note: the **Veil of Blood** in Tenebrous Reliquary item #25 explicitly *"victims who succumb arise as a blood-drenched skeleton the next round, attacking at random"* — wiki could cross-reference.)

### Lich — LOW
**Source:** Bare Bones p.60.

Wiki accurate. Source full name is **"Lich, Undead (weak) necromancer"** — wiki has this. The wiki's note about "weak necromancer variant" implying greater liches is canonical reading.

The Bedeviled Dungeons table (p.71) names **"Nechrubel-worshipping lich with a skeletal court"** as a dungeon-occupant — wiki has this. Eat Prey Kill (p.12) also names *"A Lich looking for some god damn peace and quiet"* as a Whisperbird master — wiki does not cross-reference.

### Troll (Arbint) — none

Wiki matches source. No gaps.

### Zombie (Nodh) — none

Wiki matches source. No gaps. (The wiki's quest hook explanation re: Fathmu/pale mountain/forest is accurately drawn from source.)

### Lady Porcelain — none

Wiki matches source. No gaps. Note: Bedeviled Dungeons (p.71) entry 4 reads *"A vengeful cabal of undead porcelain dolls"* — wiki references this.

### Grotesque (Thinx) — none

Wiki matches source. No gaps.

### Wickhead (Aland) — none

Wiki matches source. No gaps. Cross-references Wild Wickhead and Wickhead Brain correctly.

### Wyvern (Eulotha) — none

Wiki matches source.

### Outcasts — HIGH (Pale One + Prowler tables truncated)
**Source:** Bare Bones pp.63–67.

The wiki entry **explicitly flags** its Pale One and Prowler tables as "(unwritten in plaintext source) / Treat as canonical gaps to fill at the table." But these are NOT canonical gaps — they exist in source and `pdftotext` simply missed them. `pdfplumber` recovers the full text.

**Missing — 3. Pale One (Outcast follower)** (Bare Bones p.66):
- Specialty 3 (currently blank in wiki): *"Use one random unclean Power"*
- Specialty 4 (blank): *"Use one random sacred Power"*
- The specialty header is *"Speciality (d4), once per day"* — wiki omits "once per day".
- Values 1 (blank): *"Not having to use their speciality all the time"*
- Values 3 (blank): *"Listening to melancholic melodies"*
- Values 4 (blank): *"A couple of hours alone in darkness"*
- Values 6 (blank): *"Obscure rituals with the group"*

**Missing — 4. Prowler** (Bare Bones p.67):
- Speciality header should read *"Speciality (d4), dr8"* — wiki omits the DR8 mechanic note.
- Specialty 1 (blank): *"Disarm traps (you need to find them first)"*
- Specialty 2 (blank): *"Steal single items"*
- Specialty 3 (blank): *"Climb impossible routes alone"*
- Specialty 4 (blank): *"Finds trails and corners that keep the group hidden."*
- Values 1 (blank): *"Payment in silver"*
- Values 6 (blank): *"Getting the credit for exploits"*

The wiki's "[unwritten]" markers should all be replaced with the canonical entries above.

---

## Cult & adventure bestiary

### Akünh (Dread, Demon Spawn) — LOW
**Source:** `MBC_The-Death-Ziggurat.pdf`, pp. 2, 9.

Wiki largely accurate against source. Specific drift:
- Source consistently spells the order **"Cretun"** (pp. 2, 4 of Death Ziggurat). The wiki spells it **"Creton Order"** with a [CANON CHECK] cross-reference elsewhere. Acceptable but worth noting.
- Source text describes Akünh's heart as *"black and pulsating"*, *"embedded in a wall of pulsating flesh ten meters below"* — wiki has this.
- Source: the cultists discovered the **"rotting mouth in the woods"** but "not dared to enter" — wiki could mention this discovery point.
- The depression environment around Akünh — *"ice covers the river and heavy snowflakes occasionally drift through the air"*, *"strange effects when crushed"* black flowers — is location-flavor that primarily lives in `/wiki/locations/Death Ziggurat.md` but not referenced from the Akünh entry.

### Rot Priest — none

Wiki matches source.

### Horn Beast — none

Wiki matches source.

### Bone Bowyer — none

Wiki matches source verbatim. The bow's special is properly recorded.

### Membrane of Sarkantha — none

Wiki matches source. (Source has no HP/Morale block; wiki correctly omits.)

### Sarcopha-Ghost — none

Wiki matches source.

### Emerald Serpent — LOW
**Source:** `MBC_Sepulchre-of-the-Swamp-Witch.pdf`, p.5 (room 1), p.8 (room 6).

Wiki accurate. Minor:
- The full **Emerald Venom** description (effect on perception: *"Everything turns chromatic. Fire burns with colors never seen before: jale, dolm, and ulfire. Spectral leaf buds grow from dead matter. Everything is kaleidoscopic. Nature sings just for you. There is beauty in the world. Certain truths become clear to you. You get −1 on initiative (if using individual initiative) and fumble on 1–3 for the duration of the 7-day-long high"*) is part of the bite mechanic; wiki points to `[[Emerald Venom]]` for the detail, which is acceptable.
- The "second Emerald Serpent" lives in the **Snake Pit** (room 6) — wiki has this.

### Forked-Tongue Devotee — none

Wiki matches source. (Both Viper-spit clauses correctly preserved despite source duplication.)

### Plant of Life — none

Wiki matches source.

### Gutworm — none

Wiki matches source.

### Sagsobuth — none

Wiki matches source.

### Alchemical Ooze — none

Wiki matches source (MBC_Goblin Grinder.pdf, room 3 Laboratory, p.13).

### Fleshy Automaton — none

Wiki matches source (MBC_Bloat.pdf, room 5 Automaton Storage).

### Dusk Gnoum / Mongrel / Nesting Death — none

All three Accursed Den encounter-table A creatures match source verbatim (Rotblack Sludge p.III).

### Leviathan — LOW
**Source:** Bare Bones p.19 (Psalm IV, 4:5 & 4:6).

Wiki accurate to the only canonical text. (Leviathan has no stat block in source, only the two Misery-Psalm references.)

---

# Part II — Creatures named in source PDFs with NO wiki entry at all

These are statted (or named-and-described) creatures that appear in source but have no individual `/wiki/creatures/*.md` file. Severity is the size of the gap from the wiki user's perspective: HIGH means full stat block + ability + flavor missing entirely.

## From Bare Bones

### Two-Headed Basilisks (and SHE, HE, Verhu, Lusi, Arkh, Gorgh) — MED
**Source:** Bare Bones pp.10–11.

These four basilisk-heads are deities / monsters of the cathedral. They have lore (multi-page) but no monster stat block in Bare Bones. They appear in `/wiki/npcs/` and `/wiki/factions/` and `/wiki/locations/` but not as creatures. The Bare Bones Misery 2:6 says *"And SHE shall see HIM grow stronger. And SHE reveals herself and all shall be slain"* — implying combat encounter eventually. Flagged here because they are the most prominent **creatures** in the cosmology with no creature-page.

### Bedeviled Dungeons "Who" table — HIGH (collectively)
**Source:** Bare Bones p.71.

Twelve named dungeon-occupant entries. Wiki references several from individual creature pages (Lich, Lady Porcelain) but the following are uncited / have no wiki entry:
- **"A meaty mass of slime, larvae and spider legs"** (entry 6) — no wiki entry.
- **"A Bark-Witch and her root-children"** (entry 8) — no wiki entry.
- **"Four-legged pale gremlins stinking of dirt"** (entry 9) — no wiki entry.
- **"Tergol's escaped experiment"** (entry 10) — Tergol exists as an NPC but the escaped experiment-creature has no wiki entry.
- **"Disease spreading ochre-beetles"** (entry 11) — no wiki entry.

These are one-liners but each is a named creature/group in canon.

### Misery-table named creatures — MED
**Source:** Bare Bones pp.17–20 (Calendar of Nechrubel).

- **Psalm 1:4** *"the depths of the underworld shall bring forth flying spectres and crawling beasts"* — unnamed, no entry. Could be flagged on Bedeviled Dungeons / Calendar page.
- **Psalm 5:4** *"all those not yet of seven years and seven days shall pass. Born and unborn. And dawn shall give them life as eaters of men"* — child-eater undead, unnamed, no entry.
- **Psalm 6:5** *"The earth shall vein, bringing black serpents forth from within the earth"* — Black Serpents, named, no entry.
- **Psalm 6:6** mentions **Daejmon, the left underling of Nechrubel** — named, no entry.
- **Psalm 7:7** **Yetsabu-Nech** *"the underworld's nightmare, the black disk which stands before the sun"* — named, no entry.

## From `MBC_The-Death-Ziggurat.pdf`

### Undead (Death Ziggurat) — HIGH
**Source:** Death Ziggurat, p.8.

The "drooling, red-eyed undead" Akünh raises have a **full stat block** in source that is not present anywhere in `/wiki/creatures/`. Wiki only mentions them via alias on Akünh.md.

Source:
> **UNDEAD.** The rotting dead, awakened to serve. Drooling tongues, red eyes.
> HP 3, Morale −, No armor
> **Grapple.** Test Strength DR12 or be grappled. Subsequent attacks (by all present undead) are claw or bite (d4).
> **Will not die.** Only stays dead for one round, will then rise again with 1 HP.
> **Slow.** Can always be outrun (unless you are grappled).

Needs its own entry, since these are mechanically distinct from Zombies (Nodh), Lady Porcelain undead, Sarcopha-Ghosts, Wraiths, etc.

### Sarku — MED (statted in source, wiki entry is under `/npcs/`)
**Source:** Death Ziggurat, p.8.

Sarku has HP 15, Morale 8, Blood-sucking tongue d4 + grapple, Ethereal (immune to physical harm). The NPC wiki entry has this stat block — but the creatures README lists Sarku under "Cult Bestiary" and there is no `/wiki/creatures/Sarku.md`. Either re-classify the NPC entry as creature, or create a creature stub that points to the NPC entry. Mechanically he is a statted hostile entity.

### Death-Obsessed Cultist (creature stat block) — MED
**Source:** Death Ziggurat, p.9.

The cult faction wiki entry exists (`/factions/Death-Obsessed Cultists.md`) and references the Deathlike Silence Power. But the **stat block** is in source and missing from the wiki:
> HP 16, Morale 6, Fur armor −d2, Axe/Spear/Scythe d6
> **Deathlike silence** (Power, highest-rank only). All must test Presence DR14 or become deaf for d10 minutes. Every test requiring hearing or balance has its DR increased by 4.

Either add the stat block to the faction page or stub `/wiki/creatures/Death-Obsessed Cultist.md`.

## From `MBC_Sepulchre-of-the-Swamp-Witch.pdf`

### Strange Serpent Drug Cultist (creature stat block) — MED
**Source:** Sepulchre, p.5 (room 2 Cult Common Hall).

The cult has a faction wiki entry but no creature stat block in `/wiki/creatures/`. Source stat block:
> HP 4, Morale 4, Gatorskin vestment −D3, Knife or club D4
> **Drug-addled.** Immune to mind-affecting powers.

These are the rank-and-file (vs. Forked-Tongue Devotees, which DO have a creature page).

### Ueth the Scalehunter (creature stat block) — MED
**Source:** Sepulchre, p.6 (room 4 Scalehunter's Chamber).

Ueth has an NPC wiki page (`/wiki/npcs/Ueth.md`) — but should arguably be flagged as a creature too (per Sarku precedent). Source:
> HP 20, Morale 6, Gatorskin robe −D4, Jagged spear D8 + bleed
> **Bleed.** D2 damage every round for d4 rounds after being hit by the spear, ignores armor.

### The Swamp Witch (creature stat block) — MED
**Source:** Sepulchre, p.11 (room 9 Tomb).

NPC wiki entry exists. Source has a major creature stat block missing from `/wiki/creatures/`:
> HP 30, Morale −, Ethereal barrier −D4, Lunar Zweihänder D12 + radiance
> **Radiance.** The Lunar Zweihänder ignores all non-magical armor; each hit fills the room with radiant light. Everyone within 50′ tests Presence DR12 or takes D4 damage.
> **Eternal.** As long as the Dead Root Altar stands, the Swamp Witch does not die at 0 hp but instead evaporates and reforms in the sarcophagus with full health 3D6 rounds later. Should the Swamp Witch truly die, the Emerald Serpents, the barrier blocking the Downward Spiral and all Emerald Venom hallucinations disappear forever.

Form: *"a scraggy figure dressed in a green robe. Instead of skin, she is covered in multi colored scales, and where her head should be is just black smoke and two bright diamond eyes."*

### Srolki and Yaoxl — HIGH
**Source:** Sepulchre, p.12 (room 11 Downward Spiral).

A combined `/wiki/npcs/Srolki & Yaoxl.md` may exist but the two **antediluvian three-eyed humanoid toads** are statted creatures with no creature-page. Source:

**Srolki:**
> HP 25, Rubbery skin and Metal armor −D6, Claws D6 ×2 and Bite D10 or Croak
> **Slimespeed.** Attacks twice each round with their claws and bites or croaks once. Attack and defence tests are DR14 against Srolki.
> **Croak.** A loud croak stuns and deafens anyone within 20′ unless they test Presence DR12.

**Yaoxl:**
> HP 27, Rubbery skin −D3, Ranseur of the Maelström D10 + drain
> **Drain.** The ranseur transfers D4 hp from the target to Yaoxl on each hit.
> **Powers.** Can wield the following powers up to D3 times per day each: Metzhuotl Blind Your Eye, Nine Violet Signs Unknot the Storm, and Roskoe's Consuming Glare.

Flavor: *"Srolki and Yaoxl have guarded this pit for centuries, during which they have been partners, enemies, lovers and allies. They are willing to do almost anything to get their hands on the Croaking Trident. If the barrier is broken and one lives to tell the tale, more of their kind will appear in the area over the next d20 days. ... further down, great caverns open up, and somewhere deep are entire cities of these creatures."*

There is no wiki entry for "Antediluvian Three-eyed Toad" or "Toad-folk" as a creature category — a major gap given Sepulchre's setup.

## From `Devils Tomb.pdf`

### The Madman — HIGH
**Source:** Devil's Tomb, p.1.

Statted but no wiki entry. Source:
> **THE MADMAN.** Former graverobber, mad with spore-fever. Naked and unarmed. Cannot remember his name. Scared to death of The Angelic Choir. The most stop any one from entering the tomb. Will fire first, then bite.
> HP 2, Morale −, No armor, Bite d2 + Scales −d2 + Claws d4 (text is layout-mangled).

### Goblins (Devil's Tomb variant) — LOW
**Source:** Devil's Tomb, p.1.

Statted in this PDF (HP 6, Morale 7, Ropy skin −d2, Knife d4, Hit and defend DR14). Stats match the standard goblin — wiki Goblin entry already lists Devil's Tomb in Source. No gap.

## From `MBC_Goblin Grinder.pdf`

### The Bastard (goblin overlord) — HIGH
**Source:** Goblin Grinder, p.5.

Wiki Goblin entry references "[[The Bastard]] (goblin overlord)" but there is no wiki page for him. Source:
> HP 10, Morale 6, Mutant hide −D4, Knife D4
> **Goblin overlord.** Allied goblins fighting with The Bastard are DR16 defence (including himself) and cannot be shaken (Morale is −) unless he's killed.

Flavor: *"a torturer for a group of unsavory royals, so he eased right into upper management. He's aware enough to speak, mostly used to throw crude insults."*

### Qarg (gravedigger / mercenary) — MED
**Source:** Goblin Grinder, p.5.

NPC, may belong in `/wiki/npcs/`. Stats:
> HP 9, Morale 7, Filthy furs −D2, Cudgel D6 or Shovel D4
> Easily bribed: convincing her to leave her post or miss a delivery is a DR8 Presence test if she's offered more silver.

### Nagel Krat (alchemist, murderer) — MED
**Source:** Goblin Grinder, pp.4–5, 14.

NPC referenced from many wiki pages but stats are in source:
> HP 6, Morale 6, No armor, Knife D4
> **Smoke bomb.** DR14 Presence or Nagel gets away.

### Excited Goblin / Archer Goblin / Bucket Goblin / Fresh Goblin variants — MED
**Source:** Goblin Grinder, pp.11, 12, 14.

Sub-types of Seth-goblin with variant stats:
- **3 excited goblins (cannon room):** HP 6, Morale 8, Ropy skin −D2, Knife D4. *Quick: attacks/defense are DR14.* One has alchemical explosive (DR14 Agility within 10', D8 damage and set ablaze).
- **3 archer goblins (Fire! Fire!):** HP 6, Morale 7, Ropy skin −D2, Shortbow + flaming arrows D6. Quick DR14. One "bucket goblin" with Morale 6, oil-bucket.
- **Fresh Goblins (Grinder room):** HP 5, Morale 7, Ropy skin −D2, Bite D4. Quick DR14.

Stats subtly differ from the canonical Seth (HP 6) — wiki Goblin entry could note these adventure-specific variants.

### Ratbadger — HIGH
**Source:** `MBC_Bloat.pdf`, room 1 Vestibule.

Statted, no wiki entry:
> HP 5, Morale 9, Tough hide −d2, Nasty bite d4

Lives in the white-fungus crawlspace leading to Silas's labyrinth.

## From `MBC_Bloat.pdf`

### Silas the Fattened King — MED (NPC entry exists)
**Source:** Bloat, room 6 The Fattened King.

`/wiki/npcs/Silas the Fattened King.md` has the stat block. The creatures README cross-references this. No new gap, but he could be in `/wiki/creatures/` as well per Sarku/Ueth pattern.

## From `MÖRK BORG ROTBLACK SLUDGE.pdf`

### Bearded Man (Dining Hall) — LOW
**Source:** Rotblack Sludge, p.5, room 2.

Not statted, but a named occupant — *"Skin ashen grey, eyes dark, dressed in a dusty old cloak."* Cannot be communicated with unless everyone is seated; then he tells stories of old before slipping back. No wiki entry.

### Slumbering Skeletons (Library/Bedroom) — MED
**Source:** Rotblack Sludge, p.6, room 3.

Statted, no wiki entry. Source:
> 3 slumbering skeletons. Thoughtless, without goal.
> HP 5, Morale 7, No armor, Bony fists d4. One skeleton: Jagged scimitar d4.

Triggered by stealing flowers/books from the room.

### Tired Crystal Demon — HIGH
**Source:** Rotblack Sludge, p.6, room 3.

Statted, no wiki entry:
> Bound to this room, longing for a way to escape. Cannot be harmed. The demon will drain the text from one scroll. It sends out a Mental shockwave before vanishing into thin air.
> **Mental shockwave:** Any PC failing a Presence DR12 is unable to use Powers for the rest of the scenario and loses D6 HP.

Released when a PC yells *"you dead, arise!"* upon reading booklet #4.

### Crooked Guards — MED
**Source:** Rotblack Sludge, p.7, room 4.

Statted, no wiki entry:
> d4 crooked guards. They follow Fletcher's every word. He cursed their memories and they do not recall why they serve him. They don't care about Lesdy in the greenhouse.
> HP 8, Morale 7, Leather −d2, Sword d6 / Femur d4.

### Mad Prisoners — MED
**Source:** Rotblack Sludge, p.7, room 5.

Statted, no wiki entry:
> 10 mad prisoners. Emaciated and insane, they strangle anyone passing through.
> HP 2, Morale 4, No armor, Strangling hands d4/round (Agility DR12 to avoid; Strength DR12 to break free).

### Lesdy — MED (NPC, likely needs entry)
**Source:** Rotblack Sludge, p.12, room 11 Greenhouse.

Statted, no wiki page found:
> HP 5, Morale 4, No armor, Unarmed attack d4.
> Long dark hair, dressed in a gunny sack with armholes. Nice but manipulative. Is trying to turn the Gutworm against Fletcher. Seeks the tunnels and caves deep beneath Rotblack Sludge and believes consuming the sludge provides unique powers to control creatures.

Wiki Gutworm.md mentions her by name; no dedicated entry.

### 3 Hosts (Greenhouse) — MED
**Source:** Rotblack Sludge, p.12, room 11.

Statted, no wiki entry:
> 3 hosts. Young, dressed in rags. Zealous.
> HP 7, Morale −, No armor, Long knives d6.
> Chant: *"Lesdy... Lusi... Lesdy... the chosen, the delightful!"*

### Aldon (lost heir) — LOW
**Source:** Rotblack Sludge, p.13, room 13.

Statted-but-passive (3 HP). NPC, no wiki entry: *"pudgy and arrogant. Gnaws human bones."* The MacGuffin of the adventure.

### Fletcher, the Cannibal Warlock — HIGH
**Source:** Rotblack Sludge, p.15, room 15.

Statted, no wiki entry found. Major boss of Rotblack Sludge. Source:
> 7 feet tall, built like a grizzly. Sooty, bald and covered in tattoos. Rules the Den. Hates Lesdy in the Greenhouse but can't fit through the Tunnel.
> HP 20, Morale −, Hardened skin −d4
> **Red-hot flail d8 + severe burn** (Agility tests −2 for a day).
> **Uses a Power every third round (automatically succeeds). d4:**
> 1–2. Nine Violet Signs Unknot the Storm — d2 bolts of lightning, d6 damage each.
> 3. Daemon of Capillaries — one creature chokes for d6 rounds, d4 HP per round.
> 4. **Ich-bin-luft (unique Power):** Fletcher is invisible the next two rounds. Can still attack.
> When Fletcher takes damage, big chunks of human flesh rain down. The PC that hit him must test Agility DR8 or take d4 damage.

Backstory: *"As a child Fletcher was lead out into Sarkash and left to die. Desperate necromancers found the feral boy chewing on rabbit carcasses in a gloomy glade. They took him in, but no force or threat could control him, and he slowly grew more powerful. Eventually they too abandoned him to die, hurling him into the Accursed Den."* If Fletcher dies, the Gutworm sinks dead.

### Pillar-top Violin Skeletons — LOW
**Source:** Rotblack Sludge, room 9 Gem Room (p.11).

Mentioned: two skeletons play violin atop a 50-foot pillar in the Rotblack Sludge. *"They ignore everything and everyone."* No stats given but they are a named creature presence with no wiki note.

## From `MBC_Graves_left_wanting.pdf`

Graves Left Wanting (Graven-Tosk dungeon, full adventure) introduces a complete bestiary of creatures none of which have wiki entries.

### Widow-wraith — HIGH
**Source:** Graves Left Wanting, p.7.

> HP 15, Morale −, Icy touch d4 + special
> **Special.** Her sobbing alerts anyone to her presence; she always loses initiative. Touch drains Strength, Presence, and Agility by 1 for the fight's duration.

A "ghastly Widow-wraith" appears as a random graveyard encounter (p.6 table). Same drain mechanic as Wrat-Wraith but with sobbing flavor and locked initiative — distinct creature.

### Hungry Zombie — MED
**Source:** Graves Left Wanting, p.7.

> HP 6, Morale −, Leather scraps −d2, Claw/Bite d2 + special
> **Special.** Test Toughness DR8 or die turning into a zombie after 2 days.

A Graven-Tosk variant of Nodh-zombie (different HP). Wiki Zombie entry does not cross-reference.

### Rotted Skeleton — HIGH
**Source:** Graves Left Wanting, p.7.

> HP 5, Morale 7, Knuckles d2
> **Special.** Whenever it takes damage, a puff of vile marrow-dust leaks from its broken bones. Melee attackers test Toughness DR10 or become infected.

Distinct from Belze (Blood-drenched Skeleton). No wiki entry.

### Unbred Mutt — MED
**Source:** Graves Left Wanting, p.7.

> HP 8, Morale −, Bite d6.

A Graven-Tosk graveyard-stray dog. Compare to Eat-Prey-Kill "Mutts Unbred (d6)" entry (Graven-Tosk region) — same creature, same stat block. No wiki entry as creature.

### Half-billed Raven — MED
**Source:** Graves Left Wanting, p.7; Eat-Prey-Kill p.6 (Graven-Tosk region).

> HP 2, Morale −, Beak/Choking tongue d4/special
> **Special.** Test Agility DR12 or take d4 damage/round until Strength DR14 succeeds or the raven dies.

No wiki entry. (Mentioned in `/wiki/adventures/Eat-Prey-Kill.md` regional summary only.)

### Fogbound Skeleton — HIGH
**Source:** Graves Left Wanting, p.9, Colander Room.

> HP 7, Morale 8, No armor, Weapon of condensed fog d4
> **Special.** Shatters if an attack deals 5+ damage, but otherwise, damage is reduced to 1.

Carries the **Skeleton Unkey** (d4 dagger that opens any lock and leads to unexpected, rarely convenient places). Three of them argue at a stone table around a locked metal strongbox in the Colander Room.

### Maus / Fela Maus / Roseate Baritona — HIGH
**Source:** Graves Left Wanting, p.10, Maus' Vomatorium.

Statted indirectly via her cursed instrument's effect; no creature page. Fela Maus is *"the legendary bard-made-noble"* cursed by a bog hag, now reduced to bones floating in a coffin of yellow gall. The **Roseate Baritona** is *"a human-sized ivory horn bedecked with Maus' family's skulls and bound in magical entrails. When blown, it spews a noise that forces listeners to test Toughness DR10 or vomit acid, taking d6 damage."*

Also the **bog hag** who cursed her is mentioned but not statted — named entity.

### Twice-grown Corpse Fly — MED
**Source:** Graves Left Wanting, p.11; Eat-Prey-Kill p.6 (Graven-Tosk region).

> HP 4, Morale −, Exoskeleton −d4, Bite d4 + special
> **Special.** Test Toughness DR12 or become host for a dozen freshly laid fly eggs. Extract them within d6 days or watch them hatch in your corpse.

No wiki entry.

### Roach Herder (The Recluse of Refuse) — HIGH
**Source:** Graves Left Wanting, p.13.

> HP 4, Morale 5, Bite d4 + special / or Barbed Roach Whip d6
> **Special.** Test Toughness DR12 or become infected.

Flavor: *"a graverobber made hermit, sits on his throne, roach whip in grubby hand. After being unable to escape the cursed graveyard, his party members eventually died, leaving him terribly alone. Now he breeds cockroaches, hoping to hatch one big enough to fly him back to the city he once rejected. An insecure liar and untrustworthy narcissist who values his own skin above all else."*

### The Deadn't (Stein, Benzen, Arga) — MED
**Source:** Graves Left Wanting, p.16, Undertaker's Hut.

Three named NPCs alive in the hut — would-be escapees who killed the Undertaker:
- **Stein**, Grift merchant. HP 2, Morale 8, No armor, Shortsword d4. Carries 50 silver.
- **Benzen**, Schleswig guard. HP 3, Morale 9, Leather −d2, Crossbow d8 + 10 bolts.
- **Arga**, Galgenbeck priest. HP 4, Morale 10, Scale −d4, Staff d4. Carries a random sacred scroll.

No wiki NPC or creature entries.

### The Übertaker — HIGH
**Source:** Graves Left Wanting, p.17.

Boss of the adventure. No wiki entry. Source:
> HP 27, Morale −, Barrier (palefire) −d4
> Performs a random action each round (d4):
> 1. **SCOURGE TAKE YOU** — Creatures in melee range take d4 damage.
> 2. **BEHOLD THE POWER** — Its next attack deals maximum damage.
> 3. **NO ROE PROACH ANSWERS** — the shovel and pwins the stho ovrandom el creature appears (Defense DR14, d6 damage). [text mangled in extraction; probably "spins the shovel and a random creature appears"]
> 4. **REST IS NOW** — Skeletal hands pull a creature into the ground (prone + test Strength DR14 or d8 damage).
> When targeted by healing powers, the Übertaker loses rather than recovers HP. Upon destruction, the torn robes can be rolled up and used as an Unclean Scroll (BEHOLD THE POWER, d4 creatures' next attacks deal maximum damage).

Flavor: *"Rising, floating a few feet above the ground, is the Undertaker's body. The face is gaunt, eyes sunken and filled with mad purple fire. Rune-covered robes swirl around grim feet, the shovel a fiery polearm of doom. Upon festering, the Undertaker's body and vengeful mind hosted a being both lesser and greater than human, a servant of a faraway underworld: an Übertaker. This creature is concerned with one thing — to bring people back below dirt."*

## From `MBC_Eat-Prey-Kill.pdf` — full regional bestiary missing

`/wiki/adventures/Eat-Prey-Kill.md` summarizes this but explicitly notes the gap: *"Each beast deserves an individual entry in /wiki/creatures/ as expansion work."* Listing each here for completeness — every one of these is a fully statted named creature with one-line flavor in source. **All are HIGH** (no individual creature wiki).

**Tveland (p.4):** Antideer (d4) · Flayed Vultures (d8) · Ratbit · Feral Horses (d4) · Steppe Wolfe (and pack d8) · Tusked Bison

**Sarkash (p.5):** Skelelk (d4) · Dredgehog · Carrion Owls · Throat-cutting Warbler · Mulch-squirrels (d4) · Howler Bear

**Graven-Tosk (p.6):** Giant Skull Moth · Twice-grown Corpse Fly · Mutts Unbred (d6) · Grim-toothed Squirrel · Meatroach · Half-billed Raven (d4)

**Grift (p.7):** Uncommon Rats (d4) · Cellar Crabs (d4) · Nameless & Tameless Strays (d8) · Straw-lion · Lentil Lice (and d6 starved peasants) · Múrder Gulls (d20)

**Kergüs (p.8):** Flail-horned Muskox (herd d12) · Tar-pelted Goats (d8) · Molar Bear · Megasloth · Blubber Gulls (d8) · False Seal

**Wästland (p.9):** Liar-bird · Three-thirds-pheasant · Feather Fox · Bautaboar · Schleswig Bog-feeder (d6) (and d4 farmers) · Gold-crested Filth-crow

**Lake Onda (p.10):** Cursed Trout · Rusty Bass · The Groan · Carcasswan (lone or pair, d2) · Unresting Duck (d8) · Sursturgeon

**Valley of the Unfortunate Undead (p.11):** Phantom Rats (d10) · Grubstoppers (d10) · Tomb Ape · Gravelings (d6) · Marrow Sparrow · Bonemare

**Bergen Chrypt (pp.12–13):** Tunnel Sneak · Nephalix Monkeys (d4) · Weakwill'd Whisperbird · Vierwinged Falchon · Überwolf (d6 + regular wolves) · Ragpie

The "In the Belly of the Beast" table (p.2) also names **a long and angry flesh worm** — a creature unnamed elsewhere.

## From `MÖRK BORG CULT FERETORY_The Tablets of Ochre Obscurity.pdf`

No statted creatures. The tablet items reference effects but no creature stat blocks. Nothing to flag.

## From `MBC_Pale-one.pdf`

This is a class document. The class itself is `/wiki/classes/Pale One.md`. No new monster stat block to add to creatures.

## From `MBC_Cursed-Skinwalker.pdf`

This is a class document with six creature **forms** the Skinwalker can shift into. The forms are class abilities, not free-standing creatures, but their stat-modifying effects are mechanically distinct:
- **Murder-Plagued Rat** (tiny: DR8 defence; bite d4 carries disease — victims DR14 Presence or attack their closest ally)
- **Flayed and Dripping Wolf** (DR10 attacks; fangs d6 crit 19+; on crit all enemies test Morale; slick from blood −d2)
- **Boneskulled Raven** (defence DR10; two claw attacks d4; bony scalp d6 weapon-and-shield ignores one attack/d6 days to heal)
- **Bear from Bergen Chrypt** (DR10 Strength/Toughness/attacks; DR14 defence; thick hide −d4; claw/bite d8)
- **Life-and-Death-Lizard** (regenerate d4 HP/round; bite d6 or acid spit d4; scaly −d2)
- **Doomsaying Monkey** (DR10 Agility/defence; third eye reads unclean scrolls DR10)

These are referenced from `/wiki/classes/Cursed Skinwalker.md` already. Mentioned here for completeness; arguably each shape is canonical creature-lore (Bear from Bergen Chrypt, in particular, suggests a Bergen Chrypt species). Not necessary, but a wiki seed.

## From `MBC_Merchant.pdf`

### Chip the Rat — none (already in Merchant Inventory)

Stat block captured in `/wiki/items/Merchant Inventory.md` as Grift ware #3. No gap.

### Mikhael the Merchant (creature stats) — LOW

NPC. Stat block exists in source (HP 6 Morale 9 No armor Staff d4; Eternal Unlife). Lives in `/wiki/npcs/`. Not a creature wiki gap, but should be cross-referenced from /creatures/ if a stat list is being maintained.

---

# Part III — Summary tally

## Existing creature entries needing fixes

| Wiki entry | Severity | Issue |
|---|---|---|
| Outcasts (Pale One + Prowler tables) | HIGH | Source rows misread as "unwritten" — actually present in source, recoverable via `pdfplumber`. |
| Akünh | LOW | "Cretun"/"Creton" canon-check; minor flavor missing. |
| Scum | LOW | "(wanted, serious crime)" qualifier missing from loot. |
| Goblin | LOW | Kulvan's "three colorless pearls" detail; Tergol-experiment cross-link. |
| All other 27 existing entries | none | Match source. |

## Missing entries (priority order)

| Creature | Severity | Source |
|---|---|---|
| Undead (Death Ziggurat) | HIGH | Death Ziggurat p.8 |
| The Übertaker | HIGH | Graves Left Wanting p.17 |
| Fletcher the Cannibal Warlock | HIGH | Rotblack Sludge p.15 |
| Srolki & Yaoxl (Antediluvian Toads) | HIGH | Sepulchre p.12 |
| The Swamp Witch (creature stat) | HIGH | Sepulchre p.11 |
| Roach Herder | HIGH | Graves Left Wanting p.13 |
| Fogbound Skeleton | HIGH | Graves Left Wanting p.9 |
| Widow-wraith | HIGH | Graves Left Wanting p.7 |
| Rotted Skeleton | HIGH | Graves Left Wanting p.7 |
| Tired Crystal Demon | HIGH | Rotblack Sludge p.6 |
| The Madman | HIGH | Devil's Tomb p.1 |
| The Bastard (goblin overlord) | HIGH | Goblin Grinder p.5 |
| Ratbadger | HIGH | Bloat p.1 |
| Maus / Roseate Baritona | HIGH | Graves Left Wanting p.10 |
| The Deadn't (Stein, Benzen, Arga) | MED | Graves Left Wanting p.16 |
| Hungry Zombie / Twice-grown Corpse Fly / Half-billed Raven / Unbred Mutt | MED | Graves Left Wanting p.7, p.11; Eat-Prey-Kill p.6 |
| Rotblack interior creatures (Crooked Guards, Mad Prisoners, Lesdy, 3 Hosts, Slumbering Skeletons, Aldon, Pillar-skeletons) | MED | Rotblack Sludge |
| Sepulchre creatures (Strange Serpent Drug Cultist stat block, Ueth stat block, Swamp Witch stat block) | MED | Sepulchre |
| Death-Obsessed Cultist (stat block) | MED | Death Ziggurat p.9 |
| Excited / Archer / Bucket / Fresh Goblin variants | MED | Goblin Grinder pp.11, 12, 14 |
| Two-Headed Basilisks as creatures | MED | Bare Bones pp.10–11 |
| All Eat-Prey-Kill regional bestiary (≈50 named creatures) | HIGH (collectively) | Eat-Prey-Kill pp.4–13 |
| Misery / Bedeviled Dungeons hooks (Bark-Witch, Pale Gremlins, Ochre-beetles, Slime-Larva Mass, Black Serpents of Psalm 6:5, Yetsabu-Nech, Daejmon) | MED | Bare Bones pp.17–20, p.71 |

## PDFs successfully extracted

All 26 PDFs in `/source/` extracted cleanly via `pdfplumber`. No PDF was unreadable.
