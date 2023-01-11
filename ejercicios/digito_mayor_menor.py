"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def digit_value(n):
    max_, min_ = 0, 9
    while n >= 1:
        r = n % 10
        if r > max_:
            max_ = r
        if r < min_:
            min_ = r
        n //= 10
    return min_, max_


def digit_value_alt(n):
    max_, min_ = 0, 9
    while n:
        r = n % 10
        max_ = max(r, max_)
        min_ = min(r, min_)
        n //= 10
    return min_, max_


f = lambda g, n: g(str(n))


def main():
    n = int(input("n: "))
    menor, mayor = digit_value(n)
    print(f"Dígito mayor: {mayor}")
    print(f"Dígito mayor: {f(max, n)}")
    print(f"Dígito menor: {menor}")
    print(f"Dígito menor: {f(min, n)}")


if __name__ == "__main__":
    main()
