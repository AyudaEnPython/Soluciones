"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
VOCALES = "aeiouáéíóúAEIOUÁÉÍÓÚ"


def to_upper(text: str) -> str:
    return text.upper()


def contar_espacios(text: str) -> int:
    return text.count(" ")


def contar_vocales(text: str) -> int:
    return sum(1 for c in text if c in VOCALES)
