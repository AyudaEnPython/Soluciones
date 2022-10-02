"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: add typing later...
"""


def area(base, altura):
    return base * altura


def show(base, altura, caracter):
    for _ in range(altura):
        print(caracter*base)


def main():
    base = int(input("Base del rectángulo: "))
    altura = int(input("Altura del rectángulo: "))
    caracter = input("Caracter de relleno: ")
    print(f"Area del rectángulo: {area(base, altura)}\n")
    show(base, altura, caracter)


if __name__ == "__main__":
    main()
