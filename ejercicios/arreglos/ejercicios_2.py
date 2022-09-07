"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

1. Dado un vector cargado de elementos de tipo entero positivo y un
    número "X", imprimir el número más proximo a "X".
    Nota: Se debe asumir que todos los números son positivos y
    diferentes entre sí.

2. Dado un vector cargado de elementos de tipo entero, crear un segundo
    vector con los elementos que no se repiten y que sean múltiplos de
    tres. Finalmente imprimir el vector resultante.

3. Dado un vector cargado de elementos de tipo cadena, imprimir todas
    las palabras que contengan solo dos vocales diferentes.

4. Dados dos vectores de elementos de tipo entero, ordenar sus
    elementos de la siguiente forma: Números pares a la izquierda e
    impares a la derecha. Finalmente, imprimir el vector resultante.
"""
from random import randint, sample
from string import ascii_lowercase
from typing import List


def _random_string(k: int = 8, n: int = 10) -> List[str]:
    return ["".join(sample(ascii_lowercase, k)) for _ in range(n)]


def _random(min: int = 1, max: int = 100, n: int = 10) -> List[int]:
    return sample(range(min, max), n)


def main():
    v = _random()
    s = _random_string()
    print(f"Vector original: {v}")

    # ------------------------------------------------------------ Ejercicio 1
    x = randint(1, 100)
    print(f"Número X: {x}")
    print(f"Número más cercano: {min(v, key=lambda n: abs(n - x))}")

    # ------------------------------------------------------------ Ejercicio 2
    vr = [n for n in set(v) if n % 3 == 0]
    print(f"Vector resultante: {vr}")

    # ------------------------------------------------------------ Ejercicio 3
    print(f"Vector original: {s}")
    vd = [s for s in s if sum([s.count(x) for x in "aeiou"]) == 2]
    print(f"Palabras con dos vocales diferentes: {vd}")

    # ------------------------------------------------------------ Ejercicio 4
    vpi = sorted(v, key=lambda n: n % 2)
    print(f"Vector resultante: {vpi}")


if __name__ == "__main__":
    main()
