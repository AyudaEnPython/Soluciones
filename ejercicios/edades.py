"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Queremos guardar los nombres y las edades de los alumnos de un curso.
Realiza un programa que introduzca el nombre y la edad de cada alumno.
El proceso de lectura de datos determinará cuando se introduzca como
nombre un asterisco ('*'). Al finalizar se mostrará los siguientes
datos:
- Todos los alumnos mayores de edad.
- El alumno(a) de mayor edad.
"""

def solucion_a():
    datos = []

    while True:
        nombre = input("Nombre: ")
        if nombre == "*":
            break
        edad = int(input("Edad: "))
        datos.append((nombre, edad))

    mayores = [nombre for nombre, edad in datos if edad >= 18]
    print("Mayores de edad" , *mayores, sep=", ")
    print("Alumno(a) de mayor edad:", max(datos, key=lambda x: x[1]))


def solucion_b():
    datos = []
    
    while True:
        nombre = input("Nombre: ")
        if nombre == "*":
            break
        edad = int(input("Edad: "))
        datos.append((nombre, edad))

    print("Mayores de edad")
    for nombre, edad in datos:
        if edad >= 18:
            print(nombre)
    
    mayor = 0
    alumno = ""
    for nombre, edad in datos:
        if edad >= mayor:
            mayor = edad
            alumno = nombre
    print("Alumno(a) de mayor edad: ", alumno)