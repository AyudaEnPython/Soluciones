"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Se desea organizar una compotencia de motociclismo con la participación
de 10 competidores, los cuales serán distribuidos en las diferentes
categorías que se describen a continuación:

- Primera: cilindrajes de motos de 50 cc hasta 250cc.
- Segunda: cilindrajes de motos de 251 cc hasta 500cc.
- Tercera: cilindrajes de motos superiores a 500cc.

Por cada participante se tiene un registro con los siguientes datos:

- Identificación
- Nombres
- Cilindraje de la moto.

Elaborar un algoritmo que:

a) Al registrar un participante se debe comprobar el cilindraje dado e
    inscribirlo en la categoría correspondiente y mostrar un mensaje
    que indique su nombre y la categoría a la que fue inscrito.

b) Muestre la cantidad de participantes aceptados en cada categoría.

c) Muestre el total de participantes aceptados.

TODO: add tests.
"""
from typing import Dict, List, Tuple

CATEGORIAS: Tuple[str] = ("Primera", "Segunda", "Tercera")


def categorizar(cilindraje: int) -> str:
    """Categoriza un cilindraje de motocicleta.

    :param cilindraje: cilindraje de la motocicleta.
    :ciliandraje type: int
    :return: categoría a la que pertenece.
    :rtype: str
    """
    if cilindraje <= 250:
        return "Primera"
    elif cilindraje <= 500:
        return "Segunda"
    else:
        return "Tercera"


def cantidad(participantes: List[Tuple[str, str, int]]) -> Dict[str, int]:
    """Calcula la cantidad de participantes por categoría.

    :param participantes: lista de participantes.
    :participantes type: List[Tuple[str, str, int]]
    :return: cantidad de participantes por categoría (diccionario).
    :rtype: Dict[str, int]
    """
    return {
        categoria: len([p for p in participantes if p[3] == categoria])
        for categoria in CATEGORIAS
    }


def main():
    participantes = []
    n = 3
    for i in range(1, n+1):
        id_ = input(f"[{i}] Ingresar ID: ")
        nombres = input(f"[{i}] Ingresar nombres: ")
        cc = int(input(f"[{i}] Ingresar cilindraje: "))
        print(f"{nombres} fue aceptado en la categoría {categorizar(cc)}")
        categoria = categorizar(cc)
        participantes.append((id_, nombres, cc, categoria))
    print()
    for categoria in CATEGORIAS:
        print(
            f"Participantes en {categoria}: "
            f"{cantidad(participantes)[categoria]}"
        )
    print(f"Total de participantes aceptados: {len(participantes)}")


if __name__ == "__main__":
    main()
