"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import unittest


def _encrypt(msg: str, offset: int) -> str:
    encrypted = ""
    for letter in msg:
        if letter.isupper():
            encrypted += chr((ord(letter) + offset - 65) % 26 + 65)
        elif letter.islower():
            encrypted += chr((ord(letter) + offset - 97) % 26 + 97)
        else:
            encrypted += letter
    return encrypted


def _decrypt(msg: str, offset: int) -> str:
    return _encrypt(msg, 26 - offset)


def encrypt(msg: str, offset: int) -> str:
    return "".join(
        chr((ord(letter) + offset - 65) % 26 + 65)
        if letter.isupper() else
        chr((ord(letter) + offset - 97) % 26 + 97)
        if letter.islower() else letter for letter in msg
    )


def decrypt(msg: str, offset: int) -> str:
    return encrypt(msg, 26 - offset)


class TestEncrypt(unittest.TestCase):

    def test_encrypt(self):
        s = "Ayuda en Python"
        self.assertEqual(_encrypt(s, 4), "Ecyhe ir Tcxlsr")
        self.assertEqual(encrypt(s, 4), "Ecyhe ir Tcxlsr")

    def test_decrypt(self):
        s = "Ecyhe ir Tcxlsr"
        self.assertEqual(decrypt(s, 4), "Ayuda en Python")
        self.assertEqual(_decrypt(s, 4), "Ayuda en Python")


if __name__ == "__main__":
    unittest.main()
