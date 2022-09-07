"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ejercicio 3:
Realizar un algoritmo que calcule al media de "n" números ingresados
por teclado.

Ejercicio 4:
Realizar un algoritmo que calcule la varianza de 10000 números
generados aleatoriamente usando el módulo random.randint(a, b). El
usuario debe ingresar el límite inferior (a) y superior (b).
"""
from random import randint


# Ejercicio 3
n = int(input("Cantidad de números a ingresar: "))
print(f"Media: {sum(int(input('> ')) for _ in range(n))/n}")


# Ejercicio 4
a = int(input("Límite inferior: "))
b = int(input("Límite superior: "))
ns = [randint(a, b) for _ in range(10_000)]
print(f"Varianza: {sum((n - (sum(ns)/len(ns))) ** 2 for n in ns) / len(ns)}")
