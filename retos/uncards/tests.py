"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: If there's an invalid character it'll be like a disqualified entry.
    That behavior could be changed if the rules were more specific.
"""
import unittest

from main import validate, sol


class Test(unittest.TestCase):

    def test_validate(self):
        self.assertEqual(validate("P1[@]CZ*[ol"), "P1[@]CZ*[ol")
        self.assertEqual(validate("P1[@]CZ*[ol_"), "!!!!!!!!!!!!")

    def test_validate_other(self):
        valid = "<=?Ad@[^"
        self.assertEqual(validate("?=A^", valid), "?=A^")
        self.assertEqual(validate("?=A^_", valid), "!!!!!")

    def test_sol(self):
        self.assertEqual(sol("P1[@]", "CZ*[ol"), "UDUDA")
        self.assertEqual(sol("CZ*[ol", "P1[@]"), "ADADU")
        self.assertEqual(sol("ro1", "]cP"), "UUU")
        self.assertEqual(sol("]cP", "ro1"), "AAA")

    def test_sol_defaults(self):
        defaults = "X", "Y", "E"
        self.assertEqual(sol("P1[@]", "CZ*[ol", defaults), "XEXEY")
        self.assertEqual(sol("CZ*[ol", "P1[@]", defaults), "YEYEX")
        self.assertEqual(sol("ro1", "]cP", defaults), "XXX")
        self.assertEqual(sol("]cP", "ro1", defaults), "YYY")


if __name__ == "__main__":
    unittest.main()
