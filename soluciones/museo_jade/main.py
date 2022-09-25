"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, List
# pip install prototools
from prototools import Menu, textbox, str_input, date_input_dmy

FILENAME: str = "MuseoJade.vis"
Data = Dict[str, List[str]]


def _search(data: Data, id_: str) -> int:
    if id_ not in data:
        return 0
    return len(data[id_])


def _update(data: Data, date: str, id_: str) -> None:
    if id_ not in data:
        data[id_] = []
    data[id_].append(date)


def _validate_id(id_: str) -> str:
    if len(id_) != 9:
        raise ValueError("Cédula inválida")
    if not id_.isdigit():
        raise ValueError("La cédula debe ser un número")
    return id_


def _write(date: str, id_: str) -> None:
    with open(FILENAME, "a", newline="\n") as f:
        f.write(f"{date} {id_}\n")


def read_file() -> Data:
    with open(FILENAME, "r") as f:
        data = f.read().splitlines()
    _data = {}
    for line in data:
        date, id_ = line.split(" ")
        _update(_data, date, id_)
    return _data


def new_data(data: Data) -> None:
    date = date_input_dmy("Fecha (dd/mm/yy): ", lang="es")
    try:
        id_ = str_input("Cédula: ", function=_validate_id)
    except ValueError as e:
        print(e)
        return None
    _write(date, id_)
    _update(data, date, id_)
    textbox("Registro agregado")


def info(data: Data) -> None:
    id_ = input("Cédula: ")
    textbox(f"Total de visitas: {_search(data, id_)}")


def main():
    data: Data = read_file()
    menu = Menu()
    menu.add_options(
        ("Ingresar nuevo dato", lambda: new_data(data)),
        ("Mostrar informe", lambda: info(data)),
    )
    menu.run()


if __name__ == "__main__":
    main()
