"""Le filet de sécurité : ce fichier ne change à aucune étape."""

from colvert.census import census
from colvert.ducks import Mallard, RubberDuck, Teal


class TestCensus:
    def test_each_bird_answers_the_census_with_its_cry(self):
        reserve = {
            "Gaston, colvert": Mallard(),
            "Margot, sarcelle d'hiver": Teal(),
            "Bibi, leurre en plastique": RubberDuck(),
        }

        assert census(reserve) == [
            "Gaston, colvert : Coin-coin",
            "Margot, sarcelle d'hiver : Krik-krik",
            "Bibi, leurre en plastique : Pouic",
        ]

    def test_an_empty_reserve_gives_an_empty_census(self):
        assert census({}) == []
