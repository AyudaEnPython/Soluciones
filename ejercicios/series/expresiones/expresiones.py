"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Evalue las siguientes expresiones donde N es proporcionada por el
usuario, proponga un sub-menú.

a. \sum_{i=1}^{N} \sqrt{i^{3} - 1}  # noqa W605
b. \sum_{i=1}^{N} \frac{2^{i} - 2^{i + 1}}{i + 1}  # noqa W605
c. \sum_{i=1}^{N} (-1)^{i + 1\frac{2^{i}}{i}}  # noqa W605
d. \prod_{i=1}^{N} N(N - 1)  # noqa W605

NOTE:
- se modifica la formula en c por (ver README para más detalles):
    sum_{i=1}^{N} \frac{(-1)^{i %2B 1} 2^{i}}{i}
- se modifica en d N por i
"""
from functools import reduce
from prototools import Menu, int_input


# 3.8 > from math import prod
def prod(iterable):
    return reduce(lambda x, y: x * y, iterable, 1)


def a(n: int) -> None:
    print(f"{sum(map(lambda i: (i**3 - 1)**(0.5), range(1, n + 1)))}")


def b(n: int) -> None:
    print(
        f"{sum(map(lambda i: (2**i - 2**(i + 1)) / (i + 1), range(1, n + 1)))}"
    )


def c(n: int) -> None:
    print(
        f"{sum(map(lambda i: (-1)**(i + 1) * (2**i) / i, range(1, n + 1)))}"
    )


def d(n: int) -> None:
    print(f"{prod(map(lambda i: i * (i - 1), range(1, n + 1)))}")


def main():
    menu = Menu("Evaluación de expresiones")
    menu.add_options(
        ("Sumatoria (i^3 - 1)^1/2", lambda: a(int_input("Ingrese N: "))),
        ("Sumatoria (2^i - 2^(i+1))/(i + 1)",lambda: b(int_input("Ingrese N: "))),
        ("Sumatoria (-1)^(i+1(2^i/i))", lambda: c(int_input("Ingrese N: "))),
        ("Factorial", lambda: d(int_input("Ingrese N: "))),
    )
    menu.run()


if __name__ == "__main__":
    main()
