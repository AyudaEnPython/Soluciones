"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import choice
# pip install prototools
from prototools import clear_screen, write_letters_custom, Menu
from prototools.colorize import red, green, yellow, blue, magenta, cyan
from prototools.keyboard import move_arrow

COLORS = red, green, yellow, blue, magenta, cyan
_T = {"s": "", "x": 0}


def f(x, _):
    _T["x"] += x
    len_ = len(_T["s"])
    if _T["x"] > len_:
        _T["x"] = 0
    elif _T["x"] < 0:
        _T["x"] = len_
    clear_screen()
    write_letters_custom(_T["s"], _T["x"], choice(COLORS))


def main():
    _T["s"] = input("> ")
    clear_screen()
    write_letters_custom(_T["s"], 0, red)
    move_arrow(f)


if __name__ == "__main__":
    menu = Menu()
    menu.add_options(
        ("Ingresar frase", main)
    )
    menu.run()
