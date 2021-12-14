"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrolla un código que comience con una lista de diez “0” (lista =
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) y que pida dos números N y M. Si N está
entre 1 y 10, se deberá poner el número M en la posición N
correspondiente. Si N es 0, se le sumará el número M a todas las celdas
(es decir, todos los elementos sumarán M a sus valores). Si N es -1 y
el número M es mayor o igual a 0, se deberá mostrar la cantidad de
veces que está ese número en la lista. El programa terminará solo
cuando N y M sean ambos -1.

NOTE: El enunciado no es claro. Se decide imprimir la lista en cada
    condición.
"""
# pip install prototools
from prototools import int_input


def main():
    v = [0]*10
    while True:
        n = int_input("N: ")
        m = int_input("M: ")
        if n == -1 and m == -1:
            print(v)
            break
        if n == 0:
            v = [m + i for i in v]
            print(v)
        elif n > 0 and n <= 10:
            v[n - 1] = m
            print(v)
        elif n == -1 and m >= 0:
            print(v)
            print(v.count(m))


if __name__ == "__main__":
    main()