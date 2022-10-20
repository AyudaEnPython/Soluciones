"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Solicita al usuario un número de mes al año, e imprime:
- el nombre del mes.
- la cantidad de dias que tiene cada mes.
"""
from datetime import date
from calendar import monthrange

YEAR = date.today().year
_MESES = (
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "setiembre", "noviembre", "diciembre",
)
MESES = {x: (m, monthrange(YEAR, x)[1]) for x, m in zip(range(1, 13), _MESES)}

mes = int(input("Ingresar mes expresado en números (1-12): "))
print(f"Mes: {MESES[mes][0]}")
print(f"Dias: {MESES[mes][1]}")
