"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

output:

    +-------------+
    |    * * *    |
    |  *       *  |
    | *         * |
    | *         * |
    |  *       *  |
    |    * * *    |
    +-------------+

NOTE: add testcases
"""
from unittest import main, TestCase


def draw(r):
    c = "* "
    for i in range((2 * r) + 1):
        for j in range((2 * r)+1):
            dist = ((i - r) * (i - r) + (j - r) * (j - r)) ** (0.5)
            if (dist > r - 0.5 and dist < r + 0.5):
                print(c, end="")
            else:
                print(" " * 2, end="")     
        print()


class Test(TestCase):

    def test_draw(self):
        NotImplementedError()


if __name__ == "__main__":
    # main()
    draw(3)
