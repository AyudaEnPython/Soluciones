"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crear un módulo que permita leer una cadena que representa los cálculos
que se deben hace respetando los niveles de los operadores con el 
módulo "operadores.py".
Mínimo debe permitir trabajar con 3 números e imprimir el resultado de
la operación.
En caso se ingrese un cadena que no se puede operar imprimir un mensaje
de error.
"""

from typing import Callable, Dict

from operadores import suma, resta, multiplicacion, division

op: Dict[str, Callable] = {
    "+": suma,
    "-": resta,
    "*": multiplicacion,
    "/": division,
}


def f(s: str) -> float:
    """Calcula la operación matématica representada en una cadena
    de texto

    :param s: Representacion de la operación matématica
    :s type: str
    :return: Resultado de la operación
    :rtype: float
    """
    if s.isdigit():
        return float(s)
    if s.islower():
        return "Error"
    for c in op:
        i, o, d = s.partition(c)
        if o in op:
            return op[o](f(i), f(d))


if __name__ == "__main__":
    entrada = input("> ")
    print(f(entrada))