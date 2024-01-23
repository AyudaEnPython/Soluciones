"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

output:

    +-----------+
    | * * * * * |
    |  * * * *  |
    |   * * *   |
    |    * *    |
    |     *     |
    |    * *    |
    |   * * *   |
    |  * * * *  |
    | * * * * * |
    +-----------+

NOTE: add testcases
"""
import unittest


def draw(n: int = 5, c: str = "* ") -> None:
    """Imprime una pirámide

    :param n: Altura máxima de la pirámide
    :n type: int
    :param c: Caracter a imprimir
    :c type: str
    """
    for i in range(n, 0, -1):
        print(" "*(n - i) + c*i)
    for i in range(1, n+1):
        print(" "*(n - i) + c*i)


def draw_str(n: int = 5, c: str = "* ") -> str:
    """Imprime una pirámide

    :param n: Altura máxima de la pirámide
    :n type: int
    :param c: Caracter a imprimir
    :c type: str
    """
    r = [" "*(n - i) + c*i for i in range(n, 0, -1)]
    return "\n".join(r + r[::-1])


class Test(unittest.TestCase):

    def test_draw(self):
        NotImplementedError()


if __name__ == "__main__":
    # unittest.main()
    print(draw(5))