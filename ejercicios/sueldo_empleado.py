"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Se debe hallar el resultado de cada empleado, considerando el siguiente
requisito:
- Si es de tipo A y es casado, o tiene hijos, su sueldo será de 2500
    para el resto su sueldo será de 2000.
- Constatar los resultados del reporte:

    +-------------------+----+---------+-----+-------------+
    | Nombre empleado   |Tipo| Estado  |Hijos| Sueldo      |
    +-------------------+----+---------+-----+-------------+
    | Rosales Josué     | A  | Soltero |  3  | S/ 2,500.00 |
    | Belaunde Elías    | A  | Casado  |  0  | S/ 2,500.00 |
    | Gamarra Elizabeth | B  | Soltero |  3  | S/ 2,500.00 |
    | Gómez Claudia     | B  | Soltero |  0  | S/ 2,000.00 |
    | Linares Gustavo   | A  | Soltero |  2  | S/ 2,500.00 |
    | Meza Fernando     | B  | Casado  |  0  | S/ 2,000.00 |
    | Otoya Enrique     | A  | Soltero |  3  | S/ 2,500.00 |
    | Bustos Mario      | B  | Casado  |  0  | S/ 2,000.00 |
    | Mansilla Javier   | B  | Casado  |  3  | S/ 2,500.00 |
    | Carrasco Hugo     | A  | Soltero |  4  | S/ 2,500.00 |
    | Durand Alfonso    | B  | Casado  |  0  | S/ 2,000.00 |
    +-------------------+----+---------+-----+-------------+

Salida:

    +-----------------------------------+-----------+
    | Estadísticas                      | Resultado |
    +-----------------------------------+-----------+
    | Cantidad de sueldos de S/. 2500 = |           |
    | Cantidad de sueldos de S/. 2000 = |           |
    | Total de sueldos a pagar       S/.|           |
    +-----------------------------------+-----------+
"""
from typing import Dict, List, Tuple, Union

reporte: List[Dict[str, Union[str, int]]] = [
    {
        "nombre": "Rosales Josué", "tipo": "A",
        "estado": "Soltero", "hijos": 3,
    },
    {
        "nombre": "Belaunde Elías", "tipo": "A",
        "estado": "Casado", "hijos": 0,
    },
    {
        "nombre": "Gamarra Elizabeth", "tipo": "B",
        "estado": "Soltero", "hijos": 3,
    },
    {
        "nombre": "Gómez Claudia", "tipo": "B",
        "estado": "Soltero", "hijos": 0,
    },
    {
        "nombre": "Linares Gustavo", "tipo": "A",
        "estado": "Soltero", "hijos": 2,
    },
    {
        "nombre": "Meza Fernando", "tipo": "B",
        "estado": "Casado", "hijos": 0,
    },
    {
        "nombre": "Otoya Enrique", "tipo": "A",
        "estado": "Soltero", "hijos": 3,
    },
    {
        "nombre": "Bustos Mario", "tipo": "B",
        "estado": "Casado", "hijos": 0,
    },
    {
        "nombre": "Mansilla Javier", "tipo": "B",
        "estado": "Casado", "hijos": 3,
    },
    {
        "nombre": "Carrasco Hugo", "tipo": "A",
        "estado": "Soltero", "hijos": 4,
    },
    {
        "nombre": "Durand Alfonso", "tipo": "B",
        "estado": "Casado", "hijos": 0,
    },
]


def sueldo(empleado: Dict[str, Union[str, int]]) -> int:
    if (
        (empleado["tipo"] == "A" and empleado["estado"] == "Casado")
        or empleado["hijos"] > 0
    ):
        return 2500
    else:
        return 2000


def estadisticas(emleados: List[Dict[str, Union[str, int]]]) -> Tuple[int, int]:
    a = b = 0
    for empleado in emleados:
        if empleado["sueldo"] == 2500:
            a += 1
        else:
            b += 1
    return a, b


def main():
    total = 0
    for empleado in reporte:
        empleado["sueldo"] = sueldo(empleado)
        total += empleado["sueldo"]
    a, b = estadisticas(reporte)
    print(f"Cantidad de sueldos de S/. 2500: {a}")
    print(f"Cantidad de sueldos de S/. 2000: {b}")
    print(f"Total de sueldos a pagar S/.{total}")


if __name__ == "__main__":
    main()
