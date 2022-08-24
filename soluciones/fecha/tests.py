"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest
from utils import dia_mes, es_fecha, comparar, _escribir


class Test(unittest.TestCase):

    def test_dia_mes(self):
        self.assertEqual(dia_mes(2, 2021), 28)
        self.assertEqual(dia_mes(2, 2022), 28)
        self.assertEqual(dia_mes(2, 2023), 28)
        self.assertEqual(dia_mes(2, 2020), 29)
        self.assertEqual(dia_mes(2, 2024), 29)
        self.assertEqual(dia_mes(2, 2028), 29)

    def test_es_fecha(self):
        self.assertEqual(es_fecha(10082021), True)
        self.assertEqual(es_fecha(23082022), True)
        self.assertEqual(es_fecha(5082022), True)
        self.assertEqual(es_fecha(31092021), False)
        self.assertEqual(es_fecha(592021), False)
        self.assertEqual(es_fecha(1), False)

    def test_comparar(self):
        self.assertEqual(comparar(10082021, 10082021), 0)
        self.assertEqual(comparar(10082021, 31072021), 1)
        self.assertEqual(comparar(31072021, 10082021), -1)
        self.assertEqual(comparar(1012022, 1012022), 0)
        self.assertEqual(comparar(1012022, 2012022), -1)
        self.assertEqual(comparar(2012022, 1012022), 1)

    def test_escribir(self):
        self.assertEqual(_escribir(1032007), "1 marzo 2007")
        self.assertEqual(_escribir(29022024), "29 febrero 2024")
        self.assertEqual(_escribir(28022022), "28 febrero 2022")
        self.assertEqual(_escribir(31072019), "31 julio 2019")
        self.assertEqual(_escribir(30042015), "30 abril 2015")
        self.assertEqual(_escribir(15092025), "15 setiembre 2025")


if __name__ == "__main__":
    unittest.main()
