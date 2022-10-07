"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: Add testcases.
"""
import random
from typing import List


def hexacolors(size: int) -> List[str]:
    """Retorna una lista de colores (hexadecimal).

    :param size: Tamaño de la lista de colores
    :size type: int
    """
    return [
        "#"+"".join(random.choices("0123456789ABCDEF", k=6))
        for _ in range(size)
    ]


def hexcolors_alt(size: int) -> List[str]:
    """Retorna una lista de colores (hexadecimal).

    :param size: Tamaño de la lista de colores
    :size type: int
    """
    return [
        f"#{c[2:]}" for c in map(
            hex, random.choices(range(0xFFFFFF), k=size)
        )
    ]


def main():
    colors = hexacolors(10)  # or hexacolors_alt(10)
    print(colors)


if __name__ == "__main__":
    main()
