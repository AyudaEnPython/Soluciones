"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import sys

#Validar si es el principal
if __name__ == "__main__":
    #variable
    tamao = len(sys.argv)
    #ciclo que va estar sacando cada uno de los argumentos(elementos) que hayan ingresado
    for argumento in sys.argv:
        #validar cada uno de los argumentos
        if argumento == "-h" or argumento == "--help" or argumento== "":
            #Mostar el Menu
            print("Bienvenido al Programa x\
\n-h or --help: Ayuda\
\n-s or --suma: Sumar n Cantidad de Numeros\
\n-r or --resta: Restar n Cantidad de Numeros\
\n-m or --mult: Multiplicar n Cantidad de Numeros\
\n-d or --div: Dividir n Cantidad de Numeros")
        #Validar las opciones
        if argumento == "-s" or argumento == "--suma":
            i = 2 #Inicializar posicion donde se encuentra el argumento para comenzar operacion
            #Validar Tamaño del argumento
            if tamao > 3:
                resultado = 0
                #brincar de argumento en argumento
                while i < tamao:
                    #operacion suma
                    resultado = resultado + int( sys.argv[i] )
                    i+=1
                print(f"Resultado = {resultado}")
            else:
                print("Faltan argumentos!")

        if argumento == "-r" or argumento == "--resta":
            i = 2
            if tamao > 3:
                resultado = 0
                while i < tamao:
                    #operacion restar
                    if i == 2:
                        resultado = int( sys.argv[i] )
                    else:
                        resultado = resultado - int( sys.argv[i] )
                    i+=1
                print(f"Resultado = {resultado}")
            else:
                print("Faltan argumentos!")

        if argumento == "-m" or argumento == "--mult":
            i = 2
            if tamao > 3:
                resultado = 1
                while i < tamao:
                    #operacion multiplicar
                    resultado = resultado * int( sys.argv[i] )
                    i+=1
                print(f"Resultado = {resultado}")
            else:
                print("Faltan argumentos!")

        if argumento == "-d" or argumento == "--div":
            i = 2
            if tamao > 3:
                resultado = 0
                while i < tamao:
                    if i > 2 and int( sys.argv[i]) == 0:
                        print("Error: División x Cero")
                        resultado = None
                        break
                    #operacion division
                    elif i == 2:
                        resultado = int( sys.argv[i] )
                    else:
                        resultado = resultado / int( sys.argv[i] )
                    i+=1
                print(f"Resultado = {resultado}")
            else:
                print("Faltan argumentos!")