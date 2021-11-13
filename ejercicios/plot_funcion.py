"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Genere un programa que reciba una función cualquiera de una variable y
un intervalo de graficación para generar un archivo PNG con la gráfica
resultante.
"""
from matplotlib import pyplot as plt


def f(x):
    return x**2


x = range(-10, 11)
plt.plot(x, [f(x) for x in x])
plt.show()