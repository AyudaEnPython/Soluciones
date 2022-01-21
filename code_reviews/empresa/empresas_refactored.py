"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from prototools import float_input, int_input


class Empresa:
    
    def __init__(
        self, ingresos: float, costos: float, salarios: float, personas: int
    ) -> None:
        self.ingresos = ingresos
        self.costos = costos
        self.salarios = salarios
        self.personas = personas

    def utilidades(self) -> float:
        return self.ingresos - self.costos

    def salario(self) -> float:
        return self.salarios / self.personas

    def utilidad(self) -> float:
        return self.utilidades() / self.personas
    
    def __str__(self) -> str:
        return f"Ingresos: {self.ingresos} | Costos: {self.costos}"


def main():
    ingresos = float_input("Ingresos: ")
    costos = float_input("Costos: ")
    salarios = float_input("Salarios: ")
    personas = int_input("Personas: ")
    empresa = Empresa(ingresos, costos, salarios, personas)
    print(empresa)
    print(f"Utilidades: {empresa.utilidades()}")
    print(f"Salario por persona: {empresa.salario()}")
    print(f"Utilidad por persona: {empresa.utilidad()}")


if __name__ == "__main__":
    main()