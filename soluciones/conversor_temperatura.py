"""Conversor de temperatura

TODO: add docstrings and typing.
"""
from prototools import menu
from prototools.menu import EzMenu
from prototools.entradas import entrada_float


def _fahrenheit_to_celsius(F):
    return (F - 32)*(5/9)


def _celsius_to_fahrenheit(C):
    return (C * 9/5)+32


def f_c():
    grados = entrada_float("Temperatura (°F): ")
    print(_fahrenheit_to_celsius(grados))


def c_f():
    grados = entrada_float("Temperatura (°C): ")
    print(_celsius_to_fahrenheit(grados))


if __name__ == "__main__":
    menu = EzMenu()
    menu.agregar_opciones("De F° a °C", "De °C a °F", "Salir")
    menu.agregar_funciones(f_c, c_f)
    menu.run()