"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Una fábrica de autos produce tres modelos: sedán, camioneta y
económico. Cada auto necesita para su producción materiales, personal,
impuestos y transporte. Los costos en unidades por cada concepto son
los siguientes:

    +------------+-------+-----------+-----------+
    | Costos     | Sedán | Camioneta | Económico |
    +------------+-------+-----------+-----------+
    | Material   |     7 |         8 |         5 |
    | Personal   |    10 |         9 |         7 |
    | Impuestos  |     5 |         3 |         2 |
    | Transporte |     2 |         3 |         1 |
    +------------+-------+-----------+-----------+

Semanalmente, se producen 60 sedanes, 40 camionetas y 90 económicos.
Los costos de unidad de material, personal, impuestos y transporte son
respectivamente 5, 15, 7, 2.

Escriba un programa que muestre:
a) Las unidades semanales necesarias de material, personal, impuestos y
    transporte.
b) El costo total de un auto de cada modelo.
c) El costo total de la producción semanal.
"""
from typing import List, Iterable, Sequence, Tuple

MODELOS: Tuple[str] = ("Sedán", "Camioneta", "Económico")
CONCEPTO: Tuple[str] = ("Material", "Personal", "Impuestos", "Transporte")

unidades: Iterable[Sequence[int]] = [
    [7, 8, 5],
    [10, 9, 7],
    [5, 3, 2],
    [2, 3, 1]
]
costo_unidad: List[int] = [5, 15, 7, 2]
produccion: List[int] = [60, 40, 90]

unidades_semanales: List[int] = [
    [u[i]*p for i, p in enumerate(produccion)] for u in unidades
]
unidades_totales: List[int] = [sum(u) for u in zip(*unidades_semanales)]
costo_semanal: List[int] = [
    [unidades_semanales[i][j]*costo for j in range(len(MODELOS))]
    for i, costo in enumerate(costo_unidad)
]
totales: List[int] = [sum(x) for x in zip(*costo_semanal)]

for i, modelo in enumerate(MODELOS):
    print(f"Modelo '{modelo}'")
    for j, concepto in enumerate(CONCEPTO):
        print((
            f"{concepto:>14}: {unidades_semanales[j][i]:>3}"
            f" unidades | $ {costo_semanal[j][i]:>4}"
        ))
    print(f"{'----':>19}{'----':>18}")
    print(f"{unidades_totales[i]:>19}{totales[i]:>18}")
    print("-"*43)
print(f"Costo total de la producción semanal: {sum(totales)}")
