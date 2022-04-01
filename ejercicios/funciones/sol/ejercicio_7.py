"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass


@dataclass
class Animal:
    """
    >>> perro = Animal('perro', 'blanco')
    >>> perro.cumplir_años()
    1
    >>> perro.cumplir_años()
    2
    >>> perro.cumplir_años()
    3
    """
    especie: str
    color: str
    edad: int = 0

    def cumplir_años(self):
        self.edad += 1
        return self.edad


if __name__ == "__main__":
    import doctest
    doctest.testmod()
