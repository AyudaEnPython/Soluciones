"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def sol_a():
    # pip install prototools
    from prototools import int_input

    n = int_input("Ingrese el número de personas: ",  min=1)
    edades = [
        int_input("Ingrese la edad: ", min=1, max=100) for _ in range(n)
    ]

    print(f"Mayor edad: {max(edades)}")
    print(f"Menor edad: {min(edades)}")
    print(f"Promedio de edades: {sum(edades) / len(edades)}")


def sol_b():
    n = int(input("Ingrese el número de personas: "))
    edades = [int(input("Ingrese la edad: ")) for _ in range(n)]
    print(f"Mayor edad: {max(edades)}")
    print(f"Menor edad: {min(edades)}")
    print(f"Promedio de edades: {sum(edades) / len(edades)}")


def sol_c():
    n = int(input("Ingrese el número de personas: "))
    edades = []
    for _ in range(n):
        edades.append(int(input("Ingrese la edad: ")))
    print(f"Mayor edad: {max(edades)}")
    print(f"Menor edad: {min(edades)}")
    print(f"Promedio de edades: {sum(edades) / len(edades)}")


def sol_d():
    edades = []
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            if edad > 0:
                edades.append(edad)
            else:
                break
        except ValueError:
            pass
    print(f"Mayor edad: {max(edades)}")
    print(f"Menor edad: {min(edades)}")
    print(f"Promedio de edades: {int(sum(edades) / len(edades))}")


# and more...


if __name__ == "__main__":
    sol_a()
