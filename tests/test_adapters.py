from birdlib import ElectronicCall, Goose
from colvert.adapters import ElectronicCallAdapter, GooseAdapter
from colvert.census import census


class TestGooseAdapter:
    def test_an_adapted_goose_quacks_by_honking(self):
        assert GooseAdapter(Goose()).quack() == "Honk"

    def test_an_adapted_goose_answers_the_census(self):
        reserve = {"Gertrude, oie cendrée": GooseAdapter(Goose())}

        assert census(reserve) == ["Gertrude, oie cendrée : Honk"]

    def test_the_adapter_only_offers_the_duck_interface(self):
        assert not hasattr(GooseAdapter(Goose()), "honk")


class TestElectronicCallAdapter:
    def test_an_adapted_call_emits_at_the_frequency_given_to_the_adapter(self):
        assert ElectronicCallAdapter(ElectronicCall(), 440).quack() == (
            "Coin-coin électronique (440 Hz)"
        )

    def test_each_adapter_keeps_its_own_frequency(self):
        low = ElectronicCallAdapter(ElectronicCall(), 300)
        high = ElectronicCallAdapter(ElectronicCall(), 1200)

        assert [low.quack(), high.quack()] == [
            "Coin-coin électronique (300 Hz)",
            "Coin-coin électronique (1200 Hz)",
        ]
