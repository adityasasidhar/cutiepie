<div align="center">

<img src="logo.png" width="120" alt="Cutiepie">

# Cutiepie

**A soft VS Code theme in powder pink and turquoise on true black.**

Two accents, no noise. Pink carries structure — functions, classes, tags, JSON keys.
Turquoise carries content — strings and the things you actually typed.
Everything else stays out of the way.

[![Version](https://img.shields.io/visual-studio-marketplace/v/adityasasidhar.cutiepie?color=F7B2C9&labelColor=0A0908&style=flat-square)](https://marketplace.visualstudio.com/items?itemName=adityasasidhar.cutiepie)
[![Installs](https://img.shields.io/visual-studio-marketplace/i/adityasasidhar.cutiepie?color=76E0D0&labelColor=0A0908&style=flat-square)](https://marketplace.visualstudio.com/items?itemName=adityasasidhar.cutiepie)
[![License](https://img.shields.io/badge/license-MIT-F7B2C9?labelColor=0A0908&style=flat-square)](LICENSE)

</div>

---

## Cutiepie Dark

![Cutiepie Dark](assets/preview-dark.png)

## Cutiepie Light

![Cutiepie Light](assets/preview-light.png)

---

## Install

**From the Marketplace** — search `Cutiepie` in the Extensions panel, or:

```
ext install adityasasidhar.cutiepie
```

Then <kbd>Ctrl</kbd>+<kbd>K</kbd> <kbd>Ctrl</kbd>+<kbd>T</kbd> and pick **Cutiepie Dark** or **Cutiepie Light**.

**From source:**

```bash
git clone https://github.com/adityasasidhar/cutiepie.git
cp -r cutiepie ~/.vscode/extensions/adityasasidhar.cutiepie-1.0.0
```

---

## Palette

![Palette](assets/palette.png)

The whole theme runs on two accents plus neutrals. Nothing warm, nothing muddy.

| Role | Dark | Light |
| --- | --- | --- |
| Background | `#0A0908` | `#FEFEFE` |
| Foreground | `#FFFFFF` | `#2C2C2C` |
| **Accent** — functions, classes, tags, JSON keys, cursor, buttons | `#F7B2C9` | `#C1547F` |
| **Strings** — strings, interfaces, readonly props | `#76E0D0` | `#0E7C6B` |
| Keywords, operators, parameters | `#AFACA7` | `#616161` |
| Comments *(italic)* | `#9B808C` | `#8A6E7C` |
| Added / success | `#4FC9B0` | `#0F9B84` |
| Deleted / error | `#FF6F85` | `#D32F52` |
| Merge conflict | `#C9A0DC` | `#8E5AA8` |

A few deliberate choices worth knowing about:

- **Git and diff green is turquoise.** In a two-accent palette, turquoise already reads as
  "good" — a separate green just added a third hue for no gain.
- **Errors stay red, but rosy.** They're more saturated than the accent on purpose, so an
  error never reads as decoration.
- **Merge conflicts are lavender.** Once the warm tones were gone, orange had nowhere to sit.

---

## Recommended settings

The theme is tuned for a light editor chrome and generous line height:

```jsonc
{
  "editor.fontFamily": "'Geist Mono', 'JetBrains Mono', monospace",
  "editor.lineHeight": 1.6,
  "editor.fontLigatures": true,
  "workbench.colorTheme": "Cutiepie Dark"
}
```

---

## Development

Theme JSON in `themes/` is the source of truth. The images in `assets/` are generated
from it, so they can never drift from what actually ships:

```bash
python3 scripts/render_previews.py     # assets/preview-{dark,light}.png
python3 scripts/render_palette.py      # assets/palette.png
```

Package and publish:

```bash
npm install
npx vsce package                       # -> cutiepie-1.0.0.vsix
npx vsce publish
```

---

## Credits

Built on [**Vesper**](https://github.com/raunofreiberg/vesper) by
[Rauno Freiberg](https://github.com/raunofreiberg) — the scope structure and token
architecture are his, and this theme would not exist without that groundwork. Thank you.

## License

MIT © 2026 Aditya Sasidhar. Portions derived from Vesper, MIT © 2023 Rauno Freiberg —
see [LICENSE](LICENSE) for the full notices.
