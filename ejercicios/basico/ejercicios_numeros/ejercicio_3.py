"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import sample


def generar(x=65, y=90, n=3):
    return sample(range(x, y+1), k=n)


def main():
    numeros = generar()
    print(f"{sorted(numeros)}")


if __name__ == "__main__":
    main()
