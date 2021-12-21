"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from random import randint
respuesta=1
print('ESCAPATORIA DE LA PRISION ESPACIAL')

print('''\nTe acabas de escapar de la prision espacial junto a tu companero de celda, lograron burlar a los guardias, 
y ahora se dirigen hacia el exterior. Mientras buscan la salida se introducen en un cuartel controlado por monstruos 
alienigenas. Uno de estos, ataca a tu companero y se lo lleva de vuelta a su celda. Tu logras pasar desaperecibido 
escondido entre las sombras. Luego de cruzar este cuarto hay un pasillo. Al final de este hay 2 caminos por los que 
puedes seguir: Una puerta semi-abierta, o una escotilla en el suelo en la cual puedes saltar. \n¿Que opcion eliges?''')

respuesta=int(input('1.-Puerta semi-abierta \n2.-Escotilla en el suelo \n--> '))
while respuesta != 1 and respuesta != 2:
    print('Has ingresado mal la respuesta, vuelve a intentarlo')
    respuesta=int(input('1.-Puerta semi-abierta \n2.-Escotilla en el suelo \n--> '))

if respuesta == 1:
    print('''\nTe has encontrado con un guardia que tiene un gorro vikingo. Puedes hacer 2 cosas: Hacerte el dormido, 
    o salir corriendo. \n¿Que opcion eliges?''')       
    respuesta=int(input("1.-Hacerse el dormido \n2.-Salir Corriendo \n--> ")) 
    
    while respuesta != 1 and respuesta != 2:
        print('Has ingresado mal la respuesta, vuelve a intentarlo')
        respuesta=int(input('1.-Hacerse el dormido\n2.-Salir Corriendo \n--> '))

    if respuesta==1:
        print('''\nTe has hecho el dormido. Lamentablemente estos guardias no dejan este cuarto sin vigilar por lo tanto 
        no podras moverte mas de ahi. Has muerto de Hambre. \nFIN DEL JUEGO''') 
    
    elif respuesta==2:
        print('mas codigo')

elif respuesta ==2:
    print('''Has caido a una zona inundada, el agua te llega hasta las rodillas. Durante 30 minutos avanzas y llegas a 
            una zona abierta, seca y con luz. En este lugar hay un palo, lo tomaras o lo dejaras ahi?''')
    respuesta=int(input('1.-Tomarlo\n2.-Dejarlo \n-->'))
    while respuesta != 1 and respuesta != 2:
        print('Has ingresado mal la respuesta, vuelve a intentarlo')
        respuesta=int(input('1.-Hacerse el dormido\n2.-Salir Corriendo \n-->'))
    
    if respuesta==1:
        palo=True
        print('Has tomado el palo, sigamos adelante')
    else:
        palo=False
        print('Has dejado el palo, sigamos adelante')
    
    numero=randint(0,13)
    
    print(f'Sigues avanzazndo y te encuentras con una rata de dos metros, y esta te pregunta lo siguiente:')
    
    resultado=int(input("¿Cuanto es 13 x {numero} \n--> "))

    if 13*numero == resultado:
        print('Correcto')
    else:
        print('incorrecto')