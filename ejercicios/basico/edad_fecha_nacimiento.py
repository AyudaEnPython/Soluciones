"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Leer el año de nacimiento de 10 estudiantes del curso de Globant y
calcular cuantos años cumple cada estudiante en 2022, finalmente
indique cuantos estudiantes tiene mas de 22 años.
"""
from datetime import date

current_year = date.today().year
total = 0

for _ in range(10):
    year = int(input("Fecha de nacimiento: "))
    age = current_year - year
    print(f"Edad actual: {age} años")
    total += 1 if age > 22 else 0
print(f"Total de estudiantes mayores de 22 años: {total}")
