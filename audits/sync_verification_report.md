# Sync Verification Report

Date: 2026-05-17

## Part 1 — Unresolved Link Cleanup

Started at 30 unresolved [[wiki link]] targets; finished at **0**.

### Files Edited (Aliases Added)

| File | Aliases Added | Resolves |
|---|---|---|
| `wiki/lore/Death Realm.md` | `Realm of the Dead`, `the Realm of the Dead` | 4 link refs |
| `wiki/lore/Two-Headed Basilisks.md` | `Basilisks`, `the Basilisks` | 1 link ref |
| `wiki/items/Powers.md` | `Unclean Scrolls`, `Sacred Scrolls` (added to existing list) | 1 link ref |
| `wiki/creatures/Nephalix Monkeys.md` | `Nephalix` | 1 link ref |
| `wiki/creatures/Zombie.md` | `Undead`, `the Undead` | 2 link refs |

### Files Created (Stubs)

All new entries follow Mork Borg voice / format spec (H1 / Type / Source / 2-3 sentence body / Connections / Gaps).

| File | Aliases | Resolves |
|---|---|---|
| `wiki/locations/Catacomb Corridor.md` | `The Catacomb Corridor` | 5 link refs (3 + 2 variants) |
| `wiki/locations/Colander Room.md` | `The Colander Room` | 2 link refs |
| `wiki/locations/Maus' Vomatorium.md` | (none — bare name) | 2 link refs |
| `wiki/locations/Graveyard.md` | `the Graveyard`, `The Graveyard` | 3 link refs |
| `wiki/locations/Roach Herder's Lair.md` | `The Roach Herder's Lair` | 2 link refs |
| `wiki/locations/Roseate Baritona.md` | (none — `the X` handled by resolver) | 2 link refs |
| `wiki/locations/Tvelandian Orphanarium.md` | (none) | 2 link refs |
| `wiki/locations/The Paunchy Swine.md` | (none) | 1 link ref |
| `wiki/lore/Omens.md` | `omens`, `Omen` | 2 link refs |

### Decisions Made

- **Undead alias on Zombie.md**: chose to alias `Undead` -> `Zombie` rather than create a new disambiguation page. Zombie.md is the most canon-grounded undead entry (Bare Bones p.61 + Nodh + cure quest hook). Death Ziggurat undead and Drowned are mentioned inside Zombie.md itself in a comparison paragraph, so the lore-as-category reading works.
- **Sync script case/`the` handling**: confirmed the resolver already strips/adds the `the ` prefix and trailing `s`, so capitalization variants like `the Plague Pit` / `The Plague Pit` resolve to a single canonical page without per-variant aliases. Only had to add `the X` aliases where the canonical filename does NOT start with `The` (e.g. `Graveyard.md` needed `the Graveyard` alias, but `The Plague Pit.md` did not need anything).
- **Powers cross-link**: `[[Unclean Scrolls]]` / `[[Sacred Scrolls]]` resolve to the existing `items/Powers.md` consolidated page (which has Unclean and Sacred d10 sub-tables in-page). No separate stubs created.
- **Roseate Baritona** filed under `locations/` rather than `items/` because it is non-removable, physically situated in Maus' Vomatorium, and mechanically a hazard of the chamber rather than a portable object.

### Final Sync Run

```
Indexed 359 keys (was 336)
locations    44 entries written  (+8 new stubs)
lore         24 entries written  (+1 new — Omens)
TOTAL       314                  (was 305)

=== Unresolved [[link]] targets: 0 ===
```

Target met.

---

## Part 2 — Rendered Site Verification

Sampled six rendered HTML files. All check out.

### `docs/creatures/antideer.html`
- Frontmatter, back-link, entry-header, badge-type (`creature`), badge-source all present.
- Body renders evocative italic, Special / Lore paragraphs intact.
- Connections block links `Tveland` and `Eat-Prey-Kill` correctly.
- Gaps block present.
- **OK**

### `docs/npcs/verhu.html`
- Cross-link to lore counterpart works: `<a href="{{ '/lore/verhu.html' | relative_url }}">Verhu</a>` in the opening blockquote disambiguator and again in Connections.
- The lore/npcs split is signposted clearly ("This page covers Verhu as an active presence in play"). No duplicate-content red flag — the npcs entry is action/encounter-focused while the lore entry is cosmology.
- Badge color `badge-magenta` applied (matches "deity-as-actor" keyword rule).
- All internal links resolved.
- **OK**

### `docs/classes/fanged-deserter.html`
- Full Abilities block rendered as `<ul class="wiki-list">` with all four bullets (Built like a bull, Not a bright spark, Agility tests dr14, Illiterate).
- The "You Also Begin With One of the Following (d6)" gear list renders as ordered list with the special items (Brown Scimitar, Wizard Teeth, Old Sigurd's Sling, Shoe of Death's Horse) cross-linking correctly to `/items/...`.
- Sigurd noted in Gaps section with smart-quote properly preserved.
- **OK**

### `docs/lore/dead-gods.html`
- 10-god table renders cleanly with d10 / Name / Title columns.
- All ten gods present (Acrophoe through Öde), bold-styled names preserved.
- Liquid relative_url syntax for all internal links is intact (Bergen Chrypt, SHE, Dead God's Prophet, Two-Headed Basilisks, etc.).
- "What Their Murder Means" section follows, both paragraphs render.
- **OK**

### `docs/powers/index.html`
- Section index lists all 6 power entries alphabetically (Daemon of Capillaries, Ich-bin-luft, Metzhuotl Blind Your Eye, Nine Violet Signs Unknot the Storm, Roskoe's Consuming Glare, Slithering Strangulation).
- Section description from `SECTION_DESCRIPTIONS` rendered ("Named scrolls and tablets that bend the dying world.").
- **OK**

### `docs/powers/slithering-strangulation.html`
- Effect line, lore paragraph, jale/dolm/ulfire flavour all intact.
- Cross-links to Ueth, Strange Serpent Drug Cult, Sepulchre of the Swamp Witch, Emerald Venom all resolve.
- "Powers" link in Connections correctly routes to `/items/powers.html` (the consolidated mechanic page lives in items/).
- Badge type "Power / unclean scroll" with default neutral color (matches `scroll|tablet` rule).
- **OK**

### `docs/locations/lake-onda.html`
- Regional Fauna section is fully present after the previous truncation fix.
- All six Eat-Prey-Kill creatures listed with one-line descriptions and links: Cursed Trout, Rusty Bass, The Groan, Carcasswan, Unresting Duck, Sursturgeon.
- Connections block reflects all six in addition to Western Kingdom / Wastland / Basilisks Demand / Eat-Prey-Kill.
- Gaps block present.
- **OK**

### Issues Found

None blocking. Minor notes:
- HTML entity escaping for apostrophes shows as `&#x27;` (e.g. `Roskoe&#x27;s`, `Sigûrd&#x27;s`). This is correct/safe HTML and renders fine in a browser, but if a future style preference wants raw `'` in display text, the converter could be tweaked. Not a defect.
- Liquid `{{ '...' | relative_url }}` syntax inside raw HTML files is correct for Jekyll processing — confirmed it survives intact through the sync.

---

## Overall Verdict

**GREEN**

- 30 -> 0 unresolved links.
- 9 stubs + 5 alias edits, all in Mork Borg voice.
- Sample renders across creature / NPC / class / lore / powers index / power detail / location all clean.
- No duplicate-content collisions between lore/Verhu and npcs/Verhu (disambiguation signposted).
- No rendering regressions detected.
- Site is publishable.
