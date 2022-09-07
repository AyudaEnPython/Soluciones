"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from cmath import sqrt
from typing import Tuple, Union


# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/ecuacion_2do_grado.py
def solve(
    a: Union[int, float],
    b: Union[int, float],
    c: Union[int, float],
) -> Tuple[float, float]:
    d = b**2 - 4*a*c
    if d < 0:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)
    elif d == 0:
        x1 = x2 = -b / (2*a)
    else:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
    return x1, x2


def main():
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    x1, x2 = solve(a, b, c)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")


if __name__ == "__main__":
    main()
