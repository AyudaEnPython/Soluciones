"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Realizar el siguiente ejercicio usando funciones:

Calcular el costo total de los pasajes aéreos para un viajero en la
aerolínea VIENTOS AIR, para ello el viajero debe suminstrar los
siguientes datos para registrar su reserva:

- Clase en la que desea viajar
- Destino
- Tipo de viaje
- Número de pasajes a adquirir

Los costos de (1) un pasaje (en pesos) de acuerdo a la clase en la que
se viaja y a su destino son:

    +------------------+-----------+-----------+
    | Clase | Destinos |   Miami   |  Madrid   |
    +------------------+-----------+-----------+
    |     Primera      | 1 300 000 | 2 700 000 |
    |     Segunda      | 1 120 000 | 2 500 000 |
    |     Tercera      | 1 100 000 | 2 320 000 |
    +------------------+-----------+-----------+ # recuperado de la web

Se debe tener en cuenta que el tipo de viaje corresponde a la siguiente
tabla:

1. De negocios
2. Familiar
3. Turístico Individual

Cuando el viaje sea de negecios se realizará descuento 3% al pasaje,
cuando sea familiar el descuento será de 7% para cada pasaje
individual, cuando sea turístico el descuento será del 4.6%. Además,
dependiendo del número de pasajes a adquirir se realizará un descuento
adicional de acuerdo a la siguiente tabla:

    +----------+-----------+
    |   Rango  | Descuento |
    +----------+-----------+
    |    1 - 5 |    2.60%  |
    |   6 - 10 |    5.38%  |
    | 11 y más |    7.24%  |
    +----------+-----------+

# ---------------------------------------------------------------------
NOTE: El enunciado original no esta bien redactado, no incluye los
    datos sobre las clases, los costos de los pasajes ni los destinos.
    Se tuvo que recuperar esa información a través de una busqueda.
"""
from math import inf
from prototools import RangeDict, int_input, choice_input

TIPO = {"negocios": 0.03, "familiar": 0.07, "individual": 0.046}
ADICIONAL = RangeDict({(1, 5): 0.026, (6, 10): 0.0538, (11, inf): 0.0724})
CLASE = {
    "primera": {"Miami": 1_300_000, "Madrid": 2_700_000},
    "segunda": {"Miami": 1_120_000, "Madrid": 2_500_000},
    "tercera": {"Miami": 1_100_000, "Madrid": 2_320_000},
}

clase = choice_input(tuple(CLASE.keys()), lang="es")
destino = choice_input(("Miami", "Madrid"))
tipo = choice_input(tuple(TIPO.keys()), lang="es")
pasajes = int_input("Número de pasajes: ", min=1)

precio = CLASE[clase][destino]
precio *= (1 - TIPO[tipo])
precio *= (1 - ADICIONAL[pasajes])

print(f"El precio total es de {precio} pesos")
