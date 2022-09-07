"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Calcular: sin(x), cos(x) y e^x.
Las fórmulas matemáticas son:

sin x = \sum_{n=0}^{\infty} (-1)^n / \fact{2n+1} x^(2n+1)  # noqa: W605
cos x = \sum_{n=0}^{\infty} (-1)^n / \fact{2n} x^(2n)      # noqa: W605
e^x = \sum_{n=0}^{\infty} (-1)^n / \fact{n}                # noqa: W605

El único dato de entrada es el valor de x. La salida consiste de los
valores aproximados a 11 decimales desde el 0 hasta el 10 inclusive.
La salida debe estar en el formato similar al ejemplo e imprimirse con
la cantidad de decimales especificados.

Ejemplo de entrada
0.5

Ejemplo de salida

n  sin(0.5)      cos(0.5)      e^0.5
-- ------------- ------------- -------------
00 0.50000000000 1.00000000000 1.00000000000
01 0.47916666667 0.87500000000 1.50000000000
02 0.47942708333 0.87760416667 1.62500000000
03 0.47942553323 0.87758246528 1.64583333333
04 0.47942553862 0.87758256216 1.64843750000
05 0.47942553860 0.87758256189 1.64869791667
06 0.47942553860 0.87758256189 1.64871961806
07 0.47942553860 0.87758256189 1.64872116815
08 0.47942553860 0.87758256189 1.64872126504
09 0.47942553860 0.87758256189 1.64872127042
10 0.47942553860 0.87758256189 1.64872127069

NOTE: Las funciones son tomadas del repositorio del grupo AyudaEnPython
# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/aproximacion_series_maclaurin/main.py
"""
from math import factorial as f
# pip install prototools
from prototools import Menu, float_input, tabulate, clear_screen


def sinx(x: float, n: int) -> float:
    return sum((-1)**k * x**(2*k + 1) / f(2*k + 1) for k in range(n + 1))


def cosx(x: float, n: int) -> float:
    return sum((-1)**k * x**(2*k) / f(2*k) for k in range(n + 1))


def expx(x: float, n: int) -> float:
    return sum((x**k) / f(k) for k in range(n + 1))


def g():
    x = float_input("x: ")
    clear_screen()
    data = [
        [
            f"{n:02}",
            f"{sinx(x, n):.11f}",
            f"{cosx(x, n):.11f}",
            f"{expx(x, n):.11f}",
        ]
        for n in range(11)
    ]
    print(tabulate(data, headers=["n", f"sin({x})", f"cos({x})", f"e^({x})"]))


def main():
    menu = Menu("Aproximaciones")
    menu.add_options(
        ("Ingresar valor de x", g),
    )
    menu.run()


if __name__ == "__main__":
    main()
