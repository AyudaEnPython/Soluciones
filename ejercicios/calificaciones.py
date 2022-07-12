"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Generar una lista de 50 calificaciones aleatorias entre 0 y 100 y
determinar:

+------------------+------------------+------------------+
| Apellido paterno | Apellido paterno | Apellido paterno |
|     A .. G       |      H .. M      |       O .. Y     |
+------------------+------------------+------------------+
| Cuantas están en | Cuantas están en | Cuantas están en |
|                  |                  |                  |
| Entre 0 y 10     | Entre 0 y 15     | Entre 0 y 20     |
| Entre 11 y 30    | Entre 16 y 25    | Entre 21 y 35    |
| Entre 31 y 50    | Entre 26 y 40    | Entre 36 y 50    |
| Entre 51 y 70    | Entre 41 y 60    | Entre 51 y 75    |
| Entre 71 y 90    | Entre 61 y 80    | Entre 76 y 85    |
| Entre 91 y 100   | Entre 81 y 100   | Entre 86 y 100   |
+------------------+------------------+------------------+

y mostrar el resultado en una gráfica de asteriscos como lo muestra el
siguiente formato de salida:

    +-------------------------------------------------+
    |         GRÁFICA DE CALIFICACIONES               |
    | Categoría     Rango   Cantidad  Gráfica         |
    |     1        0 .. 20     5      *****           |
    |     2       21 .. 35     8      ********        |
    |     3       36 .. 50    10      **********      |
    |     4       51 .. 75     5      *****           |
    |     5       76 .. 85    15      *************** |
    |     6       86 .. 100    7      *******         |
    |                        -----                    |
    |                         50                      |
    +-------------------------------------------------+

NOTA: Cómo los números son aleatorios, su salida pueder ser diferente
    en cuanto a la cantidad de cada categoría.
"""
from random import randint
from typing import List, Tuple
# pip install prototools
from prototools import tabulate

MIN: int = 0
MAX: int = 100
RANGO: Tuple[Tuple[int, int]] = (
    (0, 20), (21, 35), (36, 50), (51, 75), (76, 85), (86, 100)
)


def generar_calificaciones(n: int = 50) -> List[int]:
    return [randint(MIN, MAX) for _ in range(n)]


def calificaciones_por_rango(calificaciones: List[int]) -> List[int]:
    return [
        len([c for c in calificaciones if c >= r[0] and c <= r[1]])
        for r in RANGO
    ]


def grafica(calificaciones: List[int]) -> List[str]:
    return [
        '*' * c if c > 0 else ' ' * c
        for c in calificaciones_por_rango(calificaciones)
    ]


def mostrar_resultados(
    rango: Tuple[Tuple[int, int]],
    calificaciones: List[str],
    grafica: List[str],
) -> None:
    headers = ("Categoría", "Rango", "Cantidad", "Gráfica")
    rows = [
        [f"{i + 1:^9}", f"{r[0]:>2} .. {r[1]:>3}", f"{c:>5}", g]
        for i, (r, c, g) in enumerate(zip(rango, calificaciones, grafica))
    ]
    rows += [["", "", "  ----", ""]]
    rows += [["", "", f"{sum(calificaciones):^8}", ""]]
    print("\n\t\tGráfica de calificaciones".upper())
    print(tabulate(rows, headers=headers, border_type="borderless"))


def main():
    datos = generar_calificaciones(50)
    mostrar_resultados(
        RANGO,
        calificaciones_por_rango(datos),
        grafica(datos)
    )


if __name__ == "__main__":
    main()
