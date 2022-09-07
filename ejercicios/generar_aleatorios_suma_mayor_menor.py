"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Generar en forma aleatoria N números enteros en el rango -200 a 200.
Mostrar por pantalla:
- Los números generados
- La suma de los números pares negativos generados
- El mayor y menor número generado
- Cantidad de números generados con sólo dos dígitos
"""
import unittest
from typing import List
from random import randint, seed
# pip install prototools
from prototools import int_input


# https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/generar_aleatorios.py
def generar_aleatorios(
    min: int = 1,
    max: int = 100,
    size: int = 20
) -> List[int]:
    return [randint(min, max) for _ in range(size)]


def suma(numeros: List[int]) -> List[int]:
    return sum(list(filter(lambda x: x % 2 == 0, numeros)))


def f(numeros: List[int]) -> List[int]:
    return len(list(filter(lambda x: len(str(abs(x))) == 2, numeros)))


def main():
    n = int_input("Ingresar cantidad de números a generar: ", min=1)
    numeros = generar_aleatorios(-200, 200, n)
    print(f"Números generados: {numeros}")
    print(f"Suma de los números pares negativos generados: {suma(numeros)}")
    print(f"Mayor número generado: {max(numeros)}")
    print(f"Menor número generado: {min(numeros)}")
    print(f"Cantidad de números generados con sólo dos dígitos: {f(numeros)}")


class Test(unittest.TestCase):

    def test_generar(self):
        seed(60)
        self.assertEqual(generar_aleatorios(1, 10, 4), [5, 5, 10, 3])

    def test_suma(self):
        self.assertEqual(suma([1, 2, 3, 4, 5]), 6)

    def test_f(self):
        self.assertEqual(f([1, 20, 3, 4, 5]), 1)


if __name__ == "__main__":
    main()
    # unittest.main()
