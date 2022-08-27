"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Suponga que está escribiendo una novela de ciencia ficción y necesita
una colección de nombres de planetas exóticos. Cada nombre debe estar
compuesto de 4 a 17 letras, donde la cadena alterna entre vocales y
consonantes.
La letra inicial del nombre debe estar en mayúscula.

Implemente un programa que:
- Genere 10 nombres de planetas que cumplan los criterios indicados
- Imprima los nombres de planetas ordenados alfabéticamente

En cada ejecución se generará una colección aleatoria de nombres.
Por ejemplo:

Abafora
Agekiji
Amiza
Azine
Ekaduki
Epimo
Isunot
Oham
Ufimeb
Ukovine

Para generar números aleatorios use la función randint()
"""
from random import randint, choice
from typing import Tuple

MIN, MAX = 4, 7
ABC: Tuple[str, ...] = ("", "aeiou", "bcdfghjklmnñopqrstvwxyz")


def generar() -> str:
    return "".join([choice(ABC[(-1)**x]) for x in range(randint(MIN, MAX))])


def main():
    nombres = [generar().capitalize() for _ in range(10)]
    print(*sorted(nombres), sep="\n")


if __name__ == "__main__":
    main()
