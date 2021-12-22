"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Sucesion:
a, a + b, 2a + b, 2a + 2b, 3a + 2b, 3a + 3b...

TODO: review it later.
"""
from typing import List


def sucesion(a, b, n):

    for i in range(n):
        yield i*a + (i+1)*a + 2*i*b


def sucesion_alt(n):
    t = [str(int(0.25*(2*k+3+(-1)**k))) + "a + " + str(int(0.25*(2*k+1+(-1)**(k+1)))) + "b" for k in range(n)]
    print(t)


def show(a, b):
    for i in range(b):
        print(f"{i}a + {i+1}a + {i}b -> ")
    x, y = 1, 4
    p = "a, a + b, 2a + b, "
    t = [(1, 0), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4)]
    print(p + ", ".join(f"{a}a + {b}b" for a, b in t[3:]))
    print("".join(f"{a*x} + {b*y} = {a*x + b*y}\n" for a, b in t))


def main():
    show(1, 4)
    print(list(sucesion(1, 4, 10)))
    sucesion_alt(10)


if __name__ == "__main__":
    main()