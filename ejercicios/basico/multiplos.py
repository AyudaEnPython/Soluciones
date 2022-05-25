"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Construir un programa que permita ingresar N (cantidad digitada por el
usuario) números enteros y cuente cuantos múltiplos de 2 y de 3 fueron
ingresados.
"""

n = int(input("N: "))
i2 = i3 = 0
for _ in range(n):
    numero = int(input("> "))
    if numero % 2 == 0:
        i2 += 1
    if numero % 3 == 0:
        i3 += 1
print(f"Hay {i2} múltiplos de 2 y {i3} múltiplos de 3")
