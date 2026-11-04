from birdlib import ElectronicCall, Goose


class GooseAdapter:
    def __init__(self, goose: Goose) -> None:
        self.goose = goose

    def quack(self) -> str:
        return self.goose.honk()


class ElectronicCallAdapter:
    def __init__(self, call: ElectronicCall, frequency: int) -> None:
        self.call = call
        self.frequency = frequency

    def quack(self) -> str:
        return self.call.emit(self.frequency)
