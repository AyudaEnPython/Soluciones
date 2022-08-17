#Hola, ahora que ya sabemos construir una interacción básica con nuestro programa
#de red social, vamos a agregar nuevas funcionalidades.
#
#Vamos a partir con el mismo programa de la etapa anterior, que permite dos cosas:
#1. Obtener datos del usuario
#2. Consultar y mostrar UN mensaje de estado del usuario
#
#Una característica de los programas con múltiples funcionalidades es que ofrecen un menú de acciones
#al usuario. Los menú de opciones permiten que el usuario escoja que acción realizar y podemos
#implementarlos usando un ciclo while que funcionen mientras el usuario no escoja una acción de salida.
#Cada vez que el usuario escoja una acción podemos usar una serie de 'if/elif/else' para ejecutar
#distintas secciones de código de acuerdo a lo que el usuario ha solicitado.

#Para empezar vamos a permitir que el usuario publique todos los mensajes que considere desee hasta
#que decida salir voluntariamente del programa.

############################################################
# Bienvenida

print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

# Solicitud de nombre
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

# Cálculo de edad
agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
edad = 2017-agno-1
print()

# Cálculo de estatura
estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

# Cantidad de amigos
num_amigos = int(input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centímetros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

#Usaremos una variable bool para indicar si el usuario desea continuar
#utilizando el programa o no
continuar = True

#Este ciclo se mantiene en ejecución hasta que el usuario desee salir
while continuar:

    #Solicitamos opción al usuario
    escribir_mensaje = str(input("¿Deseas escribir un mensaje? (S/N) "))

    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
        mensaje = input("Vamos a publicar un mensaje. ¿Qué piensas hoy? ")
        print()
        print("--------------------------------------------------")
        print(nombre, "dice:", mensaje)
        print("--------------------------------------------------")
    #En caso que sea otra respuesta, vamos a decidir salir.
    #Así, en la siguiente iteración el ciclo terminará
    else:
        continuar = False

#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Mi Red. ¡Hasta pronto!")

#Ahora puedes escribir mensajes todas las veces que quieras.
#Observa que hemos utilizado un ciclo while que permite repetir la acción de preguntar por un mensajes
#hasta que el usuario escribe algo distino de "S".

#Pero las redes sociales pueden ejecutar más acciones que solamente enviar mensajes.

#Te proponemos los siguientes desafíos:
#1. Este programa termina cada vez que el valor de 'escribir_mensaje' es distinto a "S" o a "s".
#   Modifique el programa para que el programa termine UNICAMENTE cuando se ingresa "N" o "n".
#   En caso que se ingrese algo distinto, debe volver a solicitar una opción al usuario.
#
#2. Modifica este menú para que le permita el usuario realizar más de una acción.
#   Por ejemplo, puedes agregar una acción que permita al usuario modificar su nombre.