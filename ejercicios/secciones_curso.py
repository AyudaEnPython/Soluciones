"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Implemente un algoritmo que solicite ingresar datos de las secciones
de un curso y lo guarda en un diccionario, considere lo siguiente:

- La clave es el código de la sección y el valor es la cantidad de
    alumnos inscritos.
- Se termina de ingresar los datos con un número negativo.
- Luego solicite ingresar una opción: a, b, x:
    Opción a: imprima la sección con más alumnos.
    Opción b: imprima la sección con menos alumnos.
    Opción x: termina el programa.

Algunos ejemplos de diálogo de este programa serían:

    +---------------------------------+
    | Seccion: 101                    |
    | Cantidad de alumnos: 29         |
    | Seccion: 102                    |
    | Cantidad de alumnos: 30         |
    | Seccion: 201                    |
    | Cantidad de alumnos: 25         |
    | Seccion: 202                    |
    | Cantidad de alumnos: 27         |
    | Seccion: -1                     |
    | Ingrese una opción (a, b, x): a |
    | Seccion con más alumnos: 102    |
    | Ingrese una opción (a, b, x): b |
    | Seccion con menos alumnos: 201  |
    | Ingrese una opción (a, b, x): x |
    +---------------------------------+
"""
from unittest import main, TestCase
from typing import Dict
# pip install prototools
from prototools import int_input, choice_input
from prototools.decorators import register, PLUGINS

MIN, MAX = 0, 50
opciones = ('a', 'b', 'x')


def ingresar_datos():
    """Ingresa los datos de las secciones"""
    datos = {}
    while True:
        codigo = int_input('Ingrese el código de la sección: ')
        if codigo < 0:
            break
        cantidad = int_input(
            'Ingrese la cantidad de alumnos: ', min=MIN, max=MAX
        )
        datos[codigo] = cantidad
    return datos


@register
def a(datos):
    """Devuelve el código de la sección con más alumnos"""
    return max(datos, key=datos.get)


@register
def b(datos):
    """Devuelve el código de la sección con menos alumnos"""
    return min(datos, key=datos.get)


def main_():
    datos = ingresar_datos()
    while True:
        opcion = choice_input(opciones, lang="es")
        if opcion == 'x':
            break
        print(PLUGINS[opcion](datos))


class Test(TestCase):

    data: Dict[int, int] = {101: 29, 102: 30, 201: 25, 202: 27}

    def test_maximo(self):
        self.assertEqual(a(self.data), 102)
    
    def test_minimo(self):
        self.assertEqual(b(self.data), 201)


if __name__ == '__main__':
    # main() # uncomment this line and comment the next one to run tests
    main_()