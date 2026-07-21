from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Ellipse, Rectangle
import numpy as np

from py_ltc_color_palettes import (
    adjust_ltc,
    bird,
    desaturate_ltc,
    info,
    ltc,
    ltc_cvd,
    palettes,
    plot_palette,
)


OUT = Path(__file__).resolve().parents[1] / "docs" / "assets" / "images"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    palette_overview()
    adjustment_showcase()
    cvd_showcase()
    bird_showcase()
    omics_examples()


def palette_overview() -> None:
    names = list(palettes)
    fig, ax = plt.subplots(figsize=(12, 13), dpi=160)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, len(names))
    ax.axis("off")

    for row, name in enumerate(reversed(names)):
        colors = palettes[name]
        y = row + 0.15
        ax.text(0, y + 0.28, name, ha="left", va="center", fontsize=8.8, fontweight="bold")
        for col, color in enumerate(colors):
            ax.add_patch(
                Rectangle(
                    (2.2 + col * 0.9, y),
                    0.82,
                    0.55,
                    facecolor=color,
                    edgecolor="white",
                    linewidth=0.8,
                )
            )

    ax.text(0, len(names) - 0.2, "ltc palettes", fontsize=16, fontweight="bold", ha="left")
    ax.text(
        2.2,
        len(names) - 0.2,
        "all upstream palette names and hex values ported to Python",
        fontsize=10,
        color="#5F6B6B",
        ha="left",
    )
    fig.tight_layout(pad=0.6)
    fig.savefig(OUT / "palette-overview.png", bbox_inches="tight")
    plt.close(fig)


def adjustment_showcase() -> None:
    rows = [
        ("maya", ltc("maya")),
        ("maya darker", adjust_ltc("maya", amount=-30)),
        ("maya lighter", adjust_ltc("maya", amount=30)),
        ("maya desaturated", desaturate_ltc("maya", amount=0.6)),
        ("maya custom", adjust_ltc("maya", amount=-25, which=[0, 3])),
    ]
    fig, ax = plt.subplots(figsize=(9, 3.2), dpi=180)
    ax.set_xlim(0, 6.8)
    ax.set_ylim(0, len(rows))
    ax.axis("off")

    for row, (label, colors) in enumerate(reversed(rows)):
        ax.text(0, row + 0.5, label, ha="left", va="center", fontsize=9, fontweight="bold")
        for col, color in enumerate(colors):
            ax.add_patch(
                Rectangle(
                    (1.65 + col, row + 0.14),
                    0.96,
                    0.72,
                    facecolor=color,
                    edgecolor="white",
                    linewidth=1,
                )
            )

    ax.text(0, len(rows) - 0.05, "palette adjustment", fontsize=14, fontweight="bold", ha="left")
    fig.tight_layout(pad=0.7)
    fig.savefig(OUT / "adjustment-showcase.png", bbox_inches="tight")
    plt.close(fig)


def cvd_showcase() -> None:
    fig, _ = ltc_cvd("expevo", severity=0.85, labels=True)
    fig.set_size_inches(8.5, 3.2)
    fig.savefig(OUT / "cvd-showcase.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def bird_showcase() -> None:
    fig, _ = bird(ltc("pantone23"))
    fig.savefig(OUT / "bird-pantone23.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    fig, _ = plot_palette(ltc("alger"))
    fig.savefig(OUT / "swatch-alger.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def omics_examples() -> None:
    rng = np.random.default_rng(10)
    pal = list(ltc("paloma"))
    heat = ltc("heatmap1", n=9, type="continuous")
    cmap = LinearSegmentedColormap.from_list("ltc_heatmap1", heat)

    fig, axes = plt.subplots(2, 2, figsize=(9.5, 7.2), dpi=170)
    for ax in axes.ravel():
        ax.spines[["top", "right"]].set_visible(False)
        ax.tick_params(labelsize=7, colors="#556060")

    matrix = np.outer(np.sin(np.linspace(0, 3 * np.pi, 18)), np.cos(np.linspace(0, 2 * np.pi, 14)))
    matrix += rng.normal(0, 0.22, matrix.shape)
    axes[0, 0].imshow(matrix, cmap=cmap, aspect="auto")
    axes[0, 0].set_title("expression heatmap", loc="left", fontsize=10, fontweight="bold")
    axes[0, 0].set_xlabel("samples", fontsize=8)
    axes[0, 0].set_ylabel("features", fontsize=8)
    axes[0, 0].set_xticks([])
    axes[0, 0].set_yticks([])

    groups = ["KO", "WT", "T1", "T2", "A"]
    values = [5.7, 5.0, 4.6, 3.8, 3.1]
    axes[0, 1].barh(groups[::-1], values[::-1], color=pal)
    axes[0, 1].set_title("differential abundance", loc="left", fontsize=10, fontweight="bold")
    axes[0, 1].set_xlabel("effect size", fontsize=8)

    for index, color in enumerate(pal):
        x = rng.normal(index, 0.11, 18)
        y = rng.normal(0.15 * index, 0.45, 18) + np.linspace(-0.2, 0.2, 18)
        axes[1, 0].scatter(x, y, s=26, color=color, alpha=0.78, edgecolor="white", linewidth=0.5)
    axes[1, 0].set_title("QC scatter", loc="left", fontsize=10, fontweight="bold")
    axes[1, 0].set_xlabel("library size", fontsize=8)
    axes[1, 0].set_ylabel("detected features", fontsize=8)

    data = [rng.normal(0.15 * i, 0.55 + 0.05 * i, 80) for i in range(len(pal))]
    parts = axes[1, 1].violinplot(data, showmeans=False, showmedians=True, widths=0.78)
    for body, color in zip(parts["bodies"], pal):
        body.set_facecolor(color)
        body.set_edgecolor("none")
        body.set_alpha(0.68)
    for key in ("cbars", "cmins", "cmaxes", "cmedians"):
        parts[key].set_color("#FFFFFF" if key == "cmedians" else "#D7DCDC")
        parts[key].set_linewidth(1.6 if key == "cmedians" else 0.9)
    axes[1, 1].set_title("sample distributions", loc="left", fontsize=10, fontweight="bold")
    axes[1, 1].set_xticks(range(1, 6), [f"C{i}" for i in range(1, 6)])

    fig.suptitle("ltc palettes in omics-style plots", x=0.02, ha="left", fontsize=15, fontweight="bold")
    fig.tight_layout(pad=1.3)
    fig.savefig(OUT / "omics-examples.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    main()
