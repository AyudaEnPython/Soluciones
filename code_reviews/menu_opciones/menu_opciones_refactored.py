"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from cmath import sqrt
# pip install prototools
from prototools.menu import EzMenu
from prototools.entradas import entrada_int

sol1 = lambda a, b, c: (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
sol2 = lambda a, b, c: (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
sol = lambda a, b, c: (sol1(a, b, c), sol2(a, b, c))
area, sum_sqrt = lambda b, h: b * h / 2, lambda x, y: (x + y) ** 0.5


def main():
    menu = EzMenu(ancho=80)
    menu.titulo("Menu de opciones")
    menu.agregar_opciones(
        "Raíz cuadrada de la suma de dos números",
        "Solución de ecuación de 2° grado",
        "Área de un triángulo",
        "Salir",
    )
    menu.agregar_funciones(
        lambda: print(sum_sqrt(
            entrada_int("Primer número: "),
            entrada_int("Segundo número: "))),
        lambda: print(sol(
            entrada_int("Coeficiente a: "),
            entrada_int("Coeficiente b: "),
            entrada_int("Coeficiente c: "))),
        lambda: print(area(
            entrada_int("Base: "),
            entrada_int("Altura: "))),
    )
    menu.run()


if __name__ == "__main__":
    main()