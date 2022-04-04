"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List
from prototools import main_loop, int_input, textbox, tabulate


def tabla_de_multiplicar(n: int) -> List[List[str]]:
    return [[f"{n}", "x", f"{i:02}", "=", f"{n*i:02}"] for i in range(1, 13)]


def main():
    n = int_input("Ingrese un número: ", min=1, max=13)
    textbox(f"Tabla de multiplicar del número {n}", width=40)
    print(tabulate(tabla_de_multiplicar(n), headless=True))


if __name__ == "__main__":
    main_loop(main)
