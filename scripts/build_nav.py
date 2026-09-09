#!/usr/bin/env python3
from pathlib import Path
import html
import re
import argparse


BASE = ""
# root where docs will be deployed to
#  "" for localhost
#  "/runebrace-docs" for GH Pages
# Set via arg when invoked
DEPLOYED_ROOT = "/runebrace-docs/docs"

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
OUT = ROOT / "docs" / "nav.html"
ORDERED_LIST = ROOT / "scripts" / "ORDERED_FILE_LIST.txt"

HEADING_RE = re.compile(r"^(#{1,4})\s+(.+?)\s*$")
EXPLICIT_ID = re.compile(r"\s*\{#([^}]+)\}\s*$")
FENCE_RE = re.compile(r"^```")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\([^)]+\)")
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
EMPH_RE = re.compile(r"[*_`]+")

def set_base_from_args() -> None:
    global BASE
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--docs",
        action="store_true",
        help='Set BASE to $DEPLOYED_ROOT',
    )
    args = parser.parse_args()
    BASE = DEPLOYED_ROOT  if args.docs else ""
    print(f"BASE set to {BASE}")

def slugify(text: str) -> str:
    text = EXPLICIT_ID.sub("", text)
    text = IMAGE_RE.sub(r"\1", text)
    text = LINK_RE.sub(r"\1", text)
    text = EMPH_RE.sub("", text)
    text = text.lower()
    text = re.sub(r"[^\w\s.\-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text.strip())
    return text or "section"

def visible_title(raw: str) -> str:
    text = EXPLICIT_ID.sub("", raw)
    text = IMAGE_RE.sub(r"\1", text)   # ![Alt](../assets/img/x.png) -> Alt
    text = LINK_RE.sub(r"\1", text)
    text = EMPH_RE.sub("", text)
    return re.sub(r"\s+", " ", text).strip()

def strip_front_matter(lines):
    if not lines or lines[0].strip() != "---":
        return lines
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return lines[i + 1 :]
    return lines

def headings(path: Path):
    lines = strip_front_matter(path.read_text(encoding="utf-8").splitlines())
    in_fence = False
    seen = {}
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
        if hid in seen:
            seen[hid] += 1
            hid = f"{hid}-{seen[hid]}"
        else:
            seen[hid] = 0
        yield level, visible_title(raw), hid

def md_to_html(md: Path) -> str:
    print(f"Path: {md}")
    rel = md.relative_to(CONTENT.resolve()).with_suffix(".html")
    if rel.name == "Index.html":
        rel = rel.with_name("index.html")
    return f"{BASE}/{rel.as_posix()}".replace("//", "/")

def sorted_docs():
    files = []
    path = Path("content/index.md")
    if not path.is_absolute():
        path = ROOT / path
    path = path.resolve()
    if not path.is_file():
        print(f"skipping missing file: {path}")
    files.append(path)

    with ORDERED_LIST.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            path = Path(line)
            if not path.is_absolute():
                path = ROOT / path
            path = path.resolve()
            if not path.is_file():
                print(f"skipping missing file: {line}")
                continue
            files.append(path)
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
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    set_base_from_args()
    build()
