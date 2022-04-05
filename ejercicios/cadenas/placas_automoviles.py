"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dadas N placas de automóvil, obtener la cantidad de placas que
contienen una secuencia determinada SEC de caracteres. Construya
el algoritmo.

Ejemplo:

Si N = 4 Placas: 649XGT, 1365SDG, 6789ERT, 1267SDG  SEC = "SDG"
Entonces: Cantidad de placas = 2
"""
from typing import List


def contar_placas(placas: List[str], secuencia: str) -> int:
    """
    >>> placas = ["649XGT", "1365SDG", "6789ERT", "1267SDG"]
    >>> contar_placas(placas, "SDG")
    2
    """
    return len([placa for placa in placas if secuencia in placa])


def main():
    n = int(input("Número de placas: "))
    placas = [input(f"Placa N° {i}: ") for i in range(1, n + 1)]
    secuencia = input("Secuencia: ")
    print(f"Cantidad de placas: {contar_placas(placas, secuencia)}")


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    main()
