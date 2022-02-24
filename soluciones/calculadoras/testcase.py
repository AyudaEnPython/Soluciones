"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

from unittest import main, TestCase

from main import op, f
from operadores import suma, resta, multiplicacion, division


class Test(TestCase):

    f = (suma, resta, multiplicacion, division)

    def test_operadores(self):
        self.assertDictEqual(
            {k:v for k, v in zip("+-*/", self.f)}, op
        )
        for operador in "+-*/":
            self.assertIn(operador, op)

    def test_dividendo_cero(self):
        with self.assertRaises(ZeroDivisionError):
            f("1/0")
        with self.assertRaises(ZeroDivisionError):
            f("15*3/0")
        with self.assertRaises(ZeroDivisionError):
            f("20-30/0")

    def test_f(self):
        self.assertEqual(f("1/3"), 0.3333333333333333)
        self.assertEqual(f("1"), 1)
        self.assertEqual(f("2*15+30-20"), 40)
        self.assertEqual(f("1-2+3-4+5-6"), -3)
        self.assertEqual(f("2+3"), 5)
        self.assertEqual(f("2+3*4"), 14)
        self.assertEqual(f("1/2"), 0.5)
        self.assertEqual(f("100-60/6"), 90)
        self.assertEqual(f("a1-2"), "Error")
        self.assertEqual(f(">run 1-2"), "Error")


if __name__ == "__main__":
    main()