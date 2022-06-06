"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Definir la función dummy() que dada una lista como argumento permita
genera listas de 1 y 0 por cada uno de los valores.

Ejemplo:
dummy(["rojo", "verde", "verde", "azul"]) = [
    [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1]
]

En el primer caso está evaluando el valor "rojo", por ello el resultado
es [1, 0, 0, 0] porque el primer elemento es rojo y los demás no. En el
segundo caso evalua "verde", por ello el resultado es [0, 1, 1, 0]
porque el segundo y tercer elemento son verde y los demás no.
Finalmente ocurre de la misma forma para "azul".
"""
from typing import Any, List


def dummy(data: List[Any], t: Any = 1, f: Any = 0) -> List[List[int]]:
    return [
        [t if x == y else f for x in data]
        for y in sorted(set(data), key=data.index)
    ]


if __name__ == "__main__":
    colors = ["rojo", "verde", "verde", "azul"]
    print(dummy(colors))
