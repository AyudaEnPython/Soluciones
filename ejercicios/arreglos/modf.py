"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crear una lista que almacene 10 números del tipo float y obtenga:
a. La sumatoria de la parte entera de cada elemento de la lista.
b. La suma de la parte decimal de cada elemento de la lista.

Nota: puede usar la función math.modf().
"""
from math import modf
from random import uniform


def main():
    numbers = [uniform(10, 100) for _ in range(10)]
    f = lambda n, xs: sum(map(lambda x: float(modf(x)[n]), xs))  # noqa: E731
    print(f"Sumatoria parte entera: {f(1, numbers)}")
    print(f"Sumatoria parte decimal: {f(0, numbers)}")


if __name__ == "__main__":
    main()
