"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un algoritmo que sume los números ingresados por el usuario y
cuando la suma sea superior a 100 deje de pedir números y muestre el
total.
"""

suma = 0
while True:
    numero = input("Ingrese un número: ")
    try:
        numero = int(numero)
    except ValueError:
        print("Error, debe ingresar un número")
        continue
    if suma + numero > 100:
        break
    suma += numero

print("La suma es:", suma)