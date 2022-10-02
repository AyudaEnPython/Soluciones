"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from random import choice, randint
from typing import List
# pip install prototools
from prototools import Canvas


def draw():
    c = Canvas(width=20, height=12)
    c.umlcard(
        1, 1,
        "Persona",
        ["genero", "edad"],
        ["es_mayor_a"]
    )
    c.umlcard(
        10, 1,
        "Estadisticas",
        ["personas"],
        [
            "promedio",
            "promedio_genero",
            "cantidad",
        ],
    )
    c.show()


@dataclass
class Person:
    genero: str
    edad: int

    def es_mayor_a(self, n: int) -> bool:
        return self.edad > n


@dataclass
class Estadisticas:
    personas: List[Person]

    def promedio(self):
        return sum([p.edad for p in self.personas]) / len(self.personas)

    def promedio_genero(self, genero: str):
        return (
            sum([p.edad for p in self.personas if p.genero == genero]) /
            len(self.personas)
        )

    def cantidad(self):
        return len([p for p in self.personas if p.es_mayor_a(30)])


def main():
    genero = "masculino", "femenino"
    personas = [
        Person(choice(genero), edad)
        for edad in [randint(15, 80) for _ in range(10)]
    ]
    e = Estadisticas(personas)
    print(f"Promedio de edades: {e.promedio()}")
    print(f"Promedio de edad de hombres: {e.promedio_genero('masculino')}")
    print(f"Cantidad de mujeres con edad mayor a 30 años: {e.cantidad()}")
    print(f"Mayor edad ingresada: {max([p.edad for p in personas])}")


if __name__ == "__main__":
    draw()
    main()
