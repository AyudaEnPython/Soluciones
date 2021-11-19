"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
import math

valor = True
while valor:
    print("Menú de  opciones")
    print("1. Raíz cuadrada de la suma de dos números: ")
    print("2. Solución de ecuación de 2° grado: ")
    print("3. Área de un triángulo: ")
    opcion = int(input("Opción: "))
    print()
    if opcion == 1:
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        raiz = lambda x,y: math.sqrt(x+y) 
        print(f"El resultado de la raíz de {num1} + {num2} es: {raiz(num1, num2)}")
        valor = False

    elif opcion == 2:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))

        solucion1 = lambda a,b,c: -b + math.sqrt(b**2 - 4*a*c)/2*a 
        solucion2 = lambda a,b,c: -b - math.sqrt(b**2 - 4*a*c)/2*a
        print(f"Primera solución para x1 = {solucion1(a,b,c)}")
        print(f"Segunda solución para x2 = {solucion2(a,b,c)}")
        valor = False

    elif opcion == 3:
        altura = int(input("Altura: "))
        base = int(input("Base: "))
        area = lambda altura,base: altura*base/2 
        print(f"El área de un triángulo con altura = {altura} y base = {base} es: {area(altura,base)}")
        valor = False

    else:
        print(f"Fuera de rango. Usted eligió: {opcion}")