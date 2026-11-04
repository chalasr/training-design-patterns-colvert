from colvert.ducks import Mallard, Quackable, RubberDuck, Teal


def build_reserve() -> dict[str, Quackable]:
    return {
        "Gaston, colvert": Mallard(),
        "Margot, sarcelle d'hiver": Teal(),
        "Bibi, leurre en plastique": RubberDuck(),
    }
