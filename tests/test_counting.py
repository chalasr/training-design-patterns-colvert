from birdlib import Goose
from colvert.adapters import GooseAdapter
from colvert.counting import QuackCounter
from colvert.ducks import Mallard, Teal


class TestQuackCounter:
    def test_the_cry_goes_through_unchanged(self):
        assert QuackCounter(Mallard()).quack() == "Coin-coin"

    def test_a_new_counter_has_counted_nothing(self):
        assert QuackCounter(Mallard()).quacks == 0

    def test_each_cry_is_counted(self):
        counter = QuackCounter(Teal())

        counter.quack()
        counter.quack()
        counter.quack()

        assert counter.quacks == 3

    def test_each_counter_counts_the_cries_of_its_own_bird(self):
        gaston = QuackCounter(Mallard())
        margot = QuackCounter(Teal())

        gaston.quack()
        gaston.quack()
        margot.quack()

        assert [gaston.quacks, margot.quacks] == [2, 1]

    def test_an_adapted_goose_can_be_counted(self):
        counter = QuackCounter(GooseAdapter(Goose()))

        assert counter.quack() == "Honk"
        assert counter.quacks == 1

    def test_a_counter_can_wrap_another_counter(self):
        inner = QuackCounter(Mallard())
        outer = QuackCounter(inner)

        outer.quack()

        assert [outer.quacks, inner.quacks] == [1, 1]

    def test_the_counted_duck_is_not_modified(self):
        duck = Mallard()

        QuackCounter(duck).quack()

        assert not hasattr(duck, "quacks")
