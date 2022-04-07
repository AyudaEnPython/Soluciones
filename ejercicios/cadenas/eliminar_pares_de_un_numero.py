"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Eliminar los números pares de un número.

123456789 -> 13579
125234334 -> 15333

NOTE: if N is a string from the start, 'casintg' won't be used.
"""
import unittest


def sol_a(N: int) -> int:
    return int(str(N).
        replace('0', '').
        replace('2', '').
        replace('4', '').
        replace('6', '').
        replace('8', '')
    )


def sol_b(N: int) -> int:
    return int(''.join(x for x in str(N) if int(x) % 2 != 0))


def sol_c(N: int) -> int:
    n = str(N)
    s = ""
    for i in range(len(n)):
        if int(n[i]) % 2 != 0:
            s += n[i]
    return int(s)


class Test(unittest.TestCase):

    cases = (
        (123456789, 13579),
        (125234334, 15333),
        (2451983, 5193),
    )
    solvers = sol_a, sol_b, sol_c

    def test_solvers(self):
        for f in self.solvers:
            for N, expected in self.cases:
                self.assertEqual(f(N), expected)


if __name__ == "__main__":
    unittest.main()
