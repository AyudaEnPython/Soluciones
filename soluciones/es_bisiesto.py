"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Calcula si el año es bisiesto.
"""
import sys
import unittest


def es_bisiesto(year: int) -> bool:
    """Calcula si el año es bisiesto.

    :param year: Año a calcular.
    :year type: int
    :return: True si es bisiesto, False en caso contrario.
    :rtype: bool
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def main():
    """
    Muestra por la terminal si el año es bisiesto o no.

    Ejemplo:
        Windows::

            $ python es_bisiesto.py 1986

        macOs/Unix/Linux::

            $ python3 es_bisiesto.py 1986
    """
    if len(sys.argv) == 2:
        year = int(sys.argv[1])
        if es_bisiesto(year):
            print(f"{year} es un año bisiesto.")
        else:
            print(f"{year} no es un año bisiesto.")


class Test(unittest.TestCase):

    def test_es_bisiesto(self):
        self.assertTrue(es_bisiesto(2000))
        self.assertTrue(es_bisiesto(1996))
        self.assertTrue(es_bisiesto(2400))
        self.assertTrue(es_bisiesto(2496))

        self.assertFalse(es_bisiesto(1900))
        self.assertFalse(es_bisiesto(2100))
        self.assertFalse(es_bisiesto(1700))
        self.assertFalse(es_bisiesto(1800))


if __name__ == '__main__':
    # unittest.main() # uncomment/comment to run tests
    main()
