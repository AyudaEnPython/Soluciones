"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Elaborar un algoritmo que lea los elementos de dos arreglos, cada uno
con 10 números enteros. Calcular los elementos de un tercer arreglo,
sumando los elementos correspondienes de los dos primeros, de la
siguiente manera: que se sume el elemento 1 del primer arreglo y el 1
del segundo y que el resultado se almacene en el 1 del tercero y así
sucesivamente. Además, se requiere que al final imprima los tres
arreglos de la siguiente forma:

#    Arreglo 1 + Arreglo 2 = Arreglo 3
#    ---------------------------------
#      99          99          999
#      99          99          999
#      99          99          999
"""
from random import randint
from typing import List

N = 10
MIN, MAX = 1, 49


def mostrar(x: List[int], y: List[int], z: List[int]) -> None:
    msg = "Arreglo 1 + Arreglo 2 = Arreglo 3\n"
    print(msg + "-" * len(msg))
    for i in range(N):
        print(f"{x[i]:>6}{y[i]:>12}{z[i]:>12}")


def main():
    p = [randint(MIN, MAX) for _ in range(N)]
    q = [randint(MIN, MAX) for _ in range(N)]
    r = [p[i] + q[i] for i in range(N)]
    mostrar(p, q, r)


if __name__ == "__main__":
    main()
