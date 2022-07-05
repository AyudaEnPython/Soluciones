"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar la diferencia de las posiciones impares.

NOTE: el enunciado no es claro.
"""

numeros = []
resultado = 0
n = int(input("Tamaño: "))
for i in range(n):
    numeros.append(int(input(f"[{i+1}]> ")))
    if i == 1:
        resultado = numeros[i]
    else:
        if i % 2 != 0:
            resultado -= numeros[i]
print(f"Resultado: {resultado}")

# ------------------------------------------------------------- alt ver
# ns = [1, 2, 3, 4, 5, 6]
# r = ns[1]
# for n in range(3, len(ns), 2):
#     r -= ns[n]
# print(r)
