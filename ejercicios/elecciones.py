"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""

PARTIDOS = {"A": "Rojo", "B": "Verde", "C": "Azul"}
menu = """\
Bienvenidos a la encuesta local para la elección del presidente
Tienes 3 opciones:
A) Robert - Partido Rojo
B) Nancy - Partido Verde
C) Cynthia - Partido Azul
"""


def ingresar_eleccion():
    print(menu)
    while True:
        opcion = input("Por favor elige una opcion: ").upper()
        if opcion in PARTIDOS:
            return opcion
        print("Opción inválida")


def main():
    eleccion = ingresar_eleccion()
    print(f"Has votado por el Partido {PARTIDOS[eleccion]}")


if __name__ == "__main__":
    main()
