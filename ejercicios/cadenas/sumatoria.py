"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dada una secuencia de caracteres de tipo numérico, separados por punto
y coma, y registrados en una cadena, separar cada número y almacenarlos
en una lista. Finalmente obetener la sumatoria de los elementos de la
lista.

Ejemplo:
secuencia = "12; -5; 0; 100; -25; 4; 18; 15; -1; -50.5"

Lista = [12, -5, 0, 100, -25, 4, 18, 15, -1, -50.5]
Sumatoria = 67,5
"""

numeros = "12; -5; 0; 100; -25; 4; 18; 15; -1; -50.5"
print(sum([float(n) for n in numeros.split(";")]))
