"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

NOTE: Se opta por cambiar algunas cosas para seguir (PEP8).
"""

print("Inicio de Sesión")
usuario = input("Usuario: ")
password = input("Contraseña: ")

if usuario == "administrador" and password == "123":
    print("Bienvenido al Sistema")
else:
    print("Usuario o contraseña incorrecta")