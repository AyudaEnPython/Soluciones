"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crear una función que represente gráficamente esta expresión:

    sin(2π*f_1*t) + sin(2π*f_2*t) 

Siendo f_1 y f_2 argumentos de entrada (por defecto 10 y 100) y
t ∈ [0, 0.5]. Además, debe mostrar:
- leyenda
- título "Dos frecuencias"
- eje x "Tiempo (t)"

y usar algún estilo de los disponibles.
"""
import numpy as np
import matplotlib.pyplot as plt


def signals(f1, f2, t):
    return np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)


def plot_f(f1, f2, t):
    plt.plot(t, signals(f1, f2, t), label="señal", c="b")
    plt.title("Dos frecuencias")
    plt.xlabel("Tiempo (t)")
    plt.ylabel("Amplitud")
    plt.legend(["señal"], loc="upper right")
    plt.show()


if __name__ == '__main__':
    f1 = 10
    f2 = 100
    t = np.linspace(0, 0.5, 1000)
    plot_f(f1, f2, t)
