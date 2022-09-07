"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import List, Union

PESOS = 0.1, 0.5, 0.4


def promediar(notas: List[int]) -> float:
    return sum(map(lambda x, y: x * y, notas, PESOS))


def ingresar_nota() -> Union[int, None]:
    try:
        nota = int(input("Ingrese nota: "))
        return nota if 0 <= nota <= 10 else None
    except ValueError:
        return None


def ingresar_datos() -> Union[List[int], None]:
    notas = []
    for _ in range(3):
        nota = ingresar_nota()
        if not nota:
            print("Nota inválida")
            return
        notas.append(nota)
    return notas


def main():
    while True:
        nombre = input("Ingrese nombre: ")
        if nombre == "":
            break
        notas = ingresar_datos()
        if notas:
            print(f"{nombre} tiene una nota de {promediar(notas)}")


if __name__ == "__main__":
    main()
