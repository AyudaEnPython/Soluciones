"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
1. Hacer un programa en Python que capture N elementos de un arreglo,
    después lea un número a buscar en el arreglo y decir si se
    encuentra y la posición que está o no se encuentra.

2. Hacer un programa en Python que capture N elementos de un arreglo,
    después los imprima y me diga cuales son pares e impares.

3. Hacer un programa en Python que lea N elementos y los almacene en un
    arreglo, decir cuántos son positivos, negativos y nulos.

4. Hacer un programa en Python que lea N elementos y los almacene en un
    arreglo, cada elemento es una nota, decir cuántos aprobaron y
    cuantos perdieron.
    Nota: aprobaron es >= 3.0 y no aprobaron es < 3.0

5. Hacer un programa en Python que capture N elementos de un arreglo y
    me lo invierta, por ej a=[3,7,4,9]  el arreglo debe quedar así:
    a=[9,4,7,3]
# ---------------------------------------------------------------------
"""
from typing import Callable, List, Union


def datos(f: Callable) -> List[Union[int, float]]:
    v = []
    n = int(input("Cantidad de elementos: "))
    for _ in range(n):
        v.append(f(input("")))
    return v


def main_1():
    v = datos(int)
    x = int(input("Número a buscar: "))
    if x in v:
        print("Se encontró en la posición:", v.index(x))
    else:
        print("No se encontró")


def main_2():
    v = datos(int)
    print("Pares:", [x for x in v if x % 2 == 0])
    print("Impares:", [x for x in v if x % 2 != 0])


def main_3():
    v = datos(int)
    print("Positivos:", [x for x in v if x > 0])
    print("Negativos:", [x for x in v if x < 0])
    print("Nulos:", [x for x in v if x == 0])


def main_4():
    v = datos(float)
    print("Aprobaron:", [x for x in v if x >= 3.0])
    print("No aprobaron:", [x for x in v if x < 3.0])


def main_5():
    v = datos(int)
    print("Original:", v)
    print("Invertido:", v[::-1])


if __name__ == "__main__":
    main_1()  # comment/uncomment to run each exercise
    # main_2()
    # main_3()
    # main_4()
    # main_5()
