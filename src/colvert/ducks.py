from typing import Protocol


class Quackable(Protocol):
    def quack(self) -> str: ...


class Mallard:
    def quack(self) -> str:
        return "Coin-coin"


class Teal:
    def quack(self) -> str:
        return "Krik-krik"


class RubberDuck:
    def quack(self) -> str:
        return "Pouic"
