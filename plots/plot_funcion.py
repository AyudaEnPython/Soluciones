"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------ Enunciado original ------------------------
Genere un programa que reciba una función cualquiera de una variable y
un intervalo de graficación para generar un archivo PNG con la gráfica
resultante.
# --------------------------------------------------------------------

Nota: El enunciado es muy general, debería ser más específico el
    instructor en cuanto a la elaboración del ejercicio.
"""
from matplotlib import pyplot as plt


def f(x): return x**2


x = range(-10, 11)
plt.plot(x, [f(x) for x in x])
plt.show()
