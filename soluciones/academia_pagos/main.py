"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, Tuple, Union
# pip install prototools
from prototools import Menu, str_input, int_input, menu_input, textbox

Data = Dict[str, Dict[str, Union[str, int]]]
HEADER = f"{'DNI':<20}{'Nombre':<20}{'Cargo':<20}{'Horas':<15}{'Pago':<15}"
CUADRO: Dict[str, Dict[str, int]] = {
    "Principal": {"horas": 50, "tarifa": 24},
    "Tutor": {"horas": 25, "tarifa": 16},
    "Asistente": {"horas": 20, "tarifa": 24},
}
docentes: Data = {
    "12345678": {
        "nombre": "Jason Becker",
        "cargo": "Principal",
        "horas": 40,
        "pago": 960
    },
    "87654321": {
        "nombre": "Shawn Lane",
        "cargo": "Tutor",
        "horas": 24,
        "pago": 384
    },
    "45612378": {
        "nombre": "Jimmy Hendrix",
        "cargo": "Asistente",
        "horas": 20,
        "pago": 480
    },
}


def _datos(dni: str, datos: Data) -> None:
    print(
        f"{dni:<20}{datos['nombre']:<20}{datos['cargo']:<20}"
        f"{datos['horas']:<15}{datos['pago']:<15}"
    )


def _estadisticas(rol: str) -> Tuple[int, int, float]:
    min_ = float("inf")
    max_ = float("-inf")
    mean_ = 0
    for _, datos in docentes.items():
        if datos["cargo"] == rol:
            mean_ += datos["pago"]
            if datos["pago"] < min_:
                min_ = datos["pago"]
            if datos["pago"] > max_:
                max_ = datos["pago"]
    mean_ /= len(docentes)
    return min_, max_, mean_


def _guardar(dni: str, nombre: str, cargo: str, horas: int) -> None:
    if dni not in docentes:
        docentes[dni] = {
            "nombre": nombre,
            "cargo": cargo,
            "horas": horas,
            "pago": horas * CUADRO[cargo]["tarifa"],
        }
    else:
        print("Error: el docente ya existe!")


def ingresar_datos() -> None:
    dni = str_input("DNI: ")
    nombre = str_input("Nombre Completo: ")
    cargo = menu_input(
        ("Principal", "Tutor", "Asistente"), numbers=True, lang="es",
    )
    horas = int_input("Horas: ", min=1, max=CUADRO[cargo]["horas"], lang="es")
    _guardar(dni, nombre, cargo, horas)


def mostrar_estadisticas() -> None:
    rol = menu_input(
        ("Principal", "Tutor", "Asistente"), numbers=True, lang="es",
    )
    min_, max_, mean_ = _estadisticas(rol)
    textbox(f"Estadísticas para el rol {rol}")
    print("\n" + HEADER)
    for dni, datos in docentes.items():
        if datos["cargo"] == rol:
            _datos(dni, datos)
    if mean_ != 0:
        print(f"\nMínimo: {min_}")
        print(f"Máximo: {max_}")
        print(f"Promedio: {mean_}")
    else:
        print("No hay datos para mostrar")


def mostrar_planilla() -> None:
    textbox("Planilla de pagos")
    print(HEADER)
    for dni, datos in docentes.items():
        _datos(dni, datos)


def main():
    menu = Menu(
        "Cachimbo",
        subtitle="Academia Preuniversitaria",
    )
    menu.add_options(
        ("Ingresar Datos", ingresar_datos),
        ("Mostrar Planilla de pagos", mostrar_planilla),
        ("Estadísticas", mostrar_estadisticas),
    )
    menu.settings(
        style="double",
        separators=True,
        subtitle_align="center",
    )
    menu.run()


if __name__ == "__main__":
    main()
