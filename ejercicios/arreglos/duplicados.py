"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Sea una lista con palabras, escribir el código Python correspondiente,
para eliminar duplicados en la lista conservando el orden de los
elementos:

Ejemplo:

miLista = ["uno", "dos", "tres", "uno", "cuatro"]
resultado = ["uno", "dos", "tres", "cuatro"]

Sugerencia: Crear una nueva lista sin duplicados.
"""
from typing import Any, List


def sol_a(arr: List[Any]) -> List[Any]:
    t = []
    for el in arr:
        if el not in t:
            t.append(el)
    return t


def sol_b(arr: List[Any]) -> List[Any]:
    return sorted(list(set(arr)), key=arr.index)


def sol_c(arr: List[Any]) -> List[Any]:
    return list(dict.fromkeys(arr))


def sol_d(arr: List[Any]) -> List[Any]:
    return [*{*arr}] # not ordered


def main():
    numeros = ["uno", "dos", "tres", "uno", "cuatro"]
    print(sol_a(numeros))
    # print(sol_b(numeros))
    # print(sol_c(numeros))
    # print(sol_d(numeros))


if __name__ == "__main__":
    main()
