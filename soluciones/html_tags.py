"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: add more implementations and tests
"""
from unittest import main, TestCase
from functools import wraps


def f(g):
    @wraps(g)
    def h(*args, **kwargs):
        return "<b>"+g(*args, **kwargs)+"</b>"
    return h


@f
def g():
    return "Hello world"


class Test(TestCase):

    def test_f(self):
        self.assertEqual(g(), "<b>Hello world</b>")


if __name__ == '__main__':
    main()