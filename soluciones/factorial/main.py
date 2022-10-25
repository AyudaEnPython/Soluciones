"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest
from typing import Callable, Dict, List
from multiprocessing import Pool


def _factorial(arrs: List[int]) -> int:
    result = 1
    for arr in arrs:
        result *= arr
    return result


def factorial_sequential(n: int) -> int:
    result = 1
    for x in range(1, n + 1):
        result *= x
    return result


def factorial_recursive(n: int, d: Dict[int, int] = {0: 1}) -> int:
    if n not in d:
        d[n] = n * factorial_recursive(n - 1, d)
    return d[n]


def factorial_threads(n: int, f: Callable, workers: int):
    pool = Pool(processes=workers)
    xs = range(1, n+1)
    slices = [xs[i::workers] for i in range(workers)]
    chunks = pool.map(f, slices)
    pool.close()
    pool.join()
    result = 1
    for chunk in chunks:
        result *= chunk
    return result


class Test(unittest.TestCase):

    def test_sequential(self):
        self.assertEqual(factorial_sequential(5), 120)

    def test_recursive(self):
        self.assertEqual(factorial_recursive(5), 120)

    def test_threads(self):
        self.assertEqual(factorial_threads(5, _factorial, 5), 120)


if __name__ == "__main__":
    unittest.main()
