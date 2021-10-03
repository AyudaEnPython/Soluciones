"""
fibo_rn : Fibonacci recursivo (naive)
fibo_rc : Fibonacci recursivo (cache)
fibo_itr: Fiboanacci iterativo (range)
fibo_itw: Fiboanacci iterativo (while)
"""
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


class Test(TestCase):
    
    funciones = (fibo_rn, fibo_rc, fibo_itr, fibo_itw)
    datos = (
        (0, 0),
        (1, 1),
        (7, 13),
        (8, 21),
        (13, 233),
        (23, 28657),
        (29, 514229),
    )

    def test_soluciones(self):
        for f in self.funciones:
            for posicion, resultado in self.datos:
                self.assertEqual(f(posicion), resultado)


if __name__ == "__main__":
    main()