from __future__ import annotations

from collections.abc import Iterator, Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class PaletteInfo:
    """Backstory metadata for an upstream ltc palette."""

    palette_name: str
    bio: str


@dataclass(frozen=True)
class Palette(Sequence[str]):
    """Immutable sequence of hex colors with an ltc palette name."""

    colors: tuple[str, ...]
    name: str

    def __iter__(self) -> Iterator[str]:
        return iter(self.colors)

    def __len__(self) -> int:
        return len(self.colors)

    def __getitem__(self, index: int | slice) -> str | tuple[str, ...]:
        return self.colors[index]

    def __repr__(self) -> str:
        colors = ", ".join(self.colors)
        return f"Palette(name={self.name!r}, colors=({colors}))"

    def __str__(self) -> str:
        return f"{self.name}\n" + "\n".join(self.colors)

    def as_list(self) -> list[str]:
        """Return a mutable list copy of the palette colors."""

        return list(self.colors)
