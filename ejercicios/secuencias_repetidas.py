"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Utilizando diseño modular, escribe un módulo que recibe dos números
enteros positivos "x" y "z",  en donde "x" > "z", y dos secuencias de
letras "a1a2...ax" y "b1b2...bz", y que devuelva el número de veces
que la segunda secuencia aparece en la primera.

Por ejemplo, cuando x=12 y z=3 y las secuencias de letras son
"afertdeafetk" y "afe", el módulo deberia devolver 2 ya que la segunda
secuencia se repite dos veces en la primera secuencia.

# ------------------------ Enunciado Modificado -----------------------
Escribe una función que reciba dos secuencias de letras "a1a2a3...am" y
"b1b2b3..bn" (siendo m > n) y que devuelva el número de veces que la
segunda secuencia aparece en la primera.

Por ejemplo, dadas las secuencias "afertdeafetk" y "afe", la función
debería retornar 2 puesto que la segunda secuencia se repite dos veces
en la primera secuencia.

    +-----------------------------------------------------------+
    | Nota: No es necesario recibir los números enteros del     |
    | enunciado original, es redundante (son los tamaños de las |
    | secuencias). Diseño modular es demasiado general, por lo  |
    | que se opta plantearlo como función que sería importada   |
    | desde otro módulo.                                        |
    +-----------------------------------------------------------+
# ---------------------------------------------------------------------
TODO: add docstring
"""
from unittest import main, TestCase


def repetidos_naive(m: int, n: int, a: str, b: str) -> int:
    c = 0
    for i in range(m):
        if a[i:i+n] == b:
            c += 1
    return c


def repetidos_a(a: str, b: str) -> int:
    c = 0
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            c += 1
    return c


def repetidos_b(a: str, b: str) -> int:
    return sum([True if a[i:i+len(b)] == b else False for i in range(len(a))])


def repetidos_c(a: str, b: str) -> int:
    return a.count(b)


class Test(TestCase):

    def test_repetidos(self):
        self.assertEqual(repetidos_naive(12, 3, "afertdeafetk", "afe"), 2)
        self.assertEqual(repetidos_a("afertdeafetk", "afe"), 2)
        self.assertEqual(repetidos_b("afertdeafetk", "afe"), 2)
        self.assertEqual(repetidos_c("afertdeafetk", "afe"), 2)
        self.assertEqual(repetidos_naive(10, 3, "abcdecdeij", "cde"), 2)
        self.assertEqual(repetidos_a("abcdecdeij", "cde"), 2)
        self.assertEqual(repetidos_b("abcdecdeij", "cde"), 2)
        self.assertEqual(repetidos_c("abcdecdeij", "cde"), 2)


if __name__ == "__main__":
    main()
