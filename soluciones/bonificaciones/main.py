"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from typing import Dict, Tuple
from random import randint, choice

TIENDAS = "san isidro", "la molina"
TIPOS = "cotidiano", "frecuente", "superior"
DIAS = (
    "lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"
)


def bonificacion_tienda(tienda: str, monto: int) -> float:
    return {
        "san isidro": {
            monto <= 100: 10.61,
            100 < monto <= 160: 20.52,
            160 < monto <= 180: 30.43,
            monto > 180: 40.11,
        },
        "la molina": {
            monto <= 250: 45.34,
            250 < monto <= 300: 50.25,
            300 < monto <= 450: 65.16,
            monto > 450: 75.13,
        }
    }[tienda][True]


def bonificacion_especial(tipo: str) -> int:
    return {"cotidiano": 10, "frecuente": 12, "superior": 20}[tipo]


def bonificacion_dia(dia: str) -> int:
    tabla: Dict[Tuple[str, ...], int] = {
        ("lunes", "martes", "miercoles"): 20,
        ("jueves", "viernes"): 15,
        ("sabado", "domingo"): 10,
    }
    return tabla[list(filter(lambda d: dia in d, tabla))[0]]


def total(tienda: str, monto: int, tipo: str, dia: str) -> float:
    return (
        bonificacion_tienda(tienda, monto) + 
        bonificacion_especial(tipo) +
        bonificacion_dia(dia)
    )


def show(tienda: float, especial: int, dia: int) -> None:
    print(f"Bonificación por monto y tienda: {tienda}")
    print(f"Bonificación por tipo de cliente: {especial}")
    print(f"Bonificación de acuerdo al día: {dia}")


def main():
    monto = randint(90, 500)
    tienda, tipo, dia = choice(TIENDAS), choice(TIPOS), choice(DIAS)
    b_tienda = bonificacion_tienda(tienda, monto)
    b_especial = bonificacion_especial(tipo)
    b_dia = bonificacion_dia(dia)
    show(b_tienda, b_especial, b_dia)
    print(f"Bonificación total: {total(tienda, monto, tipo, dia)}")


if __name__ == "__main__":
    main()
