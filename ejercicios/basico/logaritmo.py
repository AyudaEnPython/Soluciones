"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba un programa que le permita al usuario calcular el logaritmo de
número con su base. El usuario debe poder elegir los números que desee
para el cálculo, permitiendo decimales.
"""
from math import log

n = float(input("Ingrese el número: "))
b = float(input("Ingrese la base: "))
print(f"Log_{n} ({b}) = {log(n, b)}")
