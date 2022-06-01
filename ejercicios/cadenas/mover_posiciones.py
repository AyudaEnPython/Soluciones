"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Mover las letras de una cadena "n" veces.
"""


def mover_posiciones(palabra: str, pos:int) -> str:
    return palabra[len(palabra) - pos:] + palabra[:len(palabra) - pos]


def main_():
    print(mover_posiciones("perro", 2)) 


if __name__ == "__main__":
    main_() # output: "roper"
