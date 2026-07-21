# Reference

## Data

`palettes` is a read-only mapping from palette name to an immutable tuple of hex
colors.

`info` is a tuple of `PaletteInfo` records containing `palette_name` and `bio`.

## Functions

### `ltc(name, n=None, type="discrete")`

Select a palette by name. `type` must be `"discrete"` or `"continuous"`.
Discrete palettes error if `n` exceeds the number of colors in the source
palette.

### `adjust_ltc(name, amount=0, which=None)`

Darken or lighten an entire palette or selected 0-based indexes. Negative
amounts darken; positive amounts lighten.

### `custom_adjust_ltc(name, adjustments)`

Apply one lightness adjustment per color. The adjustment list must match the
palette length.

### `desaturate_ltc(name, amount=0.5, which=None)`

Reduce saturation for an entire palette or selected 0-based indexes.

### `ltc_cvd(name_or_colors, severity=1.0, labels=True)`

Preview normal, deuteranopia, protanopia, and tritanopia simulations.

### `plot_palette(palette, labels=True)`

Render a horizontal swatch bar.

### `bird(palette)`

Render the upstream bird-shaped palette preview. Requires at least five colors.
