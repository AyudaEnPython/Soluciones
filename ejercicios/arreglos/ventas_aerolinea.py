"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Una aerolínea colombiana está incursionando en el mercado ofreciendo un
primer trayecto entre Bogotá y Cali. Para ganar clientes ha ofrecido
una estrategia de venta de tiquetes por categorías. Esta empresa
requiere una aplicación para gestionar la venta de tiquetes. Cada vez
que se hace una venta, se almacena en un arreglo el código del tiquete
que se vendió. A cada tipo de tiquete le corresponde un código:
Para los de tipo económico el código es 1, para los de tipo confortable
el código es 2 y para los de tipo flexible el código es 3.

    [1, 1, 1, 3, 2, 3, 1, 3, 2, 1, 3, 3, 2, 1, 3, 1, 2, 3, 1, 2]
    Arreglo ventas de tiquetes aéreos

Clasificación de tiquetes

    +-----------------------+--------+---------------------+
    | Categoría del tiquete | Código | Precio por trayecto |
    +-----------------------+--------+---------------------+
    | Económico             |   1    |              80.000 |
    | Confortable           |   2    |             100.000 |
    | Flexible              |   3    |             130.000 |
    +-----------------------+--------+---------------------+

La aplicación debe:
1. Registrar las ventas de los tiquetes de acuerdo a su código. Las
    ventas se irán registrando hasta que el usuario diga que no.
2. Calcular e imprimir el número de tiquetes vendidos por cada tipo.
3. Calcular e imprimir el total de tiquetes vendidos.
4. Calcular e imprimir cuál es el tipo de tiquete que más se vendió.
5. Calcular e imprimir el valor de las ventas, tener en cuenta el
    precio por trayecto que se presenta en la tabla.
"""
from typing import Dict, List

CLASIFICACION: Dict[int, int] = {1: 80_000, 2: 100_000, 3: 130_000}
CATEGORIAS: Dict[int, str] = {1: "Económico", 2: "Confortable", 3: "Flexible"}


def ingresar_ventas() -> List[int]:
    ventas = []
    while True:
        codigo = input("Ingrese el código: ")
        try:
            codigo = int(codigo)
            if codigo not in CLASIFICACION:
                print("Código inválido")
                continue
            ventas.append(codigo)
            if input("Desea continuar? (s/n): ").lower() == "n":
                break
        except ValueError:
            print("Código inválido")
    return ventas


def vendidos_por_tipo(ventas: List[int]) -> Dict[int, int]:
    tipos = {k:0 for k in CLASIFICACION}
    for v in ventas:
        tipos[v] += 1
    return tipos # {x:ventas.count(x) for x in ventas} -> alt. ver


def mas_vendido(tipos: Dict[int, int]) -> str:
    mayor = 0
    for k, v in tipos.items():
        if v > mayor:
            mayor = k
    return CATEGORIAS[mayor]


def venta_total(ventas: List[int]) -> int:
    return sum(CLASIFICACION[v] for v in ventas)


def main():
    ventas = ingresar_ventas()
    tipos = vendidos_por_tipo(ventas)
    print("\nVENTAS\n")
    for k, v in tipos.items():
        print(f"Tiquetes de tipo {CATEGORIAS[k]}: {v}")
    print(f"Total de tiquetes vendidos: {len(ventas)}")
    print(f"Tipo de tiquete más vendido: {mas_vendido(tipos)}")
    print(f"Valor total de ventas: {venta_total(ventas)}")


if __name__ == "__main__":
    main()
