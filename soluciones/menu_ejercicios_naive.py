"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

1) Secuencia Fibonacci
https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/serie_fibonacci.py
2) Sumatoria primos
https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/sumatoria_primos.py
3) Números primos gemelos
https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/primos_gemelos.py
4) Máximo común divisor (MCD)
https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/mcd.py
5) Centro meteorológico
https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/promedio_temperaturas.py

NOTE: Este diseño NO ES RECOMENDABLE.
"""
from math import sqrt
from random import randint


def _data():
    return int(input("a: ")), int(input("b: "))


def es_primo(n):
        if 1 < n < 4:
            return True
        elif n < 2 or not n % 2:
            return False
        impares = range(3, int(sqrt(n) + 1), 2)
        return not any(not n % i for i in impares)


def primos(a, b):
    return (i for i in range(a, b + 1) if es_primo(i))


def serie_fibonacci():
    def f(n):
        a, b = 0, 1
        while n > 0:
            yield a
            a, b = b, a + b
            n -= 1
    n = int(input("Ingrese la cantidad de elementos de la secuencia: "))
    print(", ".join(str(x) for x in f(n)))


def sumatoria_primos():
    def f(a, b):
        return sum(i for i in range(a, b + 1) if es_primo(i))
    print("Resultado:", f(*_data()))


def primos_gemelos():
    def f(n1, n2):
        primos_ = primos(n1, n2)
        return [(i, i + 2) for i in primos_ if es_primo(i + 2)]
    print("Resultado:", f(*_data()))


def mcd():
    def f(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    print("Resultado:", f(*_data()))


def promedio_temperaturas():
    R = ("norte", "centro", "occidente", "sur", "pacifico", "caribe")
    d = {k:[randint(10, 34) for _ in range(12)] for k in R}
    pa = lambda d: {k: round(sum(v) / len(v), 2) for k, v in d.items()}
    mt = lambda d: {k: min(v) for k, v in d.items()}
    la = lambda d: {k: (min(v), max(v)) for k, v in d.items()}
    mpa = lambda d, r: max(r, key=d.get)
    a = pa(d)
    m = mt(d)
    li = la(d)
    print("Promedio anual por región")
    for k, v in a.items():
        print(f"{k}: {v}")
    print(f"Menor temperatura: {min(m, key=m.get)} {min(m.values())}")
    print("Menor y mayor temperatura por región")
    for k, v in li.items():
        print(f"{k}: {', '.join(map(str, v))}")
    print(f"Mayor promedio anual: {mpa(a, R[3:])}")


def main():
    while True:
        print("\n\tMenu\n")
        print("1) Secuencia Fibonacci")
        print("2) Sumatoria primos")
        print("3) Primos gemelos")
        print("4) Máximo común divisor (MCD)")
        print("5) Centro meteorológico")
        print("6) Salir\n")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            serie_fibonacci()
        elif opcion == "2":
            sumatoria_primos()
        elif opcion == "3":
            primos_gemelos()
        elif opcion == "4":
            mcd()
        elif opcion == "5":
            promedio_temperaturas()
        elif opcion == "6":
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()