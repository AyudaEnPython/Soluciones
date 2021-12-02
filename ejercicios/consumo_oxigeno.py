"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Consumo de oxígeno de buceadores.

Se debe diseñar un programa que calcule la tasa de consumo de aire
cuando buceas.

El programa debe desplegar un menú en donde se pueda seleccionar que se
quiere calcular:
    1. La ley de Boyle
    2. Calcular el SCA
    3. Calcular el aire consumido

1. Ley de Boyle

De acuerdo a la ley de Boyle, a medida que desciendes, el aire que
se respira esta más comprimido y hay un mayor consumo.
Características y ejemplo:
En la superficie la presión es igual a una atmósfera
Al descender 10 metros la presión aumenta y corresponde a 2 atmósferas
Al descender 20 metros la presión aumenta y corresponde a 3 atmósferas

Si un buzo respira 25 litros por minuto en superficie entonces respirará
50 lts/min a 10 mts de profundidad y 75 lts/min a 20 mts de profundidad.

Condiciones:
Realizar una función que calcule la ley de Boyle para cualquier valor
decimal mayor que 0 que se introduzca.

2.Calcular el SAC (consumo de aire en superficie)

Características y ejemplo:

Datos de entrada:
Capacidad de aire en el tanque, profundidad de buceo,
tiempo de inmersión y bares utilizados.
Para cualquier valor decimal mayor que 0 que se introduzca.

Datos de salida:
SAC

Ejemplo:
Si un buzo usa un tanque de 10.3 lts, bucea a 20 m por 20 min y usa 120
bares, tendrá los siguientes resultados:
    a. Cálculo de litros usados:
        120 bares consumidos x 10.3 lts = 1236 litros usados en el
        buceo
    b. Cálculo de litros promedio usados por minuto:
        1236/20 min (duración del buceo) = 61.8 lts por minuto
    c. Compensación por profundidad:
        Dividir el promedio de litros usados por minuto por el factor
        de profundidad, que corresponde al resultado de la ley de Boyle
        (sugerencia: utilice el punto anterior para calcularla)
        (20 mts = 3 (atmósferas)) 61.8 lts/min / 3 = 20.6 lts/min
        Para este perfil de buceo el resultado del SCA seria de 20.6
        lts/min
Calcular el SAC para cualquier valor decimal mayor que 0 que se
introduzca y para un tiempo de inmersión menor a 180 minutos.

3. Usar el SAC para el calculo de litros en una inmersión:

Datos de entrada:
Capacidad del tanque (litro), carga del tanque(bar), profundidad de
buceo (metros), tiempo de buceo (minutos), aire de reserva del tanque
(bar), SAC (lts/min)

Datos de salida:
Consumo en litros del tanque, en caso de que el consumo sea mayor a la
capacidad el programa tiene que dar los resultados y la alerta de que
no es posible hacer el buceo con esas condiciones.

Ejemplo:
Un buzo con un tanque de 10 litros sin reserva, cargado a 210 bar
quiere hacer un buceo a 30 metros por 25 minutos y tiene un SAC de 20
lts/min.

1. Primero calculamos cuanto aire hay disponible:
Un tanque de 10.3 litros a 210 bar, daria 2163 lts.

2. A 30 mts (4 atmosferas según la ley de Boyle), el consumo de aire
sería 4 bar x 20 SAC = 80 lts/min

3. Para hace un buceo de 25 minutos, necesitamos:
25 min x 80 (SAC, lts/min) = 2000 lts

Como el tanque tiene un capacidad de 2163 lts y consume 2000 lts si es
posible hacer el buceo con estas condiciones.

http://tagangadives.blogspot.com/2011/03/sabes-cual-es-tu-tasa-de-consumo-de.html

TODO: needs to be change to last version of prototools.
"""
from prototools import Menu, float_input, textbox


def atmosferas():
    profundidad = float_input("Ingresar profundidad: ", min=0)
    textbox((profundidad/10) + 1, 40)


def sca():
    capacidad = float_input("Ingresar capacidad: ", min=0)
    profundidad = float_input("Ingresar profundidad: ", min=0)
    tiempo = float_input("Ingresar tiempo: ", min=0)
    bar = float_input("Ingresar bar: ", min=0)
    textbox(round((bar * capacidad )/tiempo / ((profundidad/10) + 1), 1), 40)


def consumo():
    capacidad = float_input("Ingresar capacidad: ", min=0)
    bar = float_input("Ingresar bar: ", min=0)
    reserva = float_input("Ingresar reserva: ", min=0)
    profundidad = float_input("Ingresar profundidad: ", min=0)
    tiempo = float_input("Ingresar tiempo: ", min=0, max=180)
    sca = float_input("Ingresar sca: ", min=0)
    
    disponible = capacidad * (bar - reserva)
    requerido = (((profundidad/10) + 1) * sca) * tiempo
    textbox(f"Disponible: {disponible}\nRequerido: {requerido}", 40)


if __name__ == "__main__":
    menu = Menu()
    menu.add_options(
        ("Ley de Boyle", atmosferas),
        ("Calcular el SCA", sca),
        ("Calcular el aire consumido", consumo),
    )
    menu.run()