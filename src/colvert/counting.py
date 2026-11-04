from colvert.ducks import Quackable


class QuackCounter:
    def __init__(self, bird: Quackable) -> None:
        raise NotImplementedError

    def quack(self) -> str:
        raise NotImplementedError
