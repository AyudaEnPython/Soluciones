"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Pedir 3 números y mostrar el mayor de ellos.
"""
mayor = 0

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

if a > mayor:
    mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c

print("El mayor es:", mayor)