"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import Menu
from empresa import Empresa


def main():
    empresa = Empresa()
    menu = Menu(exit_option_text="Salir")
    menu.add_options(
        ("Agregar trabajadores", empresa.agregar),
        ("Mostrar Reporte", empresa.reporte),
        ("Eliminar trabajadores", empresa.eliminar),
    )
    menu.settings(
        header_bottom=True,
    )
    menu.run()


if __name__ == "__main__":
    main()