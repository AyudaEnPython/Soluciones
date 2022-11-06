"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import sample


def generar(x=1, y=10_000, n=10):
    return sample(range(x, y+1), k=n)


def main():
    numeros = generar()
    for numero in numeros:
        print(f"{numero:>5} -> {numero:>08b}")


if __name__ == "__main__":
    main()
