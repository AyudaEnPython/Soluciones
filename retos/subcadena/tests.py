"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest
# pip install prototools
from prototools import time_functions

from main import (
    count_substrings_a,
    count_substrings_b,
    count_substrings_c,
    count_substrings_d,
)


def test_functions():
    fs = {
        "count_substrings_a": count_substrings_a, # 0.1882
        "count_substrings_b": count_substrings_b, # 3.8251
        "count_substrings_c": count_substrings_c, # 4.2536
        "count_substrings_d": count_substrings_d, # 2.3407
    }
    time_functions(
        fs,
        args=(
            "CDCABCDCCDCDCCDCABCCDC",
            "CDC",
        ),
        globals=globals(),
    )


class Test(unittest.TestCase):

    def test_functions(self):
        self.assertEqual(
            count_substrings_a("CDCABCDCCDCDCCDCABCCDC", "CDC"), 5) # expected
        self.assertEqual(
            count_substrings_b("CDCABCDCCDCDCCDCABCCDC", "CDC"), 6)
        self.assertEqual(
            count_substrings_c("CDCABCDCCDCDCCDCABCCDC", "CDC"), 6)
        self.assertEqual(
            count_substrings_d("CDCABCDCCDCDCCDCABCCDC", "CDC"), 6)


if __name__ == "__main__":
    unittest.main()
    # test_functions()