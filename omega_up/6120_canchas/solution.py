#!/usr/bin/python3
"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

*    Estatus    : AC 
*    Porcentaje : 100.00%
*    Memoria    : 10.31 MB
*    Tiempo     : 0.82s

"""

def _get_data():
    r1 = tuple(map(int, input().split()))
    r2 = tuple(map(int, input().split()))
    return r1[:2], r1[2:], r2[:2], r2[2:]


def _area(x, y):
    return abs(x[0] - y[0]) * abs(x[1] - y[1])


def _main(data=None) -> None:
    if data is None:
        data = _get_data()
    p1, p2, p3, p4 = data
    a, b, c = _area(p1, p2), _area(p3, p4), 0
    x_ = (min(p2[0], p4[0]) - max(p1[0], p3[0]))
    y_ = (min(p2[1], p4[1]) - max(p1[1], p3[1]))
    if x_ > 0 and y_ > 0:
        c = x_ * y_
    print(a + b - c)


if __name__ == "__main__":
    _main()