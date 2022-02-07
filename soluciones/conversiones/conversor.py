"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
# pip install prototools
from prototools import str_input, int_input, textbox


def bin_to_dec() -> None:
    """Convierte un binario a decimal."""
    n = str_input("> ")
    result = int(n, 2)
    textbox(str(result))


def dec_to_bin() -> None:
    """Convierte un decimal a binario."""
    n = int_input("> ")
    result = bin(n)[2:]
    textbox(str(result))


def bin_to_hex() -> None:
    """Convierte un binario a hexadecimal."""
    n = str_input("> ")
    result = hex(int(n, 2))[2:]
    textbox(str(result))


def hex_to_bin() -> None:
    """Convierte un hexadecimal a binario."""
    n = str_input("> ")
    result = bin(int(n, 16))[2:]
    textbox(str(result))


def dec_to_hex() -> None:
    """Convierte un decimal a hexadecimal."""
    n = int_input("> ")
    result = hex(n)[2:]
    textbox(str(result))


def hex_to_dec() -> None:
    """Convierte un hexadecimal a decimal."""
    n = str_input("> ")
    result = int(n, 16)
    textbox(str(result))
