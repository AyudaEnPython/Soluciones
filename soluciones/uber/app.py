"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: it'll be refactored later...
"""
from random import randint

from main import uber_object, registrar_vehiculo


def main():
    vehiculo = registrar_vehiculo("AEP101", "Mazda", "2022")
    uber = uber_object(vehiculo, "premium")
    uber.set_calificacion(randint(3, 10))
    for _ in range(randint(6, 10)):
        uber.viaje(randint(1, 20))
    uber.mostrar()
    uber.set_calificacion(randint(1, 3))
    uber.reset()
    for _ in range(randint(1, 4)):
        uber.viaje(randint(1, 20))
    uber.mostrar()
    uber.enviar_reparacion()
    uber.viaje(3)
    uber.mostrar()
    uber.recibir_reparacion()
    uber.viaje(2)
    uber.mostrar()


if __name__ == "__main__":
    main()
