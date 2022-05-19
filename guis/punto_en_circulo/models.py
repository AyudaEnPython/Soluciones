"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from typing import Dict


MSG: Dict[int, str] = {
    0: "{} esta en el circunferencia del circulo",
    1: "{} esta en el interior del circulo",
    2: "{} esta fuera del circulo pero dentro del cuadrado inscrito",
    3: "{} esta fuera del circulo y del cuadrado inscrito",
}
CUADRANTE: Dict[str, str] = {
    "I": "A",
    "II": "B",
    "III": "C",
    "IV": "D",
}


@dataclass
class Punto:
    x: float
    y: float

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


@dataclass
class Circulo:
    c: Punto
    r: float

    def __post_init__(self) -> None:
        self.x, self.y = self.c.x, self.c.y

    def _cuadrado_inscrito(self, p: Punto) -> bool:
        return p.x <= self.c.x + self.r and p.y <= self.c.y + self.r

    def _distancia(self, p: Punto) -> bool:
        return (p.x - self.c.x) ** 2 + (p.y - self.c.y) ** 2

    def _cuadrante(self, p: Punto) -> str:
        if p.x > self.c.x and p.y > self.c.y:
            return CUADRANTE["I"]
        elif p.x < self.c.x and p.y > self.c.y:
            return CUADRANTE["II"]
        elif p.x < self.c.x and p.y < self.c.y:
            return CUADRANTE["III"]
        else:
            return CUADRANTE["IV"]

    def posicion_punto(self, p: Punto) -> bool:
        if self._distancia(p) == self.r ** 2:
            return MSG[0].format(p)
        elif self._distancia(p) < self.r ** 2:
            return MSG[1].format(p)
        elif self._cuadrado_inscrito(p):
            return (
                MSG[2].format(p) +
                f"\n{p} se encuentra en la zona {self._cuadrante(p)}"
            )
        else:
            return MSG[3].format(p)
