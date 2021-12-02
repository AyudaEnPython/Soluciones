"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

output:

    +-----------+
    |     *     |
    |    * *    |
    |   * * *   |
    |  * * * *  |
    | * * * * * |
    +-----------+

NOTE: add testcases
"""
from unittest import main, TestCase


def draw(n: int = 5, c: str = "* ") -> None:
    """Imprime una pirámide

    :param n: Altura máxima de la pirámide
    :n type: int
    :param c: Caracter a imprimir
    :c type: str
    """
    for i in range(1, n+1):
        print(" "*(n - i) + c*i)


class Test(TestCase):

    def test_draw(self):
        NotImplementedError()


if __name__ == "__main__":
    # main()
    draw(5)