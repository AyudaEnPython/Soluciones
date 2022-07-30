"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Devuelva una lista con el tamaño ingresado por teclado, y llena con las
letras del alfabeto.
Por ejemplo si se ingresa 5 debe devolver una lista = [a, b, c, d, e]
"""
from string import ascii_lowercase as abc
from typing import List


def sol(n: int) -> List[str]:
    return [abc[i] for i in range(n)]


def main():
    n = int(input("Ingrese el tamaño de la lista: "))
    print(sol(n))


if __name__ == "__main__":
    main()
