"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que busque todas las parajeas de números
"amigables" entre los números naturales menores a 500. Se dice que dos
números son "amigables" si el primero es la suma de los divisores del
segundo y viceversa.
"""
# pip instal prototools
from prototools import time_functions


def naive(N):
    for a in range(1, N):
        s = 0
        for n in range(1, a):
            if a % n == 0:
                s += n
        for b in range(1, N):
            t = 0
            for n in range(1, b):
                if b % n == 0:
                    t += n
            if s == b and t == a and a != b:
                print(a, b)


def suma_divisores(n):
    return sum(x for x in range(1, n) if n % x == 0)


def par_amigable(n):
    resultado = []
    for x in range(1, n):
        y = suma_divisores(x)
        if y < n and suma_divisores(y) == x and x != y:
            resultado.append((x, y))
    return resultado


def main(N):
    pares = par_amigable(N)
    print(*pares, sep=", ")


if __name__ == "__main__":
    # main() # uncomment this line and comment the next 2 lines to run main()
    fs = {"main": main, "naive": naive}
    time_functions(fs, args=(2000), globals=globals(), number=1)
    # outpus:
    # 'main' took 0.1237 secs
    # 'naive' took 164.6409 secs
