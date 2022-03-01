"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import int_input, magenta, show_matrix, textbox
from prototools.colorize import cyan, green, red

from utils import MIN, MAX, Aleatorios


class Vista:

    @staticmethod
    def show(items: Aleatorios) -> None:
        print(", ".join(map(str, items)))

    @staticmethod
    def read(msg: str) -> int:
        return int(input(msg))

    @staticmethod
    def info(msg: str) -> None:
        print(msg)


class VistaFancy:

    @staticmethod
    def show(items: Aleatorios) -> None:
        if len(items) < 1:
            textbox(red("No hay datos para mostrar."))
        else:
            show_matrix(items, color=magenta)

    @staticmethod
    def read(msg: str) -> int:
        return int_input(cyan(msg), min=MIN, max=MAX)

    @staticmethod
    def info(msg: str) -> None:
        textbox(green(msg), bcolor="green")
