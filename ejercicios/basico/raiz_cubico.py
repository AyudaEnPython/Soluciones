"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un programa usando estructuras de repetición en Python que
calcule la raíz cúbica de cada uno de los siguientes elementos.

[10, 5, 30, 7, 14, 2, 3, 11, 9, 4]
"""

numeros = [10, 5, 30, 7, 14, 2, 3, 11, 9, 4]

for n in numeros:
    print(f"Raíz cúbica de {n}: {n ** (1/3):.2f}")
