"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Beto desea pagar por servicio de internet, para lo cual él tiene que
elegir primero de las cuatro operadoras disponibles las cuales son:
1. Claro
2. Movistar
3. Entel
4. Bitel

Si Beto ya tuviera decidido la operadora que le dará el servicio, él
tiene que ver qué tipo de servicio desea de la operadora.
A continuación, se muestra los servicios que ofrecen las operadoras,
además del costo por cada tipo.

    +-----------+-----------------------------------------+
    | Operadora |        Tipo de Servicio y Costo         |
    +-----------+-------------+------------+--------------+
    |   Claro   | móvil = 100 | casa = 110 |  megas =  90 |
    |  Movistar | móvil = 140 | casa = 120 |  megas = 100 | 
    |   Entel   | móvil = 130 | casa = 60  |  megas =  30 | 
    |   Bitel   | móvil = 120 | casa = 80  |  megas =  50 | 
    +-----------+-------------+------------+--------------+

Beto deberá elegir primero un ítem que indicará la operadora y después
ingresar el tipo de servicio, así él sabrá cuanto pagar. Para la
implementación defina una función llamada pagoServicio que debe retornar
el pago por el servicio.

Ejemplo de ejecución 1:
Ingrese la operadora: Claro
Ingrese el servicio: casa
El pago por el servicio es: 110

Ejemplo de ejecución 2:
Ingrese la operadora: Entel
Ingrese el servicio: megas
El pago por el servicio es: 30
"""
# pip install prototools
from prototools import menu_input

SERVICIOS = {
    "claro": {"movil": 100, "casa": 110, "megas": 90},
    "movistar": {"movil": 140, "casa": 120, "megas": 100},
    "entel": {"movil": 130, "casa": 60, "megas": 30},
    "bitel": {"movil": 120, "casa": 80, "megas": 50},
}


def pago_servicio(operadora, servicio):
    return SERVICIOS[operadora][servicio]


def main():
    operadora = menu_input(tuple(SERVICIOS.keys()), numbers=True, lang="es")
    servicio = menu_input(tuple(SERVICIOS[operadora].keys()), lang="es")
    print(f"El pago por el servicio es: {pago_servicio(operadora, servicio)}")


if __name__ == "__main__":
    main()
