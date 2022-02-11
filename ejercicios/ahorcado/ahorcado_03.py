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
INTENTOS = 9
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
    return [
        i for i, letra in enumerate(frase)
        if letra.lower() == adivinada.lower()
    ]


def comprobar(indices: List[int]) -> bool:
    if indices == []:
        return False
    if len(indices) > 1 and indices not in posiciones:
        for e in indices:
            posiciones.append(e)
        return True
    else:
        posiciones.append(*indices)
        return True


def mostrar(frase: str, ch: str = "_") -> str:
    return "".join(
        letra if i in posiciones else (" " if letra == " " else ch)
        for i, letra in enumerate(frase)
    )


def main():
    numero = randint(0, len(FRASES) - 1)
    frase = FRASES[numero]
    print(mostrar(frase))
    intentos = INTENTOS
    puntos = 0
    while True:
        if intentos == 0:
            print("Perdiste, la frase era:")
            print(frase)
            break
        letra = adivinar()
        intentos -= 1
        if comprobar(obtener_indices(letra, frase)):
            puntos += 10
        actual = mostrar(frase)
        print(actual)
        if actual == frase:
            print(
                f"Felicitaciones, adivinaste la frase en"
                f" {INTENTOS - intentos} intentos."
                f"\nPuntaje: {puntos}"
            )
            break


if __name__ == "__main__":
    main()
