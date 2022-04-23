"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Cifrar los dígitos de las contraseñas de un banco (4 números) entrados
por teclado, utilizando el siguiente criterio: el primero se envía de
último, el segundo, de penúltimo y así sucesivamente. Mostrar ambos
vectores.

Clave inicial
+-----+-----+-----+-----+
|  8  |  4  |  9  |  5  |
+-----+-----+-----+-----+

Clave final
+-----+-----+-----+-----+
|  5  |  9  |  4  |  8  |
+-----+-----+-----+-----+
"""
from typing import List
# pip install prototools
from prototools import show_matrix, int_input

Vector = List[float]
SIZE = 4


def cifrar_naive(clave):
    tmp = []
    for i in range(len(clave)):
        tmp.append(clave[-(i+1)])
    return tmp


def cifrar(clave: Vector) -> Vector:
    return clave[::-1]


def cifrar_alt1(clave: Vector) -> Vector:
    return [clave[-(i+1)] for i in range(len(clave))]


def cifrar_alt2(clave: Vector) -> Vector:
    return list(reversed(clave))


def main():
    print("Ingresar contraseña")
    inicial = [int_input(f"Posicion [{i}] -> ") for i in range(SIZE)]
    final = cifrar(inicial)
    # final = cifrar_alt1(inicial)
    # final = cifrar_alt2(inicial)
    # final = cifrar_naive(inicial)
    print("Clave inicial")
    show_matrix(inicial)
    print("Clave final")
    show_matrix(final)


if __name__ == "__main__":
    main()
