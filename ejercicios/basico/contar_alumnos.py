"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
El usuario ingresa, secuencialmente, el número de estudiantes de cada una de
las 10 clases.

Escribe un programa que calcule y muestre el número total de estudiantes.


NOTE: Si de antemano se conoce el número de iteraciones es mejor usar 'for'
"""

i = 0
total = 0

while i < 10:
    cantidad = int(input(f"Cantidad de alumnos del aula N° {i+1}: "))
    total += cantidad
    i += 1

print(total)

# Usando for:
#
# total = 0
# for i in range(10):
#     cantidad = int(input(f"Cantidad de alumnos del aula N° {i+1}: "))
#     total += cantidad
# print(total)
