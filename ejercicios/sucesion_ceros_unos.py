"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que lea por teclado un número entero N, y generar
la siguiente sucesión para los primeros N términos:
0, 1, 00, 11, 000, 111, 0000, 1111, ...

NOTE: el enunciado no es muy específico.
"""
# pip install prototools
from prototools import int_input

# naive
# N = 7
# print(", ".join([f"{'0'*i}, {'1'*i}" for i in range(1, N+1)]))


def sucesion(n: int) -> str:
    """
    >>> sucesion(5)
    '0, 1, 00, 11, 000'
    """
    ns = []
    j = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            j += 1
            s = "0" * j
            ns.append(s)
        else:
            ns.append(s.replace("0", "1"))
    return ", ".join(ns)


def main():
    n = int_input("n: ", min=1, lang="es")
    print(sucesion(n))


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    main()
