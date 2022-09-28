"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

La unidad de huevos cuesta S/. 0.4, la docena cuesta S/. 4.00 y la caja
de doce docenas cuesta S/. 40.00. Hacer un programa que maximice el
número de unidades compradas con un cheque bancario.
"""
from typing import Tuple
# pip install prototools
from prototools import float_input

f = lambda x, y, z, r: x*40 + y*4 + z*.4 + r  # noqa: E731


def maximizar(n: int) -> Tuple[int, int, int]:
    x, r = divmod(n, 40)
    y, r = divmod(r, 4)
    z, r = divmod(r, .4) 
    return x, y, z, r


def main():
    n = float_input("> ", gt=0)
    x, y, z, r = maximizar(n)
    assert f(x, y, z, r) == n
    print(f"Caja de doce docenas: {x}")
    print(f"Docenas: {y}")
    print(f"Unidades: {z}")
    print(f"Vuelto: {r:.2f}")


if __name__ == "__main__":
    main()
