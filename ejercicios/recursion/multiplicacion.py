"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

La multiplicación de dos números enteros positivos se puede realizar a
partir de sumas sucesivas:

a x b = a + a + ... + a

Si se quiere multiplicar 5 y 3:
5 x 3 = 5 + 5 + 5

Se puede expresar esta definición de manera recursiva de la siguiente
manera:

        +-----------------------------------------+
        |         ╭ b = 1    => a                 |
        | a x b  -┤                               |
        |         ╰ n >= 2   => a + (a x (b - 1)) |
        +-----------------------------------------+

Desarrolle una función que implemente la multiplicación recursiva.
"""
from unittest import main, TestCase


def multiplicar(a: int, b: int) -> int:
    if b == 1:
        return a
    else:
        return a + multiplicar(a, b-1)


def multiplicar_(a: int, b: int) -> int:
    if b == 0:
        return 0
    else:
        return a + multiplicar(a, b-1)


class Test(TestCase):

    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(4, 5), 20)
        self.assertEqual(multiplicar(5, 6), 30)

    def test_multiplicar_(self):
        self.assertEqual(multiplicar_(2, 3), 6)
        self.assertEqual(multiplicar_(3, 4), 12)
        self.assertEqual(multiplicar_(4, 5), 20)
        self.assertEqual(multiplicar_(5, 6), 30)


if __name__ == '__main__':
    main()
