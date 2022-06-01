"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from dataclasses import dataclass

RENTA, DESEMPLEO = 0.08, 0.13


@dataclass
class Persona:
    dni: str
    nombre: str
    apellido: str

    def __str__(self) -> str:
        return f"[{self.dni}] {self.apellido}, {self.nombre}"


@dataclass
class Trabajador(Persona):
    sueldo: float
    pago_horas_extras: float
    horas_extras: int

    def obtener_sueldo(self) -> float:
        return self.sueldo + self.pago_horas_extras * self.horas_extras

    def obtener_descuentos(self) -> float:
        return self.obtener_sueldo() * (RENTA + DESEMPLEO)

    def obtener_sueldo_neto(self) -> float:
        return self.obtener_sueldo() - self.obtener_descuentos()

    def detalles(self) -> str:
        return (
            f"{super().__str__()}\n"
            f"Sueldo: {self.obtener_sueldo():.2f}\n"
            f"Descuentos: {self.obtener_descuentos():.2f}\n"
            f"Sueldo neto: {self.obtener_sueldo_neto():.2f}"
        )


def main():
    trabajador = Trabajador("45478432", "Jason", "Becker", 6500, 80, 10)
    print(trabajador.detalles())


if __name__ == "__main__":
    main()
