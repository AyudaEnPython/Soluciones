"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crear una aplicación de consola que permita al usuario programar alarmas
de tiempo. Para realizar esta aplicación deberá presentarle al usuario
las siguientes opciones: ver alarmas activas, agregar nueva alarma,
agregar nueva alarma con tiempo aleatorio, editar alarma existente y 
quitar alarma.

Para este ejercicio debe crear una clase llamada Reloj que contenga los
atributos necesarios para almacenar el tiempo (horas, minutos y segundos),
guiarse de las siguientes restricciones y utilizar el diagrama de clase:
- Programe un método constructor vacío que cree objetos con un tiempo 
    (horas, minutos y segundos) aleatorio.
- Programe un método que reciba las horas, minutos y segundos para la nueva
    alarma.
- Cree un método para modificar los segundos.
- Cree un método para modificar los minutos.
- Cree un método para modificar las horas.
- Programe un método que devuelva una cadena de texto que incluya la hora
    actual de la variable en formato hh:mm:ss.

* Considere el valor actual y el valor máximo que puede contener cada uno
de los atributos al momento de añadir tiempo.

            +----------------------------------------+
            |                  Reloj                 |
            +----------------------------------------+
            | - horas: int                           |
            | - minutos: int                         |
            | - segundos: int                        |
            +----------------------------------------+
            | + agregar_horas(int horas): void       |
            | + agregar_minutos(int minutos): void   |
            | + agregar_segundos(int segundos): void |
            | + visualizar(): string                 |
            +----------------------------------------+
"""
from random import randint
from prototools import Menu, int_input


class Reloj:
    def __init__(self) -> None:
        self._horas = randint(0, 24)
        self._minutos = randint(0, 59)
        self._segundos = randint(0, 59)

    def agregar_horas(self, horas):
        self._horas = horas
    
    def agregar_minutos(self, minutos):
        self._minutos = minutos

    def agregar_segundos(self, segundos):
        self._segundos = segundos

    def visualizar(self):
        return f"{self._horas:02}:{self._minutos:02}:{self._segundos:02}"


alarma = Reloj()
alarmas = []


def _entradas():
    horas = int_input("Ingrese la hora: ", min=0, max=24)
    minutos = int_input("Ingrese los minutos: ", min=0, max=59)
    segundos = int_input("Ingrese los segundos: ", min=0, max=59)
    return horas, minutos, segundos


def _agregar(alarma, horas, minutos, segundos):
    alarma.agregar_horas(horas)
    alarma.agregar_minutos(minutos)
    alarma.agregar_segundos(segundos)


def ver_alarmas():
    if alarmas == []:
        print("No hay alarmas por el momento")
    for n, alarma in enumerate(alarmas, 1):
        print(f"{n}. {alarma.visualizar()}")


def nueva_alarma():
    alarma = Reloj()
    _agregar(alarma, *_entradas())
    alarmas.append(alarma)


def alarma_aleatorio():
    alarmas.append(Reloj())
    print("Alarma aleatoria agregada")


def editar_alarma():
    ver_alarmas()
    print("Seleccionar la alarma a ser editada")
    n = int(input(">>> "))
    alarma = alarmas[n-1]
    _agregar(alarma, *_entradas())


def quitar_alarma():
    ver_alarmas()
    print("Seleccionar la alarma a ser removida")
    n = int(input(">>> "))
    alarmas.pop(n-1)


if __name__ == "__main__":
    menu = Menu("Alarmas")
    menu.add_options(
        ("Ver alarmas activas", ver_alarmas),
        ("Agregar nueva alarma", nueva_alarma),
        ("Agregar alarma aleatoria", alarma_aleatorio),
        ("Editar alarma existente", editar_alarma),
        ("Quitar alarma", quitar_alarma),
    )
    menu.run()