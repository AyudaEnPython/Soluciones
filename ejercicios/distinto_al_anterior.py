"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realice una función donde el usuario ingrese la cantidad de números que
va a introducir, al introducir cada número le debe mostrar un mensaje
cada vez que un número no sea distinto al anterior, al final debe
mostrar la sumatoria de todos los números ingresados.

Ejemplo:
¿Cuántos valores va a introducir? 3
Escriba un número: 6
Escriba un número distinto a 6: 10
Escriba un número distinto a 10: 10
¡10 no es distinto de 10!
Escriba un número distinto de 10: 9
Gracias por su colaboración.

NOTE: el ejemplo del enunciado no muestra la sumatoria y sugiere
    delegar demasiadas responsabilidades a una sola función. Se opta
    por modificar esas partes.
"""


def ingresar(p):
    while True:
        x = int(input(f"Escriba un número distinto de {p}: "))
        if x != p:
            return x
        print(f"{x} no es distinto de {p}")


def procesar(n, p):
    s = x = p
    for _ in range(n - 1):
        x = ingresar(x)
        s += x
    return s


def main():
    n = int(input("¿Cuántos valores va a introducir? "))
    p = int(input("Escriba un número: "))
    s = procesar(n, p)
    print("Gracias por su colaboración.")
    print(f"Sumatoria: {s}")


if __name__ == "__main__":
    main()
