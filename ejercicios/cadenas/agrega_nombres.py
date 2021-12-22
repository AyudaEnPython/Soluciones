"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Definir una función denominada “agrega_nombres” que reciba dos
parámetros: una lista de nombres y una tupla de tuplas. Cada componente
de la tupla contiene una tupla con dos componentes (cadenas de
caracteres) que representan un nombre y un apellido. La función deberá
agregar a la lista de nombres, los nombres de las tuplas que falten en
la lista. Debe devolver un número entero que represente la cantidad de
nombres que se agregaron a la lista.

NOTE: El enunciado no es claro.
"""
from typing import List, Tuple
from unittest import main, TestCase


# NOTE: Mutabilidad de lista.
def agrega_nombres(nombres: List[str], datos: Tuple[Tuple[str, str]]) ->int:
    agregados = 0
    for nombre, _ in datos:
        if nombre not in nombres:
            agregados += 1 
            nombres.append(nombre)
    return agregados


def main_():
    nombres = ["John", "Paul", "George"]
    datos = (("John", "Lennon"), ("George", "Harrison"), ("Ringo", "Starr"))
    print(f"Cantidad de nombres agregados: {agrega_nombres(nombres, datos)}")


class Test(TestCase):

    def test_agregar_nombres(self):
        self.assertEqual(
            agrega_nombres(
                ["Ramiro", "Alexa"],
                (("Ana", "Suarez"), ("Ramiro", "Lin")),
                ), 
            1
        )
        self.assertEqual(
            agrega_nombres(
                [],
                (("Alejandra", "Suarez"), ("Ramiro", "Lin")),
            ),
            2
        )


if __name__ == "__main__":
    main()
    #main_()