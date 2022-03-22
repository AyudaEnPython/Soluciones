"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Reto

En este desafío, el usuario ingresa una cadena y una subcadena.
Debe imprimir el número de veces que aparece la subcadena en la
cadena dada. El recorrido de la cadena se realizará de izquierda
a derecha, no de derecha a izquierda.

Por ejemplo:

cadenas de entrada:
s = "CDCABCDCCDCDCCDCABCCDD"
ss = "CDC"
"""
import unittest
# pip install prototools
from prototools import time_functions


def count_substrings_a(ss: str, sb: str) -> int:
    return ss.count(sb)


def count_substrings_b(ss: str, sb: str) -> int:
    count = 0
    len_ = len(sb)
    for i in range(len(ss)-len_+1):
        if ss[i:i+len_] == sb:
            count += 1
    return count


def count_substrings_c(ss: str, sb: str) -> int:
    count = 0
    for i in range(len(ss)):
        if ss[i:].startswith(sb):
            count += 1
    return count


def count_substrings_d(ss: str, sb: str) -> int:
    return sum(True for i in range(len(ss)) if ss[i:].startswith(sb))


def main():
    s = "CDCABCDCCDCDCCDCABCCDC"
    ss = "CDC"
    print(count_substrings_b(s, ss))


def test_functions():
    fs = {
        "count_substrings_a": count_substrings_a, # 0.1882
        "count_substrings_b": count_substrings_b, # 3.8251
        "count_substrings_c": count_substrings_c, # 4.2536
        "count_substrings_d": count_substrings_d, # 2.3407
    }
    time_functions(
        fs,
        args=(
            "CDCABCDCCDCDCCDCABCCDC",
            "CDC",
        ),
        globals=globals(),
    )


class Test(unittest.TestCase):

    def test_functions(self):
        self.assertEqual(
            count_substrings_a("CDCABCDCCDCDCCDCABCCDC", "CDC"), 5) # expected
        self.assertEqual(
            count_substrings_b("CDCABCDCCDCDCCDCABCCDC", "CDC"), 6)
        self.assertEqual(
            count_substrings_c("CDCABCDCCDCDCCDCABCCDC", "CDC"), 6)
        self.assertEqual(
            count_substrings_d("CDCABCDCCDCDCCDCABCCDC", "CDC"), 6)


if __name__ == "__main__":
    main() # uncomment / comment to switch between functions
    # unittest.main()
    # test_functions()
