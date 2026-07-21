from __future__ import annotations

from ._core import adjust_ltc, custom_adjust_ltc, desaturate_ltc, ltc
from ._data import info, palettes
from ._plots import bird, ltc_cvd, plot_palette
from ._types import Palette, PaletteInfo

__all__ = [
    "Palette",
    "PaletteInfo",
    "adjust_ltc",
    "bird",
    "custom_adjust_ltc",
    "desaturate_ltc",
    "info",
    "ltc",
    "ltc_cvd",
    "palettes",
    "plot_palette",
]

__version__ = "0.1.0"
