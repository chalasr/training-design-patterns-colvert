from colvert.__main__ import main


class TestMain:
    def test_prints_the_census_of_the_reserve(self, capsys):
        main()

        assert capsys.readouterr().out.splitlines() == [
            "Recensement de la réserve de Colvert",
            "  Gaston, colvert : Coin-coin",
            "  Margot, sarcelle d'hiver : Krik-krik",
            "  Bibi, leurre en plastique : Pouic",
            "  Gertrude, oie cendrée : Honk",
            "  Appeau électronique : Coin-coin électronique (440 Hz)",
            "Cris comptés : 5",
        ]
