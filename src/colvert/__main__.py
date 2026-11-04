from colvert.census import census
from colvert.reserve import build_reserve


def main() -> None:
    print("Recensement de la réserve de Colvert")
    for line in census(build_reserve()):
        print(f"  {line}")


if __name__ == "__main__":
    main()
