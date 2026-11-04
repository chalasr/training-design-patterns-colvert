from collections.abc import Iterator

from colvert.ducks import Quackable


class Flock:
    def __init__(self, *birds: Quackable) -> None:
        self.birds = list(birds)

    def add(self, bird: Quackable) -> None:
        self.birds.append(bird)

    def quack(self) -> str:
        return ", ".join(bird.quack() for bird in self.birds)

    def __iter__(self) -> Iterator[Quackable]:
        return iter(self.birds)
