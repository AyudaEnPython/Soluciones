"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dado un mensaje usted debe:
- Extraer los caracteres únicos.
- Crear una clave de encripción, esta consistirá en un diccionario con
    elementos que tendrán por clave los caracteres extraídos en el paso
    anterior y por valor las letras del alfabeto del inglés en
    mayúsculas.
- Encriptar el mensaje usando la clave anteriormente generada, es decir,
    debe reescribir el mensaje intercambiado los caracteres originales
    por los correspondientes del alfabeto según el diccionario.

Hasta este punto usted debe tener la clave de encripción y el mensaje
codificado. Ahora para crear un decodificador debe:
- Invertir la clave de encripción, es decir, poner los valores como
    claves y las claves como valores.
- Desencriptar el mensaje usando la clave invertida de forma similar
    como  codificó el mensaje, el resultado debe de ser el mensaje
    original.

NOTA: el enunciado original tiene errores ortográficos.
"""
from string import ascii_uppercase
from typing import Dict


def build_key(mensaje: str) -> Dict[str, str]:
    return {k: v for k, v in zip(mensaje, ascii_uppercase)}


def encriptar(key: Dict[str, str], mensaje: str) -> str:
    return "".join(key[c] for c in mensaje)


def decodificar(key: Dict[str, str], mensaje: str) -> str:
    return encriptar({v: k for k, v in key.items()}, mensaje)


def main():
    mensaje = input("> ")
    key = build_key(mensaje)
    encriptado = encriptar(key, mensaje)
    print(f"Mensaje encriptado: {encriptado}")
    print(f"Mensaje desencriptado: {decodificar(key, encriptado)}")


if __name__ == "__main__":
    main()
