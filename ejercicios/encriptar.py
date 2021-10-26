"""
Desarrolle un programa que permita encriptar un mensaje; para encriptar
desplace 3 letras hacia la derecha cada letra que compone el mensaje.
En mensaje solo tiene letras y no tienen ñ.

    +-----------------------+-----------------------+
    | Entrada               | Salida                |
    +-----------------------+-----------------------+
    | SucreCapitaldeBolivia | VXFUHFDSLWDOGHEROLYLD |
    | CunadelaLibertad      | FXQDGHODOLEHUWDG      |
    +-----------------------+-----------------------+

TODO: add more implementations

NOTE: c and d are fully implemented, a and b aren't (intentionally).
    Possibly change later (maybe using comments to point out it).
"""
from string import ascii_lowercase
from unittest import main, TestCase


def encriptar_a(s):
    def lookup(v):
        o, c = ord(v), v.lower()
        if c in ascii_lowercase:
            return chr(o + 3)
        return v
    return "".join(map(lookup, s)).upper()


def encriptar_b(s):
    return "".join(map(lambda x: chr(ord(x) + 3), s)).upper()


def encriptar_c(s, k=3, ss=ascii_lowercase):
    shift = ss[k:] + ss[:k]
    table = str.maketrans(ss, shift)
    return s.lower().translate(table).upper()


def encriptar_d(ss, k=3, a=ascii_lowercase):
    r = ""
    for s in ss.lower():
        i = a.find(s)
        j = i + k
        if j >= 26:
            j -= 26
        r += a[j]
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