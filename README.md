# MÖRK BORG — Project

A living wiki and creative expansion project for the MÖRK BORG tabletop RPG. Contains canonical lore extracted from official source PDFs, organized as a Jekyll-based wiki for GitHub Pages, plus original expansions built to spec.

---

## Project Structure

```
/source       — Official PDFs (read only, canon)
/wiki         — Canonical lore in Obsidian markdown (the source of truth)
/docs         — Jekyll site for GitHub Pages (built from wiki/)
/expansions   — Original content: new monsters, locations, tables, adventures
```

---

## The Wiki (`/wiki`)

Obsidian vault with all canonical content extracted and organized from source PDFs. Uses `[[WikiLink]]` syntax for cross-references.

Sections:

| Folder        | Contents                                                           |
| ------------- | ------------------------------------------------------------------ |
| `lore/`       | Gods, prophecies, cosmology — HE, SHE, Nechrubel, the Misery Table |
| `npcs/`       | Named characters — Josilfa Migol, the Shadow King, Swamp Witch     |
| `creatures/`  | Bestiary entries with stat blocks                                  |
| `classes/`    | Playable character classes                                         |
| `factions/`   | Organizations — the Inquisition, Creton Order, the Drowned         |
| `items/`      | Weapons, relics, equipment lists                                   |
| `locations/`  | Named places — Galgenbeck, Bergen Chrypt, Kergüs                   |
| `adventures/` | Published scenario notes and seeds                                 |
| `tables/`     | Random tables — Misery, Names, Weather, Unheroic Feats             |

Each entry follows the format defined in `CLAUDE.md`:

```markdown
# Entry Name

**Type:** [category]
**Source:** [PDF, page]

[Lore in Mörk Borg voice]

**Connections:** [[related]], [[related]]

**Gaps/Expansion Notes:** what's undefined
```

---

## The Site (`/docs`)

Jekyll site generated from the wiki source, deployable to GitHub Pages.

### Structure

```
docs/
├── _config.yml              — Jekyll config (baseurl: "", theme: null)
├── _layouts/default.html    — Single page template
├── _includes/nav.html       — Sidebar navigation (one file for all ~160 pages)
├── assets/
│   ├── style.css            — Mörk Borg aesthetic (dark, yellow, magenta)
│   └── nav.js               — Mobile nav toggle
├── index.html               — Homepage
└── [section]/
    ├── index.html           — Section listing
    └── [entry].html         — Individual entry pages
```

### Deploying to GitHub Pages

1. Push `docs/` to GitHub
2. In repo Settings → Pages, set Source to `docs/` on `main`
3. **Delete `docs/.nojekyll`** if it exists — that file disables Jekyll processing and must be removed for the site to build correctly

### Regenerating Pages

All content pages are generated from the wiki markdown source by a Python script:

```bash
python3 generate_jekyll.py
```

The script lives in the Claude outputs directory and handles:

- WikiLink → URL resolution for all ~160 pages
- Markdown → HTML conversion (paragraphs, headers, lists, bold, italic)
- Jekyll front matter injection (`layout`, `section`, `slug`)
- Section index pages
- Homepage

If you add a new wiki entry, add it to both `FILE_MAP` and `WIKI_LINKS` in the script, then rerun.

---

## Expansions (`/expansions`)

Original content built to match the Mörk Borg aesthetic and system. Not in the wiki yet — these are works in progress and seeds for development.

```
/expansions/monsters     — New creature stat blocks
/expansions/locations    — New or expanded places
/expansions/factions     — New organizations
/expansions/tables       — New random tables
/expansions/adventures   — Scenario seeds and outlines
```

---

## Source PDFs (`/source`)

Official releases used as canon. Do not contradict these. When in doubt, extrapolate darker and stranger.

Key files:

- `MÖRK BORG BARE BONES EDITION.pdf` — Core rules and setting
- `MB_Rules-reference.pdf` — Quick reference
- `MÖRK BORG CULT FERETORY_*.pdf` — Cult community content
- `MBC_*.pdf` — Individual third-party releases

---

## Tone Notes

> _The world ends by prophecy. You are small, wretched, and probably wrong about everything._

When adding content:

- Write like the text barely survived
- Lore in fragments, not exposition
- Nothing should be fully explained
- Monsters should feel wrong, not just dangerous
- No clean fantasy language

See `CLAUDE.md` for the full content generation guidelines.

---

## License

Mörk Borg Wiki is an independent production by Trevor Burkholder and is not affiliated with Ockult Örtmästare Games or Stockholm Kartell. It is published under the <a href="https://morkborg.com/license/" target="_blank">MÖRK BORG Third Party License</a>.

MÖRK BORG is copyright Ockult Örtmästare Games and Stockholm Kartell.
This is an AI-assisted fan project intended as a GM reference tool, not official content.

