"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from random import randint, random, sample
from typing import List, Tuple


@dataclass
class Guerrero:
    nombre: str
    vida: int
    fuerza: int
    precision: int
    velocidad: int
    defensa: int

    def esta_con_vida(self) -> bool:
        return self.vida > 0

    def acierto(self, other: object) -> bool:
        return random() <= (self.precision - other.velocidad) / 100

    def golpear(self, other):
        if self.acierto(other):
            ataque = max((self.fuerza - other.defensa) + randint(-10, 11), 1)
            other.vida -= ataque
            return f"Golpe certero de {self.nombre}, {ataque} de daño!"
        else:
            return f"{other.nombre} esquiva el golpe!"

    def __str__(self) -> str:
        return f"{self.nombre}: {self.vida if self.esta_con_vida() else 0}"


@dataclass
class Arena:
    guerreros: List[Guerrero] = field(default_factory=list)

    def _set_turno(self, guerreros: Tuple[Guerrero, Guerrero]) -> Tuple[Guerrero, Guerrero]:
        a, b = guerreros
        if a.velocidad < b.velocidad:
            a, b = b, a
        return a, b

    def simulacion(self):
        golpeador, receptor = self._set_turno(sample(self.guerreros, k=2))
        print(f"{golpeador.nombre} vs {receptor.nombre}")
        while golpeador.esta_con_vida() and receptor.esta_con_vida():
            print(f"> {golpeador.golpear(receptor)}")
            print(f"{golpeador} | {receptor}")
            golpeador, receptor = receptor, golpeador
        print(f"Ganador: {receptor.nombre}")


if __name__ == "__main__":
    arena = Arena([
        Guerrero("Superman", 100, 70, 80, 30, 20),
        Guerrero("Goku", 100, 60, 80, 40, 20),
        Guerrero("Chuck Norris", 200, 99, 99, 99, 99),
    ])
    arena.simulacion()
