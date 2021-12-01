"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

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
from prototools import Menu


def main():
    menu = Menu()
    menu.add_options(
        ("Triángulo",
            lambda: ingresar_datos_base_altura(Triangulo)),
        ("Cuadrilátero",
            lambda: ingresar_datos_base_altura(Cuadrilatero)),
        ("Pentágono",
            lambda: ingresar_datos_lado(Pentagono)),
        ("Hexágono",
            lambda: ingresar_datos_lado(Hexagono)),
        ("Octágono",
            lambda: ingresar_datos_lado(Octagono)),
        ("Triángulo Isósceles",
            lambda: ingresar_datos_base_altura(TrianguloIsoceles)),
        ("Triángulo Equilátero",
            lambda: ingresar_datos_lado(TrianguloEquilatero)),
        ("Cuadrado",
            lambda: ingresar_datos_lado(Cuadrado)),
        ("Rectángulo",
            lambda: ingresar_datos_base_altura(Rectangulo))
    )
    menu.run()


if __name__ == "__main__":
    main()