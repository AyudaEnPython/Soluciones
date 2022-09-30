"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import Menu

from empresa import Empresa


def main():
    empresa = Empresa()
    menu = Menu("TecnoMamba")
    menu.add_options(
        ("Ingresar pedidos", empresa.ingresar_pedidos),
        ("Mostrar importe", empresa.mostrar_importe),
    )
    menu.settings(
        header_bottom=True,
    )
    menu.run()


if __name__ == "__main__":
    main()
