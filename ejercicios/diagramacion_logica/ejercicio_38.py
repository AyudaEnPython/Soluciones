"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

from random import randint


numeros = [randint(0, 36) for _ in range(5)]

par = impar = 0

for n in numeros:
    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print(f"Porcentaje de números pares: {par / len(numeros) * 100}%")
print(f"Porcentaje de números impares: {impar / len(numeros) * 100}%")