from birdlib import ElectronicCall, Goose
from colvert.adapters import ElectronicCallAdapter, GooseAdapter
from colvert.ducks import Mallard, Quackable, RubberDuck, Teal


def build_reserve() -> dict[str, Quackable]:
    return {
        "Gaston, colvert": Mallard(),
        "Margot, sarcelle d'hiver": Teal(),
        "Bibi, leurre en plastique": RubberDuck(),
        "Gertrude, oie cendrée": GooseAdapter(Goose()),
        "Appeau électronique": ElectronicCallAdapter(ElectronicCall(), 440),
    }
