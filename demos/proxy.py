"""Démonstration formateur : un Proxy de protection devant le poste de baguage.

python demos/proxy.py
"""

from dataclasses import dataclass, field
from typing import Protocol


class RingingStation(Protocol):
    def ring(self, bird: str) -> str: ...

    def release(self, bird: str) -> str: ...


@dataclass
class FieldStation:
    rings: dict[str, str] = field(default_factory=dict)

    def ring(self, bird: str) -> str:
        ring = f"FR-{len(self.rings) + 1:04d}"
        self.rings[bird] = ring
        return f"bague {ring} posée sur {bird}"

    def release(self, bird: str) -> str:
        return f"{bird} relâché avec la bague {self.rings[bird]}"


@dataclass(frozen=True)
class Agent:
    name: str
    licensed: bool


class AccessDenied(Exception):
    pass


class ProtectedStation:
    def __init__(self, station: RingingStation, agent: Agent) -> None:
        self._station = station
        self._agent = agent

    def ring(self, bird: str) -> str:
        self._check_licence()
        return self._station.ring(bird)

    def release(self, bird: str) -> str:
        self._check_licence()
        return self._station.release(bird)

    def _check_licence(self) -> None:
        if not self._agent.licensed:
            raise AccessDenied(f"{self._agent.name} n'est pas habilité au baguage")


def ringing_session(station: RingingStation, bird: str) -> None:
    print(f"  {station.ring(bird)}")
    print(f"  {station.release(bird)}")


if __name__ == "__main__":
    station = FieldStation()
    for agent, bird in [
        (Agent("Léa", licensed=True), "Gaston"),
        (Agent("Tom", licensed=False), "Margot"),
    ]:
        print(f"{agent.name} bague {bird} :")
        try:
            ringing_session(ProtectedStation(station, agent), bird)
        except AccessDenied as error:
            print(f"  refusé : {error}")
    print(f"Bagues posées : {len(station.rings)}")
