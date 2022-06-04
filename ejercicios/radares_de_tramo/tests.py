"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from main import sol, MENSAJES


class Test(unittest.TestCase):

    cases = (
        (9165, 110, 300),
        (9165, 110, 299),
        (12000, 100, 433),
        (12000, 100, 431),
        (12000, 100, 359),
        (-1000, -50, -100),
    )
    expected = (
        MENSAJES[0],
        MENSAJES[1],
        MENSAJES[0],
        MENSAJES[1],
        MENSAJES[2],
        MENSAJES[3],
    )

    def test_sol(self):
        for (e, p, t), expected in zip(self.cases, self.expected):
            self.assertEqual(sol(e, p, t), expected)


if __name__ == "__main__":
    unittest.main()
