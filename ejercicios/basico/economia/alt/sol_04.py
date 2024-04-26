"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

numeros = []
suma = 0

n = int(input("Número de términos: "))

for x in range(1, n + 1):
    numerador = 3*x - 2
    denominador = 2*x
    numeros.append((numerador, denominador))

for numerador, denominador in numeros:
    print(f"{numerador}/{denominador}")
    suma +=  numerador/denominador
print(suma)
