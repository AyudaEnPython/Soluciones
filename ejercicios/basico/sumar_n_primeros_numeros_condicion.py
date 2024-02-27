"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Progama una función que sume los 50 primeros elementos que sean
múltiplos de 3 o de 5.

NOTE: El enunciado no indica que 'los primeros 50 elementos' sean los primeros
    50 números (1, 2, 3, ...).
"""


def sumar(numeros: list) -> int:
    suma = 0
    i = 0
    for numero in numeros:
        if numero % 3 == 0 or numero % 5 == 0:
            suma += numero
            i += 1
        if i == 50:
            return suma
    return suma


def sumar_(xs: list, n: int = 50) -> int:
    return sum([x for x in xs if (x % 3 == 0 or x % 5 == 0)][:n])


if __name__ == "__main__":
    numeros = range(1, 109)
    assert sumar(numeros) == 2733
    assert sumar_(numeros) == 2733
    assert sumar(range(1, 8)) == 14
    assert sumar_(range(1, 8)) == 14
