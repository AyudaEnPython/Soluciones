"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ingresar dos números y mostrar cual de ellos es par o si ambos lo son.
"""

x = int(input("Ingrese un número: "))
y = int(input("Ingrese otro número: "))

if x % 2 == 0 and y % 2 == 0:
    print("Ambos son pares")
elif x % 2 == 0:
    print("El primero es par")
elif y % 2 == 0:
    print("El segundo es par")
else:
    print("Ninguno es par")