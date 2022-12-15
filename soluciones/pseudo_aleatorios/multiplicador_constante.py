"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: Middle Square Algorithm, needs tests...
"""
import math
# pip install prototools
from prototools import time_functions


def int_len(x):
    return int(math.log10(x)) + 1


def get_random(x=9803, a=6965, n=5):
    d = int_len(x)
    prns = []
    for _ in range(n):
        y = a * x
        l = (y // 10 ** d) % 100
        r = (y % 10 ** d) // 100
        x = l * 100 + r
        prns.append(x/10**d)
    return prns


def get_random_(x=9803, a=6965, n=5):
    d = len(str(x)) // 2
    prns = []
    for _ in range(n):
        y = str(a * x)
        y_len = len(y)
        if len(y) % 2 != 0:
            y = "0" + y
            x = int(y[d:y_len - 1])
        else:
            d_ = len(str(x)) // 2
            x = int(y[d_:y_len - d_])
        prns.append(x/10 ** (d*2))
    return prns


def get_random_post(x=9803, a=6965, n=5):
    d = len(str(x))
    prns = []
    for _ in range(n):
        y = str(a * x)
        x = int(y[2:6])
        prns.append(x/10**d)
    return prns


def f(x=9803, a=6965, n=5):
    t = []
    for _ in range(n):
        x = int(str(a * x)[2:6])
        t.append(x/1e4)
    return t


if __name__ == "__main__":
    fs = {
        "get_random": get_random,
        "get_random_": get_random_,
        "get_random_post": get_random_post,
        "f": f,
    }
    time_functions(fs, args=(), globals=globals())
