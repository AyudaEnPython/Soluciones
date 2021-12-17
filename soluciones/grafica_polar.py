"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un inversión de giro de manera analítica mostrada en gráficas
polares, en la cual gire en sentido horario durante 15 segundos para
luego girar 15 segundos en sentido antihorario.

NOTE: Dado que no se tiene el material de lectura, ejericios previos
    realizados, ni codigos previos, se opta por implementarlo
    parcialmente.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def f(direction: int = -1) -> None:
    def update(angle):
        line.set_data([angle, angle], [0, 1])
        return line,
    
    fig = plt.figure()
    ax = fig.gca(projection = 'polar')
    fig.canvas.set_window_title('Ayuda en Python')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(direction)
    line, = ax.plot([],[], lw=2)
    fr = np.linspace(0, 2*np.pi, 120)
    fig.canvas.draw()
    a = FuncAnimation(fig, update, frames=fr, blit=True, interval=10)
    plt.show()


if __name__ == '__main__':
    f(-1) # Sentido horario
    f(1)  # Sentido antihorario