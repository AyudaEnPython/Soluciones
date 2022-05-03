"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest


def to_upper(s: str) -> str:
    return "".join(chr(ord(c) ^ 0x20) for c in s)


class Test(unittest.TestCase):

    def test_to_upper(self):
        self.assertEqual(to_upper("abc"), "ABC")
        self.assertEqual(to_upper(""), "")


if __name__ == '__main__':
    unittest.main()
