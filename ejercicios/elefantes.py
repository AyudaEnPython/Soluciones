"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Entrada:

La entrada comienza con una línea que contiene un valor positivo que
corresponde a la capacidad máxima de carga de la telaraña en kgs. Luego
sigue una línea que contiene un valor entero positivo N que corresponde
a la cantidad de elefantes sobre los que se tiene datos. Luego siguen N
líneas, cada una con un valor positivo correspondiente al peso en kgs
de cada elefante.

Salida:

La salida contiene una única línea con la cantidad máxima de elefantes
que soporta la telaraña sin romperse considerando que los elefantes
deben subirse uno a uno y en el orden que aparece en la entrada. Los
datos de entrada garantizan que eventualmente la telaraña se rompe por
lo que esa cantidad siempre será inferior a N.


    +---------+--------+
    | Entrada | Salida |
    +---------+--------+
    | 1000    | 4      |
    | 5       |        |
    | 100     |        |
    | 200     |        |
    | 300     |        |
    | 400     |        |
    | 500     |        |
    +---------+--------+
    | 500     |        |
    | 3       |        |
    | 450     |        |
    | 350     |        |
    | 250     |        |
    +---------+--------+
"""
from unittest import main, TestCase


def get_data():
    return int(input()), int(input())


def solucion_a():
    m, n = get_data()
    e = 0
    for i in range(n):
        e += int(input())
        if e > m:
            break
    print(i)


def solucion_b():
    m, n = get_data()
    i = e = 0
    while i < n:
        e += int(input())
        if e > m:
            break
        i += 1
    print(i)


def solver(m, n, data): # edge cases
    if m == 1 and n == 1:
        return 1
    e = 0
    for i in range(n):
        e += data[i]
        if e > m:
            break
    return i


class Test(TestCase):

    def test_solver(self):
        self.assertEqual(solver(1000, 5, [100, 200, 300, 400, 500]), 4)
        self.assertEqual(solver(500, 3, [450, 350, 250]), 1)
        self.assertEqual(solver(0, 1, [0]), 0)
        self.assertEqual(solver(1, 1, [1]), 1)


if __name__ == '__main__':
    # main() # uncomment and comment the next line to run tests
    solucion_a()
