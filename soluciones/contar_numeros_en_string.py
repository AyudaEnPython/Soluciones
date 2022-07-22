"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Contar la cantidad de números presente en una cadena de texto.

Ejemplo:
    'hola2mundo3' -> 2
    'hola23mundo356' -> 5
"""
import re
import unittest


def count_ss(s: str) -> int:
    return sum(map(str.isdigit, s))


def count_s(s: str) -> int:
    return len(re.findall(r'\d', s))


def count_a(s: str) -> int:
    return len([c for c in s if c.isdigit()])


def count_b(s: str) -> int:
    i = 0
    for c in s:
        if c.isdigit():
            i += 1
    return i


class Test(unittest.TestCase):

    def test_mixletternumbers(self):
        self.assertEqual(count_ss("hola2mu444n43do3"), 7)
        self.assertEqual(count_s("hola2mu444n43do3"), 7)
        self.assertEqual(count_a("hola2mu444n43do3"), 7)
        self.assertEqual(count_b("hola2mu444n43do3"), 7)

    def test_blank_space(self):
        self.assertEqual(count_ss(" 39n 3.&"), 3)
        self.assertEqual(count_s(" 39n 3.&"), 3)
        self.assertEqual(count_a(" 39n 3.&"), 3)
        self.assertEqual(count_b(" 39n 3.&"), 3)

    def test_no_digits(self):
        self.assertEqual(count_ss("a"), 0)
        self.assertEqual(count_s("a"), 0)
        self.assertEqual(count_a("a"), 0)
        self.assertEqual(count_b("a"), 0)


if __name__ == "__main__":
    unittest.main()
