"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Evaluar la siguiente función con un código que tome como valor inicial
de “n” un valor dado por el usuario (recursividad)

Si n>=3 muestre el resultado de F(13)
F(n)= 3F(n-2) - 2F(n-1)
F(1)= 3
F(2)= 1
"""
from unittest import main, TestCase

def f(n):
    if n == 1:
        return 3
    elif n == 2:
        return 1
    else:
        return 3*f(n-2) - 2*f(n-1)


class Test(TestCase):

    def test_f(self):
        self.assertEqual(f(3), 7)
        self.assertEqual(f(5), 43)
        self.assertEqual(f(8), -1091)
        self.assertEqual(f(13), 265723)


if __name__ == "__main__":
    main()