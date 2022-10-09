"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import Menu, float_input
from typing import Callable


def datos(msg: str, f: Callable):
    data = float_input(msg)
    print(f(data))


def fahrenheit_to_celsius(F: float) -> float:
    return (F - 32)*(5/9)


def celsius_to_fahrenheit(C: float) -> float:
    return (C * 9/5)+32


def main():
    menu = Menu("Conversor de Temperatura")
    menu.add_options(
        ("Fahrenheit a Celsius",
            lambda: datos("Temperatura (°F): ", fahrenheit_to_celsius)),
        ("Celsius a Fahrenheit",
            lambda: datos("Temperatura (°C): ", celsius_to_fahrenheit)),
    )
    menu.run()


if __name__ == "__main__":
    main()
