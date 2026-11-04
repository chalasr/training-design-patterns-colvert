import inspect

from birdlib import ElectronicCall, Goose
from colvert import flock
from colvert.adapters import ElectronicCallAdapter, GooseAdapter
from colvert.counting import QuackCounter
from colvert.ducks import Mallard, RubberDuck, Teal
from colvert.flock import Flock


class TestFlock:
    def test_a_flock_quacks_with_the_cries_of_all_its_members(self):
        assert Flock(Mallard(), Teal()).quack() == "Coin-coin, Krik-krik"

    def test_an_empty_flock_is_silent(self):
        assert Flock().quack() == ""

    def test_a_bird_can_join_a_flock(self):
        pond = Flock(Mallard())

        pond.add(RubberDuck())

        assert pond.quack() == "Coin-coin, Pouic"

    def test_a_flock_can_contain_another_flock(self):
        family = Flock(Mallard(), Mallard())

        assert Flock(family, Teal()).quack() == "Coin-coin, Coin-coin, Krik-krik"

    def test_a_flock_mixes_adapted_and_counted_birds(self):
        gaston = QuackCounter(Mallard())
        mixed = Flock(gaston, GooseAdapter(Goose()), ElectronicCallAdapter(ElectronicCall(), 440))

        assert mixed.quack() == "Coin-coin, Honk, Coin-coin électronique (440 Hz)"
        assert gaston.quacks == 1

    def test_iterating_over_a_flock_gives_its_members(self):
        gaston, margot = Mallard(), Teal()

        assert list(Flock(gaston, margot)) == [gaston, margot]

    def test_a_flock_never_asks_what_its_members_are(self):
        assert "isinstance" not in inspect.getsource(flock)
