"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: Se opta por cambiar algunas cosas para seguir (PEP8).
"""

print("Inicio de Sesión")
usuario = input("Usuario: ")
contraseña = input("Contraseña: ")

if usuario == "administrador" and contraseña == "123":
    print("Bienvenido al Sistema")
else:
    print("Usuario o contraseña incorrecta")