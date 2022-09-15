"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import sys
import unittest


def e():
    epsilon = 1
    while epsilon + 1 > 1:
        epsilon /= 2
    epsilon *= 2
    return epsilon


class TestEpsilon(unittest.TestCase):

    def test_epsilon(self):
        self.assertEqual(e(), sys.float_info.epsilon)


if __name__ == "__main__":
    unittest.main()
