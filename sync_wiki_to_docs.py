#!/usr/bin/env python3
"""
sync_wiki_to_docs.py — Convert /wiki/*.md to /docs/*.html for the Mork Borg Jekyll site.

Walks wiki/<section>/*.md, builds a basename-and-alias index, then renders each
file to docs/<section>/<slug>.html using a custom converter that produces the
exact HTML shape used by the published site (entry-header, badges, wiki-list,
connections-block, gaps-block, Liquid relative_url for links).

Run from anywhere. Adjust ROOT below if relocated.
"""
from __future__ import annotations

import html
import os
import re
import sys
import unicodedata
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ROOT = Path("/sessions/wizardly-vibrant-thompson/mnt/Mork Borg")
WIKI = ROOT / "wiki"
DOCS = ROOT / "docs"

SECTIONS = [
    "adventures",
    "classes",
    "creatures",
    "factions",
    "powers",       # before items so individual Power entries win over items/Powers.md aliases
    "items",
    "locations",
    "lore",
    "npcs",
    "tables",
]

# Section descriptions for auto-generated index pages
SECTION_DESCRIPTIONS = {
    "adventures": "Published scenarios from the Mörk Borg corpus.",
    "classes": "The wretched archetypes you'll drag through the mire.",
    "creatures": "Monsters, horrors, and things best avoided.",
    "factions": "Organizations shaping the end of the world.",
    "items": "Cursed relics, weapons, and equipment.",
    "locations": "Places. Fewer every day.",
    "lore": "The dying world's myths, gods, and dark prophecies.",
    "npcs": "Named figures that haunt the dying world.",
    "powers": "Named scrolls and tablets that bend the dying world.",
    "tables": "Random tables for ruining lives at the table.",
}

# Type-string keywords that get a coloured badge
BADGE_COLOR_RULES = [
    (re.compile(r"\b(demon|deity|god|spirit|cult|necrocrawl|cosmology)\b", re.I), "badge-magenta"),
    (re.compile(r"\b(NPC|arch[- ]?priestess|priestess|priest|king|queen)\b", re.I), "badge-red"),
    (re.compile(r"\b(mechanic|table|scroll|tablet)\b", re.I), None),  # default
]

UNRESOLVED_LINKS: List[Tuple[str, str]] = []  # (source_file, target)
DROPPED_FEATURES: List[Tuple[str, str]] = []  # (source_file, feature)

# Explicit slug overrides — preserves URLs already in use across the site/nav so
# we don't break inbound links when a wiki file's natural slug would differ.
SLUG_OVERRIDES = {
    ("adventures", "Sepulchre of the Swamp Witch"): "sepulchre",
    ("locations",  "Sepulchre of the Swamp Witch"): "sepulchre",
    ("factions",   "Strange Serpent Drug Cult"):    "strange-serpent-cult",
    ("locations",  "Cathedral of the Two-Headed Basilisks"): "cathedral",
    ("lore",       "The Dark Spider"):              "dark-spider",
    ("lore",       "The Dying World"):              "dying-world",
    ("npcs",       "Mikhael the Merchant"):         "mikhael",
    ("npcs",       "Silas the Fattened King"):      "silas",
    ("npcs",       "Shadow King"):                  "shadow-king",
    ("npcs",       "Swamp Witch"):                  "swamp-witch",
    ("npcs",       "Fathmu IX"):                    "fathmu-ix",
    ("npcs",       "Sigfúm the Kind"):              "sigfum-the-kind",
}

# ---------------------------------------------------------------------------
# Slug
# ---------------------------------------------------------------------------

def slugify(name: str) -> str:
    """Filename or display name -> URL slug.

    Rules:
      - Drop .md
      - Strip diacritics (Akünh -> akunh, Sigûrd -> sigurd)
      - Lowercase
      - "&" -> "and"
      - Apostrophes / quotes removed (Sigûrd's -> sigurds, Erhard's -> erhards)
      - Other non-alphanumeric -> hyphen
      - Collapse repeated hyphens, strip leading/trailing
    """
    s = name
    if s.lower().endswith(".md"):
        s = s[:-3]
    # Normalize unicode and strip combining marks
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    # & -> and
    s = re.sub(r"\s*&\s*", " and ", s)
    # Remove apostrophes and quotes (preserve adjacency: erhard's -> erhards)
    s = re.sub(r"[‘’“”'`\"]", "", s)
    # Anything else non-alphanumeric -> hyphen
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def slugify_for(section: str, name: str) -> str:
    """Slugify with per-section overrides honoured."""
    base = name[:-3] if name.lower().endswith(".md") else name
    ov = SLUG_OVERRIDES.get((section, base))
    if ov:
        return ov
    return slugify(base)


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?\n)---\s*\n", re.DOTALL)

