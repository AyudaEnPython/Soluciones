"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def intercambio(a, b):
    return b, a


def main():
    a = input("Primer valor: ")
    b = input("Segundo valor: ")
    a, b = intercambio(a, b)
    print(f"Los valores intercambiados quedan como: {a} y {b}")


if __name__ == "__main__":
    main()
