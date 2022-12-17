"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que muestre un menú que contenga:
1. Números primos
2. Números compuestos
3. Salir.

Controlar que solo se pueda elegir una de las opciones.
Solicite el ingreso de 2 números enteros que sean: límite inferior y
límite superior, entre ellos debe haber al menos 10.
Al finalizar el programa debe mostrar de acuerdo a lo elegido en el
menú, la lista de números primos o números comprendidos entre los
límites.
"""
from random import sample
# pip install prototools
from prototools import Menu, int_input
from typing import Iterable, List

N = 10


def es_primo_(n: int) -> bool:
    if 1 < n < 4:
        return True
    elif n < 2 or not n % 2:
        return False
    impares: Iterable = range(3, int((n**0.5) + 1), 2)
    return not any(not n % i for i in impares)


def ingresar_límites(limites: List[int]) -> List[int]:
    min_ = int_input("Límite inferior: ", min=0)
    max_ = int_input("Límite superior: ", min=min_+ N)
    limites.pop()
    return limites.append(sample(range(min_, max_+1), k=N))


def _primos(xs: List[int]) -> None:
    print(*[x for x in sorted(xs[-1]) if es_primo_(x)], sep=", ")


def _compuestos(xs: List[int]) -> None:
    print(*[x for x in sorted(xs[-1]) if not es_primo_(x)], sep=", ")


def main():
    xs = [None]
    menu = Menu()
    menu.add_options(
        ("Ingresar límites", lambda: ingresar_límites(xs)),
        ("Números primos", lambda: _primos(xs)),
        ("Números compuestos", lambda: _compuestos(xs)),
    )
    menu.run()


if __name__ == "__main__":
    main()
