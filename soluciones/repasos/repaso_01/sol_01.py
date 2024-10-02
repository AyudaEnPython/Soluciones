import unittest
from random import choice, randint


def generar_cadena_adn() -> str:
    return "".join(choice("ACGT") for _ in range(randint(6, 22)))


def pares_ordenados(cadena: str) -> int:
    return sum(True for i in range(len(cadena) - 1) if cadena[i] <= cadena[i+1])


def combinar_cadenas(a: str, b: str, idx: int) -> str:
    return a[:idx] + b + a[idx:]


class TestFunctions(unittest.TestCase):

    def test_generar_cadena_adn(self) -> None:
        cadena = generar_cadena_adn()
        self.assertIsInstance(cadena, str)
        self.assertTrue(all(c in "ACGT" for c in cadena))

    def test_pares_ordenados(self) -> None:
        self.assertEqual(pares_ordenados("AAAGTTA"), 5)
        self.assertEqual(pares_ordenados("TTGTATATG"), 4)
    
    def test_combinar_cadenas(self) -> None:
        a = "AAATTGACCA"
        b = "CATCTAAGCA"
        self.assertEqual(
            combinar_cadenas(a, b, 3),
            "AAACATCTAAGCATTGACCA",
        )


if __name__ == "__main__":
    unittest.main()
