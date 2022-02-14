"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba un programa en Python para encontrar los números que son
divisibles por 7 y múltiplos de 5 entre 1500 y 2700 (ambos incluidos).
"""

numeros = []
for numero in range(1500, 2701):
    if numero % 7 == 0 and numero % 5 == 0:
        numeros.append(numero)
print(numeros)
