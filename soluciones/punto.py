"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from math import sqrt


class Punto:

    def __init__(self, x=0, y=0):
        self.mover(x, y)

    def mover(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.mover(0, 0)

    def distancia(self, otro_punto):
        return sqrt(
            (self.x - otro_punto.x) ** 2 +
            (self.y - otro_punto.y) ** 2
        )


def main():
    a = Punto()
    b = Punto()
    b.mover(5, 0)
    print(b.distancia(a))
    assert (b.distancia(a) == a.distancia(b))
    a.mover(3, 4)
    print(a.distancia(b))
    print(a.distancia(a))
    c = Punto(3, 5)
    print(c.x, c.y)


if __name__ == "__main__":
    main()
