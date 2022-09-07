"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa para una empresa que tiene salas de juegos para
todas las edades y quiere calcular de forma automática el precio que
debe cobrar a sus clientes por entrar. El programa debe preguntar al
usuario la edad del cliente y mostrar el precio de la entrada. Si el
cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 8
años debe pagar S/.5 y si es mayor a 18 años, S/.10.
"""

edad = int(input("Ingresar edad: "))

if edad < 4:
    print("Entrada gratis")
elif 4 <= edad <= 8:
    print("Entrada S/.5")
else:
    print("Entrada S/.10")
