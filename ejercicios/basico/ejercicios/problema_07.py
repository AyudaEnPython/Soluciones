"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribe un programa que solicite al usuario el ingreso de dos números
diferentes y muestre en pantalla al mayor de los dos.
"""

x = int(input("Ingrese un número: "))
y = int(input("Ingrese otro número distinto: "))

if x > y:
    print(f"El mayor es {x}.")
else:
    print(f"El mayor es {y}.")
