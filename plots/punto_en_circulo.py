"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from collections import namedtuple
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from typing import Tuple
# pip install prototools
from prototools import float_input

Punto: Tuple[float, float] = namedtuple("Punto", ["x", "y"])


def show_plot(c: Punto, p: Punto, r: float) -> None:
    fig, ax = plt.subplots()
    ax.add_patch(Rectangle(
        (c.x-r, c.y-r), 2*r, 2*r, color="g", fill=False
    ))
    ax.add_artist(plt.Circle(
        (c.x, c.y), r, color="b", fill=False
    ))
    ax.set_aspect(1)
    ax.scatter(p.x, p.y, c="r")
    plt.show()


def get_data() -> Punto:
    h = float_input("h: ")
    k = float_input("k: ")
    r = float_input("r: ")
    x = float_input("x: ")
    y = float_input("y: ")
    return Punto(h, k), Punto(x, y), r


def get_zone(p: Punto, c: Punto) -> int:
    if p.x > c.x and p.y > c.y:
        return "A"
    elif p.x < c.x and p.y > c.y:
        return "B"
    elif p.x < c.x and p.y < c.y:
        return "C"
    else:
        return "D"


def _inside_circle(c: Punto, p: Punto) -> bool:
    return (p.x - c.x) ** 2 + (p.y - c.y) ** 2


def _inside_square(c: Punto, p: Punto, r: float) -> bool:
    return p.x <= c.x + r and p.y <= c.y + r


def show_result(c: Punto, p: Punto, r: float) -> str:
    if _inside_circle(c, p) < r ** 2:
        return f"{p} esta en el interior del circulo"
    elif _inside_circle(c, p) == r ** 2:
        return f"{p} esta en el circunferencia del circulo"
    elif _inside_square(c, p, r):
        return (
            f"{p} esta fuera del circulo pero dentro del cuadrado\n"
            f"{p} se encuentra en la zona {get_zone(p, c)}"
        )
    else:
        return f"{p} está fuera del circulo y del cuadrado"


def main():
    c, p, r = get_data()
    print(show_result(c, p, r))
    show_plot(c, p, r)


if __name__ == "__main__":
    main()
