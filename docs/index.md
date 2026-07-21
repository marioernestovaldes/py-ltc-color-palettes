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
brightness, simulate color-vision deficiency, and preview omics-style chart
types including heatmaps, bars, line plots, scatter plots, boxplots, violin
plots, volcano plots, and PCA scores.

## What Is Included

- All upstream palette names, hex values, and bios.
- Discrete palette lookup with `ltc("maya")`.
- Continuous interpolation with `ltc("heatmap0", n=11, type="continuous")`.
- Lightness adjustment with `adjust_ltc()` and `custom_adjust_ltc()`.
- Desaturation with `desaturate_ltc()`.
- Color-vision-deficiency previews with `ltc_cvd()`.
- Matplotlib swatch and bird plots.

See the [Palette Gallery](gallery.md) for the full palette list and
[Examples](examples.md) for the fuller package tour.

## Reference Implementation

The authoritative source for palette names, hex values, bios, and original R
behavior is [`loukesio/ltc-color-palettes`](https://github.com/loukesio/ltc-color-palettes).
