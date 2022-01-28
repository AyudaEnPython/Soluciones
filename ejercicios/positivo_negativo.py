"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Realizar una función llamada sumarNumeros donde se ingrese números a
una lista y la función devolverá otra lista con los valores obtenidos
de la suma de los números positivos y negativos que se ingresaron en la
primera lista. El programa termina cuando se ingrese 0.

NOTE: Se opta por renombrar la función a sumar_numeros (PEP8). Además,
    si se esta trabajando con funciones, se deberia implementar una
    función para la entrada de datos.
TODO: add typing, docstring and tests later.
"""


def ingresar_numeros():
    numeros = []
    while True:
        n = int(input("Ingrese el número: "))
        if n == 0:
            break
        else:
            numeros.append(n)
    return numeros


def sumar_numeros(numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado


numeros = ingresar_numeros()
print(f"La suma de los números es: {sumar_numeros(numeros)}")