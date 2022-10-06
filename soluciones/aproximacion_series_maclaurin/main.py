"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from math import factorial as f
# pip install prototools
from prototools import Menu, textbox, int_input

N = 10


def sinx(x, n=N):
    return sum((-1)**k * x**(2*k + 1) / f(2*k + 1) for k in range(n + 1))


def cosx(x, n=N):
    return sum((-1)**k * x**(2*k) / f(2*k) for k in range(n + 1))


def expx(x, n=N):
    return sum((x**k) / f(k) for k in range(n + 1))


def arcsenx(x, n=N):
    return sum(
        (f(2*k) * x**(2*k + 1)) / (4**k * (f(k)**2) * (2*k + 1))
        for k in range(n + 1)
    )


def _f(f, a, b, n):
    if f == arcsenx:
        if a < -1 or b > 1:
            textbox("Fuera de dominio")
            return
    h = (abs(a) + abs(b)) / n
    t, k = [], a
    while k <= b:
        t.append(round(k, 2))
        k += h
    for i in t:
        print(f"x: {i:>4}  f({i:>4.1f}) -> {f(i):>6.2f}")


@dataclass
class Solution:
    a: int = -1
    b: int = 1
    n: int = 10

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def set_n(self, n):
        self.n = n

    def evaluar(self, f):
        _f(f, self.a, self.b, self.n)


def main():
    sol = Solution()
    menu = Menu("Aproximacion de Funciones")
    menu.add_options(
        ("Ingresar el valor de a",
            lambda: sol.set_a(int_input("Ingrese el valor de a: "))),
        ("Ingresar el valor de b",
            lambda: sol.set_b(int_input("Ingrese el valor de b: "))),
        ("Ingresar el valor de n",
            lambda: sol.set_n(int_input("Ingrese el valor de n: "))),
        ("Evaluación de la función exp(x) en la partición",
            lambda: sol.evaluar(expx)),
        ("Evaluación de la función sen(x) en la partición",
            lambda: sol.evaluar(sinx)),
        ("Evaluación de la función cos(x) en la partición",
            lambda: sol.evaluar(cosx)),
        ("Evaluación de la función arcsen(x) en la partición",
            lambda: sol.evaluar(arcsenx)),
    )
    menu.settings(header_bottom=True)
    menu.run()


if __name__ == "__main__":
    main()
