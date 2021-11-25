"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass, field
from typing import Dict
from pandas import DataFrame
from random import choices
from string import digits


@dataclass
class Volume:
    id_: str
    name: str


@dataclass
class Book(Volume):
    isbn: str

    def __str__(self) -> str:
        return f"{self.id_} | {self.name} | {self.isbn}"


@dataclass
class Magazine(Volume):
    issn: str

    def __str__(self) -> str:
        return f"{self.id_} | {self.name} | {self.issn}"


@dataclass
class Library:
    name: str
    address: str
    volumes: Dict[str, Volume] = field(default_factory=dict)

    def add(self, volume: Volume):
        if volume.id_ in self.volumes:
            raise ValueError(f"El id {volume.id_} ya existe")
        self.volumes[volume.id_] = volume
    
    def remove(self, id_: str):
        if id_ not in self.volumes:
            raise ValueError(f"El id {id_} no existe")
        del self.volumes[id_]

    def save(self):
        return DataFrame(self.volumes.values()) 


if __name__ == "__main__":
    random_code = lambda: "".join(choices(digits, k=10))

    library = Library("AyudaEnPython", "cloud")
    books = ("Core Python", "Modern C++", "Rust in Action")
    magazines = ("Guitar World", "Guitarist", "Guitar Player")
    for id_, book in enumerate(books, 1):
        library.add(Book(str(id_), book, random_code()))
    for id_, magazine in enumerate(magazines, len(books) + 1):
        library.add(Magazine(str(id_), magazine, random_code()))
    try:
        library.add(Magazine("6", "Guitar Player", random_code()))
    except ValueError as e:
        print(e)
    print(library)
    library.remove("6")
    df = library.save()
    print(df)
    df.to_excel("data.xlsx", index=False)