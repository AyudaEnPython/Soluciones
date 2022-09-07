"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrollar un programa en Python que permita ingresar N códigos. Debe
validar que no se ingrese un código duplicado, para ello debe crear
obligatoriamente una función que valide la duplicidad. Ejemplo de
diálogo de este programa:

    +---------------------------------------------------+
    | Ingrese total de códigos: 4                       |
    | Código 1: 125                                     |
    | Código 2: 100                                     |
    | Código 3: 125                                     |
    | Error, código duplicado                           |
    | Código 3: 63                                      |
    | Código 4: 75                                      |
    +---------------------------------------------------+

TODO: add testcases
"""
from typing import List


def validar_codigos(n: int) -> List[int]:
    """Valida que los códigos a ingresar no contengan duplicados.
    Retorna una lista de códigos sin duplicados.

    :param n: Cantidad de códigos
    :n type: int
    :return: Lista de códigos sin duplicados
    :rtype: List[int]
    """
    codigos = []
    i = 1
    while i <= n:
        codigo = int(input(f"Código {i}: "))
        if codigo in codigos:
            print("Error, código duplicado")
            continue
        codigos.append(codigo)
        i += 1
    return codigos


def main():
    n = int(input("Ingrese total de códigos: "))
    codigos = validar_codigos(n)
    print(codigos)


if __name__ == "__main__":
    main()
