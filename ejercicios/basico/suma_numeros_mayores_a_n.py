"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un algoritmo que sume solo aquellos números ingresados por el
usuario que sean mayores a 10.

"""

# ---------------- usando while, espacio en blanco para salir del bucle
N = 10
suma = 0
while True:
    numero = input("Ingrese un número: ")
    if numero == "":
        break
    try:
        numero = int(numero)
        if numero >= N:
            suma += numero
    except ValueError:
        print("El valor ingresado no es un número")
print("La suma es:", suma)

# ------------------------------------------------------- usando listas
N = 10
numeros = []
while True:
    numero = input("Ingrese un número: ")
    if numero == "":
        break
    try:
        numero = int(numero)
        if numero >= N:
            numeros.append(numero)
    except ValueError:
        print("El valor ingresado no es un número")
print("La suma es:", sum(numeros))

# ----------------------- usando for e indicando la cantidad de números
N = 10
cantidad = int(input("Ingrese la cantidad de números a sumar: "))
for _ in range(cantidad):
    numero = int(input("Ingrese un número: "))
    if numero >= N:
        suma += numero
print("La suma es:", suma)
