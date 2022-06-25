"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Diseñe un programa que lea, por cada vehículo, que pasa por un peaje,
el tipo y la cantidad de pasajeros que transporta. Muestre, a
continuación, un reporte indicando:

- La cantidad total de vehículos de cada tipo que pasaron por el peaje.
- La cantidad total de pasajeros por cada tipo de vehículo.

Los tipos de vehículos por considerar son: automóvil, camión, camioneta,
omnibus y otros.

NOTE: el enunciado es muy general.
"""
from random import choice, randint
from collections import namedtuple
from typing import Dict, List

Vehiculo = namedtuple("Vehiculo", "tipo cantidad")
MIN, MAX = 20, 40
TIPOS: Dict[str, int] = {
    "automóvil": 5,
    "camión": 3,
    "camioneta": 7,
    "omnibus": 47,
    "otros": 2,
}


def _vehiculos(n: int) -> List[Vehiculo]:
    vehiculos: List[Vehiculo] = []
    for _ in range(n):
        tipo = choice(tuple(TIPOS.keys()))
        cantidad = randint(1, TIPOS[tipo])
        vehiculos.append(Vehiculo(tipo, cantidad))
    return vehiculos


def main():
    data: Dict[str, List[int, int]] = {k: [0, 0] for k in TIPOS.keys()}
    vehiculos = _vehiculos(randint(MIN, MAX))
    for vehiculo in vehiculos:
        data[vehiculo.tipo][0] += 1
        data[vehiculo.tipo][1] += vehiculo.cantidad
    print("\nReporte de vehículos\n")
    print(f"Total de vehículos: {len(vehiculos)}")
    for tipo, (cantidad, pasajeros) in data.items():
        print(f"{tipo}: {cantidad}, pasajeros: {pasajeros}")


if __name__ == "__main__":
    main()
