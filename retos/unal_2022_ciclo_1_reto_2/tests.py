"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from main import sol


class Test(unittest.TestCase):

    cases = (
        (  "OPL",   "TDA", "FINQSWDCVFOROQITVRZ", "DDDDDDPPPPDDMMMDDDD"),
        ("LPBJU", "EZYHX", "XPSVHVORFURKEIMGLCB", "PDDDPPPPPDDDPPPPDDM"),
    )

    def test_sol(self):
        for a, b, s, expected in self.cases:
            with self.subTest(a=a, b=b, s=s):
                self.assertEqual(sol(a, b, s), expected)


if __name__ == "__main__":
    unittest.main()
