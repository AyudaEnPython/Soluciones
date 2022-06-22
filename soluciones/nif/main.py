"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import Menu

from utils import Data, grabar, buscar, imprimir


def main():
    data: Data = {}
    menu = Menu()
    menu.add_options(
        ("Grabar", lambda: grabar(data)),
        ("Buscar", lambda: buscar(data)),
        ("Imprimir Certificados", lambda: imprimir(data)),
    )
    menu.run()


if __name__ == "__main__":
    main()
