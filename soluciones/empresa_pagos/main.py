"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import Menu
from prototools.colorize import magenta, cyan, red

from empresa import Empresa


def main():
    empresa = Empresa()
    menu = Menu(
        cyan("Menu"),
        exit_option_text=red("Salir"),
        exit_option_color=red,
    )
    menu.add_options(
        ("Agregar trabajadores", empresa.agregar),
        ("Mostrar Reporte", empresa.reporte),
        ("Eliminar trabajadores", empresa.eliminar),
    )
    menu.settings(
        style="double",
        color=magenta,
        options_color=cyan,
        header_bottom=True,
    )
    menu.run()


if __name__ == "__main__":
    main()