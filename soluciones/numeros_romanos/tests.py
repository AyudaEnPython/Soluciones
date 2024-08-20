"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest

from models import Number


class TestNumber(unittest.TestCase):

    def setUp(self):
        self.n = Number(10)
        self.invalid_entries = -10, "ABC", "IM"
        self.valid_entries = {
            1987: (1987, "MCMLXXXVII"),
            "2": (2, "II"),
            "MCMXCIX": (1999, "MCMXCIX"),
        }

    def test_init_(self):
        for k, (v, r) in self.valid_entries.items():
            n = Number(k)
            self.assertEqual(n.value, v)
            self.assertEqual(n.roman, r)
        for i in self.invalid_entries:
            with self.assertRaises(ValueError):
                Number(i)

    def test_is_valid_roman(self):
        for s in ("IX", "X", "MCM", "LVI"):
            self.assertTrue(Number.is_valid_roman(s))
        for s in ("IIII", "VV", "IVI", "LL"):
            self.assertFalse(self.n.is_valid_roman(s))

    def test_convert(self):
        cases = 10, "10", "X"
        for value in cases:
            result = self.n._convert(value)
            self.assertEqual(result, 10)

    def test_to_roman(self):
        cases = {10: "X", 1987: "MCMLXXXVII", 3999: "MMMCMXCIX"}
        for value, expected in cases.items():
            result = self.n._to_roman(value)
            self.assertEqual(result, expected)

    def test_to_int(self):
        cases = {"X": 10, "MCMLXXXVII": 1987, "MMMCMXCIX": 3999}
        for roman, expected in cases.items():
            result = self.n._to_int(roman)
            self.assertEqual(result, expected)

    def test_output(self):
        expected_output = f"Integer: {self.n.value} | Roman: {self.n.roman}"
        self.assertEqual(str(self.n), expected_output)

    def test_add(self):
        x, y = Number(10), Number(20)
        a, b, c = Number("V"), Number("MCMXCIX"), Number("I")
        expected = ((30, "XXX"), (15, "XV"), (15, "XV"), (2000, "MM"))
        for n, (v, r) in zip((x + y, x + 5, x + a, b + c), expected):
            self.assertEqual(n.value, v)
            self.assertEqual(n.roman, r)

    def test_errors(self):
        for other in ("ABC", -5, 3990):
            with self.assertRaises(ValueError):
                self.n + other
        for other in (3.14, 3+2j, b'0101'):
            with self.assertRaises(TypeError):
                self.n + other

    def test_validate_boundaries(self):
        valid_values = 0, 1, 3999
        invalid_values = -1, 4000
        for value in valid_values:
            try:
                Number._validate_boundaries(value)
            except ValueError:
                self.fail(
                    f"_validate_boundaries raised ValueError"
                    f" unexpectedly for value: {value}"
                )
        for value in invalid_values:
            with self.assertRaises(ValueError):
                Number._validate_boundaries(value)


if __name__ == '__main__':
    unittest.main()
