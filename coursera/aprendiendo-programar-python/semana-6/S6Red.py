#El módulo 'os' nos permitirá consultar si un archivo existe.
import os

def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
                  _                  __
       ____ ___  (_)  ________  ____/ /
      / __ `__ \/ /  / ___/ _ \/ __  /
     / / / / / / /  / /  /  __/ /_/ /
    /_/ /_/ /_/_/  /_/   \___/\__,_/

    """)

def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas. ")
    return nombre

def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en qué año naciste. "))
    return 2017-agno-1

def obtener_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
    metros = int(estatura)
    centimetros = int( (estatura - metros)*100 )
    return (metros, centimetros)

def obtener_sexo():
    sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    while sexo != 'M' and sexo != 'F':
        sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    return sexo

def obtener_pais():
    pais = input("Indica tu país de nacimiento: ")
    return pais

def obtener_lista_amigos():
    linea = input("Muy bien. Finalmente, escribe una lista con los nombres de tus amigos, separados por una ',': ")
    amigos = linea.split(",")
    return amigos


def mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos):
    print("--------------------------------------------------")
    print("Nombre:   ", nombre)
    print("Edad:     ", edad, "años")
    print("Estatura: ", estatura_m, "m y ", estatura_cm, "centímetros")
    print("Sexo:     ", sexo)
    print("País:     ", pais)
    print("Amigos:   ", len(amigos))
    print("--------------------------------------------------")

def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje")
    print("  2. Mostrar mi muro")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: "))
    while opcion < 0 or opcion > 5:
        print("No conozco la opción que has ingresado. Inténtalo otra vez.")
        opcion = int(input("Ingresa una opción: "))
    return opcion

def obtener_mensaje():
    mensaje = input("Ahora vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    return mensaje

def mostrar_mensaje(origen, mensaje):
    print("--------------------------------------------------")
    print(origen+":", mensaje)
    print("--------------------------------------------------")


#Muestra los mensajes recibidos
def mostrar_muro(muro):
     print("------ MURO ("+str(len(muro))+" mensajes) ---------")
     for mensaje in muro:
         print(mensaje)
     print("--------------------------------------------------")

#Publica un mensaje en el timeline personal y en el de los amigos
def publicar_mensaje(origen, amigos, mensaje, muro):
    print("--------------------------------------------------")
    print(origen, "dice:", mensaje)
    print("--------------------------------------------------")
    #Agrega el mensaje al final del timeline local
    muro.append(mensaje)
    #Agrega, al final del archivo de cada amigo, el mensaje publicado
    for amigo in amigos:
        if existe_archivo(amigo+".user"):
            archivo = open(amigo+".user","a")
            archivo.write(origen+":"+mensaje+"\n")
            archivo.close()

def existe_archivo(ruta):
    return os.path.isfile(ruta)

def leer_usuario(nombre):
    archivo_usuario = open(nombre+".user","r")
    nombre = archivo_usuario.readline().rstrip()
    edad = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    sexo = archivo_usuario.readline().rstrip()
    pais = archivo_usuario.readline().rstrip()
    amigos = archivo_usuario.readline().rstrip().split(",")
    estado = archivo_usuario.readline().rstrip()
    #Lee el 'muro'. Esto es, todos los mensajes que han sido publicados en el timeline del usuario.
    muro = []
    mensaje = archivo_usuario.readline().rstrip()
    while mensaje != "":
        muro.append(mensaje)
        mensaje = archivo_usuario.readline().rstrip()
    #Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()
    return(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro)

def escribir_usuario(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro):
    archivo_usuario = open(nombre+".user","w")
    archivo_usuario.write(nombre+"\n")
    archivo_usuario.write(str(edad)+"\n")
    archivo_usuario.write(str(estatura_m + estatura_cm/100)+"\n")
    archivo_usuario.write(sexo+"\n")
    archivo_usuario.write(pais+"\n")
    archivo_usuario.write(",".join(amigos)+"\n")
    archivo_usuario.write(estado+"\n")
    #Escribe el 'timeline' en el archivo, a continuación del último estado
    for mensaje in muro:
        archivo_usuario.write(mensaje+"\n")
    #Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
    archivo_usuario.close()
