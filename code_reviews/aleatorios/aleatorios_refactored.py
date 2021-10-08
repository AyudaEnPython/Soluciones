from random import randint
from typing import List


def aleatorios(min: int = 1, max: int = 100, size: int = 20) -> List[int]:
    return [randint(min, max) for _ in range(randint(min, size))]


def suma(numeros: List[int]) -> int:
    return sum(numeros)


if __name__ == "__main__":
    print(suma(aleatorios()))