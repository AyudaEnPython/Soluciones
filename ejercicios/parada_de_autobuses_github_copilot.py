"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

#================== Resuelto por Github Copilot AI ===================#
#                                                                     #
# NOTE: Si bien es cierto que el autocompletado de Github Copilot es  #
# muy bueno (aquí nuevamente sugirió el "muy bueno"), no se ha        #
# probado la solución de Copilot. Tambien recalcar que el código      #
# producido esta lejos de perfecto y puede mejorarse mas.             #
#                                                                     #
#======================================================================

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

NOTE: needs to be tested.
"""


def llegar_persona_parada(cola_personas, cola_autobuses):
    """
    Función que llega una persona a una parada.
    """
    persona = input("Nombre de la persona: ")
    autobus = int(input("Número de autobús: "))
    if cola_personas[autobus-1] == []:
        cola_personas[autobus-1] = [persona]
    else:
        cola_personas[autobus-1].append(persona)


def llegar_bus_parada(cola_personas, cola_autobuses):
    """
    Función que llega un autobús a una parada.
    """
    autobus = int(input("Número de autobús: "))
    plazas = int(input("Número de plazas libres: "))
    if plazas > len(cola_personas[autobus-1]):
        plazas = len(cola_personas[autobus-1])
    for i in range(plazas):
        print(cola_personas[autobus-1].pop(0))


def buscar_personas_parada(cola_personas, cola_autobuses):
    """
    Función que busca una persona en una parada.
    """
    persona = input("Nombre de la persona: ")
    for i in range(len(cola_personas)):
        if persona in cola_personas[i]:
            print("Autobús:", i+1)
            break
    else:
        print("No está en ninguna de las colas")


def pintar_parada(cola_personas, cola_autobuses):
    """
    Función que pinta por pantalla las personas de una parada.
    """
    for i in range(len(cola_personas)):
        print("Autobús", i+1, ":", cola_personas[i])


def salvar_parada_fichero(cola_personas, cola_autobuses):
    """
    Función que salva la parada en un fichero.
    """
    fichero = input("Nombre del fichero: ")
    with open(fichero, "w") as f:
        for i in range(len(cola_personas)):
            for j in range(len(cola_personas[i])):
                f.write(str(i+1)+" "+cola_personas[i][j]+"\n")
            f.write("\n")


def cargar_parada_fichero(cola_personas, cola_autobuses):
    """
    Función que carga la parada de un fichero.
    """
    fichero = input("Nombre del fichero: ")
    with open(fichero, "r") as f:
        for linea in f:
            if linea != "\n":
                autobus = int(linea.split()[0])
                persona = linea.split()[1]
                cola_personas[autobus-1].append(persona)


def salir_programa():
    """
    Función que sale del programa.
    """
    print("Saliendo del programa...")


def menu(cola_personas, cola_autobuses):
    """
    Función que muestra el menú.
    """
    print("""
    1. LLegar Persona Parada
    2. Llegar Bus Parada
    3. Buscar Personas Parada
    4. Pintar Parada
    5. Salvar Parada Fichero
    6. Cargar Parada Fichero
    7. Salir del programa
    """)


def main():
    """
    Función principal del programa.
    """
    cola_personas = [[], [], [], []]
    cola_autobuses = [[], [], [], []]
    while True:
        menu(cola_personas, cola_autobuses)
        opcion = int(input("Opción: "))
        if opcion == 1:
            llegar_persona_parada(cola_personas, cola_autobuses)
        elif opcion == 2:
            llegar_bus_parada(cola_personas, cola_autobuses)
        elif opcion == 3:
            buscar_personas_parada(cola_personas, cola_autobuses)
        elif opcion == 4:
            pintar_parada(cola_personas, cola_autobuses)
        elif opcion == 5:
            salvar_parada_fichero(cola_personas, cola_autobuses)
        elif opcion == 6:
            cargar_parada_fichero(cola_personas, cola_autobuses)
        elif opcion == 7:
            salir_programa()
            break
        else:
            print("Opción incorrecta")


if __name__ == "__main__":
    main()
