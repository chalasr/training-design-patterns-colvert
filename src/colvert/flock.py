from collections.abc import Iterator

from colvert.ducks import Quackable


class Flock:
    def __init__(self, *birds: Quackable) -> None:
        raise NotImplementedError

    def add(self, bird: Quackable) -> None:
        raise NotImplementedError

    def quack(self) -> str:
        raise NotImplementedError

    def __iter__(self) -> Iterator[Quackable]:
        raise NotImplementedError
