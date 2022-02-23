"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Cree un programa que solicite al usuario una lista de calificaciones
separadas por comas.
Divida la cadena en calificaciones individuales y almacénelas en una
lista para luego convertir cada calificación en un entero. Deberá
utilizar una sentencia try/except para informar al usuario cuando los
valores introducidos no puedan ser convertidos debido a un error de
tipeo o formato.

TODO: add typing and testcases later.
"""


def convertir_notas(notas):
    try:
        return [int(nota) for nota in notas.split(",")]
    except ValueError:
        print("No se pudo convertir la nota")
        return []


def main():
    notas = input("Ingrese las notas separadas por comas: ")
    print(convertir_notas(notas))


if __name__ == "__main__":
    main()
