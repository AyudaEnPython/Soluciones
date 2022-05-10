"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crear una función contar_vocales() que reciba una palabra y cuente
cuántas letras "a" tiene, cuantas letras "e" tiene y así hasta
completar todas las vocales. Se puede hacer que el usuario sea quien
elija la palabra.
"""
import io
from collections import Counter
from textwrap import dedent
from typing import Dict
from unittest import main, TestCase
from unittest.mock import patch


def naive_contar_vocales(s: str) -> None:
    a = e = i = o = u = 0
    for letra in s.lower():
        if letra == "a":
            a += 1
        elif letra == "e":
            e += 1
        elif letra == "i":
            i += 1
        elif letra == "o":
            o += 1
        elif letra == "u":
            u += 1
    print(f"Vocal a: {a} veces")
    print(f"Vocal e: {e} veces")
    print(f"Vocal i: {i} veces")
    print(f"Vocal o: {o} veces")
    print(f"Vocal u: {u} veces")


def contar_vocales(s: str) -> Dict[str, int]:
    vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    for letra in s.lower():
        if letra in vocales:
            vocales[letra] += 1
    return vocales


def contar_vocales_count(s: str) -> Dict[str, int]:
    vocales = {}
    for vocal in "aeiou":
        vocales[vocal] = s.lower().count(vocal)
    return vocales


def contar_vocales_dc(s: str) -> Dict[str, int]:
    return {vocal: s.lower().count(vocal) for vocal in "aeiou"}


def contar_vocales_Counter(s: str) -> Dict[str, int]:
    return dict(Counter(c for c in s.lower() if c in "aeoiu"))


def user_inpur() -> str:
    return input("Ingrese una palabra: ")


def main_():
    resultado: Dict[str, int] = contar_vocales(user_inpur())
    for k, v in resultado.items():
        print(f"Vocal {k}: {v} veces")


class Test(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    def assert_stdout(self, expected_output, mock_output, function=None):
        if function:
            function()
        self.assertEqual(mock_output.getvalue(), expected_output)

    def test_naive_contar_vocales(self):
        self.assert_stdout(
            dedent(
                """\
                Vocal a: 2 veces
                Vocal e: 2 veces
                Vocal i: 1 veces
                Vocal o: 2 veces
                Vocal u: 1 veces
                """
            ),
            function=lambda: naive_contar_vocales("sexagesimocuarto"),
        )

    def test_contar_vocales(self):
        self.assertEqual(
            contar_vocales("sexagesimocuarto"),
            {"a": 2, "e": 2, "i": 1, "o": 2, "u": 1},
        )
        self.assertEqual(
            contar_vocales("hola mundo"),
            {"a": 1, "e": 0, "i": 0, "o": 2, "u": 1},
        )

    def test_contar_vocales_count(self):
        self.assertEqual(
            contar_vocales_count("sexagesimocuarto"),
            {"a": 2, "e": 2, "i": 1, "o": 2, "u": 1},
        )
        self.assertEqual(
            contar_vocales_count("hola mundo"),
            {"a": 1, "e": 0, "i": 0, "o": 2, "u": 1},
        )

    def test_contar_vocales_dc(self):
        self.assertEqual(
            contar_vocales_dc("sexagesimocuarto"),
            {"a": 2, "e": 2, "i": 1, "o": 2, "u": 1},
        )
        self.assertEqual(
            contar_vocales_dc("hola mundo"),
            {"a": 1, "e": 0, "i": 0, "o": 2, "u": 1},
        )

    def test_contar_vocales_Counter(self):
        self.assertEqual(
            contar_vocales_Counter("sexagesimocuarto"),
            {"a": 2, "e": 2, "i": 1, "o": 2, "u": 1},
        )
        self.assertEqual(
            contar_vocales_Counter("hola mundo"),
            {"a": 1, "o": 2, "u": 1},
        )


if __name__ == "__main__":
    main() # uncomment and comment the next line to run tests
    #main_()