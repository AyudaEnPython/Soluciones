"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrolle un algoritmo en Python que permita solicitar a un usuario
números enteros (positivos o negativos) que se almacenará en una lista
N cantidad de veces. Si usted introduce el número 0, el algoritmo
dejará de almacenar elementos en la lista (el 0, (cero) no deberá ser
parte de esa lista).
Una vez ingresado el 0 (cero) mostrará por pantalla, la lista con los
números ingresados y preguntará al usuario si quiere eliminar alguno de
estos. Si el número ingresado se encuentra, lo eliminará y mostrará
nuevamente la lista actualizada. En caso de que no exista el número que
el usuario ingresa por teclado, mostrará un mensaje. "El número
ingresado no está en la lista".
"""
from typing import List
# pip install prototools
from prototools import int_input, bool_input


def _buscar(xs: List[int], x: int) -> bool:
    if x in xs:
        return True
    return False


def ingresar_numeros(n: int) -> List[int]:
    xs = []
    i = 0
    while i < n:
        x = int_input("Ingrese un número: ", lang="es")
        if x == 0:
            break
        elif _buscar(xs, x):
            print("El número ya está en la lista.")
        else:
            xs.append(x)
            i += 1
    return xs


def eliminar(xs: List[int], x: int) -> List[int]:
    if _buscar(xs, x):
        xs.remove(x)
        print(f"El número {x} fue eliminado de la lista.")
        print("Lista actualizada:", xs)
        return xs
    else:
        print("El número ingresado no está en la lista.")
        return xs


def main():
    n = int_input("Ingresar N: ", min=1, lang="es")
    numeros = ingresar_numeros(n)
    print("Numeros ingresados:", numeros)
    opcion = bool_input(
        "Desea eliminar algún número? (s/n): ",
        true_value="s",
        false_value="n",
        lang="es",
    )
    if opcion:
        n = int_input("Ingrese un número: ")
        numeros = eliminar(numeros, n)
    else:
        print("No se eliminarán números")


if __name__ == "__main__":
    main()
