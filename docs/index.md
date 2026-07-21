# py-ltc-color-palettes

`py-ltc-color-palettes` is a Python port of the R package
[`loukesio/ltc-color-palettes`](https://github.com/loukesio/ltc-color-palettes).
It brings the same curated color palettes, bios, palette adjustments, CVD
preview, swatch plot, and bird plot to Python.

## Install

```bash
pip install py-ltc-color-palettes
```

For local development:

```bash
pip install -e ".[dev]"
```

## Quick Start

```python
from py_ltc_color_palettes import ltc, plot_palette

maya = ltc("maya")
fig, ax = plot_palette(maya)
```

## Explorer

Use the [Palette Explorer](palette-explorer.html) to switch palettes, adjust
brightness, simulate color-vision deficiency, and preview six chart types.

## Reference Implementation

The authoritative source for palette names, hex values, bios, and original R
behavior is [`loukesio/ltc-color-palettes`](https://github.com/loukesio/ltc-color-palettes).
