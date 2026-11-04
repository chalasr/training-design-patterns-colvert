from collections.abc import Mapping

from colvert.ducks import Quackable


def census(reserve: Mapping[str, Quackable]) -> list[str]:
    return [f"{name} : {bird.quack()}" for name, bird in reserve.items()]
