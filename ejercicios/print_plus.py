"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

a) Programar una función llamada print_plus que tome de parámetro un
    String e imprima dicho String, más un espacio, más la cantidad
    de caracteres "#" consecutivos necesarios para completar un
    s de largo 50.
b) Para la función del inciso a): Si el String pasado por parámetro
    está vacio ("") entonces imprimir 50 caracteres "#" consecutivos,
    sin espacios.
c) Programar una función llamada get_info que no tome parámetros y
    retorne una tupla de tres elementos de tipo String: Tu(s)
    nombre(s), Tu(s) Apellido(s) y tu DNI.

En el programa principal:

d) Llamar a la función get_info y guardar su retorno en una variable
    llamada info.
e) Ejecutar la función print con la variable info como parámetro.
f) Ejecutar la función print_plus 5 veces consecutivas con los
    siguientes parámetros:
    i) Una String vacía
    ii) El primer elemento (index 0) de la variable info
    iii) El segundo elemento de la variable info
    iv) El tercer elemento de la variable info
    v) Una String vacía
g) Solicitar al usuario el ingreso de una palabra con el s
    "Ingrese una palabra: " y almacenar dicho ingreso en una variable
    llamada palabra. Ejecutar la función print_plus con la variable
    palabra como parámetro.

Ejemplo de funcionamiento/output esperado:

('Nombre1 Nombre2', 'Apellido', '12345678')
##################################################
Nombre 1 Nombre 2 ################################
Apellido #########################################
12345678 #########################################
##################################################
Ingrese una palabra: Telescopio
Telescopio #######################################

"""


def get_info():
    return ("Yngwie Johann", "Malmsteen", "12345678")


def print_plus(s="", c="#", n=50):
    print(f"{s if not s else s + ' '}".ljust(n, c))


def main():
    info = get_info()
    print(info)
    print_plus()
    for dato in info:
        print_plus(dato)
    print_plus()
    print_plus(input("Ingresar una palabra: "))


if __name__ == "__main__":
    main()
