from prototools.menu import EzMenu

from models import Avion, Pasajero, Tripulante, Vuelo
from utils import load_data


def _informacion():
    data = load_data("data.json") #soluciones/aereolinea/data.json
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
    menu = EzMenu()
    menu.agregar_opciones(
        "Mostrar información",
        "Listar pasajeros",
        "Listar tripulantes",
        "Buscar pasajero",
        "Bajar pasajero",
        "Salir"
    )
    menu.agregar_funciones(
        lambda: vuelo.mostrar_informacion(),
        lambda: vuelo.avion.mostrar_pasajeros(),
        lambda: vuelo.avion.mostrar_tripulantes(),
        lambda: print(vuelo.avion.buscar_pasajero(input("dni: "))),
        lambda: vuelo.avion.bajar_pasajero(input("dni: ")),
    )
    menu.run()


if __name__ == '__main__':
    main()