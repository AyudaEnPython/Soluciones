"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Creá un programa que pida introducir un número y un modo. Los modos
serán “par” o “impar”. Luego se imprimirán todos los números pares o
impares (según corresponda) desde 0 hasta el número introducido.
"""
from typing import List
# pip install prototools
from prototools import choice_input, int_input


def f(n: int, m: str) -> List[int]:
    """Devuelve una lista con los números pares o impares
    según corresponda.

    :param n: Número
    :n type: int
    :param m: Modo, par o impar.
    :m type: str
    :return: Lista de números pares o impares (dependiendo del modo)
    :rtype: List[int]
    >>> f(7, "par")
    [2, 4, 6]
    """
    return [x*2 if m == "par" else (x*2) - 1 for x in range(1, n//2 + 1)]


def main():
    print(f(
        int_input("n: ", lang="es"),
        choice_input(("par", "impar"), lang="es"),
    ))


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    main()
