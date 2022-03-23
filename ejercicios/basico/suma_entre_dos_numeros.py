"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribe un programa que solicite dos números enteros al usuario y
muestre por pantalla la suma de todos los números enteros que hay
entre los dos números (ambos números incluidos).

Ejemplo:

Introduce el número de inicio: 4
Introduce el número de fin: 8
El resusltado es: 30
"""

inicio = int(input("Introduce el número de inicio: "))
fin = int(input("Introduce el número de fin: "))

if inicio > fin:
    inicio, fin = fin, inicio

print(f"El resusltado es: {sum(range(inicio, fin + 1))}")
