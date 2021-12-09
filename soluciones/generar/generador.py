"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: Se opta por cambiar los nombres propuestos por el enunciado.
"""
from math import ceil, floor
from random import uniform
from typing import List


def ingresar_numero(min_: int, max_: int, indicacion: str) -> int:
    """Pide un numero y lo devuelve.

    :param min_: numero minimo
    :min_ type: int
    :param max_: numero maximo
    :max_ type: int
    :param indicacion: indicacion para el usuario
    :indicacion type: str
    :return: numero ingresado
    :rtype: int
    """
    while True:
        try:
            numero = int(input(indicacion))
        except ValueError:
            print("El valor ingresado no es valido.")
            continue
        if numero < min_ or numero > max_:
            print("El valor ingresado no es valido.")
            continue
        return numero


def generador() -> List[int]:
    """Genera una lista de numeros aleatorios.

    :return: lista de numeros aleatorios.
    :rtype: list
    """
    REDONDEAR = {1: ceil, 2: floor, 3: round}
    INDICACIONES = (
        "¿Cuántos números quieres generar? [1-20]: ",
        ("¿Cómo quieres redondear los números? " \
            "[1]Al alza [2]A la baja [3]Normal: ")
    )
    cantidad = ingresar_numero(1, 20, INDICACIONES[0])
    tipo = ingresar_numero(1, 3, INDICACIONES[1])
    aleatorios = []
    for _ in range(cantidad):
        n = uniform(0, 100)
        print(f"Antes de redondear: {n}")
        n = REDONDEAR[tipo](n)
        print(f"Después de redondear: {n}")
        aleatorios.append(n)
    return aleatorios


def main():
    aleatorios: List[int] = generador()
    print(f"Los números generados fueron: {', '.join(map(str, aleatorios))}.")


if __name__ == "__main__":
    main()