"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Elaborar un algoritmo que lea el nombre de un vendedro y las ventas
realizadas en cada uno de los 30 días del mes, que las almacene en un
arreglo y que imprima el reporte siguiente:

    +-----------------------------------+
    | Nombre del vendedor: XXXXXXXX     |
    | Venta del día 1: 999,999.99       |
    | Venta del día 2: 999,999.99       |
    | ...                               |
    | Venta del día 30: 999,999.99      |
    |                                   |
    | Venta total del mes: 9,999,999.99 |
    +-----------------------------------+

Donde la venta total del mes se calcula mediante la suma de las ventas
realizadas en cada uno de los 30 días.

Además, debe calcular:

    +--------------------------------------------+
    | Total de elementos arriba de la media: 999 |
    | Total de elementos abajo de la media:  999 |
    | Total de elementos igual a la media:   999 |
    +--------------------------------------------+
"""
from typing import List, Tuple

N = 30


def get_data() -> Tuple[str, List[float]]:
    nombre = input("Nombre del vendedor: ")
    ventas = [
        float(input(f"Venta del dia {i+1}: "))
        for i in range(N)
    ]
    return nombre, ventas


def reporte(nombre: str, ventas: List[float]):
    print(f"Nombre del vendedor: {nombre}")
    for i in range(N):
        print(f"Venta del dia {i+1}: {ventas[i]:.2f}")
    print(f"Venta total del mes: {sum(ventas)}")


def media_info(ventas: List[float]) -> Tuple[int, int, int]:
    media = round(sum(ventas) / N, 2)
    arriba = len([venta for venta in ventas if venta > media])
    abajo = len([venta for venta in ventas if venta < media])
    igual = len([venta for venta in ventas if venta == media])
    return arriba, abajo, igual


def main():
    nombre, ventas = get_data()
    reporte(nombre, ventas)
    arriba, abajo, igual = media_info(ventas)
    print(f"Total de elementos arriba de la media: {arriba}")
    print(f"Total de elementos abajo de la media: {abajo}")
    print(f"Total de elementos igual a la media: {igual}")


if __name__ == "__main__":
    main()
