"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass
from typing import Dict

TIPO: Dict[str, float] = {"MAYORISTA 4.5%": 0.045, "MINORISTA 1.9%": 0.190}
CREDITO: Dict[str, float] = {
    "0 DÍAS 0%": 0.000,
    "15 DÍAS 8.5%": 0.085,
    "30 DÍAS 12.5%": 0.125,
}


def output(c: object, p: object, n: int = 25) -> str:
    return (
        f"{'Código del cliente':>{n}}: {c.codigo}\n"
        f"{'Nombre del cliente':>{n}}: {c.nombre}\n\n"
        f"{'Producto':>{n}}: {p.nombre}\n"
        f"{'Precio':>{n}}: S/. {p.precio:.2f}\n"
        f"{'Cantidad':>{n}}: {p.cantidad}\n\n"
        f"{'Importe':>{n}}: S/. {p.total:.2f}\n"
        f"{'Descuento':>{n}}: S/. {p.descuento:.2f}\n"
        f"{'Interés':>{n}}: S/. {p.interes:.2f}\n"
        f"{'Total':>{n}}: S/. {p.calcular_precio():.2f}\n"
    )


@dataclass
class Cliente:
    codigo: str
    nombre: str


@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int
    credito: str
    tipo: str

    def __post_init__(self):
        self.total = round(self.precio * self.cantidad, 2)
        self.interes = round(CREDITO[self.credito] * self.total, 2)
        self.descuento = round(TIPO[self.tipo] * self.total, 2)

    def calcular_precio(self) -> float:
        return round(
            self.precio * self.cantidad - self.descuento + self.interes,
            2,
        )


class Proforma:

    def __init__(self, cliente: Cliente, producto: Producto) -> None:
        self.cliente = cliente
        self.producto = producto

    def title(self, n: int = 51) -> str:
        bars = "+" + "-"*n + "+"
        title_ = "PROFORMA"
        return f"{bars}\n|{title_:^{n}}|\n{bars}\n\n"

    def __str__(self) -> str:
        return self.title() + output(self.cliente, self.producto)


if __name__ == "__main__":
    cliente = Cliente("P001", "Juan Lopez Guevara")
    producto = Producto("Teclado", 35, 10, "15 DÍAS 8.5%", "MAYORISTA 4.5%")
    proforma = Proforma(cliente, producto)
    print(proforma)
