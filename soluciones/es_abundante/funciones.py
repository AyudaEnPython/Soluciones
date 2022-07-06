"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List


def mcd(a: int, b: int):
    for x in range(min(a, b), 0, -1):
        if a % x == 0 and b % x == 0:
            return x
    return 1


def factores(n: int) -> List[int]:
    return [x for x in range(1, n) if n % x == 0]


def es_abundante(n: int) -> bool:
    return sum(factores(n)) > n
