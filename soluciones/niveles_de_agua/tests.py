"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from main import niveles, promedio_int, fuera_de_rango


class Test(unittest.TestCase):

    cases = (
        (list(range(1, 7)), 3, [3, 4, 5]),
        (list(range(3, 6)), 4, [2]),
        (list(range(5, 8)), 6, [2])
    )

    def test_niveles(self):
        self.assertEqual(len(niveles(1)), 1)
        self.assertEqual(len(niveles(150)), 150)
        self.assertEqual(len(niveles(365)), 365)

    def test_promedio_int(self):
        self.assertEqual(promedio_int([1, 2]), 1)
        self.assertEqual(promedio_int([1, 2, 3, 4, 5]), 3)
        self.assertEqual(promedio_int([1, 2, 3, 4, 5, 6]), 3)

    def test_fuera_de_rango(self):
        self.assertEqual(fuera_de_rango([1, 2, 3, 4, 5], 3), [3, 4])
        self.assertEqual(fuera_de_rango([1, 2, 3, 4, 5, 6], 3), [3, 4, 5])
        self.assertEqual(fuera_de_rango([1, 2, 3, 4, 5], 2), [2, 3, 4])

    def test_main(self):
        for days, mean_, expected in self.cases:
            self.assertEqual(promedio_int(days), mean_)
            self.assertEqual(fuera_de_rango(days, mean_), expected)


if __name__ == "__main__":
    unittest.main()
