"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


class DniException(Exception):
    """Excepción para DNI"""


def validar(dni: str) -> str:
    """Valida un DNI
    
    :param dni: DNI a validar
    :dni type: str
    :return: DNI validado
    :rtype: str
    """
    if len(dni) != 8:
        raise DniException("El DNI debe tener 8 caracteres")
    if not dni.isdigit():
        raise DniException("El DNI debe contener solo números")
    return dni


class Persona:
    
    def __init__(self, nombre: str, apellido: str, dni: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.__dni = validar(dni)
    
    @property
    def dni(self) -> str:
        return self.__dni
    
    @dni.setter
    def dni(self, dni: str) -> None:
        self.__dni = validar(dni)
