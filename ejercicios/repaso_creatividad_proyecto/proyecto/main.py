"""
Desarrolle herencia jerárquica en baase a una clase Poligono que tiene
métodos abstractos area() y perimetro(). Implemente la clase Triangulo,
Cuadrilatero, Pentagono, Hexagono y Octagono que extienda esta clase
base con los métodos area() y perimetro().
Tambien implemente la clase TrianguloIsoceles, TrianguloEquilatero,
Rectangulo y Cuadrado que tienen las relaciones de herencia apropiadas.
Finalmente escriba un programa sencillo que permita a los usuarios
crear poligonos de varios tipos introduciendo sus dimensiones
geométricas y el programa muestre el área y el perímetro.
"""
from models import (
    Triangulo,
    Cuadrilatero,
    Pentagono,
    Hexagono,
    Octagono,
    TrianguloIsoceles,
    TrianguloEquilatero,
    Cuadrado,
    Rectangulo
)
from utils import ingresar_datos_base_altura, ingresar_datos_lado
from prototools.menu import EzMenu


def main():
    menu = EzMenu()
    menu.agregar_opciones(
        "Triangulo",
        "Cuadrilatero",
        "Pentagono",
        "Hexagono",
        "Octagono",
        "TrianguloIsoceles",
        "TrianguloEquilatero",
        "Cuadrado",
        "Rectangulo",
        "Salir"
    )
    menu.agregar_funciones(
        lambda: ingresar_datos_base_altura(Triangulo),
        lambda: ingresar_datos_base_altura(Cuadrilatero),
        lambda: ingresar_datos_lado(Pentagono),
        lambda: ingresar_datos_lado(Hexagono),
        lambda: ingresar_datos_lado(Octagono),
        lambda: ingresar_datos_base_altura(TrianguloIsoceles),
        lambda: ingresar_datos_lado(TrianguloEquilatero),
        lambda: ingresar_datos_lado(Cuadrado),
        lambda: ingresar_datos_base_altura(Rectangulo),
    )
    menu.run()


if __name__ == "__main__":
    main()