"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def suma_digitos(n):
    return sum(int(n) for n in str(n))


def ingresar():
    numeros = []
    while True:
        n = input("> ")
        try:
            n = int(n)
        except ValueError:
            continue
        else:
            if n == 0:
                return numeros
            numeros.append(n)


def main():
    numeros = ingresar()
    for numero in numeros:
        print(f"{numero} -> {suma_digitos(numero)}")


if __name__ == "__main__":
    main()
