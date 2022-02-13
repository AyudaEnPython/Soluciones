"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Genere una matriz de 25 x 40 con números decimales al azar entre 0 y 1.
Mostrar los numeros del perimetro y calcularlo.
"""
from random import random

arr = [[random() for _ in range(40)] for _ in range(25)]
r_arr = list(map(list, zip(*arr)))
perimetro = [*arr[0], *arr[-1], *r_arr[0][1:-1], *r_arr[-1][1:-1]]
print(perimetro)
print(sum(perimetro))
