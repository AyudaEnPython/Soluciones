"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Un BOEING 747 tiene una capacidad de carga para equipaje de
aproximadamente 18000 Kg. Realice un programa que ingrese equipaje al
avión solicitando el peso de cada carga por teclado y que entregue al
operador el valor de la carga sabiendo que:

Se deben rechazar los bultos de más de 500 Kg. El valor por Kg del
bulto es:
- de 0 a 25 Kg $1000 por Kg.
- de 26 a 300 Kg $1500 por Kg.
- de 301 a 500 Kg $2000 por Kg.

Notar que los pesos siempre estarán en Kg (sin decimales). Considere
que el precio por un bulto de 30 Kg es 30*1500 y no 25*1000 + 5*1500.

Cuando se intente agregar un nuevo bulto y con este se sobrepasen los
18000 Kg de carga en el avión, el programa no debe agregar dicho bulto
y debe mostrar la siguiente información con respecto al vuelo:
- Número total de bultos
- Peso del bulto más pesado
- Peso promedio de los bultos
- Ingreso total por concepto de carga en el avión.

Nota:
Asuma que los bultos se ingresan uno por uno. Además, habrán
suficientes bultos para copar la capacidad del avión.
"""
from typing import List

MAX = 18_000
BULTO_MAX = 500


def ingresar_carga() -> List[int]:
    bultos = []
    while True:
        bulto = input("Ingrese el peso del bulto: ")
        try:
            bulto = int(bulto)
            if bulto > BULTO_MAX:
                print("El bulto es demasiado pesado")
                continue
            if sum(bultos) + bulto > MAX:
                print("El avión no tiene suficiente capacidad")
                break
            bultos.append(bulto)
        except ValueError:
            print("El peso debe ser un número")
            continue
        if input("¿Desea ingresar otro bulto? (s/n): ") == "n":
            break
    return bultos


def _valor(bulto: int) -> int:
    if bulto <= 25:
        return 1000 * bulto
    elif 26 <= bulto <= 300:
        return 1500 * bulto
    else:
        return 2000 * bulto


def total(bultos: List[int]) -> int:
    return sum(_valor(b) for b in bultos)


def main():
    bultos = ingresar_carga()
    print(f"Número total de bultos: {len(bultos)}")
    print(f"Bulto más pesado: {max(bultos)}")
    print(f"Peso promedio: {sum(bultos) / len(bultos):.2f}")
    print(f"Ingreso total: {total(bultos)}")


if __name__ == "__main__":
    main()
