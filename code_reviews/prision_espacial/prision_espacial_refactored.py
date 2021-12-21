"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
# pip install prototools
from prototools import int_input, text_align, banner
from prototools.colorize import cyan, red, green, yellow, magenta


@banner("", width=80)
def opcion(opcion_1, opcion_2):
    print(magenta("¿Que opcion eliges?"))
    print(yellow(f"1.- {opcion_1}\n2.- {opcion_2}"))
    return int_input(red("> "), min=1, max=2, lang="es")


N = randint(0, 13)
INTRO = """
Te acabas de escapar de la prision espacial junto a tu companero de celda,
lograron burlar a los guardias, y ahora se dirigen hacia el exterior. Mientras
buscan la salida se introducen en un cuartel controlado por monstruos
alienigenas. Uno de estos, ataca a tu companero y se lo lleva de vuelta a su
celda. Tu logras pasar desaperecibido escondido entre las sombras. Luego de
cruzar este cuarto hay un pasillo. Al final de este hay 2 caminos por los que
puedes seguir: Una puerta semi-abierta, o una escotilla en el suelo en la cual
puedes saltar. 
"""
PARRAFOS = (
    """
    Te has encontrado con un guardia que tiene un gorro vikingo. Puedes
    hacer 2 cosas: Hacerte el dormido, o salir corriendo.
    """,
    """
    Has caido a una zona inundada, el agua te llega hasta las rodillas.
    Durante 30 minutos avanzas y llegas a una zona abierta, seca y con luz. En
    este lugar hay un palo, lo tomaras o lo dejaras ahi?
    """,
    """
    Te has hecho el dormido. Lamentablemente estos guardias no dejan este
    cuarto sin vigilar por lo tanto no podras moverte mas de ahi.
    Has muerto de Hambre.
    """,
    """
    Sigues avanzazndo y te encuentras con una rata de dos metros, y esta te
    pregunta lo siguiente:
    """,
    """
    Has {} el palo, sigamos adelante.    
    """
)

text_align(magenta("ESCAPATORIA DE LA PRISION ESPACIAL"), align="center")
print(cyan(INTRO))
eleccion = opcion("Puerta semi-abierta", "Escotilla en el suelo")
if eleccion == 1:
    print(cyan(PARRAFOS[0]))
    eleccion = opcion("Hacerse el dormido", "Salir corriendo")
    if eleccion == 1:
        print(cyan(PARRAFOS[2]))
        text_align(red("FIN DEL JUEGO"))
    else:
        print('mas codigo')
else:
    print(cyan(PARRAFOS[1]))
    eleccion = opcion("Tomarlo", "Dejarlo")
    accion = "tomado" if eleccion == 1 else "dejado"
    print(cyan(PARRAFOS[4].format(accion)))
    print(cyan(PARRAFOS[3]))
    print(magenta(f"¿Cuanto es 13 x {N}?"))
    resultado = int_input(red("> "))
    print(green('Correcto') if resultado == 13 * N else red('Incorrecto'))