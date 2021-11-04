"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from unittest import main, TestCase

from solution import _main


class Test(TestCase):

    data = (
        [5, 3, 0, 3, 0, 0, 0, 0, 0, 1],
        [3, 3, 3, 0, 1],
        [1, 2, 3],
        [3, 3, 3],
        [1, 1, 1, 1],
        [100_000, 100_000],
        [5, 3, 0, 3, 7, 10, 0, 0, 1], 
        [7, 1, 5, 0, 0, 6, 1, 1, 0, 0, 2], 
    )
    cases = {
        "025": (
            (12, 8), (10, 6), (6, 3), (9, 6), (4, 1),
            (200000, 199998), (29, 23), (23, 16)
        ),
        "050": (
            (12, 8), (10, 7), (6, 4), (9, 7), (4, 1),
            (200000, 100000), (29, 23), (23, 14)
        ),
        "100": (
            (12, 8), (10, 7), (6, 4), (9, 7), (4, 1),
            (200000, 199999), (29, 23), (23, 14)
        ),
    }

    def test_solution_main(self):
        for inputs, expected in zip(self.data, self.cases["100"]):
            with self.subTest(inputs=inputs):
                self.assertEqual(_main(inputs), expected)


if __name__ == "__main__":
    main()