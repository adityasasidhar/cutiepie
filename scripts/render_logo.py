#!/usr/bin/env python3
"""
Render logo.png — a heart fading from the theme's pink accent to its string
colour, on the theme background. Colours are read from the dark theme so the
icon always matches what ships.

    python3 scripts/render_logo.py
"""
import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
SIZE, SS = 256, 4                  # final size, supersample factor
W = SIZE * SS


def theme_colours():
    theme = json.loads((ROOT / "themes" / "cutiepie-dark-color-theme.json").read_text())
    tokens = {t["name"]: t["settings"] for t in theme["tokenColors"]}
    accent = tokens["Function, Special Method"]["foreground"]
    string = tokens["String, Symbols, Inherited Class"]["foreground"]
    bg = theme["colors"]["editor.background"][:7]
    to_rgb = lambda h: tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))
    return to_rgb(accent), to_rgb(string), to_rgb(bg)


def heart_point(t):
    """Parametric heart, normalised into a 0..1 box."""
    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x / 17.0, -y / 17.0     # flip y for image coords


def main():
    top, bottom, bg = theme_colours()

    mask = Image.new("L", (W, W), 0)
    pts = []
    for i in range(720):
        hx, hy = heart_point(i * math.pi / 360)
        pts.append((W / 2 + hx * W * 0.40, W / 2 + hy * W * 0.40))
    ImageDraw.Draw(mask).polygon(pts, fill=255)

    grad = Image.new("RGB", (1, W))
    for y in range(W):
        f = y / (W - 1)
        f = f * f * (3 - 2 * f)                     # smoothstep for a softer blend
        grad.putpixel((0, y), tuple(round(top[c] + (bottom[c] - top[c]) * f) for c in range(3)))
    grad = grad.resize((W, W))

    # soft glow so the heart reads against the dark square
    glow = mask.filter(ImageFilter.GaussianBlur(W // 22)).point(lambda v: int(v * 0.38))

    img = Image.new("RGB", (W, W), bg)
    img.paste(grad, (0, 0), glow)
    img.paste(grad, (0, 0), mask)

    card = Image.new("L", (W, W), 0)
    ImageDraw.Draw(card).rounded_rectangle([0, 0, W - 1, W - 1], radius=W // 6, fill=255)
    out = Image.new("RGBA", (W, W), (0, 0, 0, 0))
    out.paste(img, (0, 0), card)

    dest = ROOT / "logo.png"
    out.resize((SIZE, SIZE), Image.LANCZOS).save(dest)
    print(f"wrote {dest.relative_to(ROOT)}  {SIZE}x{SIZE}")


if __name__ == "__main__":
    main()
