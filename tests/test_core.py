from __future__ import annotations

import pytest

from py_ltc_color_palettes import (
    Palette,
    adjust_ltc,
    custom_adjust_ltc,
    desaturate_ltc,
    info,
    ltc,
    palettes,
)


EXPECTED_PALETTES = {
    "paloma": ("#83AF9B", "#C8C8A9", "#f8da8a", "#f7bf95", "#fe8ca1"),
    "maya": ("#3d5a80", "#98c1d9", "#e0fbfc", "#ee6c4d", "#293241"),
    "dora": ("#52777A", "#542437", "#C02942", "#D95B43", "#ECD078"),
    "ploen": ("#3F5671", "#83A1C3", "#CEB5C8", "#FAC898", "#B17776"),
    "olga": ("#c9e3c2", "#8bc8cb", "#eccd80", "#f5ab70", "#9c87a1"),
    "mterese": ("#f7ddaa", "#fac3ad", "#f897a1", "#9298BA", "#9cbeed"),
    "gaby": ("#fceaab", "#f1a890", "#a8c4cc", "#82A0C2", "#85496F"),
    "franscoise": ("#5980B1", "#b96a8d", "#A55062", "#E05256", "#E9A986"),
    "fernande": ("#ff7676", "#F9D662", "#7cab7d", "#75B7D1"),
    "sylvie": ("#E8B961", "#E88170", "#C6BDE8", "#5DB7C4", "#FD95BC"),
    "expevo": ("#FC4E07", "#E7B800", "#00AFBB", "#8B4769", "#1d457f", "#808080"),
    "minou": ("#00798c", "#d1495b", "#edae49", "#66a182", "#2e4057", "#8d96a3"),
    "kiss": ("#FF7C7E", "#FEC300", "#9E3F71", "#31BCBA", "#E20035"),
    "hat": ("#efb306", "#eb990c", "#e8351e", "#cd023d", "#852f88", "#4e54ac", "#0f8096", "#7db954", "#17a769", "#000000"),
    "reading": ("#EFBC68", "#919F89", "#EDBDAE", "#57717C", "#5F97A4", "#CAEAC8", "#95A1AE", "#C8CFD6"),
    "alger": ("#000000", "#1A5B5B", "#ACC8BE", "#F4AB5C", "#D1422F"),
    "trio1": ("#0E7175", "#FD7901", "#C35BCA"),
    "trio2": ("#89973D", "#E8B92F", "#A45E41"),
    "trio3": ("#E69F00", "#56B4E9", "#009E73"),
    "trio4": ("#94475E", "#364C54", "#E5A11F"),
    "heatmap0": ("#001219", "#005F73", "#0A9396", "#94D2BD", "#E9D8A6", "#EE9B00", "#CA6702", "#AE2012", "#9B2226"),
    "pantone23": ("#7A92A5", "#1F2C43", "#FFB000", "#842c48", "#46483d"),
    "remains": ("#69326E", "#EEEDC0", "#FF6D1F", "#EED455"),
    "midnight": ("#16232A", "#FF5B04", "#075056", "#E4EEF0"),
    "lincoln": ("#EEE9DF", "#C9C1B1", "#2C3B4D", "#FFB162", "#A35139", "#1B2632"),
    "luminaries": ("#FF5B04", "#075056", "#233038", "#FDF6E3", "#F4D47C", "#D3DBDD"),
    "seafarer": ("#013D5A", "#FCF3E3", "#BDD3CE", "#708C69", "#E4A25B"),
    "shuggie": ("#5B5F8D", "#9BB29E", "#DA6B51", "#F1DCBA", "#484149"),
    "heatmap1": ("#4d7799", "#7fa4c4", "#c5c8d4", "#d48e95", "#b5515b"),
    "heatmap2": ("#ca0020", "#f4a582", "#f7f7f7", "#92c5de", "#0571b0"),
    "heatmap3": ("#d7191c", "#fdae61", "#ffffbf", "#abd9e9", "#2c7bb6"),
    "casa_natal": ("#245E55", "#ED773C", "#808BC5", "#C63F3E", "#EAC119", "#EAA7C7", "#9ED6DF", "#1D1D1B", "#EAE4DA"),
}

