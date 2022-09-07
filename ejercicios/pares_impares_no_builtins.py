"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Números pares / impares
Nota: No esta permitido usar ningún método de Python para manipulación
de listas/tuplas excepto el uso de len.
Temas: Estructura condicional, Estructura repetitiva, Manipulación de
listas de números enteros.

1. Llenado automático de una lista de números.

    Llenar automáticamente una lista en Python con los primeros N
    números pares, donde N es un valor mayor o igual a 2 y menor o
    igual a 100, N es la cantidad de números pares a mostrar (validar
    N):
    Ejemplo:

    Input: 19
    Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30,
            32, 34, 36, 38]

2. Números pares e impares.

    Dada la siguiente tupla de 125 números enteros aleatorios entre 1
    y 20:

    tupla = (
        11, 11, 2, 9, 5, 9, 4, 8, 18, 8, 10, 5, 14, 19, 10, 9, 16,
        17, 5, 8, 6, 5, 19, 20, 2, 10, 16, 5, 2, 13, 7, 13, 18, 5,
        14, 15, 8, 15, 5, 8, 16, 14, 16, 3, 1, 3, 8, 2, 19, 17, 8,
        5, 13, 15, 2, 17, 4, 6, 8, 20, 15, 10, 11, 14, 5, 19, 8,
        14, 5, 16, 18, 12, 19, 18, 10, 4, 8, 5, 4, 18, 16, 7, 8,
        16, 8, 2, 16, 17, 7, 2, 6, 7, 17, 1, 14, 3, 13, 8, 17, 11,
        11, 2, 9, 5, 9, 4, 8, 18, 8, 10, 5, 14, 19, 10, 9, 16, 17,
        5, 8, 6, 5, 19, 20, 8, 6
    )

    Realice un algoritmo en Python que calcule:
    a. La cantidad de números pares y la cantidad de números impares.
    b. El porcentaje de números pares y el porcentaje de números impares.
    c. El promedio de números pares y promedio de números impares.
    d. El mayor número par y el mayor número impar.
    e. El menor número par y el menor número impar.

3. Número con mayor repetición.

    A partir de la tupla del segundo punto, obtener una lista con los
    números pares y mostrar el número par que tiene mayor número de
    repeticiones. De igual forma con los números impares.

    Input:
    La misma tupla del segundo punto.
    Output:
    El numero par con mayores repeticiones es: __ y se repite: __ veces
    El numero impar con mayores repeticiones es: __ y se repite: __ veces
"""
from collections import Counter

# 1
while True:
    try:
        n = input("n: ")
        if 1 <= int(n) <= 100:
            n = int(n)
            break
        else:
            print("Solo se admiten enteros positivos entre 1 y 100")
    except ValueError:
        print("Solo se admiten números")
pares_ = []
i, x = 0, 2
while i < n:
    if x % 2 == 0:
        pares_ += [x]
        i += 1
    x += 1
print(pares_)

# 2
aleatorios = (
    11, 11, 2, 9, 5, 9, 4, 8, 18, 8, 10, 5, 14, 19, 10, 9, 16, 17, 5, 8, 6, 5,
    19, 20, 2, 10, 16, 5, 2, 13, 7, 13, 18, 5, 14, 15, 8, 15, 5, 8, 16, 14,
    16, 3, 1, 3, 8, 2, 19, 17, 8, 5, 13, 15, 2, 17, 4, 6, 8, 20, 15, 10, 11,
    14, 5, 19, 8, 14, 5, 16, 18, 12, 19, 18, 10, 4, 8, 5, 4, 18, 16, 7, 8, 16,
    8, 2, 16, 17, 7, 2, 6, 7, 17, 1, 14, 3, 13, 8, 17, 11, 11, 2, 9, 5, 9, 4,
    8, 18, 8, 10, 5, 14, 19, 10, 9, 16, 17, 5, 8, 6, 5, 19, 20, 8, 6,
)
pares = list(filter(lambda x: x % 2 == 0, aleatorios))
impares = list(filter(lambda x: x % 2 != 0, aleatorios))
# a
print(len(pares), len(impares))
# b
print((len(pares)*100)/len(aleatorios), (len(impares)*100)/len(aleatorios))
# c
print(sum(pares)/len(pares), sum(impares)/len(impares))
# e
print(max(pares), max(impares))
# d
print(min(pares), min(impares))

# 3
par = Counter(pares).most_common(1)
impar = Counter(impares).most_common(1)
print(
    f"El numero par con mayores repeticiones es: {par[0][0]} y se repite:"
    f" {par[0][1]} veces"
)
print(
    f"El numero impar con mayores repeticiones es: {impar[0][0]} y se repite:"
    f" {impar[0][1]} veces"
)
