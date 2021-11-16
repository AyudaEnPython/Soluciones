"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Calcula si el año es bisiesto.
"""
from unittest import main, TestCase


def es_bisiesto(year: int) -> bool:
    """Calcula si el año es bisiesto.

    :param year: Año a calcular.
    :year type: int
    :return: True si es bisiesto, False en caso contrario.
    :rtype: bool
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


class Test(TestCase):

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
    main()