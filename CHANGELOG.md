# Changelog

All notable changes to Cutiepie are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] — 2026-07-31

### Changed

- The second accent is now **pale sky blue** instead of turquoise: `#AFDCF2` in the dark
  theme, `#2E86BA` in the light one. It carries strings, interfaces, and readonly properties.
- Git and diff "added" colours follow it to `#7FC8EC` / `#3D97C6`.
- Terminal ANSI blue moved to periwinkle (`#7B93F0` dark, `#3949AB` light) so it no longer
  collides with the new string colour.
- The icon gradient now fades pink into pale blue, and is generated from the dark theme
  by `scripts/render_logo.py` rather than hand-authored.

## [1.0.0] — 2026-07-31

### Added

- **Cutiepie Dark** — powder pink (`#F7B2C9`) and turquoise (`#76E0D0`) on true black (`#0A0908`).
- **Cutiepie Light** — deep rose (`#C1547F`) and deep turquoise (`#0E7C6B`) on near-white.
- Full workbench coverage: terminal ANSI palette, git decorations, diff editor,
  bracket pair colourisation, inlay hints, and semantic token colours.
- Generated preview and palette images under `assets/`, rendered directly from the
  theme files by `scripts/`.

[1.1.0]: https://github.com/adityasasidhar/cutiepie/releases/tag/v1.1.0
[1.0.0]: https://github.com/adityasasidhar/cutiepie/releases/tag/v1.0.0
