"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Make a 3D surface plot of the function z = cos(xy)cos(sqrt(x^2 + y^2))
in the domain -pi <= x <= pi and -pi <= y <= pi.
"""
import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return np.cos(x * y) * np.cos(np.sqrt(x**2 + y**2))


def show_plot(*axes, title="Superficie", title_color="r", color="y", size=10):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot_surface(*axes, color=color)
    ax.set_xlabel("Eje X", fontsize=size)
    ax.set_ylabel("Eje Y", fontsize=size)
    ax.set_zlabel("Eje Z", fontsize=size)
    ax.set_title(title, color=title_color)
    plt.show()


if __name__ == "__main__":
    x, y = np.meshgrid(
        np.linspace(-1*np.pi, np.pi, 100),
        np.linspace(-1*np.pi, np.pi, 100),
    )
    z = f(x, y)
    show_plot(x, y, z)
