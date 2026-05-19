# Mörk Borg Wiki — Source Audit Report

**Date:** 2026-05-17
**Scope:** All seven wiki categories (creatures, locations, classes, NPCs, lore, items, factions, tables, adventures) audited against every source PDF in `/source/`.
**Method:** Six parallel research passes. Each pass extracted source PDFs with `pdfplumber` (which recovers Mörk Borg's typographic spreads where `pdftotext` does not) and compared canon text against the corresponding wiki entries.

---

## TL;DR

The wiki has a real coverage problem and the cause is mostly traceable to one technical issue and one editorial pattern.

**The technical issue:** much of the wiki was originally built from `pdftotext` output. Bare Bones Edition and several supplements use typographic-art layouts that `pdftotext` flattens into noise — so wiki entries flagged "(unwritten in plaintext source)" or "expansion gap" usually have the canonical content sitting recoverable in the PDF. `pdfplumber` got it back cleanly in every case tested.

**The editorial pattern:** missing content has been re-framed as "expansion opportunity" instead of "canon to recover." Several wiki pages now read as if the source was silent when in fact the source is full.

The fix is mechanical, not creative: re-extract with `pdfplumber`, drop the recovered passages back into the affected entries, preserve the page references.

The Cult-supplement classes (Forlorn Philosopher, Pale One, Cursed Skinwalker, Dead God's Prophet, Sacrilegious Songbird) and the NPCs sourced from individual booklets are mostly fine. The damage is concentrated in Bare Bones-sourced material.

---

## Severity rollup

| Category | HIGH | MED | LOW | Source detail |
|---|---|---|---|---|
| Classes | 6 | 0 | 5 | [audit_classes.md](audit_classes.md) |
| Creatures (existing entries) | 1 | 0 | 3 | [audit_creatures.md](audit_creatures.md) |
| Creatures (missing entries) | 14 + ~50 EPK | ~15 | — | same |
| Locations | 4 | 9 | several | [audit_locations.md](audit_locations.md) |
| NPCs | 5 (+ 12 missing) | 7 | several | [audit_npcs.md](audit_npcs.md) |
| Lore | 0 | 5 | 6 | [audit_lore.md](audit_lore.md) |
| Items / Factions / Tables / Adventures | 8 | many | many | [audit_items_factions_tables_adventures.md](audit_items_factions_tables_adventures.md) |

**HIGH** = mechanically required content missing or so truncated the entry is unplayable from the wiki.
**MED** = significant flavor or named-detail gap; partial canonical content.
**LOW** = minor truncation or stylistic drift.

---

## Top-priority fixes (recommended order)

Ordered by ratio of canon-recoverable-now to effort.

### 1. The Bare Bones six classes — HIGH (one fix, six entries)

`Fanged Deserter`, `Gutterborn Scum`, `Esoteric Hermit`, `Wretched Royalty`, `Heretical Priest`, `Occult Herbmaster` are all missing 70–85% of canonical playable content (Abilities blocks, origin tables, gear/specialty tables). The Bare Bones spreads on pp. 46–57 contain the full text, recoverable in one extraction pass. Fixing this restores the wiki's value as a playable reference.

### 2. The Bare Bones table truncations — HIGH

- **Adventure Seeds** — `Who` d20 column has only 5/20 entries.
- **Bedeviled Dungeons** — `In What State` (1/10) and `What Did They Leave` (2/12) sub-tables nearly empty.
- **Powers** — d10 Unclean + d10 Sacred scrolls; ~19 of 20 missing.
- **Equipment** — starting Armor d4 and starting-item d12 tables absent.
- **Troubling Tales d20** — table absent entirely from wiki.

Same root cause as the classes. One extraction pass repairs all of them.

### 3. The Misery / cosmology dead links — MED-but-load-bearing

Wiki entries throughout NPCs, locations, and creatures point at `[[Verhu]]`, `[[Nechrubel]]`, `[[Akünh]]` style links. The lore entries for Verhu and Nechrubel do exist; Akünh is referenced from `npcs/README.md` but has no NPC entry (he has a creature entry under that name). Audit `npcs/README.md` and resolve the dangling link. Also: lore is missing **two named entries** that the rest of the wiki implicitly depends on — *Dead Gods / Slain Pantheon* (10 named gods from the Dead God's Prophet booklet) and *Forgotten Mind-Cult* (Feretory p. 64). Both should be lifted into `/wiki/lore/`.

### 4. Eat-Prey-Kill regional bestiary — HIGH (largest absolute gap)

~50 named statted regional creatures (Antideer, Howler Bear, Skelelk, Meatroach, Tomb Ape, Übertaker [wolf variant], Bonemare, Ragpie, etc.) exist in the EPK booklet with full stat blocks. The wiki has ~23 of 54 names and zero stat blocks. The adventures entry self-flags this. Largest single creative win available, though also the largest lift.

### 5. Graves Left Wanting — HIGH

The Graven-Tosk wiki location entry is a stub vs. the Graves Left Wanting booklet, which contains: 9 named sub-locations, 4 named NPCs (Stein, Benzen, Arga — "the Deadn't"; Fela Maus; Erhard; the Roach Herder; the Undertaker/Übertaker), a d8 Sensory Strangeness table, stat blocks for the Hungry Zombie, Twice-grown Corpse Fly, etc., and the Übertaker climax encounter. Fix touches `locations/Graven-Tosk.md`, `adventures/Graves Left Wanting.md`, several new creature entries, and several new NPC entries.

### 6. Tenebrous Reliquary cursed items — HIGH

Wiki self-flags 24 of 36 cursed items missing (Volt Thrower, War Starter, Cup of Peace, Chaos Blade, Crown of Burning Stars, etc.). Straight transcription job from the booklet.

### 7. Sepulchre + Death Ziggurat dungeon tables — HIGH

- Sepulchre: 11-chamber dungeon collapsed into a paragraph; Srolki/Yaoxl/Swamp Witch stat blocks dropped.
- Death Ziggurat: d10 ruins / d10 search / d12 events / d10 minor / d6 major treasure tables (~40 entries) referenced but not transcribed.

### 8. Missing NPC entries — HIGH

Twelve named NPCs lack wiki entries despite having stat blocks or substantial source presence: *Verhu*, *Nechrubel*, *Akünh* (NPC pass — separate from the creature entry), *Arkh*, *Lusi*, *Gorgh*, *HE*; from Graves Left Wanting — *Fela Maus*, *Erhard*, *The Roach Herder*, *The Undertaker / Übertaker*, *The Deadn't* (Stein, Benzen, Arga); from Rotblack Sludge — *King Lenard II*.

Several of these (Verhu, Nechrubel, HE, Lusi, Gorgh, Arkh) are cosmic entities that live in both `/lore/` and `/npcs/`. Decide which canonical home each gets, then resolve the cross-links.

### 9. Per-entry HIGH fixes (single-file repairs)

These are small, contained, and unblock dependent cross-references:

- `npcs/Aldon.md` — restore King Lenard II eye-socket puzzle; bullwhip damage is d4+d4, not d4.
- `npcs/Lesdy.md` — restore the three hosts stat block (HP 7, Morale —, Long knives d6).
- `npcs/Mikhael the Merchant.md` — three regional inventory tables (Tveland / Wästland / Kergüs, 18 items) flattened to a stub link.
- `npcs/Silas the Fattened King.md` — restore the tongue-shaped knife (d6, eat-or-die-within-the-hour) buried in his sewage pit.
- `npcs/Shadow King.md` — restore King Lenard II reference (presumed prior Shadow King, anchors the hereditary line).
- `creatures/Outcasts.md` — recover Pale One specialties 3–4 and 8 missing rows across Pale One + Prowler tables (pdfplumber recoverable).
- `locations/Tveland.md` — Lady Porcelain phrasing ("exquisite and deeply impractical cruelty"); Klefunheim; EPK creature canon.
- `locations/Galgenbeck.md` — Shimmering Fields cosmology; named NPCs Arga, Urgrip Wikt, Jota Klefunheim; Misery 1:1 connection.

---

## Cross-cutting issues

**Canon-check / spelling drift:**
- `Cretun` vs. `Creton` — flagged in creatures audit. Pick one and replace globally.
- Merchant Inventory labels region 2 as "Western Kingdom" — canon spelling is **Wästland**.
- `Sigfúm the Kind`: source uses present tense "is mocked," wiki rewrote to "Once mocked."

**Page references are inconsistent.** Some entries cite PDF + page, some only PDF, some nothing. Standardize on `[PDF filename, page N]` per `CLAUDE.md`.

**Dead `[[link]]` audit recommended.** Multiple entries link to wiki pages that don't exist (most prominently `[[Akünh]]` from the NPCs README and the Verhu/Nechrubel/HE/Lusi/Gorgh/Arkh references in NPC bios).

**`[CANON CHECK]` flag is being used inconsistently** with the CLAUDE.md spec.

---

## What the audit did NOT find

Worth noting so you know what's actually clean:

- **Misery Table is not truncated.** Canon is 37 prophecies (d66 with 7:7 as the singular cap), not 49. The current `Misery Table.md` matches Bare Bones pp. 17–20 verse-for-verse. Minor procedural canon missing (the "no repeats" rule and the *"Burn the book"* closer) but the table contents are complete.
- **Cult-supplement classes** (Forlorn Philosopher, Pale One, Cursed Skinwalker, Dead God's Prophet, Sacrilegious Songbird) are essentially complete. Minor polish only.
- **Most existing creature entries** (27 of 31) match source faithfully.
- **Most lore entries** match source. Two missing pages (Dead Gods, Forgotten Mind-Cult), some calendar/Misery procedural rules to add.

---

## Recommended next step

Pick one of these and I'll do the work:

1. **Re-extract Bare Bones with `pdfplumber` and backfill the six classes + the table truncations in one pass.** Highest fidelity-per-effort ratio. The other extractions can use the same script.
2. **Re-extract and backfill all HIGH-severity entries in priority order above.** Larger lift, comprehensive restoration.
3. **Tackle one category at a time** — pick which (classes / locations / NPCs / creatures / items-tables-adventures / lore polish).
4. **Just fill the missing entries** (the 14 absent creatures, 12 absent NPCs, EPK regional bestiary) — leaves existing truncations for later.
5. **Stop here.** The per-category audit files are detailed enough to fix by hand.

Each per-category audit file (linked in the rollup table) contains the full diagnosis with quoted source passages, page references, and severity-tagged item lists — that's what you'd work from if you wanted to direct fixes piece by piece.

---

## Note on `extract.py`

A leftover helper script `extract.py` exists at the project root from the audit pass. It's a small `pdfplumber` wrapper used during research. Couldn't remove it due to file permissions — safe to delete by hand. It's the same script you'd want to keep around if you go with option 1 or 2 above.
