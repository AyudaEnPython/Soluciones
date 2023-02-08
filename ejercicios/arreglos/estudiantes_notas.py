"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
[
    ["José", [15, 18, 19]],
    ["María", [14, 17]],
    ["Victoria", [15, 13, 18, 12]],
    ["Kike", [6, 15, 12]],
]

Utilizando lista por comprensión mostrar la siguiente impresión.
Considere que la cantidad de estudiantes y notas podría aumentar o
disminuir.

Ejemplo de ejecución:

José: Promedio: 17.3 mayor: 19 menor: 15
María: Promedio: 15.5 mayor: 17 menor: 14
Victoria: Promedio: 14.5 mayor: 18 menor: 12
Kike: Promedio: 11.0 mayor: 15 menor: 6
"""
from statistics import mean

from prototools import tabulate

registro = [
    ["José", [15, 18, 19]],
    ["María", [14, 17]],
    ["Victoria", [15, 13, 18, 12]],
    ["Kike", [6, 15, 12]],
]

print("\n".join(
    f"{r[0]}: Promedio: {mean(r[1]):.1f} mayor: {max(r[1])} menor: {min(r[1])}"
    for r in registro
))

print("-"*45)

output = [
    [nombre, round(mean(notas), 1), max(notas), min(notas)]
    for (nombre, notas) in registro
]
print(tabulate(output, headers=["", "Promedio", "Mayor", "Menor"]))
