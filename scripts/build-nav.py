#!/usr/bin/env python3
from pathlib import Path
import re
import html

ROOT = Path(__file__).resolve().parents[1]
#DOCS = ROOT / "content"
OUT = ROOT / "docs" / "nav.html"   # or ROOT / "nav.html"

HEADING_RE = re.compile(r"^(#{1,4})\s+(.+?)\s*$")
EXPLICIT_ID = re.compile(r"\s*\{#([^}]+)\}\s*$")
FENCE_RE = re.compile(r"^```")

def slugify(text: str) -> str:
    text = EXPLICIT_ID.sub("", text)
    text = re.sub(r"[*_`]+", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.lower()
    text = re.sub(r"[^\w\s.\-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text.strip())
    return text or "section"

def strip_front_matter(lines):
    if not lines or lines[0].strip() != "---":
        return lines
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return lines[i + 1 :]
    return lines

def headings(path: Path):
    print("Path: " , path)
    lines = strip_front_matter(path.read_text(encoding="utf-8").splitlines())
    in_fence = False
    for line in lines:
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = HEADING_RE.match(line)
        if not m:
            continue
        level = len(m.group(1))
        raw = m.group(2).strip()
        idm = EXPLICIT_ID.search(raw)
        hid = idm.group(1) if idm else slugify(raw)
        title = EXPLICIT_ID.sub("", raw).strip()
        title = re.sub(r"[*_`]+", "", title)
        yield level, title, hid

def md_to_html(md: Path) -> str:
    if not md.is_absolute():
        md = ROOT / md
    md = md.resolve()
    content = (ROOT / "content").resolve()
    rel = md.relative_to(content).with_suffix(".html")
    if rel.name == "Index.html":
        rel = rel.with_name("index.html")
    return rel.as_posix()

def sorted_docs():
    files = []
    with open("ORDERED_FILE_LIST.txt", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            files.append((ROOT / line).resolve())
            print(files)
    return files

def build():
    lines = [
        '<div class="layout">',
        '<nav class="sidebar">',
        "  <ul>",
    ]
    for md in sorted_docs():
        href_file = md_to_html(md)
        items = list(headings(md))
        if not items:
            continue
        for level, title, hid in items:
            indent = "    " + "  " * (level - 1)
            href = href_file if level == 1 else f"{href_file}#{hid}"
            lines.append(
                f'{indent}<li class="h{level}">'
                f'<a href="{html.escape(href, quote=True)}">'
                f"{html.escape(title)}</a></li>"
            )
    lines += [
        "  </ul>",
        "</nav>",
        '<main class="content">',
        "",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    build()
