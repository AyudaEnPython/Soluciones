"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Implemente un algoritmo, usando una función recursiva, que resuelva la
siguiente sumatoria:

    E(n, p) = 1**p + 2**p + 3**p + 4**p + ... + n**p

- El programa debe pedir al usuario que ingrese un número n, y el
    número p.
- Luego debe calcular el valor de E(n, p) usando una función recursiva.
- Al final del código en un comentario, analize y escriba la
    complejidad algorítmica de su código.

Algunos ejemplos del diálogo de este programa serían:

    +-----------------------------------------+
    | Input n: 2                              |
    | Input p: 1                              |
    | Output: 3                               |
    +-----------------------------------------+

    +-----------------------------------------+
    | Input n: 4                              |
    | Input p: 2                              |
    | Output: 30                              |
    +-----------------------------------------+
"""
from unittest import main, TestCase
# Ejercicio idéntico a:
# https://github.com/AyudaEnPython/Soluciones/blob/main/ejercicios/recursion/sumatoria.py
# solo cambia la multiplicación por potencia (retorno del caso base cambia a 1)


def E(n: int, p: int) -> int: # Big O -> O(n)
    if n == 1:
        return 1
    else:
        return n**p + E(n-1, p)


def main_():
    n = int(input("Input n: "))
    p = int(input("Input p: "))
    print(f"Output: {E(n, p)}")


class Test(TestCase):

    def test_E(self):
        self.assertEqual(E(2, 1), 3)
        self.assertEqual(E(4, 2), 30)


if __name__ == '__main__':
    #main() # uncomment this line and comment the next one to run the test
    main_()