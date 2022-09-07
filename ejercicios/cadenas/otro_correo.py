"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un programa que pregunte el correo electrónico del usuario en
la consola y muestre por pantalla otro correo electrónico como sigue:

Ejemplo:

Entrada: jesus.perez@UASB.edu.bo
Salida: Jesus.Perez@usab.edu
"""


def separar_correo(correo: str) -> str:
    """
    >>> correo = "jesus.perez@UASB.edu.bo"
    >>> separar_correo(correo)
    'Jesus.Perez@uasb.edu.bo'
    """
    usuario, dominio = correo.split("@")
    return f"{usuario.title()}@{dominio.lower()}"


def main():
    print(separar_correo(input("Ingresar correo: ")))


if __name__ == "__main__":
    # import doctest
    # doctest.testmod()
    main()
