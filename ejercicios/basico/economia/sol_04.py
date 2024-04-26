"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import int_input


def f(n):
    return [(3*x - 2, 2*x) for x in range(1, n+1)]


def g(xs):
    for x, y in xs:
        print(f"{x}/{y}")


def h(xs):
    return sum(x/y for x, y in xs)


def main():
    t = int_input("n: ", min=1, lang="es")
    xs = f(t)
    g(xs)
    print(f"Suma: {h(xs)}")


if __name__ == "__main__":
    main()
