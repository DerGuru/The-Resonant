#!/usr/bin/env python3
"""
Build EPUB3 from the standalone XHTML files in Chapters/Epub/.

Usage:
    python Scripts/build_epub_from_xhtml.py
    python Scripts/build_epub_from_xhtml.py --out My_Book.epub
"""

import argparse
import re
import sys
import uuid
import zipfile
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

# ── config ────────────────────────────────────────────────────────────────────
ROOT   = Path(__file__).parent.parent
XDIR   = ROOT / "Chapters" / "Epub"
COVER  = ROOT / "CoverArt.jpg"

TITLE  = "The Resonant"
AUTHOR = "J. He"
LANG   = "en"

# ── helpers ───────────────────────────────────────────────────────────────────

class _HeadingExtractor(HTMLParser):
    """Extract text from the first <h1> or <h2>."""
    def __init__(self):
        super().__init__()
        self.result = None
        self._active = False
        self._buf: list[str] = []

    def handle_starttag(self, tag, attrs):
        if self.result is None and tag in ("h1", "h2"):
            self._active = True

    def handle_endtag(self, tag):
        if self._active and tag in ("h1", "h2"):
            self._active = False
            self.result = " ".join("".join(self._buf).split())

    def handle_data(self, data):
        if self._active:
            self._buf.append(data)


def _extract_title(html: str) -> str:
    p = _HeadingExtractor()
    p.feed(html)
    return p.result or "Chapter"


def _extract_body(html: str) -> str:
    """Return inner content of <body>…</body>."""
    m = re.search(r"<body[^>]*>(.*?)</body>", html, re.DOTALL | re.IGNORECASE)
    return m.group(1).strip() if m else html


def _safe_id(stem: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]", "_", stem)


def _sort_key(p: Path):
    name = p.stem
    if name.startswith("__"):
        return ("000", name)   # Preface always first
    m = re.match(r"^(\d+)", name)
    prefix = m.group(1) if m else "999"
    return (prefix, name)


# ── XML/XHTML builders ────────────────────────────────────────────────────────

def _chapter_xhtml(body: str, title: str) -> str:
    return f"""\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="{LANG}">
<head>
  <meta charset="UTF-8"/>
  <title>{title}</title>
  <link rel="stylesheet" type="text/css" href="../style.css"/>
</head>
<body>
{body}
</body>
</html>"""


def _nav_xhtml(chapters: list[dict]) -> str:
    items = "\n".join(
        f'      <li><a href="chapters/{c["stem"]}.xhtml">{c["title"]}</a></li>'
        for c in chapters
    )
    return f"""\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml"
      xmlns:epub="http://www.idpf.org/2007/ops"
      xml:lang="{LANG}">
<head>
  <meta charset="UTF-8"/>
  <title>Table of Contents</title>
</head>
<body>
  <nav epub:type="toc" id="toc">
    <h1>Contents</h1>
    <ol>
{items}
    </ol>
  </nav>
</body>
</html>"""


def _content_opf(chapters: list[dict], has_cover: bool, uid: str) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    manifest_chapters = "\n".join(
        f'    <item id="{c["id"]}" href="chapters/{c["stem"]}.xhtml"'
        f' media-type="application/xhtml+xml"/>'
        for c in chapters
    )
    spine_refs = "\n".join(
        f'    <itemref idref="{c["id"]}"/>'
        for c in chapters
    )
    cover_manifest = (
        '\n    <item id="cover-image" href="cover.jpg"'
        ' media-type="image/jpeg" properties="cover-image"/>'
        if has_cover else ""
    )
    cover_meta = (
        '\n    <meta name="cover" content="cover-image"/>'
        if has_cover else ""
    )

    return f"""\
<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf"
         version="3.0"
         unique-identifier="bookid">

  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="bookid">{uid}</dc:identifier>
    <dc:title>{TITLE}</dc:title>
    <dc:creator>{AUTHOR}</dc:creator>
    <dc:language>{LANG}</dc:language>
    <meta property="dcterms:modified">{now}</meta>{cover_meta}
  </metadata>

  <manifest>
    <item id="nav" href="nav.xhtml"
          media-type="application/xhtml+xml" properties="nav"/>
    <item id="css" href="style.css" media-type="text/css"/>{cover_manifest}
{manifest_chapters}
  </manifest>

  <spine>
{spine_refs}
  </spine>

</package>"""


CONTAINER_XML = """\
<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0"
           xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf"
              media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>"""

# Clean, readable CSS for EPUB readers
STYLESHEET = """\
body {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 1em;
  line-height: 1.7;
  margin: 1em 2em;
  max-width: 38em;
  color: #111;
}
h1, h2, h3 {
  font-family: "Helvetica Neue", Arial, sans-serif;
  margin-top: 2.5em;
  margin-bottom: 0.5em;
  line-height: 1.3;
}
p {
  margin: 0.3em 0;
  text-indent: 1.5em;
}
p:first-of-type, h1 + p, h2 + p, h3 + p, hr + p {
  text-indent: 0;
}
hr {
  border: none;
  border-top: 1px solid #bbb;
  margin: 2em auto;
  width: 40%;
}
em  { font-style: italic; }
strong { font-weight: bold; }
code, pre {
  font-family: "Courier New", monospace;
  font-size: 0.9em;
}
blockquote {
  margin-left: 1.5em;
  padding-left: 1em;
  border-left: 3px solid #ccc;
  color: #444;
}"""


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=str(ROOT / "The_Resonant_EN.epub"),
                        help="Output .epub path")
    args = parser.parse_args()
    output = Path(args.out)

    # Collect + sort XHTML files
    xhtml_files = sorted(XDIR.glob("*.xhtml"), key=_sort_key)
    if not xhtml_files:
        sys.exit(f"ERROR: no .xhtml files found in {XDIR}")

    # Parse each file
    chapters = []
    for f in xhtml_files:
        raw = f.read_text(encoding="utf-8")
        chapters.append({
            "stem":  f.stem,
            "id":    _safe_id(f.stem),
            "title": _extract_title(raw),
            "body":  _extract_body(raw),
        })

    uid       = str(uuid.uuid4())
    has_cover = COVER.exists()

    # Assemble ZIP / EPUB
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as z:
        # mimetype MUST be first and uncompressed
        info = zipfile.ZipInfo("mimetype")
        info.compress_type = zipfile.ZIP_STORED
        z.writestr(info, "application/epub+zip")

        z.writestr("META-INF/container.xml", CONTAINER_XML)
        z.writestr("OEBPS/content.opf",      _content_opf(chapters, has_cover, uid))
        z.writestr("OEBPS/nav.xhtml",        _nav_xhtml(chapters))
        z.writestr("OEBPS/style.css",        STYLESHEET)

        if has_cover:
            z.write(str(COVER), "OEBPS/cover.jpg")

        for c in chapters:
            z.writestr(
                f'OEBPS/chapters/{c["stem"]}.xhtml',
                _chapter_xhtml(c["body"], c["title"])
            )

    kb = round(output.stat().st_size / 1024, 1)
    print(f"Done: {output}  ({kb} KB, {len(chapters)} chapters)")


if __name__ == "__main__":
    main()
