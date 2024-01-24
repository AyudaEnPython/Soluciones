"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english
speakers are welcome.

NOTE: Used the following link for the test_cases:
- https://en.wikipedia.org/wiki/Table_of_prime_factors
"""
import unittest


def prime_factors_list(n):
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


def prime_factors_dict(n):
    if n <= 1:
        return {}
    fs = {}
    while n % 2 == 0:
        fs[2] = fs.get(2, 0) + 1
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            fs[i] = fs.get(i, 0) + 1
            n //= i
        i += 2
    if n > 1:
        fs[n] = 1
    return fs


class TestPrimeFactors(unittest.TestCase):

    def setUp(self):
        self.test_cases_list = [
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
            (1234567890, [2, 3, 3, 5, 3607, 3803]),
            (600851475143, [71, 839, 1471, 6857]),
        ]
        self.test_cases_dict = [
            (n, {f: fs.count(f) for f in set(fs)})
            for n, fs in self.test_cases_list
        ]

    def run_test_cases(self, f, tests):
        for n, expected in tests:
            with self.subTest(n=n, expected=expected):
                self.assertEqual(f(n), expected)
    
    def test_prime_factors_list(self):
        self.run_test_cases(prime_factors_list, self.test_cases_list)

    def test_prime_factors_dict(self):
        self.run_test_cases(prime_factors_dict, self.test_cases_dict)


if __name__ == "__main__":
    unittest.main()
