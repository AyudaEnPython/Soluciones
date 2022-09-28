"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Problema Planteado

Un banco les ha encargado que generen un simulador de cuotas y
cronogramas de pago de préstamos personales para los clientes. Para
ello se han establecido las siguientes condiciones:

- El programa termina cuando el cliente no quiere hacer más
    soluciones.
- La primera vez el cliente debe ingresar sus apellidos, nombres y DNI
- Luego iniciará la simulación y el programa solicitará:
    - Monto del préstamo, el cual debe estar entre 5000 y 3000 soles
    - Los días de pago, que pueden ser los 15 o 25 de cada mes, a
        partir del mes siguiente al desembolso
    - La fecha de desembolsos se asumirá como la fecha del día
- La relación entre los montos, cuotas y tasas se muestra en el
siguiente cuadro:

    +--------------------+--------+--------------------+
    | Monto del préstamo | Cuotas | Tasa Efectiva Anual|
    +--------------------+--------+--------------------+
    |   [5000 - 10000]   |   12   |        26%         |
    |  ]10000 - 15000]   |   18   |        24%         |
    |  ]15000 - 20000]   |   24   |        22%         |
    |  ]20000 - 25000]   |   30   |        20%         |
    |  ]25000 - 30000]   |   36   |        18%         |
    +--------------------+--------+--------------------+

Generación del cronograma de pagos

El factor se calcula de la siguiente manera:

    +----------+---------+
    | Tasa     |     18% |
    +----------+---------+
    | Cuotas   |      12 |
    +----------+---------+
    | Préstamo |10,000.00|
    +----------+---------+
    | Cuota    |  909.84 |
    +----------+---------+

La columna d1 se calcula de la siguiente manera:

- Para la primera cuota es la diferencia de días entre la fecha de
    vencimiento de la primera cuota y la fecha de desembolso.
- A partir de la segunda es la diferencia entre fechas de vencimiento

Por ejemplo, para la segunda cuota es la:
    fecha_vto_cuota2 - fecha_vto_cuota1

El cáculo para las siguientes cuotas es de la misma forma. Los
intereses de la cuota se calculan como:
capital * factor_cuota
El capital en la primera cuota es el monto del préstamo:
amortizacion = cuota - intereses de la cuota
Desde la segunda cuota:
capital = capital de cuota anterior - amortizacion de cuota anterior

NOTE: If there's a bug, please report it asap.
"""
from models import Cliente, Cuota, Cronograma
from utils import convertir_fecha, show
# pip install prototools
from prototools import float_input, choice_input, date_input, main_loop


def _registrar_cliente():
    cliente = Cliente(
        apellidos=input("Ingresar apellidos: "),
        nombres=input("Ingresar nombres: "),
        dni=input("Ingresar DNI: "),
    )
    return cliente


def _registrar_cuota():
    cuota = Cuota(
        monto_prestamo=float_input("Préstamo: ", min=5_000, max=30_000),
        dias_pago=choice_input(("15", "25"), prompt="Días de pago: "),
        fecha=convertir_fecha(date_input("de desembolso")),
    )
    return cuota


def procesar():
    cliente = _registrar_cliente()
    cuota = _registrar_cuota()
    cronograma = Cronograma(cliente, cuota)
    show(cronograma.data)


if __name__ == "__main__":
    main_loop(procesar)
