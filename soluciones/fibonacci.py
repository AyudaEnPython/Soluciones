"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

fibo_rn : Fibonacci recursivo (naive)
fibo_rc : Fibonacci recursivo (cache)
fibo_itr: Fiboanacci iterativo (range)
fibo_itw: Fiboanacci iterativo (while)
"""
from operator import imod
from unittest import main, TestCase


def fibo_rn(n: int):
    if n <=1:
        return n
    else:
        return fibo_rn(n-1) + fibo_rn(n-2)


def fibo_rc(n: int, cache: dict = {0:0, 1:1}):
    if n not in cache:
        cache[n] = fibo_rc(n-1, cache) + fibo_rc(n-2, cache)
    return cache[n]


def fibo_itr(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def fibo_itw(n: int) -> int:
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a+b
        i += 1
    return a


def fibo_gen(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


class Test(TestCase):
    
    funciones = (fibo_rn, fibo_rc, fibo_itr, fibo_itw)
    datos = (
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (11, 89),
        (12, 144),
        (13, 233),
        (23, 28657),
        (29, 514229),
    )

    def test_soluciones(self):
        for f in self.funciones:
            for posicion, resultado in self.datos:
                self.assertEqual(f(posicion), resultado)

    def test_fibo_gen(self):
        gen = fibo_gen(13)
        for i in range(13):
            self.assertEqual(next(gen), self.datos[i][1])


if __name__ == "__main__":
    main()
