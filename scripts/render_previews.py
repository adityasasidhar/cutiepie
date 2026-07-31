#!/usr/bin/env python3
"""
Render the marketing screenshots in assets/ straight from the theme files,
so the previews can never drift from the actual colours that ship.

    python3 scripts/render_previews.py dark
    python3 scripts/render_previews.py light
    python3 scripts/render_previews.py            # both

Requires Pillow and a DejaVu Sans Mono install (standard on most Linux boxes).
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")

FONT_MONO = FONT_DIR / "DejaVuSansMono.ttf"
FONT_ITALIC = FONT_DIR / "DejaVuSansMono-Oblique.ttf"
FONT_UI = FONT_DIR / "DejaVuSans.ttf"

FONT_SIZE, LINE_HEIGHT, PAD, GUTTER, CHROME = 30, 46, 44, 78, 54


def load_theme(variant):
    path = ROOT / "themes" / f"cutiepie-{variant}-color-theme.json"
    return json.loads(path.read_text())


def sample_lines(theme):
    """The snippet, expressed as (text, colour, italic) runs per line."""
    tokens = {t["name"]: t["settings"] for t in theme["tokenColors"]}
    ui = theme["colors"]

    fn = tokens["Function, Special Method"]["foreground"]
    string = tokens["String, Symbols, Inherited Class"]["foreground"]
    kw = tokens["Keyword, Storage"]["foreground"]
    var = tokens["Variables"]["foreground"]
    num = tokens["Number, Constant, Function Argument, Tag Attribute, Embedded"]["foreground"]
    cls = tokens["Class, Support"]["foreground"]
    cmt = tokens["Comment"]["foreground"]
    pun = ui["editor.foreground"]

    return [
        [("// her very own theme  <3", cmt, 1)],
        [],
        [("import", kw, 0), (" { ", pun, 0), ("describe", var, 0), (", ", pun, 0),
         ("test", var, 0), (", ", pun, 0), ("expect", var, 0), (" } ", pun, 0),
         ("from", kw, 0), (" ", pun, 0), ('"bun:test"', string, 0)],
        [],
        [("class", kw, 0), (" ", pun, 0), ("Cutiepie", cls, 0), (" ", pun, 0), ("{", pun, 0)],
        [("  ", pun, 0), ("readonly", kw, 0), (" pink ", var, 0), ("= ", pun, 0), ('"#F7B2C9"', string, 0)],
        [("  ", pun, 0), ("readonly", kw, 0), (" turquoise ", var, 0), ("= ", pun, 0), ('"#76E0D0"', string, 0)],
        [("  ", pun, 0), ("readonly", kw, 0), (" loveLevel ", var, 0), ("= ", pun, 0), ("9001", num, 0)],
        [("}", pun, 0)],
        [],
        [("test", fn, 0), ("(", pun, 0), ('"uses only the colours she likes"', string, 0), (", ", pun, 0),
         ("async", kw, 0), (" () ", pun, 0), ("=> ", kw, 0), ("{", pun, 0)],
        [("  ", pun, 0), ("const", kw, 0), (" theme ", var, 0), ("= ", pun, 0),
         ("new", kw, 0), (" ", pun, 0), ("Cutiepie", cls, 0), ("()", pun, 0)],
        [],
        [("  ", pun, 0), ("expect", fn, 0), ("(theme).", pun, 0), ("toContain", fn, 0),
         ("(", pun, 0), ('"powder pink"', string, 0), (")", pun, 0)],
        [("  ", pun, 0), ("expect", fn, 0), ("(theme).", pun, 0), ("toContain", fn, 0),
         ("(", pun, 0), ('"turquoise"', string, 0), (")", pun, 0)],
        [("  ", pun, 0), ("expect", fn, 0), ("(theme).", pun, 0), ("not", kw, 0), (".", pun, 0),
         ("toContain", fn, 0), ("(", pun, 0), ('"golden"', string, 0), (")", pun, 0)],
        [("  ", pun, 0), ("expect", fn, 0), ("(theme.loveLevel).", pun, 0),
         ("toBeGreaterThan", fn, 0), ("(", pun, 0), ("9000", num, 0), (")", pun, 0)],
        [("})", pun, 0)],
    ]


def render(variant):
    theme = load_theme(variant)
    ui = theme["colors"]
    lines = sample_lines(theme)

    mono = ImageFont.truetype(str(FONT_MONO), FONT_SIZE)
    italic = ImageFont.truetype(str(FONT_ITALIC), FONT_SIZE)
    ui_font = ImageFont.truetype(str(FONT_UI), 22)

    width = PAD * 2 + GUTTER + int(mono.getlength("M") * 62)
    height = PAD * 2 + LINE_HEIGHT * len(lines) + CHROME

    img = Image.new("RGB", (width, height), ui["editor.background"][:7])
    draw = ImageDraw.Draw(img)

    # window chrome, coloured from the theme's own UI keys
    draw.rectangle([0, 0, width, CHROME], fill=ui["titleBar.activeBackground"])
    draw.line([(0, CHROME), (width, CHROME)], fill=ui["sideBar.border"])
    dots = [ui["editorError.foreground"], ui["editorWarning.foreground"],
            ui["gitDecoration.addedResourceForeground"]]
    for i, dot in enumerate(dots):
        draw.ellipse([20 + i * 26, 20, 34 + i * 26, 34], fill=dot)
    draw.text((110, 16), f"cutiepie.test.ts  —  Cutiepie {variant.capitalize()}",
              font=ui_font, fill=ui["titleBar.activeForeground"])

    y = CHROME + PAD
    for n, line in enumerate(lines, 1):
        draw.text((PAD, y), str(n).rjust(3), font=mono,
                  fill=ui["editorLineNumber.foreground"])
        x = PAD + GUTTER
        for text, colour, is_italic in line:
            font = italic if is_italic else mono
            draw.text((x, y), text, font=font, fill=colour)
            x += font.getlength(text)
        y += LINE_HEIGHT

    out = ROOT / "assets" / f"preview-{variant}.png"
    img.save(out)
    print(f"wrote {out.relative_to(ROOT)}  {img.size[0]}x{img.size[1]}")


if __name__ == "__main__":
    targets = sys.argv[1:] or ["dark", "light"]
    for v in targets:
        render(v)
