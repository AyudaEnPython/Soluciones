"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Base de datos:

trabajadores = {
    "Daniel": {
        "área": "ventas",
        "desempeño": 30,
    },
    "Alan": {
        "área": "recursos humanos",
        "desempeño": 85,
    },
    "Jose": {
        "área": "ventas",
        "desempeño": 89,
    },
}


- Escribe una función que identifique a los trabajadores con bajo
    desempeño. Si se encuentra alguno, se debe mostrar "Se
    recomienda despedir al trabajador". Luego, se elimina/n de la
    base de datos.
- Aplica la función a la base de datos de trabajadores. Luego,
    muestra los nombres de los empleados restantes en una columna
    marcada como:
    "Los trabajadores con mejor desempeño son:
    X
    Y
    Z"

NOTE: el diseño que plantea el enunciado no es el correcto.
"""
from typing import Dict, List, Union

BAJO, ALTO = 60, 85

trabajadores: Dict[str, Dict[str, Union[str, int]]] = {
    "Daniel": {
        "área": "ventas",
        "desempeño": 30,
    },
    "Alan": {
        "área": "recursos humanos",
        "desempeño": 85,
    },
    "Jose": {
        "área": "ventas",
        "desempeño": 89,
    },
    "Yngwie": {
        "área": "gerencia",
        "desempeño": 70,
    }
}


def desempeño(nivel: str) -> List[str]:
    return [
        nombre for nombre, datos in trabajadores.items()
        if nivel == "bajo" and datos["desempeño"] < BAJO
        or nivel == "alto" and datos["desempeño"] >= ALTO
    ]


def despedir(data: List[str]) -> None:
    for nombre in data:
        del trabajadores[nombre]


def recomendacion(data: List[str]) -> None:
    if not data:
        return
    for nombre in data:
        print(f"Se recomienda despedir al trabajador: {nombre}")


def show(nivel: str, texto: str) -> None:
    print(f"Los trabajadores con {texto} desempeño son:")
    for nombre in desempeño(nivel):
        print(nombre)


def main():
    bajo_desempeño = desempeño("bajo")
    recomendacion(bajo_desempeño)
    despedir(bajo_desempeño)
    show("alto", "mejor")


if __name__ == "__main__":
    main()
