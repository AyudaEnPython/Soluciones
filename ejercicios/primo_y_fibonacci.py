"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Primo y Fibonacci. Los números Fibonacci tienen la siguiente secuencia
0, 1, 1, 2, 3, 5, 8, 13 y así sucesivamente. Realizar un programa que
permita imprimir el n-ésimo término primo de la serie de Fibonacci.
Imprima en la salida un número por cada caso de entrada.

Ejemplo de entrada
1
2
3
4

Ejemplo de salida
2
3
5
13
"""
from math import sqrt
from typing import Iterable

from prototools import int_input, time_functions


# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/fibonacci.py
def fibo_gen(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/fibonacci.py
def fibo_itw(n: int) -> int:
    a, b = 0, 1
    i = 0
    while i < n:
        a, b = b, a+b
        i += 1
    return a


# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/es_primo.py
def es_primo(n: int) -> bool:
    if 1 < n < 4:
        return True
    elif n < 2 or not n % 2:
        return False
    impares: Iterable = range(3, int(sqrt(n) + 1), 2)
    return not any(not n % i for i in impares)


def f(n: int) -> int:
    i = j = k = r = 0
    while j != n:
        i += 1
        k = fibo_itw(i)
        if es_primo(k):
            j += 1
            r = k
    return r


def g(n: int) -> int:
    j = 0
    for i in fibo_gen(n**2):
        if es_primo(i):
            j += 1
        if j == n:
            return i


def main():
    n = int_input(min=0, lang="es")
    print(f(n))
    # print(g(n))


if __name__ == "__main__":
    # main()
    fs = {"f": f, "g": g}
    time_functions(fs, args=(5), globals=globals())
    # 'f' took 10.6349 secs
    # 'g' took 7.1475 secs
