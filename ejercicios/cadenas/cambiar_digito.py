"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dado un número N cambiar el dígito menor que tenga N por el dígito X
dado.

N = 654243
X = 5
Output: 654543

N = 9341615
X = 8
Output: 9348685

NOTE: if N is a string from the start, 'casintg' won't be used.
"""
import unittest


def sol_a(N: int, X: int) -> int:
    return int(str(N).replace(str(min(str(N))), str(X)))


def sol_b(N: int, X: int) -> int:
    return int("".join(
        x if int(x) != min(int(x) for x in str(N)) else str(X) for x in str(N)
    ))


def sol_c(N: int, X: int) -> int:
    n = [int(x) for x in str(N)]
    s = ""
    min_ = min(n)
    for i in range(len(n)):
        if n[i] == min_:
            n[i] = X
        s += str(n[i])
    return int(s)


class Test(unittest.TestCase):

    cases = (
        (654243, 5, 654543),
        (9341615, 8, 9348685),
        (121, 1, 121),
        (10201, 3, 13231)
    )
    solvers = sol_a, sol_b, sol_c

    def test_solvers(self):
        for f in self.solvers:
            for N, X, expected in self.cases:
                self.assertEqual(f(N, X), expected)


if __name__ == "__main__":
    unittest.main()
