"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Calcular cuantos granos de arroz tendríamos en la ultima casilla, si
por cada casilla de una matriz 3x4 pusiéramos un grano en la primera
casilla y el triple en la siguiente.
"""

CASILLAS = 12

total = sum(3 ** n for n in range(CASILLAS))
print(f"En la última casilla tendríamos {total} granos de arroz.")
