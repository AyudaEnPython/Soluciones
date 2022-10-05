"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from modelos import Punto
from utils import crear_coordenadas, mostrar, crear_coordenadas_usuario


def main():
    coordenadas = crear_coordenadas(Punto)
    mostrar(coordenadas)


def main_alt():
    coordenadas = crear_coordenadas_usuario(Punto)
    mostrar(coordenadas)


if __name__ == "__main__":
    main()
    # main_alt()
