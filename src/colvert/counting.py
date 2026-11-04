from colvert.ducks import Quackable


class QuackCounter:
    def __init__(self, bird: Quackable) -> None:
        self.bird = bird
        self.quacks = 0

    def quack(self) -> str:
        self.quacks += 1
        return self.bird.quack()
