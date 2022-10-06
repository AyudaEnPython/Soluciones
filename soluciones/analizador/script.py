# flake8: noqa
def a():
    print("a")

def B(): print("b")

def C():

    print("c")

x = "Una cadena muy larga que sobrepasa los 79 carateres por linea definidos en PEP8"
#comentario innecesario: Se imprime por pantalla usando list comprehension
[print("Sobre uso de list_comprehension") for x in range(1, 10)]

# etc