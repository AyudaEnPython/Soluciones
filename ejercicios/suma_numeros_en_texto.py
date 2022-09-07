"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ingresar un texto que contenga letras y números. Obtener la suma de
todos los números incluidos en el texto.

Ejemplo:

texto = "El 23 de mayo de 1973 se inauguró el edificio CPM, el cual" \
    " se encontraba en la calle Rawson al 1300"

Resultado: 23 + 1773 + 1300 = 3296
"""
import re
import unittest

REGEX = re.compile(r"[-+]?\d*\.?\d+|[-+]?\d+")


def solver(s: str) -> int:
    return sum(int(x) for x in s.split() if x.isdigit())


def regex_solver(s: str) -> int:
    return sum(float(x) for x in REGEX.findall(s))


def main_():
    s = input('Ingrese un texto: ')
    print(solver(s))


class Test(unittest.TestCase):

    data = (
        (
            "El 23 de mayo de 1973 se inauguró el edificio CPM, el cual"
            " se encontraba en la calle Rawson al 1300", 3296
        ),
        ("La última versión estable fue el 4 de octubre del 2021", 2025),
    )
    data_decimals = (
        ("Hoy es 11.33 de lo que sea 2021..", 2032.33),
        ("Un 10.5 en -20 +15 del test #3", 8.5),
        ("t3xT0#&_+A1I3n4d0..-1 *-2-0", 8),
    )

    def test_solver(self):
        for text, expected in self.data:
            self.assertEqual(solver(text), expected)

    def test_regex_solver(self):
        for text, expected in self.data_decimals:
            self.assertEqual(regex_solver(text), expected)


if __name__ == "__main__":
    # main()  # uncomment/comment to run tests
    main_()
