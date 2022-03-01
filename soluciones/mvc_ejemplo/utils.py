"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
from typing import List

Aleatorios = List[int]
MIN, MAX = 0, 100


def aleatorios(size: int = 10, min: int = 0, max: int = 20) -> Aleatorios:
    return [randint(min, max) for _ in range(size)]
