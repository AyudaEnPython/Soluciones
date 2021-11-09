"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escriba un programa mediante una función valide si es una dirección de 
correo electrónico pertenece al dominio calufa.com, debe pedir al
usuario que ingrese el correo, si pertenece a calufa le enviará un
mensaje "Valido", sino "Inválido". Además, incorpore un ciclo de modo
que el usuario pueda decidir si desea ingresar otro correo electrónico.

TODO: add more implementations and testcases
"""


def validar_correo(usuario: str, dominio: str = '@calufa.com') -> bool:
    """
    Función que valida si un correo electrónico pertenece al dominio
    calufa.com.

    :param usuario: correo electrónico a validar
    :type usuario: str
    :param dominio: dominio a validar
    :type dominio: str
    :return: True si pertenece al dominio calufa.com, False si no
    :rtype: bool
    """
    if usuario.endswith(dominio):
        return True
    return False


def main():
    while True:
        usuario = input("Ingrese un correo electrónico: ")
        if validar_correo(usuario):
            print("Válido")
        else:
            print("Inválido")
        continuar = input("¿Desea ingresar otro correo? (s/n): ")
        if continuar.lower() == 'n':
            break


if __name__ == "__main__":
    main()