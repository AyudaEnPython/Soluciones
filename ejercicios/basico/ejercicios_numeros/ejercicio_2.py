"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def frecuencia(numero, digito):
    return str(numero).count(str(digito))


def ingresar(texto):
    while True:
        n = input(texto)
        try:
            return int(n)
        except ValueError:
            continue


def main():
    numero = ingresar("Número entero: ")
    digito = ingresar("Dígito: ")
    print(f"Ocurrencias: {frecuencia(numero, digito)}")


if __name__ == "__main__":
    main()
