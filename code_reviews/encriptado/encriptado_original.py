"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
with open('code_reviews/encriptado/mensaje.txt') as arc:
    cadena = arc.readline()
    print ("Mensaje Cifrado: \n",cadena, "\n")
    largo=len(cadena)
    inicio=0
    cadena_final=""
    caracter=""
    while inicio < largo:
        if cadena[inicio] in "1":
            caracter="a"
        elif cadena[inicio] in "2":
            caracter="e"
        elif cadena[inicio] in "3":
            caracter="i"
        elif cadena[inicio] in "4":
            caracter="o"
        elif cadena[inicio] in "5":
            caracter="u"
        else:
            caracter=cadena[inicio]
        cadena_final+= caracter
        inicio+=1

def encontrar_palabra_larga(cadena_final):
    longitud = max(cadena_final.split(), key=len)
    print ("\nLa palabra con mayor numero de caracteres es: " ,longitud)
    print ("Numero de caracteres: ",len(longitud) )
    print ("Mensaje Descifrado: \n",cadena_final)

encontrar_palabra_larga(cadena_final)