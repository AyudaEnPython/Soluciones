"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from decimal import Decimal, getcontext
from typing import Tuple


def read_input() -> Tuple[int, list]:
    data = []
    with open("input.txt", "r") as f:
        for line in f:
            data.append(int(line))
    return data[0], data[1:]


# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/es_primo.py
def es_primo(n: int) -> bool:
    """Determina si un número es primo.

    :param n: número a evaluar.
    :n type: int
    :return: True si es primo, False en caso contrario.
    :rtype: bool
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def solver(n: int) -> None:
    getcontext().prec = 40
    if not es_primo(n):
        print(f"{n}: -1")
    else:
        n_ = f"{Decimal(1)/Decimal(n):.40f}"
        print(f"{n}:", " ".join(n_[2:]))


def main():
    n, data = read_input()
    for x in range(n):
        solver(data[x])


if __name__ == "__main__":
    main()
