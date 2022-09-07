"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Ingresar A, B, y C tres variables enteras que representan las ventas
de tres productos A, B, y C respectivamente. Utilizando dichas
variables, elabora los siguientes programas:

- El programa debe indicar si B es el número mayor o no.
- El programa debe indicar si alguno de los números ingresados es menor
    a 30.
- El programa debe indicar cual es la venta promedio.
- El programa debe indicar cual es el producto más vendido.

NOTE: Las indicaciones no son precisas, "si B es el número mayor o no"
    se puede interpretar como "si B es el más vendido".
"""

A = int(input("Ingrese la venta del producto A: "))
B = int(input("Ingrese la venta del producto B: "))
C = int(input("Ingrese la venta del producto C: "))

mayor = max(A, B, C)
menor = min(A, B, C)
promedio = (A + B + C) / 3

if mayor == B:
    print("El producto B es el más vendido.")
else:
    print("El producto B no es el más vendido.")

if A < 30 or B < 30 or C < 30:
    print("Alguno de los productos es menor a 30.")

print("La venta promedio es:", promedio)
print("El producto más vendido es:", mayor)
