"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Even though the group is only for spanish speakers, english speakers
are welcome.
-----------------------------------------------------------------------

Given a list of numbers, stop processing input after the cumulative sum
of all the input becomes negative.

Input format: A list of integers to be processed
Constrains: All numbers input are integers between -1000 and 1000
Output format: Print all the numbers before the cumulative sum become
negative.

Sample Input
1
2
88
-100
49

Sample Output
1
2
88
"""
from typing import List


def solution(data: List[int]) -> None:
    s = 0
    for n in data:
        s += n
        if s < 0:
            return None
        print(n)


def main():
    solution([1, 2, 88, -100, 49])


if __name__ == "__main__":
    main()
