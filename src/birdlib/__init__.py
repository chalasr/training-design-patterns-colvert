"""birdlib : une bibliothèque tierce. Colvert l'utilise, mais ne peut pas la modifier."""


class Goose:
    def honk(self) -> str:
        return "Honk"


class ElectronicCall:
    def emit(self, frequency: int) -> str:
        return f"Coin-coin électronique ({frequency} Hz)"
