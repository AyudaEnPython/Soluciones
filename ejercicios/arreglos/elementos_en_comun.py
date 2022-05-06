"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Leer y almacenar N números en una lista A, lo propio sobre otra lista
B y determine cuantos números de A se encuentran en B.

Sugerencia: Llenar las listas A y B empleando números al azar
    random.randrange().

NOTE: El enunciado no contempla números repetidos.
"""
from random import randrange

N = 10
f = lambda min, max: [randrange(min, max+1) for _ in range(N)]
g = lambda a, b: len(list(filter(lambda x: x in b, a)))


def main():
    A, B = f(0, 20), f(0, 20)
    print(f"A: {A}\nB: {B}")
    print(f"Números de A que se encuentran en B: {g(A, B)}")


if __name__ == "__main__":
    main()
