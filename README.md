# py-ltc-color-palettes

Python replica of the R package [`loukesio/ltc-color-palettes`](https://github.com/loukesio/ltc-color-palettes).

This package ports the upstream palettes, palette metadata, color adjustments,
color-vision-deficiency preview, swatch plot, and bird plot to Python. The API is
Pythonic where R syntax does not translate directly: use quoted palette names and
0-based indexes for `which`.

## Links

- Documentation: <https://marioernestovaldes.github.io/py-ltc-color-palettes/>
- Live palette explorer: <https://marioernestovaldes.github.io/py-ltc-color-palettes/palette-explorer.html>
- Source repository: <https://github.com/marioernestovaldes/py-ltc-color-palettes>
- Upstream R reference: <https://github.com/loukesio/ltc-color-palettes>

## Install

```bash
pip install py-ltc-color-palettes
```

For local development:

```bash
pip install -e ".[dev]"
```

## Usage

```python
from py_ltc_color_palettes import (
    adjust_ltc,
    bird,
    desaturate_ltc,
    ltc,
    ltc_cvd,
    palettes,
    plot_palette,
)

print(list(palettes))

maya = ltc("maya")
print(maya)

first_three = ltc("maya", n=3)
continuous = ltc("remains", n=10, type="continuous")

darker = adjust_ltc("maya", amount=-30)
muted = desaturate_ltc("maya", amount=0.6)
selected = adjust_ltc("maya", amount=-25, which=[0, 3])

fig, ax = plot_palette(maya)
fig, ax = bird(ltc("pantone23"))
fig, ax = ltc_cvd("expevo", severity=0.6)
```

## Documentation

The hosted MkDocs Material site is available at
<https://marioernestovaldes.github.io/py-ltc-color-palettes/>.

The live palette explorer is available directly at
<https://marioernestovaldes.github.io/py-ltc-color-palettes/palette-explorer.html>.
It includes live palette selection, brightness adjustment, color-vision
simulation, and omics-style chart previews.

Build the MkDocs Material site locally:

```bash
mkdocs serve
```

## Reference

The authoritative reference implementation is the R package at
`https://github.com/loukesio/ltc-color-palettes`, specifically the upstream
`main`/v0.4.0 behavior used when this Python port was created.

Palette data and license text are ported from the upstream MIT-licensed project.
