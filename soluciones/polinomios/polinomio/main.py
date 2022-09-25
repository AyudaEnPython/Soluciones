"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List
# pip install prototools
from prototools import int_input, float_input


def f(grado: int, coeficientes: List[int], x: float) -> float:
    """Calcula el valor de un polinomio de grado n

    :param grado: grado del polinomio
    :grado type: int
    :param coeficientes: coeficientes del polinomio
    :coeficientes type: List[int]
    :param x: valor de x
    :x type: float
    :return: valor del polinomio
    :rtype: float
    """
    return sum(coeficientes[i] * x**i for i in range(grado + 1))


def main():
    grado = int_input("Ingrese el grado del polinomio: ")
    coeficientes = []
    for i in range(grado + 1):
        coeficientes.append(float_input(f"Ingrese el coeficiente de x^{i}: "))
    x = float_input("Ingrese el valor de x: ")
    print(f"El valor del polinomio es: {f(grado, coeficientes, x)}")


if __name__ == "__main__":
    main()
