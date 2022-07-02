"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Elabore un programa que solicite un número entero N al usuario y lea un
archivo de texto, luego el programa debe imprimir las líneas con N
palabras del archivo de texto.

Por ejemplo:

Archivo de texto

    +------------------------------------------------+
    | Hola a todos                                   |
    | Hoy es un buen día                             |
    | La gasolina subió de precio                    |
    | Ricardo Gareca renovó con la selección peruana |
    +------------------------------------------------+

Para el valor de N=5, el programa imprime:

    +------------------------------------------------+
    | Hoy es un buen día                             |
    | La gasolina subió de precio                    |
    +------------------------------------------------+
"""
from typing import List

FILENAME = "data.txt"


def read_file(filename: str) -> List[str]:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().splitlines()


def counter(data: List[str], n: int):
    return [line for line in data if len(line.split()) == n]


def show(data: List[str]) -> None:
    if not data:
        print("No hay resultados")
        return
    print("\n".join(data))


def main():
    data = read_file(FILENAME)
    n = int(input("Ingrese un número: "))
    show(counter(data, n))


if __name__ == "__main__":
    main()
