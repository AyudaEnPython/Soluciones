"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Realizar un programa donde crees un archivo txt donde debes crear solo
el archivo y abrirlo luego llenarlo con nombres apellidos y edad, luego
de esto mostrar por consola a manera de diccionario lo que agregaste
al archivo.txt
"""
from typing import Dict, List


def open_file(filename: str, encoding="utf-8") -> List[str]:
    with open(filename, encoding=encoding) as f:
        return f.read().splitlines()


def to_dict(data: List[str]) -> List[Dict[str, str]]:
    return [
        dict(nombre=nombre, apellido=apellido, edad=edad)
        for (nombre, apellido, edad) in (line.split(" ") for line in data)
    ]


def main():
    data = open_file("data.txt")
    print(to_dict(data))


if __name__ == "__main__":
    main()
