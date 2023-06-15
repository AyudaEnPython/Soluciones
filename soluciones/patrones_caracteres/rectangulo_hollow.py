"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

input: 5
output:

    +-----------+
    | * * * * * |
    | *       * |
    | *       * |
    | *       * |
    | * * * * * |
    +-----------+

NOTE: add testcases
"""
import unittest


def draw(n: int, c: str="* ") -> None:
    for i in range(n):
        if i in (0, n-1):
            print(f"{c*n}")
        else:
            print(f"{c}{'  '*(n-2)}{c}")


class Test(unittest.TestCase):

    def test_draw(self):
        NotImplementedError()


if __name__ == "__main__":
    draw(5)
