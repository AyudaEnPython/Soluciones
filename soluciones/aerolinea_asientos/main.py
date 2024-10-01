"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import Menu
from prototools.colorize import cyan, magenta, yellow

from utils import (
    asientos_disponibles,
    comprar_pasaje,
    estadisticas,
    anular_venta,
    listar_pasajeros,
)


def main():
    asientos = [True] * 42
    pasajeros = {}
    menu = Menu(
        cyan("Alitas de Murciélago"),
        yellow("Ayuda en Python"),
        exit_option_text=magenta("Salir"),
        exit_option_color=magenta,
    )
    menu.add_options(
        ('Mostrar asientos disponibles',
            lambda: print(asientos_disponibles(asientos))),
        ('Comprar pasaje',
            lambda: comprar_pasaje(asientos, pasajeros)),
        ('Totales',
            lambda: print(estadisticas(asientos))),
        ('Anular venta',
            lambda: anular_venta(asientos, pasajeros)),
        ('Listado de pasajeros',
            lambda: listar_pasajeros(pasajeros)),
    )
    menu.settings(
        subtitle_align="center",
        style="double",
        color=magenta,
        separators=True,
    )
    menu.run()


if __name__ == '__main__':
    main()
