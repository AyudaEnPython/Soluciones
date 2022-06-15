"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List

MAX: int = 140


def es_multiplo_7(n: int) -> bool:
    while True:
        n_, u = divmod(n, 10)
        n_ -= 2*u
        if n_ > MAX:
            n = n_
            continue
        else:
            break
    if n_ % 7 == 0:
        return True
    else:
        return False


def get_data() -> List[int]:
    numeros = []
    n = int(input("Cantidad de números a verificiar: "))
    for i in range(n):
        numeros.append(int(input(f"[{i+1}] Ingrese un número: ")))
    return numeros
