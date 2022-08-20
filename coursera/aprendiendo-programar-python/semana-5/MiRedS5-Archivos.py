#Hola.
#Hasta ahora nuestra red social incluye estas características:

#El programa de la semana anterior permitía:
#1. Obtener datos del usuario
#2. Consultar y mostrar varios mensajes de estado del usuario
#3. Escoger entre distintas acciones que el usuario puede realizar
#4. Modificar el perfil del usuario
#
#Y además algunas de estas funcionalidades están encapsulados en un módulo, de manera
#que tu código principal es cada vez más corto y puedes concentrarte en la funcionalidad principal.

#Vamos por la siguiente evolución de nuestra red social.

#Habrás notado que cada vez que ejecutamos nuestro programa de red social, debemos ingresar
#todos los datos del usuario que está utilizando el programa, antes de poder alcanzar
#el menú de opciones. Esto es bastante engorroso.

#Sin embargo, ahora sabemos que podemos utilizar memoria secundaria de nuestro computador,
#esto es, espacio del disco, para guardar archivos. Vamos a usar esto para que nuestro
#programa pueda recordar los datos de los usuarios, y evitar tener que escribirlos en cada ocasión.

#Y la estrategia que usaremos es la siguiente.
#Cada vez que un usuario nuevo utilice nuestro programa, vamos a guardar un archivo con sus datos.
#El nombre de este archivo será el nombre del usuario, seguido de la extensión '.user'.
#En este archivo guardaremos una línea por cada variable importante de nuestro usuario.

#De esta manera, la próxima vez que ejecutemos nuestro programa, lo primero que haremos será preguntar
#el nombre del usuario, y ver si existe un archivo con ese nombre.
#Si existe, entonces lo leemos desde el disco, y evitamos tener que preguntar todos sus datos.
#Si no existe, entonces seguimos comportándonos como antes, lo tratamos como un usuario nuevo, y preguntamos
#sus datos para luego crear un archivo.


#Recordemos que en este módulo están todos las funciones adicionales que hemos creado.
import S5Red as Red
#El módulo 'os' nos permitirá consultar si un archivo existe.
import os

Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a Mi Red")

#Verificamos si el archivo existe
if os.path.isfile(nombre+".user"):
    #Esto lo hacemos si ya había un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    archivo_usuario = open(nombre+".user","r")
    nombre = archivo_usuario.readline()
    edad = int(archivo_usuario.readline())
    estatura = float(archivo_usuario.readline())
    estatura_m = int(estatura)
    estatura_cm = int( (estatura - estatura_m)*100 )
    sexo = archivo_usuario.readline()
    pais = archivo_usuario.readline()
    num_amigos = int(archivo_usuario.readline())
    estado = archivo_usuario.readline()
    #Una vez que hemos leido los datos del usuario no debemos olvidar cerrar el archivo
    archivo_usuario.close()

else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo hacíamos antes
    print()
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    num_amigos = Red.obtener_num_amigos()
    estado = ""

#En ambos casos, al llegar aquí ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)
Red.mostrar_mensaje(nombre, None, estado)

#Ahora podemos mostrar el menu y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.mostrar_mensaje(nombre, None, estado)
    elif opcion == 2:
        estado = Red.obtener_mensaje()
        for i in range(num_amigos):
            nombre_amigo = input("Ingresa el nombre de tu amigo o amiga: ")
            Red.mostrar_mensaje(nombre, nombre_amigo, estado)
    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)
    elif opcion == 4:
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        sexo = Red.obtener_sexo()
        pais = Red.obtener_pais()
        num_amigos = Red.obtener_num_amigos()
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos)
    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ",nombre+".user")
        archivo_usuario = open(nombre+".user","w")
        archivo_usuario.write(nombre+"\n")
        archivo_usuario.write(str(edad)+"\n")
        archivo_usuario.write(str(estatura_m + estatura_cm/100)+"\n")
        archivo_usuario.write(sexo+"\n")
        archivo_usuario.write(pais+"\n")
        archivo_usuario.write(str(num_amigos)+"\n")
        archivo_usuario.write(estado+"\n")
        #Una vez que hemos escrito todos los datos del usuario en el archivo, no debemos olvidar cerrarlo
        archivo_usuario.close()
        print("Archivo",nombre+".user","guardado")



print("Gracias por usar Mi Red. ¡Hasta pronto!")

#Cuando ejecutes este programa por primera vez, verás que se crea un archivo nuevo en tu computador
#cada vez que ingresas con el nombre de un usuario nuevo. Prueba a ingresar
#con un nombre de usuario que ya habías usado antes.

#Este programa es bastante más completo que los que teníamos antes, sin embargo aún tiene cosas
#por mejorar. Por ejemplo, ¿qué ocurre si el archivo está mal escrito, o si le falta alguna línea?
#¿Qué ocurre si en una ocasión ingreso mi nombre con mayúsculas, y en otra ocasión lo hago con minúsculas?
#
#Te invitamos a corregir dos detalles en este programa
#1. Al leer las líneas del archivo, siempre se leen como últimos caracteres, algunos caracteres blancos como
#   espacios y el caracter de cambio de línea ('\n'). Esto hace que los nombres de archivos creados incluyan
#   estos caracteres adicionales. Puedes utilizar los métodos de str para eliminar este tipo de caracteres
#   que llamamos "no imprimibles"
#2. Utiliza tu conocimiento de funciones para crear funciones que lean desde un archivo,
#   y retornen el conjunto de datos leídos, de manera de encapsular el proceso de lectura y escritura,
#   y reducir el tamaño de tu código.
