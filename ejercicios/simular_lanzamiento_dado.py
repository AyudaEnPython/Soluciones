"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrollar un programa en el que un ordenador lanza N veces un dado y
cuenta cuantas veces el n° 4 y el n° 3 salen. Para efectuar el
lanzamiento del dado, debe importar la clase random.
"""
from random import randint
from typing import Dict


def simular_lanzamientos(n: int) -> Dict[int, int]:
    resultado = {k: 0 for k in range(1, 7)}
    for _ in range(n):
        resultado[randint(1, 6)] += 1
    return resultado


def main():
    n = int(input("Número de lanzamientos: "))
    resultado = simular_lanzamientos(n)
    print(f"n° 3: {resultado[3]}")
    print(f"n° 4: {resultado[4]}")


if __name__ == "__main__":
    main()
