"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# UNCards

En las universidades de Colombia se ha creado un juego, donde dos
equipos se enfrentan utilizando un conjunto de caracteres, para
determinar el ganador en cada turno se hace a través del peso (el
código ASCII) de cada uno de los caracteres.

En la final del torneo para este juego se esta enfrentando la
Universidad Nacional de Colombia y la Universidad de los Andes, tu
debes desarrollar un programa que ayude a decidir que equipo va
ganando en cada uno de los turnos:

## Reglas

1. Ambos equipos arrancan con 0 puntos.
2. Los puntos se van acumulando en cada turno.
3. El ganador de cada turno es el que más puntaje lleve acumulado hasta
    el momento.
4. Un equipo obtiene un punto si un carácter elegido en el turno `i` es
    mayor al de su oponente.
5. Si la Universidad Nacional de Colombia va ganando se debe usar la U,
    si los Andes va ganando se debe usar A y si hay empate se debe usar
    la D.

Cada equipo puede formar una secuenci de caracteres de los siguientes
caracteres validos para la final:
k V + * @ a A Z 1 P [ ] C o l e r

## Ejemplos

Se recibirá dos entradas, la primera corresponde a los caracteres
usados por la Universidad Nacional de Colombia y la segunda por los
caracteres usados por la Universidad de los Andes en cada turno, la
salida debe ser una cadena de caracteres indicando que equipo va
ganando en cada turno.

    +--------+-------+
    |Entrada |Salida |
    +--------+-------+
    | P1[@]  | UDUDA |  
    | CZ*[ol |       |
    +--------+-------+
    | ro1    | UUU   |
    | ]cP    |       |
    +--------+-------+
"""
import unittest
from typing import Dict, Tuple

VALID = "kV+*@aAZ1P[]Coler"
DEFAULTS = "U", "A", "D"


def _load_players(default_: Tuple[str, str]) -> Dict[str, int]:
    return {name: 0 for name in default_}


def validate(input_: str, valid: str = VALID) -> str:
    if not all(c in valid for c in input_):
        raise ValueError("Invalid characters") # return "!"*len(input_)
    return input_


def sol(xs: str, ys: str, d: Tuple[Tuple[str, str], str] = DEFAULTS) -> str:
    (a, b, t), p, s = d, _load_players(d[:-1]), ""
    for x, y in zip(xs, ys):
        if ord(x) > ord(y):
            p[a] += 1
        elif ord(x) < ord(y):
            p[b] += 1
        if p[a] > p[b]:
            s += a
        elif p[a] < p[b]:
            s += b
        else:
            s += t
    return s


def main():
    U = validate(input())
    A = validate(input())
    print(sol(U, A))


class Test(unittest.TestCase):

    def test_validate(self):
        self.assertEqual(validate("P1[@]CZ*[ol"), "P1[@]CZ*[ol")
        with self.assertRaises(ValueError):
            validate("P1[@]CZ*[ol_")

    def test_validate_other(self):
        valid = "<=?Ad@[^"
        self.assertEqual(validate("?=A^", valid), "?=A^")
        with self.assertRaises(ValueError):
            validate("?=A^$_", valid)

    def test_sol(self):
        self.assertEqual(sol("P1[@]", "CZ*[ol"), "UDUDA")
        self.assertEqual(sol("ro1", "]cP"), "UUU")

    def test_sol_defaults(self):
        defaults = "X", "Y", "E"
        self.assertEqual(sol("P1[@]", "CZ*[ol", defaults), "XEXEY")
        self.assertEqual(sol("ro1", "]cP", defaults), "XXX")


if __name__ == "__main__":
    # unittest.main()
    main()
