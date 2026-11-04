from birdlib import ElectronicCall, Goose


class GooseAdapter:
    def __init__(self, goose: Goose) -> None:
        raise NotImplementedError

    def quack(self) -> str:
        raise NotImplementedError


class ElectronicCallAdapter:
    def __init__(self, call: ElectronicCall, frequency: int) -> None:
        raise NotImplementedError

    def quack(self) -> str:
        raise NotImplementedError
