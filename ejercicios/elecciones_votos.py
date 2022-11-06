"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Se tienen los resultados de las últimas elecciones para alcade. En
dichas elecciones hubo 4 candidatos. Los electores fueron 500
personas. Haga un programa que obtenga los siguientes resultados:
- Genere aleatoriamente los votos obtenidos por cada candidato (
    números aleatorios del 1 - 4).
- Muestre el total de votos obtenidos por cada candidato.
- Muestre el candidato con mayor cantidad de votos.
"""
from random import randint

CANDIDATOS = 4
ELECTORES = 500


def generar_votos():
    votos = [0] * CANDIDATOS
    for _ in range(ELECTORES):
        votos[randint(0, 3)] += 1
    return votos


def resultados(votos):
    for i, total in enumerate(votos, 1):
        print(f"El candidato N° {i} obtuvo {total} votos.")


def mayor(votos):
    return votos.index(max(votos)) + 1


def main():
    votos = generar_votos()
    resultados(votos)
    print(f"El candidato N°{mayor(votos)} ganó las elecciones")


if __name__ == "__main__":
    main()
