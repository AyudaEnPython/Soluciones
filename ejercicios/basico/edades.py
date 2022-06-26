"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Diseñe un programa que permita ingresar las edades, de una en una,
de un conjunto de personas y muestre, luego de cada ingreso:

- La cantidad de personas ingresadas.
- La cantidad de personas mayores de edad.
- La cantidad de personas menores de edad.
"""

cantidad = mayores = menores = 0

while True:
    try:
        edad = int(input("Ingrese edad: "))
    except ValueError:
        print("Edad inválida")
        continue
    if edad <= 0:
        break
    if edad >= 18:
        mayores += 1
    else:
        menores += 1
    cantidad += 1
    print(f"Cantidad de personas: {cantidad}")
    print(f"Personas mayores de edad: {mayores}")
    print(f"Personas menores de edad: {menores}")
