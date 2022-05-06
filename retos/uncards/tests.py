"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from main import validate, sol


class Test(unittest.TestCase):

    def test_validate(self):
        self.assertEqual(validate("P1[@]CZ*[ol"), "P1[@]CZ*[ol")
        with self.assertRaises(ValueError):
            validate("P1[@]CZ*[ol_")

    def test_validate_other(self):
        valid = "<=?Ad@[^"
        self.assertEqual(validate("?=A^", valid), "?=A^")
        with self.assertRaises(ValueError):
            validate("?=A^$_", valid)

    def test_sol(self):
        self.assertEqual(sol("P1[@]", "CZ*[ol"), "UDUDA")
        self.assertEqual(sol("ro1", "]cP"), "UUU")

    def test_sol_defaults(self):
        defaults = "X", "Y", "E"
        self.assertEqual(sol("P1[@]", "CZ*[ol", defaults), "XEXEY")
        self.assertEqual(sol("ro1", "]cP", defaults), "XXX")


if __name__ == "__main__":
    unittest.main()
