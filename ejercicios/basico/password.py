"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Crea un programa que pida al usuario una contraseña, de forma
repetitiva mientras que no introduzca "asdasd". Cuando finalmente
escriba la contraseña correcta, se le dirá "Bienvenido" y terminará
el programa.
"""

contraseña = "asdasd"
while True:
    contraseña = input("> ")
    if contraseña == "asdasd":
        break
print("Bienvenido")
