"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Creá un programa que pida introducir un número y un modo. Los modos
serán “par” o “impar”. Luego se imprimirán todos los números pares o 
mpares (según corresponda) desde 0 hasta el número introducido.
"""
from random import randint
from typing import List
# pip install prototools
from prototools import choice_input, int_input


def f(n: int, m: str) -> List[int]:
    return [x*2 if m == "par" else (x*2) - 1 for x in range(1, n//2 + 1)]

n = int_input("n: ", lang="es")
modos = ("par", "impar")
modo = choice_input(modos, lang="es")
print(f(n, modo))