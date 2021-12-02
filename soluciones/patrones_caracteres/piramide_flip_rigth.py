"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Imprimir el patrón siguiente usando bucles:

    +---------------+
    | *             |
    | * *           |
    | * * *         |
    | * * * *       |
    | * * * * *     |
    | * * * *       |
    | * * *         |
    | * *           |
    | *             |
    +---------------+

NOTE: add testcases
"""
from unittest import main, TestCase


def naive():
    for i in range(5):
        for j in range(i+1):
            print("*", end="")
        print("")
    for i in range(4, 0, -1):
        for j in range(i):
            print("*", end="")
        print("")


def alt():
    n = 5
    c = "*"
    for i in range(1, n+1):
        print("*"*i)
    for i in range(n-1, 0, -1):
        print("*"*i)


def draw(n: int = 5, c: str = "* ") -> None:
    """Imprime una pirámide (rotada)

    :param n: Altura máxima de la pirámide
    :n type: int
    :param c: Caracter a imprimir
    :c type: str
    """
    for i in range(1, n+1):
        print(c*i)
    for i in range(n-1, 0, -1):
        print(c*i)


class Test(TestCase):

    def test_draw(self):
        NotImplementedError()


if __name__ == "__main__":
    # main()
    draw(5)