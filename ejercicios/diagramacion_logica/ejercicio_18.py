"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# del repositorio del grupo AyudaEnPython:
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/mayor_de_tres_numeros.py

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

print(f"El mayor es: {mayor}")