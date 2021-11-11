"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

1. Crear un programa que maneje "N" cantidad de datos de tipo real en
    una lista. Una vez ingresados los datos por teclado en la lista, el
    programa debe calcular el promedio de todos los datos e indicar
    cuantos números de la lista son menores a ese promedio.

2. Crear un programa que maneje "N" cantidad de datos de tipo real en
    una lista. Una vez ingresados los datos por teclado en la lista, el
    programa debe calcular el promedio de todos los datos.
    Posteriormente, el programa debe crear una segunda lista cuyos
    elementos serán la diferencia (resta) entre el promedio y cada dato
    de la lista original.

3: Escribir una función que reciba una muestra de números en una lista
    y devuelva otra lista con sus raices cuadradas.
"""
from typing import List


def _datos() -> List[float]:
    data = []
    n = int(input("Ingrese la cantidad de datos que desea ingresar: "))
    for _ in range(n):
        data.append(float(input("Ingrese un dato: ")))
    return data


def problema_1():
    numeros = _datos()
    promedio = sum(numeros) / len(numeros)
    menores_promedio = len([x for x in numeros if x < promedio])
    print(f"Promedio: {promedio}")
    print(f"Menores: {menores_promedio}")


def problema_2():
    numeros = _datos()
    promedio = sum(numeros) / len(numeros)
    diferencia = [x - promedio for x in numeros]
    print(f"Promedio: {promedio}")
    print(f"Diferencia: {diferencia}")


def problema_3():
    numeros = _datos()
    raices = [x ** 0.5 for x in numeros]
    print(f"Raices cuadradas: {raices}")


if __name__ == "__main__":
    problema_1()
    problema_2()
    problema_3()