"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Se desea simular el comportamiento de una para de autobús a la que
pueden llegar 5 autobuses diferentes (numerados del 1 al 5). Cuando
llegue un autobús con n plazas libres, las personas que estén esperando
subirán por orden de llegada a la parada hasta completar las plazas
vacias o no haber esperado más personas dicho autobús. Con las
siguientes opciones de menú:

- LLegar Persona Parada: Se pedirá por teclado el nombre de la persona
    y el número del autobús que está esperando. Si la cola de personas
    que espera ese autobús está llena, se informará del suceso, en caso
    contrario se colocará a la persona en la cola correspondiente.

- Llegar Bus Parada: Se pedirá por teclado el número del autobús y el 
    número de plazas libres que tiene el autobús. Se quitarán de la
    cola (mostrando su nombre por pantalla) tantas personas como plazas
    libres haya o hasta que la cola esté vacía.

- Buscar Personas Parada: Se pide el nombre de una persona y se muestra
    el número de autobús que está esperando. Si no está en ninguna de
    las colas, se informará del suceso.

- Pintar Parada: Muestra por orden todas las personas que están en cada
    una de las colas.

- Salvar Parada Fichero: Se pedirá el nombre de un fichero y se
    almacenará toda la información en un fichero de texto con el
    siguiente formato:
    
    <numero de bus><persona1><ESPACIO><persona2>...<personaN><PUNTO>

- Cargar Parada Fichero: Se pedirá el nombre de un fichero y se cargará
    toda la información de un fichero de texto con el mismo formato de
    grabación. La información se añadirá a la ya existente, es decir,
    que la parada puede o no estar vacía.

- Salir del programa: Se pedirá confirmación de salida.

PARADA DE AUTOBUSES
===================

A. Llegar Persona Parada
B. Llegar Bus Parada
C. Buscar Personas Parada
D. Pintar Parada
E. Salvar Parada Fichero
F. Cargar Parada Fichero
X. Salir del programa
Introduzca una opción:

Despues de cada opción se hará una pausa y se limpiará la pantalla
antes de volver al menú principal.

Aspectos a implementar:
- Define el tipo TCadena como un array de caracteres.
- CopiaCadena: copia la cadena que se pasa como argumento en otra
    cadena.
- IgualCadena: nos dice si dos cadenas que se pasan como argumentos
    son iguales.
- CrearCola: crea una cola nueva.
- DestruirCola: destruye la cola que se la pasa como parámetro.
- MeterCola: mete un elemento en la cola que se la pasa como parámetro.
- SacarCola: saca un elemento de la cola.
- ColaLLena: nos dice si una cola está llena.
- ColaVacia: nos dice si una cola está vacía.

NOTE: Se opta por un rediseño, opuesto a lo que se indica en el
ejercicio para aumentar la legibilidad del código.

still needs some work
"""
from prototools.menu import EzMenu

MAXIMA_CAPACIDAD = 20
CANTIDAD_DE_AUTOBUSES = 5
autobuses = [[], [], [], [], []]
pasajeros = [[], [], [], [], []]


def hacer_cola():
    pasajero = input("Nombre del pasajero: ")
    autobus = int(input("Autobus: "))
    if len(pasajeros[autobus - 1]) < MAXIMA_CAPACIDAD:
        pasajeros[autobus - 1].append(pasajero)
    else:
        print("La cola está llena.")


def llegada_de_autobus():
    autobus = int(input("Autobus: "))
    asientos = int(input("Asientos libres: "))
    for i in range(asientos):
        if len(pasajeros[autobus - 1]) > 0:
            autobuses[autobus - 1].append(pasajeros[autobus - 1].pop(0))
        else:
            print("La cola está vacía.")


def buscar_pasajero():
    pasajero = input("Nombre del pasajero: ")
    for i in range(len(pasajeros)):
        if pasajero in pasajeros[i]:
            print("El pasajero está esperando el autobús", i + 1)
            break
    else:
        print("El pasajero no está en ningún cola.")


def mostrar_colas():
    for i in range(len(pasajeros)):
        print("Autobús", i + 1, ":", pasajeros[i])


def mostrar_autobuses():
    for i in range(len(autobuses)):
        print("Autobús", i + 1, ":", autobuses[i])


def guardar_informacion():
    with open("info.txt", "w") as f:
        for i in range(len(pasajeros)):
            f.write(str(i + 1))
            for pasajero in pasajeros[i]:
                f.write(" " + pasajero)
            f.write(".\n")


def cargar_informacion():
    with open("info.txt", "r") as f:
        for linea in f:
            for pasajero in linea.split():
                autobus = int(pasajero[0])
                pasajeros[autobus - 1].append(pasajero[1:])


if __name__ == '__main__':
    menu = EzMenu()
    menu.agregar_opciones(
        'Ingresar a la cola',
        'Llegada de Autobus',
        'Buscar pasajero',
        'Mostrar colas',
        'Mostrar autobuses',
        'Guardar informacion',
        'Cargar informacion',
        'Salir del programa',
    )
    menu.agregar_funciones(
        hacer_cola,
        llegada_de_autobus,
        buscar_pasajero,
        mostrar_colas,
        mostrar_autobuses,
        guardar_informacion,
        cargar_informacion,
    )
    menu.run()