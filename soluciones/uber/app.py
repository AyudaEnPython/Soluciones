"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from main import uber_object, registrar_vehiculo


def main():
    vehiculo = registrar_vehiculo("ABC123", "Toyota", "2020")
    uber = uber_object(vehiculo, "premium")
    uber.set_calificacion(5)
    uber.viaje(2)
    uber.viaje(4)
    uber.viaje(1)
    uber.mostrar()
    uber.set_calificacion(1)
    uber.reset()
    uber.viaje(2)
    uber.mostrar()
    uber.enviar_reparacion()
    uber.viaje(3)
    uber.mostrar()
    uber.recibir_reparacion()
    uber.viaje(2)
    uber.mostrar()


if __name__ == "__main__":
    main()
