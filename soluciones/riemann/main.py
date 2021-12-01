"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

def f(x: int) -> int:
    return x**2 + 6*x + 3


def riemann(a: int, b: int, n: int) -> float:
    """Calcula el area de una región de una función
    en el intervalo [a, b] con n subintervalos.
    """
    h = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + i*h)*h
    return s


if __name__ == '__main__':
    print(riemann(1, 10, 100))