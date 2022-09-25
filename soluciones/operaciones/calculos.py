"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Callable
from operaciones import suma, resta, multiplicacion, division
from utils import ingresar_numero
# pip install prototools
from prototools import Menu


def _numeros(operacion: Callable) -> None:
    x: float = ingresar_numero("Ingrese el primer número: ")
    y: float = ingresar_numero("Ingrese el segundo número: ")
    print(f"Resultado: {operacion(x, y)}")


def main():
    menu = Menu()
    menu.add_options(
        ("Sumar", lambda: _numeros(suma)),
        ("Restar", lambda: _numeros(resta)),
        ("Multiplicar", lambda: _numeros(multiplicacion)),
        ("Dividir", lambda: _numeros(division)),
    )
    menu.run()


if __name__ == '__main__':
    main()