EXPECTED_INFO = {
    "paloma": "Daughter of Francoise Gilot and Pablo Picasso",
    "maya": "Daughter of Marie-Therese Walter and Pablo Ruiz Picasso",
    "dora": "French photographer, painter, and poet",
    "ploen": "A beautiful village in Northern Germany",
    "olga": "Olga Khokhlova was a Russian ballet dancer",
    "mterese": "Marie-Therese Walter was a French model and mother of Maya",
    "gaby": "Gabrielle Depeyre Lespinasse was a French dancer",
    "franscoise": "Francoise Gilot was a significant French painter",
    "fernande": "Fernande was a French model and artist",
    "sylvie": "Sylvette David is a French artist and model",
    "expevo": "A palette that is often being used by biologists",
    "minou": "Minou was Picasso's favorite cat",
    "kiss": "Inspired by The Kiss Picasso 1925",
    "hat": "Inspired by Woman in Hat Picasso 1937",
    "reading": "Inspired by Two Girls Reading Picasso 1934",
    "alger": "Inspired by Les femmes d'Alger Picasso 1955",
    "trio1": "A discrete color palette to visualize 3 variables",
    "trio2": "A discrete color palette to visualize 3 variables",
    "trio3": "A discrete color palette to visualize 3 variables",
    "trio4": "A discrete color palette to visualize 3 variables",
    "heatmap0": "A diverging color palette suitable for heatmaps",
    "pantone23": "Soft Chaos was released by Pantone in Summer 23",
    "remains": "Inspired by The Remains of the Day by Kazuo Ishiguro (Booker Prize 1989)",
    "midnight": "Inspired by Midnight's Children by Salman Rushdie (Booker Prize 1981)",
    "lincoln": "Inspired by Lincoln in the Bardo by George Saunders (Booker Prize 2017)",
    "luminaries": "Inspired by The Luminaries by Eleanor Catton (Booker Prize 2013)",
    "seafarer": "Inspired by The Old Man and the Sea theme - maritime literary palette",
    "shuggie": "Inspired by Shuggie Bain by Douglas Stuart (Booker Prize 2020)",
    "heatmap1": "Blue and Red diverging palette 7 - ideal for heatmaps and expression data",
    "heatmap2": "Blue and Red diverging palette 8 - classic diverging scheme",
    "heatmap3": "Blue and Red diverging palette 9 - warm-cool diverging palette",
    "casa_natal": "Casa Natal on the Plaza de la Merced, the birthplace of Picasso",
}


def test_palette_data_matches_upstream_names_counts_and_values() -> None:
    assert dict(palettes) == EXPECTED_PALETTES
    assert {item.palette_name: item.bio for item in info} == EXPECTED_INFO


def test_ltc_discrete_default_and_subset() -> None:
    palette = ltc("maya")
    assert isinstance(palette, Palette)
    assert palette.name == "maya"
    assert tuple(palette) == palettes["maya"]
    assert tuple(ltc("maya", n=3)) == palettes["maya"][:3]


def test_ltc_continuous_interpolates_requested_count() -> None:
    palette = ltc("remains", n=10, type="continuous")
    assert len(palette) == 10
    assert palette[0] == "#69326E"
    assert palette[-1] == "#EED455"


def test_ltc_validation() -> None:
    with pytest.raises(KeyError):
        ltc("missing")
    with pytest.raises(ValueError, match="type"):
        ltc("maya", type="other")
    with pytest.raises(ValueError, match="greater"):
        ltc("maya", n=6)
    with pytest.raises(ValueError, match="non-negative"):
        ltc("maya", n=-1)


def test_adjust_ltc_uses_zero_based_which_and_preserves_others() -> None:
    adjusted = adjust_ltc("maya", amount=-25, which=[0, 3])
    assert adjusted.name == "maya_adj-25"
    assert adjusted[1] == palettes["maya"][1]
    assert adjusted[2] == palettes["maya"][2]
    assert adjusted[4] == palettes["maya"][4]
    assert adjusted[0] != palettes["maya"][0]
    assert adjusted[3] != palettes["maya"][3]


def test_custom_adjust_ltc_and_desaturate_ltc() -> None:
    custom = custom_adjust_ltc("remains", [-30, 0, 40, 0])
    assert custom.name == "remains_custom"
    assert custom[1] == palettes["remains"][1]
    assert custom[3] == palettes["remains"][3]

    muted = desaturate_ltc("maya", amount=0.6, which=[0])
    assert muted.name == "maya_desat"
    assert muted[0] != palettes["maya"][0]
    assert muted[1:] == palettes["maya"][1:]


def test_adjustment_validation() -> None:
    with pytest.raises(IndexError):
        adjust_ltc("maya", amount=10, which=[5])
    with pytest.raises(ValueError):
        custom_adjust_ltc("maya", [1, 2])
    with pytest.raises(ValueError):
        desaturate_ltc("maya", amount=1.5)
