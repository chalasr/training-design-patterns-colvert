from birdlib import ElectronicCall, Goose
from colvert.adapters import ElectronicCallAdapter, GooseAdapter
from colvert.ducks import Mallard, Quackable, RubberDuck, Teal
from colvert.flock import Flock


def build_reserve() -> dict[str, Quackable]:
    return {
        "Gaston, colvert": Mallard(),
        "Margot, sarcelle d'hiver": Teal(),
        "Bibi, leurre en plastique": RubberDuck(),
        "Gertrude, oie cendrée": GooseAdapter(Goose()),
        "Appeau électronique": ElectronicCallAdapter(ElectronicCall(), 440),
        "Volée de l'étang nord": Flock(Mallard(), Mallard(), Teal()),
        "Volée de passage": Flock(
            GooseAdapter(Goose()), GooseAdapter(Goose()), Flock(Mallard(), Teal())
        ),
    }
