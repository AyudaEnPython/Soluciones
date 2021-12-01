"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Realizar el siguiente Menú:

1. Hacer una función que dado un vector de números enteros determine
    cuantos números son pares.
2. Hacer una función que determine cuál es el mayor de los datos de un
    vector.
3. Hacer una función que dado dos vectores del mismo tamaño retorne un
    vector con la suma de los dos vectores recibidos como parámetros.
4. Hacer las funciones necesarias que resuelva lo siguiente:
        Que se generen 2 vectores de forma aleatoria con valores entre
        el 1 y 15, del primer vector se genere otro vector con los
        números factoriales y del segundo vector se genere otro vector
        con las potencias, finalmente se muestren todos los vectores y
        la suma de los vectores de factoriales + el vector de las
        potencias.
# ---------------------------------------------------------------------
NOTE: El enunciado original no esta bien redactado. No hay indicaciones
    claras sobre el 'menú', solo pide realizar funciones cuando en
    realidad no son necesarias.
"""
from random import randint
from typing import Dict, List
# pip install prototools
from prototools import Menu


def _factorial(n: int, d: Dict[int, int] = {0:1}) -> int:
    if n not in d:
        d[n] = n * _factorial(n - 1, d)
    return d[n]


def pares(v: List[int]) -> int:
    return len([x for x in v if x % 2 == 0])


def mayor(v: List[int]) -> int:
    return max(v)


def suma(v1: List[int], v2: List[int]) -> List[int]:
    return [x + y for x, y in zip(v1, v2)]


def factorial(v: List[int]) -> List[int]:
    return list(map(_factorial, v))


def potencia(v: List[int]) -> List[int]:
    return [x ** 2 for x in v]


def aleatorio(min: int = 1, max: int = 15, size: int =10) -> List[int]:
    return [randint(min, max) for _ in range(size)]


def f1():
    v1 = aleatorio()
    print(f'Vector: {v1}')
    print(f'Cantidad de pares: {pares(v1)}')


def f2():
    v1 = aleatorio()
    print(f'Vector: {v1}')
    print(f'Número mayor: {mayor(v1)}')


def f3():
    v1 = aleatorio()
    v2 = aleatorio()
    print(f'Vector 1: {v1}')
    print(f'Vector 2: {v2}')
    print(f'Suma de vectores: {suma(v1, v2)}')


def f4():
    v1 = aleatorio()
    v2 = aleatorio()
    v3 = factorial(v1)
    v4 = potencia(v2)
    print(f'Vector 1: {v1}')
    print(f'Vector 2: {v2}')
    print(f'Vector 3: {v3}')
    print(f'Vector 4: {v4}')
    print(f'Suma de vectores: {suma(v3, v4)}')


def main():
    menu = Menu()
    menu.add_options(
        ("Pares", f1),
        ("Mayor", f2),
        ("Suma", f3),
        ("Factorial, Pontecia, Suma", f4),
    )
    menu.run()


if __name__ == '__main__':
    main()