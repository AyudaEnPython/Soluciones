"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: If there's a bug, report it asap.
"""
from prototools import Menu

from models import Avion, Pasajero, Tripulante, Vuelo
from utils import load_data


def _informacion():
    data = load_data("data.json")  # soluciones/aereolinea/data.json
    avion = Avion(
        data["avion"]["modelo"],
        data["avion"]["fabricante"],
        [
            Tripulante(**data["piloto"]),
            Tripulante(**data["copiloto"]),
        ]
    )
    for pasajero in data["pasajeros"]:
        p = Pasajero(**pasajero)
        if avion.registrar_pasajero(p):
            avion.pasajeros.append(p)
    return Vuelo(avion, data["aerolinea"])


def main():
    vuelo = _informacion()
    menu = Menu()
    menu.add_options(
        ("Mostrar información", lambda: vuelo.mostrar_informacion()),
        ("Listar pasajeros", lambda: vuelo.avion.mostrar_pasajeros()),
        ("Listar tripulantes", lambda: vuelo.avion.mostrar_tripulantes()),
        ("Buscar pasajero",
            lambda: print(vuelo.avion.buscar_pasajero(input("DNI: ")))),
        ("Bajar pasajero",
            lambda: vuelo.avion.bajar_pasajero(input("DNI: "))),
    )
    menu.run()


if __name__ == '__main__':
    main()
