"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Diseñar un programa que cuente la cantidad de dígitos que posee y a
partir de estos diga si pertenece a unidades, decenas o centenas
(debe ser con ciclos y enteros).
"""
from typing import Dict

table: Dict[int, str] = {
    1: "unidades", 2: "decenas", 3: "centenas",
    4: "unidades de millar", 5: "decenas de millar", 6: "centenas de millar",
}


def contar_digitos(n: int) -> int:
    n = abs(n)
    i = 0
    while n > 0:
        n //= 10
        i += 1
    return i  # oneliner: from math import log10; int(log10(n)) + 1


def sol(n: int) -> None:
    i = contar_digitos(n)
    print(f"El numero {n} tiene {contar_digitos(n)} digitos")
    for x in str(n):
        print(f"{x} {table[i]}")
        i -= 1


def main():
    n = int(input("Ingrese un numero: "))
    sol(n)


if __name__ == "__main__":
    main()
