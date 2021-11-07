"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Asume s is a string of lower case characters. Write a program that
prints the longest substring of s in which the letters occur in
alphabetical order.

For example, if: s = "azcbobobegghakl", then your program should print:

    Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if:
s = "abcbcd", then your program should print:

    Longest substring in alphabetical order is: abc

TODO: make some minor changes.
"""
from unittest import main, TestCase


def solution_a(s):
    current = s[0]
    longest = s[0]
    for curr in s[1:]:
        if curr >= current[-1]:
            current += curr
            if len(current) > len(longest):
                longest = current
        else:
            current = curr
    return longest


def solution_b(s):
    tmp = s[0]
    longest = s[0]
    for current, next_ in zip(s, s[1:]):
        if next_ >= current:
            tmp += next_
        else:
            sub = "".join(tmp)
            if len(sub) > len(longest[0]):
                longest = sub
            elif len(sub) == len(longest[0]):
                longest += next_
            tmp = next_
    return longest


def solution_c(s):
    current = s[0]
    longest = s[0]
    for i in range(len(s)-1):
        if s[i+1] >= s[i]:
            current += s[i+1]
            if len(current) >= len(longest):
                longest = current
        else:
            current = s[i+1]
    return longest


def solution_d(s):
    current = s[0]
    longest = s[0]
    for actual, next_ in zip(s, s[1:]):
        if next_ >= actual:
            current += next_
            if len(current) > len(longest):
                longest = current
        else:
            current = next_
    return longest


class Test(TestCase):

    def test_solutions(self):
        self.assertEqual(solution_a("azcbobobegghakl"), "beggh")
        self.assertEqual(solution_b("azcbobobegghakl"), "beggh")
        self.assertEqual(solution_c("azcbobobegghakl"), "beggh")
        self.assertEqual(solution_d("azcbobobegghakl"), "beggh")


if __name__ == "__main__":
    main()