"""Démonstration formateur : le @decorator de Python, à comparer à QuackCounter.

python demos/function_decorator.py
"""

import functools
from collections.abc import Callable


def count_calls(function: Callable[[], str]) -> Callable[[], str]:
    calls = 0

    @functools.wraps(function)
    def wrapper() -> str:
        nonlocal calls
        calls += 1
        print(f"  appel n° {calls} de {function.__name__}")
        return function()

    return wrapper


@count_calls
def mallard_cry() -> str:
    """Le cri du colvert."""
    return "Coin-coin"


if __name__ == "__main__":
    print(mallard_cry())
    print(mallard_cry())
    print(f"nom : {mallard_cry.__name__} ; documentation : {mallard_cry.__doc__}")
