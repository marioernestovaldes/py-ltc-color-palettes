from __future__ import annotations

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pytest

from py_ltc_color_palettes import bird, ltc, ltc_cvd, plot_palette


def test_plot_palette_returns_matplotlib_objects() -> None:
    fig, ax = plot_palette(ltc("maya"))
    assert fig.__class__.__name__ == "Figure"
    assert len(ax.patches) == 5
    plt.close(fig)


def test_bird_returns_matplotlib_objects() -> None:
    fig, ax = bird(ltc("pantone23"))
    assert fig.__class__.__name__ == "Figure"
    assert len(ax.patches) == 5
    plt.close(fig)


def test_bird_requires_palette_and_five_colors() -> None:
    with pytest.raises(TypeError):
        bird(["#000000", "#FFFFFF", "#FF0000", "#00FF00", "#0000FF"])  # type: ignore[arg-type]
    with pytest.raises(ValueError):
        bird(ltc("trio1"))


def test_ltc_cvd_returns_four_rows() -> None:
    fig, ax = ltc_cvd("expevo", severity=0.6)
    assert fig.__class__.__name__ == "Figure"
    assert len(ax.get_yticklabels()) == 4
    assert len(ax.patches) == 24
    plt.close(fig)


def test_ltc_cvd_accepts_custom_color_vectors() -> None:
    fig, ax = ltc_cvd(["#000000", "#FFFFFF"], labels=False)
    assert len(ax.patches) == 8
    plt.close(fig)


def test_ltc_cvd_validates_severity() -> None:
    with pytest.raises(ValueError):
        ltc_cvd("maya", severity=1.1)
