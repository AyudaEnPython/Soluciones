"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que, dada una lista, devuelva una nueva lista cuyo
contenido sea igual a la original pero invertida. Así, dada la lista
["Di", "buen", "dia", "a", "papa"], deberá devolver
["papa", "a", "dia", "buen", "Di"].
"""

palabras = ["Di", "buen", "dia", "a", "papa"]

# print(palabras[::-1])

invertido = []
for i in range(len(palabras), 0, -1):
    invertido.append(palabras[i - 1])
print(invertido)