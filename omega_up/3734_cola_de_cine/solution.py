#!/usr/bin/python3
"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

*    Estatus    : AC 
*    Porcentaje : 100.00%
*    Memoria    : 10.20 MB
*    Tiempo     : 0.30s

NOTE: _main and _main_alt are equivalent and both are correct.
    Runtime does not change too much.
"""

def _get_data():
    data = [int(input())]
    while True:
        n = int(input())
        if n == -1:
            break
        data.append(n)
    return data


def _main(data=None) -> None:
    if data is None:
        data = _get_data()
    m, p = data[0], 0
    for n in data:
        if n != 0:
            p += n
        if p > m:
            m = p
        p -= 1
    return sum(data), m


def _main_alt() -> None:
    m = 0; n = 0; t = 0; c = 0; p = 0;
    while (n != -1):
        n = int(input())
        c += 1
        if c == 1: m += n
        t += n
        if n != 0: p+= n
        if p > m: m = p
        p -= 1
    t += 1
    print(t, m)


if __name__ == "__main__":
    _main()
    #_main_alt()