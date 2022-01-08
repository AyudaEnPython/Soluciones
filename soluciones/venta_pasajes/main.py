"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import Menu

from ventas import Gestor
from database import VentaDAO


def main():
    menu = Menu()
    ventas = Gestor(VentaDAO())
    menu.add_options(
        ("Registrar Venta", ventas.registrar),
        ("Modificar Venta", ventas.modificar),
        ("Eliminar Venta", ventas.eliminar),
        ("Seleccionar Venta", ventas.seleccionar),
    )


if __name__ == '__main__':
    main()