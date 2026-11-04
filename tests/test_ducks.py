from colvert.ducks import Mallard, RubberDuck, Teal


class TestMallard:
    def test_a_mallard_says_coin_coin(self):
        assert Mallard().quack() == "Coin-coin"


class TestTeal:
    def test_a_teal_says_krik_krik(self):
        assert Teal().quack() == "Krik-krik"


class TestRubberDuck:
    def test_a_rubber_duck_squeaks(self):
        assert RubberDuck().quack() == "Pouic"
