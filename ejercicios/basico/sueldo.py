"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Un vendedor recibe un sueldo base más un 10% extra por comisión de sus
ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de
comisiones por las tres ventas que realiza en el mes y el total que
recibirá en el mes tomando en cuenta su sueldo base y comisiones.
"""
# pip install prototools
from prototools import float_input

VENTAS, EXTRA = 3, 0.1


def main():
    sueldo_base = float_input("Ingrese el sueldo base: ")
    ventas = [float_input(f"Ingrese la venta {i+1}: ") for i in range(VENTAS)]
    comision = sum(ventas) * EXTRA
    print(f"La comisión por las ventas es: {comision}")
    print(f"El sueldo total es: {sueldo_base + comision}")


if __name__ == "__main__":
    main()
