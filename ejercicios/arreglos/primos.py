"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Devuelva una lista con el tamaño ingresado por teclado, y llena de
números primos. Por ejemplo si se ingresa 5 debe devolver una
lista = [1, 2, 3, 5, 7]
"""
from typing import List


def es_primo(n: int) -> bool:
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def sol(n: int) -> List[int]:
    i = j = 0
    result = []
    while j < n:
        if es_primo(i):
            j += 1
            result.append(i)
        i += 1
    return result


def main():
    n = int(input("Ingrese el tamaño de la lista: "))
    print(sol(n))


if __name__ == "__main__":
    main()
