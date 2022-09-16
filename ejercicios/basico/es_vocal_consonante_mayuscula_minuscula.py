"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ingresar una letra e indicar si la letra es vocal, consonante,
mayúscula o minúscula.
"""

VOCALES = "aeiouáéíóú"
CONSONANTES = "bcdfghjklmnñpqrstvwxyz"

letra = input("> ")

if letra.lower() in VOCALES:
    tipo = "vocal"
elif letra.lower() in CONSONANTES:
    tipo = "consonante"
else:
    tipo = None

if letra.isupper():
    tamaño = "mayúscula"
else:
    tamaño = "minúscula"

if tipo is None or not letra:
    print("Digita una vocal o consonante")
else:
    print(f"{letra} es {tipo} y esta en {tamaño}")
