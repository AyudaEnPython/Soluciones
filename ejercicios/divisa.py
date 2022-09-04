"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Solicitar una moneda (divisa) y el valor que quiere cambiar a dólar, el
sistema debe imprimir cuantos dolares son de acuerdo a la moneda.

Monedas => Mexico, Colombia, Chile, Argentina
"""
from typing import Dict
# pip install prototools
from prototools import menu_input, float_input

CONVERSION: Dict[str, float] = {
    "mexico": 0.049,
    "colombia": 0.00023,
    "chile": 0.0011,
    "argentina": 0.0072,
}


def converter(local: float, foreign: str) -> float:
    return round(local * CONVERSION[foreign], 2)


def main():
    print("Seleccionar la divisa local")
    pais = menu_input(tuple(CONVERSION), numbers=True)
    monto = float_input("Ingresar el monto: ", min=0)
    print(f"{pais.capitalize()}| {monto} -> $ {converter(monto, pais)}")


if __name__ == "__main__":
    main()
