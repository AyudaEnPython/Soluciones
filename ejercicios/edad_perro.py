"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crea un programa, que calcule el equivalente humano de la edad de un
perro. Si los dos primeros años de vida de un perro equivalen diez años
humanos, y los siguientes años de vida de un perro equivalen cada uno a
cuatro años humanos.
"""


def calcular(edad: int) -> int:
    if edad <= 2:
        return 10 * edad
    else:
        return 20 + 4 * (edad - 2)


def main():
    edad = int(input("Ingrese la edad del perro: "))
    print("La edad del perro es:", calcular(edad))


if __name__ == "__main__":
    main()
