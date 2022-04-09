"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

TODO: mockup... needs farther development
"""
from dataclasses import dataclass, field
from typing import List

TIPOS = "Novela", "Teatro", "Poesia", "Ensayo", "Teoria"


@dataclass
class Persona:
    nombre: str


@dataclass
class Autor(Persona):
    nacionalidad: str
    dob: str


@dataclass
class Libro:
    _id: int
    nombre: str
    tipo: str
    editorial: str
    año: str
    autor: Autor
    copias: int
    _estado: bool = field(init=False, repr=False)


@dataclass
class Lector:
    _id: int
    _max: int
    libro: Libro = field(default=None)
    _estado: bool = field(init=False, repr=False)


@dataclass
class Biblioteca:
    libros: List[Libro] = field(default_factory=list)
    lectores: List[Lector] = field(default_factory=list)


if __name__ == "__main__":
    libro = Libro(
        1,
        "Vaideology",
        "Teoria",
        "Hal Leonard PUB CO",
        "2020",
        Autor("Americano", "01/01/1930", "Steve Vai"),
        4,
    )
    print(libro)
