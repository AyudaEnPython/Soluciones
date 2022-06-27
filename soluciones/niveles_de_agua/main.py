"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
from typing import List


MIN, MAX = 0, 50
DIAS = 365
LIMITE = 5


def get_data(n = DIAS):
    return [int(input("> ")) for _ in range(n)]


def niveles(dias: int):
    return [randint(MIN, MAX) for _ in range(dias)]


def promedio_int(xs: List[int]) -> int:
    return int(sum(xs) / len(xs))


def fuera_de_rango(xs: List[int], limite: int) -> List[int]:
    return sorted([i for i, x in enumerate(xs) if x > limite])


def main():
    # dias = get_data()
    dias = niveles(DIAS)
    promedio = promedio_int(dias)
    dias_fuera_de_rango = fuera_de_rango(dias, promedio + LIMITE)
    print(f"Días: {dias}")
    print(f"Promedio: {promedio}")
    print(f"Días fuera de rango: {dias_fuera_de_rango}")


if __name__ == "__main__":
    main()
