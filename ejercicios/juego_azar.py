"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Elaborar un programa que simule un juego, donde se generen los 6
números al azar, y se generen hasta 100 jugadores. El programa debe
indicar si alguno ganó el premio principal, o cuántos consiguieron 5 o
4 aciertos de los números al azar.
"""
import unittest
from random import sample
from collections import Counter
from typing import List

MAX = 10
JUGADORES = 100


def solve_naive(a: List[int], b: List[int]) -> int:
    return len([n for n in a if n in b])


def solve_intersection(a: List[int], b: List[int]) -> int:
    return len(list(set(a).intersection(b)))


def solve_counter(a: List[int], b: List[int]) -> int:
    def frequency(b, a):
        d = dict(Counter(b))
        return {k: d.get(k, 0) for k in a}
    return sum(frequency(a, b).values())


def generar_numeros() -> List[int]:
    return sample(list(range(1, MAX+1)), k=6)


def generar_jugadores() -> List[int]:
    return [generar_numeros() for _ in range(JUGADORES)]


def main(funcion):
    seis, cinco, cuatro = [], [], []
    ganador, jugadores = generar_numeros(), generar_jugadores()
    for posicion, jugador in enumerate(jugadores):
        aciertos = funcion(jugador, ganador)
        if aciertos == 6:
            seis.append(posicion)
        if aciertos == 5:
            cinco.append(posicion)
        if aciertos == 4:
            cuatro.append(posicion)
    print(f"Número ganador: {' - '.join(map(str, ganador))}")
    print(
        f"Ganadores: {len(seis)}\n5 aciertos: {len(cinco)}\n"
        f"4 aciertos: {len(cuatro)}"
    )


def main_test(_f):
    s, f, f_ = [], [], []
    w = [1, 24, 52, 29, 94, 13]
    ps = [
        [19, 24, 52, 29, 94, 13],
        [1, 24, 53, 29, 94, 13],
        [12, 44, 52, 59, 34, 23],
        [52, 94, 1, 13, 24, 29],
        [1, 24, 5, 29, 4, 13],
        [1, 2, 3, 4, 5, 6],
    ]
    for i, p in enumerate(ps):
        t = _f(p, w)
        s.append(i) if t == 6 else (
            f.append(i) if t == 5 else (
                f_.append(i) if t == 4 else None
            )
        )
    return tuple(map(len, (s, f, f_)))


class Test(unittest.TestCase):

    f = (solve_naive, solve_intersection, solve_counter)

    def test_main(self):
        for f in self.f:
            self.assertEqual(main_test(f), (1, 2, 1))


if __name__ == "__main__":
    unittest.main()
