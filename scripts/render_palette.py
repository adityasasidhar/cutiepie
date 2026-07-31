#!/usr/bin/env python3
"""
Render assets/palette.png — the swatch card used in the README.
Colours are read from the theme files, so the card stays truthful.

    python3 scripts/render_palette.py
"""
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")

# (label, where to read the colour from)
#   ("ui", key)    -> theme["colors"][key]
#   ("tok", name)  -> theme["tokenColors"] entry with that name
SWATCHES = [
    ("Background", ("ui", "editor.background")),
    ("Foreground", ("ui", "editor.foreground")),
    ("Accent", ("tok", "Function, Special Method")),
    ("Strings", ("tok", "String, Symbols, Inherited Class")),
    ("Keywords", ("tok", "Keyword, Storage")),
    ("Comments", ("tok", "Comment")),
    ("Added", ("ui", "gitDecoration.addedResourceForeground")),
    ("Deleted", ("ui", "gitDecoration.deletedResourceForeground")),
]

SW, GAP, PAD, ROW_GAP = 128, 18, 44, 34
CARD_W = PAD * 2 + len(SWATCHES) * SW + (len(SWATCHES) - 1) * GAP


def resolve(theme, source):
    kind, key = source
    if kind == "ui":
        return theme["colors"][key][:7].upper()
    for t in theme["tokenColors"]:
        if t["name"] == key:
            return t["settings"]["foreground"][:7].upper()
    raise KeyError(key)


def load(variant):
    return json.loads((ROOT / "themes" / f"cutiepie-{variant}-color-theme.json").read_text())


def main():
    title_f = ImageFont.truetype(str(FONT_DIR / "DejaVuSans-Bold.ttf"), 26)
    label_f = ImageFont.truetype(str(FONT_DIR / "DejaVuSans.ttf"), 17)
    hex_f = ImageFont.truetype(str(FONT_DIR / "DejaVuSansMono.ttf"), 16)

    rows = [("Cutiepie Dark", load("dark")), ("Cutiepie Light", load("light"))]
    row_h = 40 + SW + 52
    height = PAD * 2 + row_h * len(rows) + ROW_GAP * (len(rows) - 1)

    img = Image.new("RGB", (CARD_W, height), "#0A0908")
    d = ImageDraw.Draw(img)

    y = PAD
    for title, theme in rows:
        d.text((PAD, y), title, font=title_f, fill="#FFFFFF")
        sy = y + 40
        for i, (label, source) in enumerate(SWATCHES):
            colour = resolve(theme, source)
            x = PAD + i * (SW + GAP)
            d.rounded_rectangle([x, sy, x + SW, sy + SW], radius=14,
                                fill=colour, outline="#2A2A2A", width=1)
            d.text((x, sy + SW + 10), label, font=label_f, fill="#C8C4C0")
            d.text((x, sy + SW + 30), colour, font=hex_f, fill="#7E7A76")
        y += row_h + ROW_GAP

    out = ROOT / "assets" / "palette.png"
    img.save(out)
    print(f"wrote {out.relative_to(ROOT)}  {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    main()
