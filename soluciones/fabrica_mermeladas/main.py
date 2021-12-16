"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import Menu

from sistema.fabrica import Fabrica


def main():
    menu = Menu()
    fabrica = Fabrica()
    menu.add_options(
        ("Ingresar ventas",
            fabrica.ingresar_ventas),
        ("Mostrar resúmenes totales",
            fabrica.resumenes_totales),
        ("Mostrar detalles por producto",
            fabrica.mostrar_detalles_por_producto),
        ("Mostrar detalles por tipo de envase",
            fabrica.mostrar_detalles_por_tipo_de_envase),
    )
    menu.run()


if __name__ == "__main__":
    main()