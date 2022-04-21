"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un programa qeu pida un número y que se diga si el mismo es
primo o no, el programa debe pedir números hasta que el número
ingresado sea cero.

Ejemplo:
Digite un número: 3
Salida: el número es primo
Digite un número: 4
Salida: el número no es primo
Digite un número: 7
Salida: el número es primo
Digite un número: 0
"Muchas gracias por utilizar el programa. Hasta pronto"
"""


# https://github.com/AyudaEnPython/Soluciones/blob/main/soluciones/es_primo.py
def es_primo(n: int) -> bool:
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n < 2:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
    return True


def main():
    while True:
        n = input("Digite un número: ")
        if n == "0":
            print("Muchas gracias por utilizar el programa. Hasta pronto")
            break
        try:
            n = int(n)
            if es_primo(n):
                print(f"El número {n} es primo")
            else:
                print(f"El número {n} no es primo")
        except ValueError:
            print("El valor ingresado no es un número, intentar de nuevo")


if __name__ == "__main__":
    main()
