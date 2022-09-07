"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english
speakers are welcome.
"""
from random import randint


def generate_points(n):
    return [randint(1, 10) for _ in range(n)]


def f(arr):
    return arr[1:-1]


if __name__ == '__main__':
    numbers = generate_points(randint(4, 10))
    print(f"Before: {numbers}")
    print(f" After:    {f(numbers)}")