def split_frontmatter(text: str) -> Tuple[dict, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    body = text[m.end():]
    return fm, body


# ---------------------------------------------------------------------------
# Index build (basename + alias -> (section, slug, display))
# ---------------------------------------------------------------------------

def build_index() -> Dict[str, Tuple[str, str, str]]:
    """Return basename(lowercase, normalized) -> (section, slug, display_name)."""
    index: Dict[str, Tuple[str, str, str]] = {}

    def add(key: str, section: str, slug: str, display: str) -> None:
        k = key.strip().lower()
        # also normalize away diacritics for lookup
        k_norm = "".join(
            c for c in unicodedata.normalize("NFKD", k) if not unicodedata.combining(c)
        )
        if k not in index:
            index[k] = (section, slug, display)
        if k_norm not in index:
            index[k_norm] = (section, slug, display)

    for section in SECTIONS:
        sec_dir = WIKI / section
        if not sec_dir.is_dir():
            continue
        for md in sorted(sec_dir.iterdir()):
            if not md.is_file() or md.suffix.lower() != ".md":
                continue
            name = md.stem
            if name.upper() == "README":
                continue
            slug = slugify_for(section, name)
            add(name, section, slug, name)

            # parse frontmatter aliases
            try:
                fm, _ = split_frontmatter(md.read_bytes().decode("utf-8", errors="replace"))
            except Exception:
                fm = {}
            aliases = fm.get("aliases") if isinstance(fm, dict) else None
            if isinstance(aliases, list):
                for a in aliases:
                    if isinstance(a, str):
                        add(a, section, slug, a)

    return index


# ---------------------------------------------------------------------------
# Inline conversion (wiki links, bold, italic, inline code)
# ---------------------------------------------------------------------------

WIKI_LINK_RE = re.compile(r"\[\[([^\[\]\|]+?)(?:\|([^\[\]]+?))?\]\]")


def _strip_wiki_link_syntax(s: str) -> str:
    """Render [[A|B]] as B, [[A]] as A, and **x** / *x* as just x — for plain-text
    contexts like badges where we don't want HTML."""
    def repl(m):
        return (m.group(2) or m.group(1)).strip()
    s = WIKI_LINK_RE.sub(repl, s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"\*(.+?)\*", r"\1", s)
    return s
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ITALIC_RE = re.compile(r"(?<![\*\w])\*(?!\s)([^\*\n]+?)(?<!\s)\*(?![\*\w])")
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")

# Placeholders used so we can convert markdown features without their output
# interfering with later regex passes.
_TOKEN_PREFIX = "\x00MBPLACEHOLDER"

def _make_token_table():
    tokens = []
    def store(html_str: str) -> str:
        tokens.append(html_str)
        return f"{_TOKEN_PREFIX}{len(tokens)-1}\x00"
    def restore(text: str) -> str:
        def sub(m):
            return tokens[int(m.group(1))]
        return re.sub(re.escape(_TOKEN_PREFIX) + r"(\d+)\x00", sub, text)
    return store, restore


def resolve_wiki_link(target: str, display: Optional[str], index: Dict[str, Tuple[str, str, str]], source_file: str) -> str:
    target = target.strip()
    display = (display or target).strip()
    key = target.lower()
    key_norm = "".join(c for c in unicodedata.normalize("NFKD", key) if not unicodedata.combining(c))
    candidates = [key, key_norm]
    # Try with leading "the " toggled
    for c in list(candidates):
        if c.startswith("the "):
            candidates.append(c[4:])
        else:
            candidates.append("the " + c)
    # Try with trailing 's' stripped (handles "Basilisks" vs "Two-Headed Basilisks", etc.)
    for c in list(candidates):
        if c.endswith("s") and len(c) > 3:
            candidates.append(c[:-1])
    hit = None
    for c in candidates:
        if c in index:
            hit = index[c]
            break
    if hit:
        section, slug, _ = hit
        url = f"{{{{ '/{section}/{slug}.html' | relative_url }}}}"
        return f'<a href="{url}">{html.escape(display)}</a>'
    UNRESOLVED_LINKS.append((source_file, target))
    return f'<span class="unresolved">{html.escape(display)}</span>'


def convert_inline(text: str, index: Dict[str, Tuple[str, str, str]], source_file: str) -> str:
    """Convert inline markdown (wiki links, bold, italic, code) to HTML.

    Order matters: tokens replace fully-formed HTML so later regex passes
    don't re-process them.
    """
    store, restore = _make_token_table()

    # Inline code first
    def code_sub(m):
        return store(f"<code>{html.escape(m.group(1))}</code>")
    text = INLINE_CODE_RE.sub(code_sub, text)

    # Wiki links (before bold/italic so display text inside [[...|]] is intact)
    def link_sub(m):
        link_html = resolve_wiki_link(m.group(1), m.group(2), index, source_file)
        return store(link_html)
    text = WIKI_LINK_RE.sub(link_sub, text)

    # Escape remaining special chars
    text = html.escape(text, quote=False)

    # Bold
    text = BOLD_RE.sub(lambda m: f"<strong>{m.group(1)}</strong>", text)
    # Italic (single *)
    text = ITALIC_RE.sub(lambda m: f"<em>{m.group(1)}</em>", text)

    # Restore tokens (which were already HTML-escaped where needed)
    text = restore(text)
    return text


# ---------------------------------------------------------------------------
# Block-level conversion
# ---------------------------------------------------------------------------

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
HR_RE = re.compile(r"^-{3,}\s*$")
UL_RE = re.compile(r"^(\s*)[-*+]\s+(.*)$")
OL_RE = re.compile(r"^(\s*)\d+\.\s+(.*)$")
TABLE_ROW_RE = re.compile(r"^\|.*\|\s*$")
TABLE_DIVIDER_RE = re.compile(r"^\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
BLOCKQUOTE_RE = re.compile(r"^>\s?(.*)$")


def parse_blocks(md: str) -> List[Tuple[str, object]]:
    """Tokenize markdown into a list of ("type", data) tuples.

    Types: 'heading', 'ul', 'ol', 'table', 'blockquote', 'paragraph', 'hr', 'blank'.
    """
    lines = md.split("\n")
    blocks: List[Tuple[str, object]] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        if stripped == "":
            i += 1
            continue

        if HR_RE.match(stripped):
            blocks.append(("hr", None))
            i += 1
            continue

        m = HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            text = m.group(2)
            blocks.append(("heading", (level, text)))
            i += 1
            continue

        # Table
        if TABLE_ROW_RE.match(line) and i + 1 < n and TABLE_DIVIDER_RE.match(lines[i + 1].strip()):
            header = line
            i += 2  # skip divider
            rows = []
            while i < n and TABLE_ROW_RE.match(lines[i]):
                rows.append(lines[i])
                i += 1
            blocks.append(("table", (header, rows)))
            continue

        # Blockquote
        if BLOCKQUOTE_RE.match(line):
            quote_lines = []
            while i < n and BLOCKQUOTE_RE.match(lines[i]):
                quote_lines.append(BLOCKQUOTE_RE.match(lines[i]).group(1))
                i += 1
            blocks.append(("blockquote", quote_lines))
            continue

        # List (ul/ol)
        if UL_RE.match(line) or OL_RE.match(line):
            list_lines = []
            list_type = "ul" if UL_RE.match(line) else "ol"
            while i < n:
                cur = lines[i]
                if not cur.strip():
                    # Lookahead: continue list if next non-blank is still a list item with same/greater indent
                    j = i + 1
                    while j < n and not lines[j].strip():
                        j += 1
                    if j < n and (UL_RE.match(lines[j]) or OL_RE.match(lines[j])):
                        list_lines.append("")
                        i += 1
                        continue
                    break
                if UL_RE.match(cur) or OL_RE.match(cur):
                    list_lines.append(cur)
                    i += 1
                else:
                    # Continuation line indented under previous item
                    if cur.startswith("  ") or cur.startswith("\t"):
                        list_lines.append(cur)
                        i += 1
                    else:
                        break
            blocks.append((list_type, list_lines))
            continue

        # Paragraph
        para = [line]
        i += 1
        while i < n:
            nxt = lines[i]
            if (
                not nxt.strip()
                or HEADING_RE.match(nxt)
                or HR_RE.match(nxt.strip())
                or UL_RE.match(nxt)
                or OL_RE.match(nxt)
                or BLOCKQUOTE_RE.match(nxt)
                or (TABLE_ROW_RE.match(nxt) and i + 1 < n and TABLE_DIVIDER_RE.match(lines[i + 1].strip()))
            ):
                break
            para.append(nxt)
            i += 1
        blocks.append(("paragraph", "\n".join(para)))
    return blocks


def render_table(header_line: str, row_lines: List[str], index, source_file: str) -> str:
    def split_row(s: str) -> List[str]:
        s = s.strip()
        if s.startswith("|"):
            s = s[1:]
        if s.endswith("|"):
            s = s[:-1]
        return [c.strip() for c in s.split("|")]

    headers = split_row(header_line)
    out = ['<table class="entry-table">', "<thead>", "<tr>"]
    for h in headers:
        out.append(f"<th>{convert_inline(h, index, source_file)}</th>")
    out.append("</tr></thead>")
    out.append("<tbody>")
    for r in row_lines:
        cells = split_row(r)
        # pad/truncate to header length
        while len(cells) < len(headers):
            cells.append("")
        cells = cells[: len(headers)]
        out.append("<tr>")
        for c in cells:
            out.append(f"<td>{convert_inline(c, index, source_file)}</td>")
        out.append("</tr>")
    out.append("</tbody></table>")
    return "\n".join(out)


def render_list(list_type: str, lines: List[str], index, source_file: str) -> str:
    """Render flat (non-nested) list. Nested children are not common in the
    wiki and will be flattened with a note in DROPPED_FEATURES."""
    items: List[str] = []
    cur: Optional[List[str]] = None
    list_re = UL_RE if list_type == "ul" else OL_RE
    for line in lines:
        m = list_re.match(line)
        if m:
            if cur is not None:
                items.append("\n".join(cur))
            cur = [m.group(2)]
        else:
            # continuation
            if cur is not None and line.strip():
                cur.append(line.strip())
            elif cur is not None and not line.strip():
                cur.append("")  # paragraph break inside li
    if cur is not None:
        items.append("\n".join(cur))

    tag = "ul" if list_type == "ul" else "ol"
    parts = [f'<{tag} class="wiki-list">']
    for item in items:
        # If multi-paragraph in li, separate by <br><br>
        if "\n\n" in item:
            paras = [convert_inline(p, index, source_file) for p in item.split("\n\n")]
            parts.append("<li>" + "<br><br>".join(paras) + "</li>")
        else:
            joined = item.replace("\n", " ")
            parts.append(f"<li>{convert_inline(joined, index, source_file)}</li>")
    parts.append(f"</{tag}>")
    return "\n".join(parts)


def render_blocks(blocks, index, source_file: str, title_h1: Optional[str]) -> Tuple[str, Optional[str], Optional[str]]:
    """Render blocks into the main body plus optionally a Connections and Gaps
    HTML snippet that should be appended at the end."""
    out: List[str] = []
    connections_html: Optional[str] = None
    gaps_html: Optional[str] = None

    for kind, data in blocks:
        if kind == "heading":
            level, text = data
            if level == 1 and title_h1 is not None and text.strip() == title_h1.strip():
                # Skip — H1 is moved to entry-header by the wrapper
                continue
            inline = convert_inline(text, index, source_file)
            if level == 1:
                out.append(f"<h1>{inline}</h1>")
            elif level == 2:
                out.append(f'<h2 class="section-header">{inline}</h2>')
            elif level == 3:
                out.append(f'<h3 class="section-header">{inline}</h3>')
            else:
                out.append(f"<h{level}>{inline}</h{level}>")
        elif kind == "paragraph":
            text = data
            # Check for Connections / Gaps special paragraphs
            cm = re.match(r"^\*\*Connections:\*\*\s*(.+)$", text.strip(), re.DOTALL)
            gm = re.match(r"^\*\*Gaps/Expansion Notes:\*\*\s*(.+)$", text.strip(), re.DOTALL)
            if cm:
                inner = convert_inline(cm.group(1).strip(), index, source_file)
                connections_html = (
                    '\n<div class="connections-block">\n'
                    '  <span class="connections-label">Connections</span>\n'
                    f"  <p>{inner}</p>\n"
                    "</div>"
                )
                continue
            if gm:
                inner = convert_inline(gm.group(1).strip(), index, source_file)
                gaps_html = (
                    '\n<div class="gaps-block">\n'
                    '  <span class="gaps-label">Gaps / Expansion Notes</span>\n'
                    f"  <p>{inner}</p>\n"
                    "</div>"
                )
                continue
            inline = convert_inline(text, index, source_file)
            # Replace literal newlines in paragraph with spaces
            inline = inline.replace("\n", " ")
            out.append(f"<p>{inline}</p>")
        elif kind in ("ul", "ol"):
            out.append(render_list(kind, data, index, source_file))
        elif kind == "table":
            header, rows = data
            out.append(render_table(header, rows, index, source_file))
        elif kind == "blockquote":
            inner = "<br>".join(convert_inline(l, index, source_file) for l in data)
            out.append(f"<blockquote>{inner}</blockquote>")
        elif kind == "hr":
            out.append("<hr>")

    return "\n".join(out), connections_html, gaps_html


# ---------------------------------------------------------------------------
# Header metadata extraction
# ---------------------------------------------------------------------------

TYPE_LINE_RE = re.compile(r"^\*\*Type:\*\*\s*(.+)$", re.M)
SOURCE_LINE_RE = re.compile(r"^\*\*Source:\*\*\s*(.+)$", re.M)


def extract_h1_and_meta(body: str) -> Tuple[Optional[str], Optional[str], Optional[str], str]:
    """Pull the first H1, Type: line, and Source: line out of body.
    Returns (h1, type_str, source_str, body_with_meta_removed).
    The H1 line is kept in the body (we'll skip it during render based on title match).
    """
    h1 = None
    type_str = None
    source_str = None

    lines = body.split("\n")
    new_lines = []
    skip_blank_after = False
    found_h1 = False
    for line in lines:
        if not found_h1:
            m = re.match(r"^#\s+(.+?)\s*$", line)
            if m:
                h1 = m.group(1).strip()
                found_h1 = True
                new_lines.append(line)
                continue
        # Match Type: / Source: only in the head region (before any other content)
        tm = TYPE_LINE_RE.match(line)
        sm = SOURCE_LINE_RE.match(line)
        if tm and type_str is None:
            type_str = tm.group(1).strip()
            skip_blank_after = True
            continue
        if sm and source_str is None:
            source_str = sm.group(1).strip()
            skip_blank_after = True
            continue
        if skip_blank_after and line.strip() == "" and type_str and source_str:
            skip_blank_after = False
            # Still emit one blank to separate paragraphs cleanly
            new_lines.append(line)
            continue
        skip_blank_after = False
        new_lines.append(line)
    return h1, type_str, source_str, "\n".join(new_lines)


def badge_classes_for(type_str: Optional[str]) -> str:
    if not type_str:
        return ""
    for pat, color in BADGE_COLOR_RULES:
        if pat.search(type_str):
            return color or ""
    return ""


# ---------------------------------------------------------------------------
# Conversion of a single file
# ---------------------------------------------------------------------------

def convert_file(md_path: Path, section: str, index: Dict[str, Tuple[str, str, str]]) -> Tuple[str, str]:
    """Return (slug, html_text) for the given .md file."""
    raw = md_path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("utf-8", errors="replace")
        DROPPED_FEATURES.append((f"{section}/{md_path.name}", "file contains invalid UTF-8 (decoded with replacement)"))
    frontmatter, body = split_frontmatter(text)
    h1, type_str, source_str, body_clean = extract_h1_and_meta(body)
    title = h1 or md_path.stem
    slug = slugify_for(section, md_path.stem)

    source_file = f"{section}/{md_path.name}"
    blocks = parse_blocks(body_clean)
    body_html, conn_html, gaps_html = render_blocks(blocks, index, source_file, title_h1=h1)

    # Build header
    section_label = {
        "adventures": "Adventures",
        "classes": "Classes",
        "creatures": "Creatures",
        "factions": "Factions",
        "items": "Items",
        "locations": "Locations",
        "lore": "Lore",
        "npcs": "NPCs",
        "powers": "Powers",
        "tables": "Tables",
    }[section]

    badge_color = badge_classes_for(type_str)
    badge_color_attr = f" {badge_color}" if badge_color else ""
    badge_type_html = (
        f'    <span class="badge-type{badge_color_attr}">{html.escape(_strip_wiki_link_syntax(type_str))}</span>\n'
        if type_str
        else ""
    )
    badge_source_html = (
        f'        <span class="badge badge-source">{html.escape(_strip_wiki_link_syntax(source_str))}</span>\n'
        if source_str
        else ""
    )
    meta_block = ""
    if badge_type_html or badge_source_html:
        meta_block = (
            '  <div class="entry-meta">\n'
            f"{badge_type_html}{badge_source_html}"
            "  </div>\n"
        )

    fm_lines = [
        "---",
        "layout: default",
        f'title: "{title.replace(chr(34), chr(39))}"',
        f"section: {section}",
        f"slug: {slug}",
        "---",
    ]

    out = []
    out.append("\n".join(fm_lines))
    out.append(f'<a href="{{{{ \'/{section}/\' | relative_url }}}}" class="back-link">{section_label}</a>')
    out.append('<div class="entry-header">')
    out.append(f"  <h1>{html.escape(title)}</h1>")
    if meta_block:
        out.append(meta_block.rstrip())
    out.append("</div>")
    if body_html.strip():
        out.append(body_html)
    if conn_html:
        out.append(conn_html)
    if gaps_html:
        out.append(gaps_html)
    return slug, "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Section index pages (built from wiki/<section>/README.md if present, else generated)
# ---------------------------------------------------------------------------

def build_section_index(section: str, index: Dict[str, Tuple[str, str, str]]) -> str:
    label = {
        "adventures": "Adventures", "classes": "Classes", "creatures": "Creatures",
        "factions": "Factions", "items": "Items", "locations": "Locations",
        "lore": "Lore", "npcs": "NPCs", "powers": "Powers", "tables": "Tables",
    }[section]
    desc = SECTION_DESCRIPTIONS.get(section, "")

    # Collect all entries in this section
    entries = []
    sec_dir = WIKI / section
    for md in sorted(sec_dir.iterdir()):
        if not md.is_file() or md.suffix.lower() != ".md":
            continue
        if md.stem.upper() == "README":
            continue
        slug = slugify_for(section, md.stem)
        # Try to get the H1 title for display
        try:
            text = md.read_bytes().decode("utf-8", errors="replace")
            _, body = split_frontmatter(text)
            m = re.search(r"^#\s+(.+?)\s*$", body, re.M)
            display = m.group(1).strip() if m else md.stem
        except Exception:
            display = md.stem
        entries.append((display, slug))
    entries.sort(key=lambda e: e[0].lower())

    fm = [
        "---",
        "layout: default",
        f'title: "{label}"',
        f"section: {section}",
        f"slug: {section}-index",
        "---",
    ]
    out = ["\n".join(fm)]
    out.append('<div class="entry-header">')
    out.append(f"  <h1>{label}</h1>")
    if desc:
        out.append(f'  <p class="section-description">{html.escape(desc)}</p>')
    out.append("</div>")
    out.append('<ul class="index-list">')
    for display, slug in entries:
        url = f"{{{{ '/{section}/{slug}.html' | relative_url }}}}"
        out.append(f'  <li><a href="{url}">{html.escape(display)}</a></li>')
    out.append("</ul>")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Homepage update (just fix counts)
# ---------------------------------------------------------------------------

def update_homepage_counts() -> None:
    """Rewrite docs/index.html with current section counts.

    Full rewrite is safer than regex patching because section-card markup spans
    multiple lines with attribute strings that confuse anchored regexes.
    """
    path = DOCS / "index.html"
    if not path.exists():
        return

    section_count: Dict[str, int] = {}
    for sec in SECTIONS:
        sec_dir = WIKI / sec
        if not sec_dir.is_dir():
            section_count[sec] = 0
            continue
        section_count[sec] = sum(
            1
            for md in sec_dir.iterdir()
            if md.is_file() and md.suffix.lower() == ".md" and md.stem.upper() != "README"
        )

    home_descriptions = {
        "lore": "The dying world's myths, gods, and dark prophecies.",
        "npcs": "Named figures that haunt the dying world.",
        "adventures": "Published scenarios from the Mörk Borg corpus.",
        "classes": "The wretched archetypes you'll drag through the mire.",
        "creatures": "The horrors that will end you.",
        "factions": "Organizations wrestling over the scraps.",
        "items": "Cursed relics, weapons, and equipment.",
        "locations": "Places. Fewer every day.",
        "tables": "Random tables for ruining lives at the table.",
        "powers": "Named scrolls and tablets that bend the dying world.",
    }
    home_labels = {
        "lore": "Lore", "npcs": "NPCs", "adventures": "Adventures",
        "classes": "Classes", "creatures": "Creatures", "factions": "Factions",
        "items": "Items", "locations": "Locations", "tables": "Tables",
        "powers": "Powers",
    }
    order = ["lore", "npcs", "adventures", "classes", "creatures", "factions",
             "items", "locations", "tables", "powers"]

    parts = [
        "---",
        "layout: default",
        'title: "Home"',
        "section: home",
        "---",
        '<div class="home-hero">',
        '  <h1 class="home-title">MÖRK BORG</h1>',
        '  <p class="home-subtitle">A Fan-made Wiki of a Dying World</p>',
        '  <p class="home-intro">The world ends by prophecy. Seven Miseries tick down the calendar. You are small, wretched, and',
        '    doomed. This wiki catalogs what little remains to be known before the black sun sets for the last time.</p>',
        '</div>',
        '<div class="section-grid">',
    ]
    for s in order:
        parts.append(f"  <a href=\"{{{{ '/{s}/' | relative_url }}}}\" class=\"section-card\">")
        parts.append(f'    <span class="section-card-label">{home_labels[s]}</span>')
        parts.append(f'    <span class="section-card-count">{section_count.get(s, 0)} entries</span>')
        parts.append(f'    <span class="section-card-desc">{html.escape(home_descriptions[s])}</span>')
        parts.append('  </a>')
    parts.append('</div>')
    path.write_text("\n".join(parts) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print(f"Wiki:  {WIKI}")
    print(f"Docs:  {DOCS}")
    if not WIKI.exists():
        print("Wiki directory not found.", file=sys.stderr)
        return 2

    print("Building basename + alias index...")
    index = build_index()
    print(f"  Indexed {len(index)} keys")

    section_counts = {s: 0 for s in SECTIONS}
    section_skipped = {s: 0 for s in SECTIONS}

    for section in SECTIONS:
        sec_src = WIKI / section
        if not sec_src.is_dir():
            continue
        sec_dst = DOCS / section
        sec_dst.mkdir(parents=True, exist_ok=True)

        for md in sorted(sec_src.iterdir()):
            if not md.is_file() or md.suffix.lower() != ".md":
                continue
            if md.stem.upper() == "README":
                section_skipped[section] += 1
                continue
            slug, html_text = convert_file(md, section, index)
            (sec_dst / f"{slug}.html").write_text(html_text, encoding="utf-8")
            section_counts[section] += 1

        # Build section index
        idx_html = build_section_index(section, index)
        (sec_dst / "index.html").write_text(idx_html, encoding="utf-8")

    update_homepage_counts()

    # Report
    print("\n=== Section conversion summary ===")
    total = 0
    for s in SECTIONS:
        print(f"  {s:12s} {section_counts[s]:4d} entries written (+ index.html)")
        total += section_counts[s]
    print(f"  {'TOTAL':12s} {total:4d}")

    print(f"\n=== Unresolved [[link]] targets: {len(UNRESOLVED_LINKS)} ===")
    seen = {}
    for src, tgt in UNRESOLVED_LINKS:
        seen.setdefault(tgt, []).append(src)
    for tgt in sorted(seen.keys(), key=lambda t: (-len(seen[t]), t.lower())):
        srcs = seen[tgt]
        sample = ", ".join(sorted(set(srcs))[:3])
        more = "" if len(set(srcs)) <= 3 else f" (+{len(set(srcs)) - 3} more)"
        print(f"  [{len(srcs)}x] {tgt}  -- e.g. {sample}{more}")

    if DROPPED_FEATURES:
        print(f"\n=== Dropped / degraded features: {len(DROPPED_FEATURES)} ===")
        for src, feat in DROPPED_FEATURES:
            print(f"  {src}: {feat}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
