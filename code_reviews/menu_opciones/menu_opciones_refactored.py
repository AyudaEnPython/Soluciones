"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from cmath import sqrt
# pip install prototools
from prototools import Menu, int_input

sol1 = lambda a, b, c: (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
sol2 = lambda a, b, c: (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
sol = lambda a, b, c: (sol1(a, b, c), sol2(a, b, c))
area, sum_sqrt = lambda b, h: b * h / 2, lambda x, y: (x + y) ** 0.5


def main():
    menu = Menu()
    menu.add_options(
        ("Raíz cuadrada de la suma de dos números",
        lambda: print(sum_sqrt(
            int_input("Primer número: "),
            int_input("Segundo número: ")))),
        ("Solución de ecuación de 2° grado",
        lambda: print(sol(
            int_input("a: "),
            int_input("b: "),
            int_input("c: ")))),
        ("Área de un triángulo",
        lambda: print(area(
            int_input("Base: "),
            int_input("Altura: ")))),
    )
    menu.run()


if __name__ == "__main__":
    main()