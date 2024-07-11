"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List
# pip install prototools
from prototools import tabulate, cyan, magenta


def tabla_de_multiplicar(n: int, c: int) -> List[List[str]]:
    return [
        [f"{i:>2} x {j:>2} = {j*i:^3}" for i in range(n, c+n)]
        for j in range(1, 11)
    ]


def show(n: int, c: int) -> None:
    t = tabla_de_multiplicar(n, c)
    print(tabulate(
        t, color=magenta, align="center",
        headers=[cyan(f"Tabla del {i}") for i in range(n, n+len(t[0]))],
    ))


def main():
    show(1, 5)
    show(6, 5)


if __name__ == "__main__":
    main()
