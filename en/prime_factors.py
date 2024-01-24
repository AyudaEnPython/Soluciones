"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english
speakers are welcome.

NOTE: Used the following link for the test_cases:
- https://en.wikipedia.org/wiki/Table_of_prime_factors
"""
import unittest


def prime_factors(n):
    fs = []
    while n % 2 == 0:
        fs.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            fs.append(i)
            n = n // i
    if n > 2:
        fs.append(n)
    return fs


class TestPrimeFactors(unittest.TestCase):

    def test_prime_factors(self):
        test_cases = [
            (1, []),
            (2, [2]),
            (3, [3]),
            (4, [2, 2]),
            (5, [5]),
            (12, [2, 2, 3]),
            (29, [29]),
            (99, [3, 3, 11]),
            (186, [2, 3, 31]),
            (331, [331]),
            (666, [2, 3, 3, 37]),
            (780, [2, 2, 3, 5, 13]),
            (1000, [2, 2, 2, 5, 5, 5]),
            (1024, [2] * 10),
            (1234567890, [2, 3, 3, 5, 3607, 3803])
            (600851475143, [71, 839, 1471, 6857])
        ]
        for n, expected in test_cases:
            with self.subTest(n=n, expected=expected):
                self.assertEqual(prime_factors(n), expected)


if __name__ == "__main__":
    unittest.main()
