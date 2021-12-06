"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Desarrolle un programa que permita encriptar un mensaje; para encriptar
desplace 3 letras hacia la derecha cada letra que compone el mensaje.
En mensaje solo tiene letras y no tienen ñ.

    +-----------------------+-----------------------+
    | Entrada               | Salida                |
    +-----------------------+-----------------------+
    | SucreCapitaldeBolivia | VXFUHFDSLWDOGHEROLYLD |
    | CunadelaLibertad      | FXQDGHODOLEHUWDG      |
    +-----------------------+-----------------------+

TODO: review it later for possible changes

NOTE: c and d are fully implemented, a and b aren't (intentionally).
    Possibly change later (maybe using comments to point out it).
"""
from string import ascii_lowercase
from unittest import main, TestCase


def encriptar_a(s: str, k: int = 3) -> str:
    return "".join(map(lambda x: chr(ord(x) + k), s)).upper()


def encriptar_b(s: str, k: int = 3, alpha: str = ascii_lowercase) -> str:
    def lookup(v, alpha=alpha):
        o, c = ord(v), v.lower()
        if c in alpha:
            return chr(o + k)
        return v
    return "".join(map(lookup, s)).upper()


def encriptar_c(s: str, k: int = 3, ss: str = ascii_lowercase) -> str:
    shift = ss[k:] + ss[:k]
    table = str.maketrans(ss, shift)
    return s.lower().translate(table).upper()


def encriptar_d(ss: str, k: int = 3, alpha: str = ascii_lowercase) -> str:
    r = ""
    for s in ss.lower():
        i = alpha.find(s)
        j = i + k
        if j >= 26:
            j -= 26
        r += alpha[j]
    return r.upper()


class Test(TestCase):

    data = (
        ("SucreCapitaldeBolivia", "VXFUHFDSLWDOGHEROLYLD"),
        ("CunadelaLibertad", "FXQDGHODOLEHUWDG"),
    )

    def test_encriptar_no_az(self):
        self.assertNotEqual(encriptar_a("z"), "C")
        self.assertNotEqual(encriptar_b("z"), "C")

    def test_encriptar_az(self):
        self.assertEqual(encriptar_c("z"), "C")
        self.assertEqual(encriptar_d("z"), "C")

    def test_encriptar(self):
        for s, r in self.data:
            self.assertEqual(encriptar_a(s), r)
            self.assertEqual(encriptar_b(s), r)
            self.assertEqual(encriptar_c(s), r)
            self.assertEqual(encriptar_d(s), r)


if __name__ == "__main__":
    main()