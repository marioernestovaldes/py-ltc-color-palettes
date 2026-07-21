# Examples

These examples mirror the main workflows from the upstream R package, translated
to Python.

## Select A Palette

```python
from py_ltc_color_palettes import ltc

alger = ltc("alger")
print(alger)
```

Python callers always pass palette names as strings.

## Discrete And Continuous Palettes

Use the default discrete mode when one color maps to one group. Request a
continuous palette when colors should interpolate across a numeric range.

```python
from py_ltc_color_palettes import ltc

groups = ltc("expevo")
first_three = ltc("maya", n=3)
gradient = ltc("heatmap0", n=11, type="continuous")
```

## Palette Swatches

```python
from py_ltc_color_palettes import ltc, plot_palette

fig, ax = plot_palette(ltc("alger"))
fig.savefig("alger.png", dpi=160, bbox_inches="tight")
```

## Bird Plot

```python
from py_ltc_color_palettes import bird, ltc

fig, ax = bird(ltc("pantone23"))
fig.savefig("pantone23-bird.png", dpi=160, bbox_inches="tight")
```

## Adjust, Brighten, Darken, And Desaturate

`adjust_ltc()` darkens negative amounts and lightens positive amounts.
`which` uses normal Python 0-based indexes.

```python
from py_ltc_color_palettes import adjust_ltc, custom_adjust_ltc, desaturate_ltc

darker = adjust_ltc("maya", amount=-30)
lighter = adjust_ltc("maya", amount=30)
selected = adjust_ltc("maya", amount=-25, which=[0, 3])
custom = custom_adjust_ltc("maya", [-40, -20, 0, 20, 40])
muted = desaturate_ltc("maya", amount=0.6)
```

## Color-Vision-Deficiency Preview

`ltc_cvd()` shows normal, deuteranopia, protanopia, and tritanopia previews.

```python
from py_ltc_color_palettes import ltc_cvd

fig, ax = ltc_cvd("maya")
fig, ax = ltc_cvd("expevo", severity=0.6)
```

## Matplotlib Usage

The returned `Palette` behaves like an immutable sequence of hex strings, so it
can be passed directly to Matplotlib color arguments.

```python
import matplotlib.pyplot as plt
import numpy as np

from py_ltc_color_palettes import ltc

rng = np.random.default_rng(42)
groups = ["KO", "WT", "T1", "T2", "A"]
values = rng.normal(loc=[4, 6, 5, 7, 4.5], scale=0.5)

fig, ax = plt.subplots(figsize=(5, 3))
ax.bar(groups, values, color=ltc("paloma"))
ax.set_ylabel("normalized abundance")
fig.tight_layout()
```

For an interactive visual comparison across omics-style plots, use the
[Palette Explorer](palette-explorer.html).
