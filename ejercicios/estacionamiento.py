"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

El parqueadero (estacionamiento) Autoseguro necesita crear un programa
para que sus empleados puedan calcular el valor a pagar por el uso del
parqueadero (estacionamiento).

- Solamente se reciben 3 tipos de vehículos: automóviles, camionetas y
    motos. El valor estipulado para cada uno de estos vehículos por
    minuto es de $100, $120 y $70 respectivamente. El parqueadero sólo
    funciona de 7:00 a.m. a 7:00 p.m.
- El programa debe capturar la placa del vehículo, el tipo de vehículo
    (se debe presentar un menú con los 3 tipos y el valor por minuto),
    la hora de entrada y la hora de salida (se necesita utilizar la
    hora militar, es decir de 24 horas).
- Como salida se debe mostrar la información capturada, la cantidad de
    minutos que duró el vehículo estacionado y el valor a pagar.
- Debe utilizar una clase con sus atributos, el método constructor y 3
    métodos para: capturar la información, calcular la cantidad de
    minutos y el valor a pagar por el parqueadero, y mostrar la
    información.
- Todos los datos ingresados por el usuario deben ser validados.
- El programa debe funcionar mientras el usuario necesite ingresar más
    registros.

NOTA: El problema sugiere un diseño demasiado acoplado, por ejemplo la
    clase es responsable del ingreso de los datos. Se opta por un
    diseño mas desacoplado aumentando la legibilidad del código, su
    reusabilidad y la facilidad para realizar los casos de prueba.
"""
import unittest
from datetime import datetime
from dataclasses import dataclass
from typing import Dict, Tuple

# pip install prototools
from prototools import choice_input, time_input, main_loop, textbox, text_align

TIPOS: Tuple[str] = ("Automovil", "Camioneta", "Moto")
PRECIOS: Tuple[int] = (100, 120, 70)


@dataclass
class Vehiculo:
    placa: str
    tipo: str

    def __str__(self) -> str:
        return f"Placa del vehiculo: {self.placa}\n" \
                f"Tipo de vehiculo: {self.tipo}\n"


@dataclass
class Cronometro:
    entrada: str
    salida: str

    def duracion(self) -> int:
        entrada = datetime.strptime(self.entrada, "%H:%M:%S")
        salida = datetime.strptime(self.salida, "%H:%M:%S")
        return (salida - entrada).seconds // 60


class Estacionamiento:
    
    precios: Dict[str, int] = {k:v for k, v in zip(TIPOS, PRECIOS)}

    def __init__(
        self,
        vehiculo: Tuple[str, str],
        tiempo: Tuple[str, str]
    ) -> None:
        self.vehiculo = Vehiculo(*vehiculo)
        self.cronometro = Cronometro(*tiempo)
        self.minutos = self.cronometro.duracion()
        self.__monto()

    def __monto(self) -> None:
        self.monto = self.precios[self.vehiculo.tipo] * self.minutos

    def info(self) -> str:
        return (
            f"{self.vehiculo}\n"
            f"Minutos estacionados: {self.minutos} minutos\n"
            f"Monto a pagar: $ {self.monto}"
        )


def mostrar_detalles(estacionamiento: Estacionamiento) -> None:
    textbox("Detalles del Registro", ancho=40, alineacion="centro")
    print(estacionamiento.info())
    text_align("Fin del proceso", ancho=40)


def datos() -> Tuple[Tuple[str, str], Tuple[str, str]]:
    textbox("Registro", ancho=40, alineacion="centro")
    placa = input("Ingresar placa: ").upper()
    print(f"Tipo de vehículo: {' - '.join(tipo for tipo in TIPOS)}")
    tipo = choice_input(TIPOS, "Ingresar tipo: ").capitalize()
    entrada = time_input("Hora de entrada: ").strftime("%H:%M:%S")
    salida = time_input("Hora de salida: ").strftime("%H:%M:%S")
    return (placa, tipo), (entrada, salida)


def autoseguro_main():
    vehiculo, tiempo = datos()
    estacionamiento = Estacionamiento(vehiculo, tiempo)
    mostrar_detalles(estacionamiento)


class Test(unittest.TestCase):

    v, t = ("AEP-101", "Moto"), ("7:00:00", "7:30:00")

    def setUp(self) -> None:
        self.estacionamiento = Estacionamiento(self.v, self.t)
        self.cronometro = Cronometro(*self.t)

    def test_Vehiculo(self):
        v = Vehiculo(*self.v)
        self.assertEqual(v.placa, "AEP-101")
        self.assertEqual(v.tipo, "Moto")

    def test_Cronometro(self):
        c = Cronometro(*self.t)
        self.assertEqual(c.duracion(), 30)

    def test_Estacionamiento(self):
        self.assertEqual(self.estacionamiento.vehiculo.placa, "AEP-101")
        self.assertEqual(self.estacionamiento.vehiculo.tipo, "Moto")
        self.assertEqual(self.estacionamiento.cronometro.duracion(), 30)
        self.assertEqual(self.estacionamiento.monto, 2100)


if __name__ == "__main__":
    main_loop(autoseguro_main)
    # unittest.main() # comment main_lopp and uncomment this line to execute the test
