from __future__ import annotations

from collections.abc import Sequence

from colorspace import deutan, protan, tritan
from matplotlib import pyplot as plt
from matplotlib.colors import to_rgb
from matplotlib.patches import Polygon, Rectangle

from ._core import PaletteInput, _coerce_palette, _normalize_hex
from ._data import info_by_name
from ._types import Palette


def plot_palette(palette: PaletteInput, labels: bool = True):
    """Visualize a palette as a horizontal swatch bar."""

    name, colors = _coerce_palette(palette)
    title, subtitle = _title_and_subtitle(name, colors)
    fig, ax = plt.subplots(figsize=(max(4.5, len(colors) * 0.9), 1.8))

    for index, color in enumerate(colors):
        ax.add_patch(Rectangle((index, 0), 1, 1, facecolor=color, edgecolor="white", linewidth=1))
        if labels:
            ax.text(index + 0.5, -0.12, color, ha="center", va="top", fontsize=8, color="#333333")

    ax.set_xlim(0, len(colors))
    ax.set_ylim(-0.35 if labels else 0, 1)
    ax.set_axis_off()
    fig.suptitle(title, fontstyle="italic", y=0.98)
    ax.set_title(subtitle, fontsize=10, color="#555555", pad=10)
    fig.tight_layout()
    return fig, ax


def bird(palette: Palette) -> tuple[plt.Figure, plt.Axes]:
    """Visualize an ltc palette in the upstream bird shape."""

    if not isinstance(palette, Palette):
        raise TypeError("Input must be a Palette object. Use ltc() to create one.")
    if len(palette) < 5:
        raise ValueError(f"Bird visualization requires at least 5 colors. Current palette has {len(palette)} colors.")

    title, subtitle = _title_and_subtitle(palette.name, palette.colors)
    fig, ax = plt.subplots(figsize=(4.8, 5.2))

    ax.add_patch(Rectangle((0, -5), 5, 17, facecolor=palette[0], edgecolor="none"))
    _add_polygon(ax, [(2, 0), (3, 2), (3, 8), (2, 10)], palette[1])
    _add_polygon(ax, [(3, 8), (3.22, 8), (3, 7.33)], palette[2])
    _add_polygon(ax, [(1.99, 5), (2.5, 6.5), (3.01, 5), (3.01, 2), (2, -0.01), (2, 1)], palette[3])
    _add_polygon(ax, [(2, 1), (2.5, 3), (2.5, -2), (2, -4)], palette[4])

    ax.set_xlim(-0.2, 5.2)
    ax.set_ylim(-5.2, 12.2)
    ax.set_aspect("equal")
    ax.set_axis_off()
    fig.suptitle(title, fontstyle="italic", y=0.98)
    ax.set_title(subtitle, fontsize=10, color="#555555", pad=10)
    fig.tight_layout()
    return fig, ax


def ltc_cvd(name_or_colors: PaletteInput, severity: float = 1.0, labels: bool = True):
    """Preview a palette under common color-vision-deficiency simulations."""

    if isinstance(severity, bool) or not isinstance(severity, (int, float)):
        raise TypeError("severity must be numeric")
    severity = float(severity)
    if severity < 0 or severity > 1:
        raise ValueError("`severity` must be between 0 and 1.")

    name, colors = _coerce_palette(name_or_colors)
    color_list = list(colors)
    vision = {
        "Normal": tuple(colors),
        "Deuteranopia": tuple(_normalize_hex(color) for color in deutan(color_list, severity=severity)),
        "Protanopia": tuple(_normalize_hex(color) for color in protan(color_list, severity=severity)),
        "Tritanopia": tuple(_normalize_hex(color) for color in tritan(color_list, severity=severity)),
    }

    types = list(vision)
    fig, ax = plt.subplots(figsize=(max(5.5, len(colors) * 1.0), 2.8))
    for row, vision_type in enumerate(reversed(types)):
        row_colors = vision[vision_type]
        for col, color in enumerate(row_colors):
            ax.add_patch(Rectangle((col, row), 1, 1, facecolor=color, edgecolor="white", linewidth=1.2))
            if labels:
                ax.text(
                    col + 0.5,
                    row + 0.5,
                    color.upper(),
                    ha="center",
                    va="center",
                    fontsize=7.5,
                    color=_label_color(color),
                )

    ax.set_xlim(0, len(colors))
    ax.set_ylim(0, len(types))
    ax.set_xticks([])
    ax.set_yticks([row + 0.5 for row in range(len(types))])
    ax.set_yticklabels(list(reversed(types)))
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title("Colour vision deficiency simulation", fontsize=10, color="#6B6B6B", loc="left")
    fig.suptitle(name, fontweight="bold", x=0.125, ha="left")
    fig.tight_layout()
    return fig, ax


def _add_polygon(ax: plt.Axes, coordinates: Sequence[tuple[float, float]], color: str) -> None:
    ax.add_patch(Polygon(coordinates, closed=True, facecolor=color, edgecolor="none"))


def _label_color(color: str) -> str:
    red, green, blue = (channel * 255 for channel in to_rgb(color))
    luminance = red * 0.299 + green * 0.587 + blue * 0.114
    return "#1A1A1A" if luminance > 150 else "#FFFFFF"


def _title_and_subtitle(name: str, colors: Sequence[str]) -> tuple[str, str]:
    item = info_by_name.get(name)
    if item is None:
        return name or "Custom Palette", f"{len(colors)} colors"
    return item.palette_name, item.bio
