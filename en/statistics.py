"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english
speakers are welcome.
-----------------------------------------------------------------------

Statistics
----------
You will be receiving key-value pairs on separate lines separated by ":"
until you receive the command "statistics". Sometimes you may receive a
product more than once, in that case you have to add the new quantity to
the existing one.

    +------------+--------------------+
    | Input      | Output             |
    +------------+--------------------+
    | bread: 4   | Products in stock: |
    | cheese: 2  | - bread: 5         |
    | ham: 1     | - cheese: 2        |
    | bread: 1   | - ham: 1           |
    | statistics | Total Products: 3  |
    |            | Total Quantity: 8  |
    +------------+--------------------+
"""
import unittest
from typing import Dict, List


def read_input() -> List[str]:
    while True:
        line = input()
        if line == "statistics":
            break
        else:
            yield line


def solver(data: List[str]) -> Dict[str, int]:
    products = {}
    for line in data:
        key, value = line.split(":")
        value = int(value)
        if key in products:
            products[key] += value
        else:
            products[key] = value
    return products


def show(data: Dict[str, int]):
    print("Products in stock:")
    for key, value in data.items():
        print(f"- {key}: {value}")
    print(f"Total Products: {len(data)}")
    print(f"Total Quantity: {sum(data.values())}")


def main():
    data = read_input()
    show(solver(data))


class Test(unittest.TestCase):

    def test_solver(self):
        self.assertEqual(
            solver(
                ["bread: 4", "cheese: 2", "ham: 1", "bread: 1"]),
                {"bread": 5, "cheese": 2, "ham": 1},
            )
        self.assertEqual(
            solver(
                ["cheese: 5", "ham: 3", "ham: 1", "cheese: 4"]),
                {"cheese": 9, "ham": 4},
            )


if __name__ == '__main__':
    # unittest.main() # uncomment this and comennt the next one to run tests
    main()