"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crear un programa en Python que permita al usuario ingresar:
- Los montos de las compras de un cliente (se desconce la cantidad de
    datos que se cargará, la cual puede cambiar en cada ejecución)
- Si ingresa un monto negativo, no se debe procesar y se debe pedir que
    ingrese un nuevo monto.

Al finalizar, informar:
- La cantidad y subtotal de cada producto ingresado.
- El total a pagar teniendo en cuenta que si las ventas superan el
    total de $10.000, se le debe aplicar 10% de descuento.
- Mostrar el monto a pagar con descuento y sin descuento.
"""
from typing import List, Tuple
# pip install prototools
from prototools import int_input, float_input, main_loop

UMBRAL = 20
DESCUENTO = 0.1


def ingresar() -> Tuple[List[int], List[float]]:
    cantidades, montos = [], []
    articulos = int_input("Cantidad de articulos: ")
    for _ in range(articulos):
        cantidad = int_input("Cantidad del producto: ")
        precio = float_input("Precio del producto: ")
        cantidades.append(cantidad)
        montos.append(cantidad * precio)
    return cantidades, montos


def calcular_descuento(monto: float) -> float:
    return {
        monto > UMBRAL: DESCUENTO,
        monto <= UMBRAL: 0,
    }[True] * monto


def main():
    cantidades, montos = ingresar()
    total = sum(montos)
    descuento = calcular_descuento(total)
    for cantidad, monto in zip(cantidades, montos):
        print(f"{cantidad} producto(s) a ${monto}")
    print(f"Monto a pagar sin descuento: {total}")
    print(f"Monto a pagar con descuento: {total - descuento}")


if __name__ == "__main__":
    main_loop(main)
