"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# del repositorio del grupo AyudaEnPython:
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/ecuacion_2do_grado.py

from cmath import sqrt


def solucion(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
    elif d == 0:
        x1 = x2 = (-b/(2*a))
    else:
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
    return f"x1 = {x1}, x2 = {x2}"


p_a = (1, 3, 2) # P(x) = x^2 + 3x + 2
p_b = (2, 4, 2) # P(x) = 2x^2 + 4x + 2
p_c = (3, 0, 2) # P(x) = 3x^2 + 2

print(solucion(*p_a)) # x1 = -1.0, x2 = -2.0
print(solucion(*p_b)) # x1 = -1.0, x2 = -1.0
print(solucion(*p_c)) # x1 = 0.8164965809277259j, x2 = -0.8164965809277259j