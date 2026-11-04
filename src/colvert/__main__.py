from colvert.census import census
from colvert.counting import QuackCounter
from colvert.reserve import build_reserve


def main() -> None:
    reserve = {name: QuackCounter(bird) for name, bird in build_reserve().items()}
    print("Recensement de la réserve de Colvert")
    for line in census(reserve):
        print(f"  {line}")
    print(f"Cris comptés : {sum(bird.quacks for bird in reserve.values())}")


if __name__ == "__main__":
    main()
