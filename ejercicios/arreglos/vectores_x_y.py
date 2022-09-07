"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dado los vectores X e Y de 100 números enteros positivos y negativos.
Los vectores X e Y guardan las abscisas y las ordenadas de los puntos
en el plano cartesiano respectivamente. Determinar:

- El punto que se encuentra más alejado del eje de las ordenadas (Y).
- La distancia mayor entre todos los puntos y mostrar aquellos que
    cumplieron la condición.
- Determinar la distancia del origen de coordenadas a la recta que
    pasa por los puntos que tuvieron la mayor distancia.
"""
from random import randint
from typing import List
from collections import namedtuple
import unittest

Punto = namedtuple("Punto", ["x", "y"])
Puntos = List[Punto]
SIZE = 100


def _convertir(x: List[int], y: List[int]) -> Puntos:
    return [Punto(x, y) for x, y in zip(x, y)]


def _distancia(a: Punto, b: Punto) -> float:
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


def _recta(p: Punto, q: Punto):
    m = (q.y - p.y) / (q.x - p.x)
    b = p.y - m * p.x
    return m, b


def puntos_aleatorios():
    return [
        Punto(randint(-100, 100), randint(-100, 100)) for _ in range(SIZE)
    ]


def lejano(puntos: Puntos) -> float:
    return max(puntos, key=lambda punto: abs(punto.y)).y


def distancia_mayor_puntos(puntos: Puntos) -> float:
    return max([
        (_distancia(puntos[i], puntos[j]), (puntos[i], puntos[j]))
        for i in range(len(puntos))
        for j in range(i+1, len(puntos))
    ])


def distancia_origen(puntos: Puntos) -> float:
    p, q = puntos
    m, b = _recta(p, q)
    return abs(b) / ((m ** 2 + 1) ** 0.5)


def main():
    puntos = puntos_aleatorios()
    print(f"Punto más alejado del eje Y: {lejano(puntos)}")
    d, puntos = distancia_mayor_puntos(puntos)
    print(f"La distancia mayor entre todos los puntos es: {d}")
    print(
        f"La distancia del origen de coordenadas a la recta que "
        f"pasa por los puntos que tuvieron la mayor distancia es: "
        f"{distancia_origen(puntos)}"
    )


class Test(unittest.TestCase):

    x = [2, -2, 1, -1]
    y = [4, 2, 1, -1]

    def test_punto(self):
        punto = Punto(1, 1)
        self.assertEqual(punto.x, 1)
        self.assertEqual(punto.y, 1)

    def test_convertir(self):
        puntos = [Punto(x, y) for x, y in zip(self.x, self.y)]
        self.assertEqual(_convertir(self.x, self.y), puntos)

    def test_distancia(self):
        a = Punto(1, 1)
        b = Punto(2, 2)
        self.assertEqual(_distancia(a, b), 2**0.5)

    def test_recta(self):
        m, b = _recta(Punto(-3, 1), Punto(-2, -3))
        self.assertEqual(m, -4.0)
        self.assertEqual(b, -11.0)

    def test_puntos(self):
        puntos = _convertir(self.x, self.y)
        self.assertEqual(lejano(puntos), 4)

    def test_distancia_mayor_puntos(self):
        puntos = _convertir(self.x, self.y)
        d, puntos = distancia_mayor_puntos(puntos)
        self.assertEqual(d, 5.830951894845301)
        self.assertEqual(puntos, (Punto(2, 4), Punto(-1, -1)))

    def test_distancia_origen(self):
        puntos = _convertir(self.x, self.y)
        _, puntos = distancia_mayor_puntos(puntos)
        self.assertEqual(distancia_origen(puntos), 0.3429971702850176)


if __name__ == "__main__":
    main()
    # unittest.main()
