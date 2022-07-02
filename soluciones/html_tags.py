"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: improve naming
"""
from unittest import main, TestCase
from functools import wraps


def f(g):
    @wraps(g)
    def f_(*args, **kwargs):
        return "<b>"+g(*args, **kwargs)+"</b>"
    return f_


def f_(s):
    def f(g):
        @wraps(g)
        def g_(*args, **kwargs):
            return f"<{s}>{g(*args, **kwargs)}</{s}>"
        return g_
    return f


@f
def g():
    return "Hello world"


@f_("h1")
def h():
    return "Headline"


@f_("p")
def i():
    return "Paragraph"


class Test(TestCase):

    def test_f(self):
        self.assertEqual(g(), "<b>Hello world</b>")
        self.assertEqual(h(), "<h1>Headline</h1>")
        self.assertEqual(i(), "<p>Paragraph</p>")


if __name__ == '__main__':
    main()
