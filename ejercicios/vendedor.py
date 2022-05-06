"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

+------------+------------+------------+------------+
|Plan/Estrato|      A     |      B     |     C      |
+------------+------------+------------+------------+
|     1      | $30,000.00 | $35,000.00 | $45,000.00 |
+------------+------------+------------+------------+
|     2      | $45,000.00 | $50,000.00 | $60,000.00 |
+------------+------------+------------+------------+
|     3      | $55,000.00 | $60,000.00 | $70,000.00 |
+------------+------------+------------+------------+
|     4      | $70,000.00 | $75,000.00 | $85,000.00 |
+------------+------------+------------+------------+

Datos de entrada:
Nombre del vendedor
Plan vendido (A, B, C)
Estrato socioeconómico (1, 2, 3, 4)

Calculos:
Valor de la venta

Datos de salida:
Todos los datos de entrada
El valor de cada venta
Al final, el acumulado de las ventas

* No se conoce cuantos vendedores se van a procesar
"""
from typing import Dict, List, Union
# pip install prototools
from prototools import int_input, menu_input

CUADRO: Dict[str, List[int]] = {
    "A": [30_000, 45_000, 55_000, 70_000],
    "B": [35_000, 50_000, 60_000, 75_000],
    "C": [45_000, 60_000, 70_000, 85_000],
}


def datos() -> Dict[str, Union[str, int]]:
    nombre = input("Nombre del vendedor: ").title()
    # plan = input("Plan vendido (A, B, C): ").upper()
    plan = menu_input(tuple(CUADRO.keys()), numbers=True)
    # estrato = int(input("Estrato socioeconómico (1, 2, 3, 4): "))
    estrato = int_input("Estrato socioeconómico (1, 2, 3, 4): ", min=1, max=4)
    valor = CUADRO[plan][estrato - 1]
    return dict(nombre=nombre, plan=plan, estrato=estrato, valor=valor)


def info(data: Dict[str, Union[str, int]]) -> str:
    return (
        f"{data['nombre']:<18}|{data['plan']:^6}|{data['estrato']:^9}|"
        f" ${data['valor']:>10,.2f}"
    )


def mostrar(informe: List[str], total: int) -> None:
    print("-" * 48)
    print(f"{'Vendedor':<18}|{'Plan':^6}|{'Estrato':^9}|{'Valor':>10}")
    print("\n".join(informe))
    print("-" * 48)
    print(f"Total: $ {total}")


def main():
    informe, total = [], 0
    while True:
        data = datos()
        informe.append(info(data))
        total += data["valor"]
        if input("¿Continuar? (si/no): ").lower() in "no":
            break
    mostrar(informe, total)


if __name__ == "__main__":
    main()
