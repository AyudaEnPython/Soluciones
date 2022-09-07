"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Cree una función que muestre en pantalla los nombres de los vehículos
que cumplan con un criterio de búsqueda dado por el usuario. El usuario
debe seleccionar si desea filtrar por fuerza o precio, y luego pedirle
un valor. La función debe mostrar en pantalla aquellos vehículos que
tengan un valor igual o superior al indicado por el usuario.

    +-----------------------------------------------------------+
    | referencia = [                                            |
    |   "DeLorean", "Mustang", "i8", "5008", "C300", "Model X"] |
    | fuerza = [130, 1200, 228, 120, 255, 259]                  |
    | precio = [25000, 35630, 148500, 37000, 41400, 105000]     |
    +-----------------------------------------------------------+
"""
from typing import List

vehiculos = ["DeLorean", "Mustang", "i8", "5008", "C300", "Model X"]
fuerza = [130, 1200, 228, 120, 255, 259]
precio = [25000, 35630, 148500, 37000, 41400, 105000]


def filtrar(c: str, v: int, r: List[str] = vehiculos) -> List[str]:
    """Devuelve los vehículos que cumplan con el criterio dado.

    :param c: criterio
    :c type: str
    :param v: valor a comparar
    :v type: int
    :param r: lista de vehículos
    :r type: List[str]
    :return: lista de vehículos que cumplan con el criterio dado
    :rtype: List[str]
    """
    return [r[i] for i in range(len(c)) if c[i] >= v]


def mostrar(resultado: List[str]) -> None:
    """Muestra los vehículos en pantalla.

    :param resultado: lista de vehículos filtrados
    :resultado type: List[str]
    :rtype: None
    """
    print(*resultado, sep="\n")


def main():
    criterio = input("Ingresar criterio -> (f)uerza o (p)recio: ").lower()
    if criterio not in "fp":
        print("Criterio inválido")
    else:
        valor = input("Ingresar valor: ")
        try:
            valor = int(valor)
            mostrar(filtrar(fuerza if criterio == "f" else precio, valor))
        except ValueError:
            print("Valor inválido")


if __name__ == "__main__":
    main()
