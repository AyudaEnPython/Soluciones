"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# del repositorio del grupo AyudaEnPython:
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/ecuacion_2do_grado.py

from cmath import sqrt

a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

d = b*b - 4*a*c
if d < 0:
    x1 = (-b + sqrt(d))/(2*a)
    x2 = (-b - sqrt(d))/(2*a)
elif d == 0:
    x1 = x2 = (-b/(2*a))
else:
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - d**0.5)/(2*a)

print(f"x1 = {x1}")
print(f"x2 = {x2}")