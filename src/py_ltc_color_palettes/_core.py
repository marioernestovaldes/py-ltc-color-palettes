from __future__ import annotations

from collections.abc import Iterable, Sequence
import warnings

import numpy as np
from colorspace import darken, desaturate, lighten
from matplotlib.colors import to_hex, to_rgb

from ._data import palettes
from ._types import Palette

PaletteInput = str | Palette | Sequence[str]


def ltc(name: str, n: int | None = None, type: str = "discrete") -> Palette:
    """Select a palette by name.

    Parameters mirror the R package where practical. Python callers must pass a
    quoted palette name, for example ``ltc("maya")``.
    """

    if type not in {"discrete", "continuous"}:
        raise ValueError("type must be either 'discrete' or 'continuous'")

    colors = _palette_by_name(name)
    count = len(colors) if n is None else _validate_n(n)

    if type == "discrete":
        if count > len(colors):
            raise ValueError("Number of requested colors greater than what palette can offer")
        return Palette(tuple(colors[:count]), name)

    return Palette(tuple(_interpolate(colors, count)), name)


def adjust_ltc(name: str, amount: float = 0, which: Iterable[int] | None = None) -> Palette:
    """Darken or lighten a palette, optionally adjusting selected 0-based indexes."""

    amount = _validate_number(amount, "amount")
    if amount < -100 or amount > 100:
        warnings.warn(
            "'amount' should be between -100 and 100. Values outside this range may produce unexpected results.",
            stacklevel=2,
        )

    colors = list(_palette_by_name(name))
    indexes = _resolve_indexes(which, len(colors))

    if amount < 0:
        replacement = darken([colors[index] for index in indexes], amount=abs(amount) / 100)
    elif amount > 0:
        replacement = lighten([colors[index] for index in indexes], amount=amount / 100)
    else:
        replacement = [colors[index] for index in indexes]

    for index, color in zip(indexes, replacement):
        colors[index] = _normalize_hex(color)

    return Palette(tuple(colors), f"{name}_adj{_format_amount(amount)}")


def custom_adjust_ltc(name: str, adjustments: Sequence[float]) -> Palette:
    """Apply one lightness adjustment per color in a palette."""

    colors = list(_palette_by_name(name))
    if len(adjustments) != len(colors):
        raise ValueError(f"'adjustments' must have same length as palette ({len(colors)} colors)")

    adjusted = colors[:]
    for index, raw_amount in enumerate(adjustments):
        amount = _validate_number(raw_amount, "adjustments")
        if amount < 0:
            adjusted[index] = _normalize_hex(darken([colors[index]], amount=abs(amount) / 100)[0])
        elif amount > 0:
            adjusted[index] = _normalize_hex(lighten([colors[index]], amount=amount / 100)[0])

    return Palette(tuple(adjusted), f"{name}_custom")


def desaturate_ltc(name: str, amount: float = 0.5, which: Iterable[int] | None = None) -> Palette:
    """Reduce palette saturation, optionally for selected 0-based indexes."""

    amount = _validate_number(amount, "amount")
    if amount < 0 or amount > 1:
        raise ValueError("'amount' must be between 0 and 1")

    colors = list(_palette_by_name(name))
    indexes = _resolve_indexes(which, len(colors))
    replacement = desaturate([colors[index] for index in indexes], amount=amount)

    for index, color in zip(indexes, replacement):
        colors[index] = _normalize_hex(color)

    return Palette(tuple(colors), f"{name}_desat")


def _coerce_palette(value: PaletteInput) -> tuple[str, tuple[str, ...]]:
    if isinstance(value, Palette):
        return value.name, value.colors
    if isinstance(value, str):
        return value, _palette_by_name(value)
    return "palette", tuple(value)


def _palette_by_name(name: str) -> tuple[str, ...]:
    try:
        return palettes[name]
    except KeyError as exc:
        available = ", ".join(palettes)
        raise KeyError(f"Palette {name!r} not found. Available palettes: {available}") from exc


def _interpolate(colors: Sequence[str], n: int) -> list[str]:
    if n == 0:
        return []
    if n == 1:
        return [_normalize_hex(colors[0])]

    rgb = np.array([to_rgb(color) for color in colors], dtype=float)
    source = np.linspace(0.0, 1.0, len(colors))
    target = np.linspace(0.0, 1.0, n)
    interpolated = np.column_stack(
        [np.interp(target, source, rgb[:, channel]) for channel in range(3)]
    )
    return [_normalize_hex(to_hex(color, keep_alpha=False)) for color in interpolated]


def _resolve_indexes(which: Iterable[int] | None, length: int) -> list[int]:
    if which is None:
        return list(range(length))

    indexes = list(which)
    for index in indexes:
        if not isinstance(index, int) or isinstance(index, bool):
            raise TypeError("'which' must contain integer indexes")
        if index < 0 or index >= length:
            raise IndexError(f"'which' must contain valid 0-based indexes (0 to {length - 1})")
    return indexes


def _validate_n(n: int) -> int:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    return n


def _validate_number(value: float, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"'{name}' must be numeric")
    return float(value)


def _normalize_hex(color: str) -> str:
    return to_hex(color, keep_alpha=False).upper()


def _format_amount(amount: float) -> str:
    return str(int(amount)) if amount.is_integer() else str(amount)
