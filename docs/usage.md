# Usage

## List Palettes

```python
from py_ltc_color_palettes import palettes

print(list(palettes))
```

## Select Palettes

```python
from py_ltc_color_palettes import ltc

alger = ltc("alger")
first_three = ltc("maya", n=3)
continuous = ltc("remains", n=10, type="continuous")
```

Python callers use quoted palette names. Index arguments such as `which` use
normal Python 0-based indexing.

## Adjust Palettes

```python
from py_ltc_color_palettes import adjust_ltc, custom_adjust_ltc, desaturate_ltc

darker = adjust_ltc("maya", amount=-30)
lighter = adjust_ltc("maya", amount=30)
selected = adjust_ltc("maya", amount=-25, which=[0, 3])
custom = custom_adjust_ltc("maya", [-40, -20, 0, 20, 40])
muted = desaturate_ltc("maya", amount=0.6)
```

## Plot Palettes

```python
from py_ltc_color_palettes import bird, ltc, plot_palette

fig, ax = plot_palette(ltc("alger"))
fig, ax = bird(ltc("pantone23"))
```

## Check Color-Vision Accessibility

```python
from py_ltc_color_palettes import ltc_cvd

fig, ax = ltc_cvd("maya")
fig, ax = ltc_cvd("expevo", severity=0.6)
```

All plotting helpers return Matplotlib figure and axes objects.
