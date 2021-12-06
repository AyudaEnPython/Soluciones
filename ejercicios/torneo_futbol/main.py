"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

En un torneo de fútbol participan K equipos . El torneo se juega con el
sistema de todos contra todos. Por cada partido disputado de dispone de
la siguiente información.
    A: numero de equipo
    B: código del resultado (P:perdido , E:empatado, G:ganado)

Se arma un lote de datos con todos los resultados del torneo agrupados
por nro de equipo. Desarrollar un programa que imprima:
    1. Por cada equipo su número y el puntaje total que obtuvo (suma 3
        si gana 1 si empata).
    2. Nro de equipo que totalizó con menor cantidad de puntos (hay
        solo uno).

---
NOTE: Los partidos ganados deben de ser igual a la cantidad de partidos
    perdidos y ambas cantidades sumadas deber ser igual a k(k-1):
    G + P + E = k(k-1) -> E = k(k-1) - (G + P)

TODO: add alternative main to read txt file.
"""
import random
from typing import Any, Callable, List
from unittest import main, TestCase
from unittest.mock import patch


def _generate_data(teams: int, states="GPE", min_: int = 0) -> str:
    """Generate random game results and validate it. Wins must equal
    losses and their sum plus the number of ties must equal the total
    number of games played.
    
    T = k(k-1) - (W + L)

    :param teams: Number of teams
    :type teams: int
    :return: Result of tournament
    :rtype: str

    ..todo:: refactor and implement a better match result.
    """
    t = teams * (teams-1)
    w = random.randint(min_, t/2+1)
    gs = list(map(lambda x, y: x*y, (w, w, t - 2*w), states))
    gs = [i for j in gs for i in j]
    random.shuffle(gs)
    pos_t, res = list(range(1, teams+1)), ""
    for pos in pos_t:
        for _ in range(teams-1):
            res += str(pos) + gs.pop() + " "
    return res[:-1]


def read_data(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return f.read().replace("\n", " ")


def data_from_gen_func(size: int = 4) -> List[str]:
    return _generate_data(size).split(" ")


def data_from_str(data: str) -> List[str]:
    return data.split(" ")


# filename="resultados.txt" if executed from torneo_futbol/main.py
def data_from_txt(filename="ejercicios/torneo_futbol/resultados.txt"):
    return read_data(filename).split(" ")


def main_input() -> str:
    min_, res, k = float("inf"), "", int(input("k: "))
    for i in range(k):
        p = 0
        for _ in range(k-1):
            r = input(f"{i+1}> ").upper()
            p += 3 if r[-1] == "G" else (1 if r[-1] == "E" else 0)
        (min_, t) = (p, i+1) if p < min_ else (min_, t)
        res += f"{i+1} -> {p}\n"
    res += f"{t}"
    return res


def main_alt(f: Callable, args: Any = None) -> str:
    min_, res, rs = float("inf"), "", f() if args is None else f(args)
    k = int(abs((-1 -((4*len(rs))**0.5))//2))
    rs = [rs[i:i+(k-1)] for i in range(0, len(rs), k-1)]
    print(rs)
    for i in range(k):
        p = 0
        for r in rs[i]:
            p += 3 if r[-1] == "G" else (1 if r[-1] == "E" else 0)
        (min_, t) = (p, r[0]) if p < min_ else (min_, t)
        res += f"{r[0]} -> {p}\n"
    res += f"{t[0]}"
    return res


class Test(TestCase):

    inputs = ("4", "g", "g", "e", "g", "e", "p", "g", "p", "p", "e", "e", "p")
    data = "1G 1G 1E 2G 2E 2P 3G 3P 3P 4E 4E 4P"
    result = "1 -> 7\n2 -> 4\n3 -> 3\n4 -> 2\n4"

    @patch("builtins.input", side_effect=inputs)
    def test_main_input(self, mocked_input):
        response = main_input()
        self.assertEqual(response, self.result)

    def test_main_alt(self):
        self.assertEqual(main_alt(data_from_txt), self.result)
        self.assertEqual(main_alt(data_from_str, self.data), self.result)


if __name__ == "__main__":
    main()