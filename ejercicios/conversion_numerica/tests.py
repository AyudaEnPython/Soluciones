"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from decimal_base import convert


tests = (
    ("28496", 10, {2: "110111101010000", 8: "67520", 16: "6F50"}),
    ("34526", 8, {2: "11100101010110", 8: "34526", 16: "3956"}),
)


class Test(unittest.TestCase):

    def test_convert(self):
        for n, b, d in tests:
            for k, r in d.items():
                self.assertEqual(convert(n, b, k), r)


if __name__ == "__main__":
    unittest.main()
