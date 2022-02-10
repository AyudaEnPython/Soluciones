"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: needs refactor, add tests later.
"""
from random import randint
from string import ascii_lowercase as abc, ascii_uppercase as ABC
from typing import List

FRASES = [
    "Vive tu momento",
    "Nunca subestimes el poder de la música",
    "Nunca olvides lo mucho que tu familia te ama",
]
posiciones = []


def adivinar() -> str:
    while True:
        letra = input("Letra: ")
        if len(letra) != 1:
            print("Debe ingresar una sola letra")
        elif letra not in abc + ABC + "áéíóúÁÉÍÓÚñÑ":
            print("Debe ingresar una letra")
        else:
            return letra


def obtener_indices(adivinada: str, frase: str) -> List[int]:
    return [i for i, letra in enumerate(frase) if letra == adivinada]


def comprobar(indices: List[int]) -> None:
    if indices == []:
        return
    if len(indices) > 1 and indices not in posiciones:
        for e in indices:
            posiciones.append(e)
    else:
        posiciones.append(*indices)


def mostrar(frase: str) -> str:
    return "".join(
        letra if i in posiciones else (" " if letra == " " else "-")
        for i, letra in enumerate(frase)
    )


def main():
    frase = FRASES[randint(0, len(FRASES) - 1)]
    print(mostrar(frase))
    while True:
        letra = adivinar()
        comprobar(obtener_indices(letra, frase))
        actual = mostrar(frase)
        print(actual)
        if actual == frase:
            print("Felicitaciones, adivinaste la frase")
            break


if __name__ == "__main__":
    main()
