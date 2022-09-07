"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Encriptar y desencriptar frases usando las vocales AEIOU. Cada letra de
la frase que coincida con una letra de la clave se sustituye por un
número siguiendo el orden 02468.

NOTE: Add tests later.
"""


def encriptar(frase: str, clave: str, s: str = "02468") -> str:
    """Función que encripta una frase.

    :param frase: Frase a encriptar.
    :type frase: str
    :param clave: Clave de encriptación.
    :type clave: str
    :param s: Símbolo de sustitución.
    :type s: str
    :return: Frase encriptada.
    :rtype: str
    """
    for letra in frase.lower():
        if letra in clave:
            frase = frase.replace(letra, s[clave.find(letra)])
    return frase


def desencriptar(frase: str, clave: str, s: str = "02468") -> str:
    """Función que desencripta una frase.

    :param frase: Frase a desencriptar.
    :type frase: str
    :param clave: Clave de encriptación.
    :type clave: str
    :param s: Símbolo de sustitución.
    :type s: str
    :return: Frase desencriptada.
    :rtype: str
    """
    for letra in frase:
        if letra in s:
            frase = frase.replace(letra, clave[s.find(letra)])
    return frase


def main():
    CLAVE = "aeiou"

    mensaje = "Ayuda En Python"
    print(f"Mensaje original: {mensaje}")

    encriptado = encriptar(mensaje, CLAVE)
    print(f"Mensaje encriptado: {encriptado}")

    desencriptado = desencriptar(encriptado, CLAVE)
    print(f"Mensaje desencriptado: {desencriptado}")


if __name__ == "__main__":
    main()
