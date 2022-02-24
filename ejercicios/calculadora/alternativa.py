"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from operator import add, sub, mul, truediv
# pip install prototools
from prototools import float_input, choice_input, main_loop

OPERADORES = {"+": add, "-": sub, "*": mul, "/": truediv}


def main():
    x = float_input("Ingrese un número: ", lang="es")
    operador = choice_input(tuple(OPERADORES.keys()), lang="es")
    y = float_input("Ingrese un número: ", lang="es")
    try:
        resultado = OPERADORES[operador](x, y)
        print(f"{x} {operador} {y} = {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")


if __name__ == "__main__":
    main_loop(main)
