from typing import Dict


class Lector:

    def __init__(self, codigos: Dict[str, float]) -> None:
        self.codigos = codigos

    def leer(self, sku: str) -> str:
        if sku not in self.codigos:
            raise KeyError(f"El código {sku} no está registrado")
        return sku


class CajaRegistradora:

    def __init__(self) -> None:
        self.productos = {}
        self.ventas = []

    def registrar_producto(self, sku: str, precio: float) -> None:
        self.productos[sku] = precio

    def registrar_venta(self, sku: str) -> None:
        lector = Lector(self.productos)
        try:
            self.ventas.append(lector.leer(sku))
        except KeyError as e:
            print(e)

    def calcular(self) -> float:
        return sum(self.productos[sku] for sku in self.ventas)


if __name__ == "__main__":
    caja = CajaRegistradora()
    caja.registrar_producto("A", 62.0)
    caja.registrar_producto("B", 145.5)
    caja.registrar_producto("C", 140.5)
    caja.registrar_venta("C")
    caja.registrar_venta("A")
    caja.registrar_venta("A")
    caja.registrar_venta("B")
    print(caja.calcular())
