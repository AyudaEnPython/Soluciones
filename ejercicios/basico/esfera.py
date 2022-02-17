"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Esfera. Escriba un programa que calcule el radio r de una esfera de
volumen v (cm^3). Una vez calculado r, utilice este valor para calcular
el área de la superficie de la esfera.

Ejemplo de entrada:
Ingrese el volúmen (cm3): 350

Ejemplo de salida:
El área es 240.18
"""
from math import pi

v = float(input("Ingrese el volumen (cm3): "))
r = (v / (4/3 * pi)) ** (1/3)
area = 4 * pi * (r ** 2)
print(f"El área es {round(area, 2)}")
