"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
from string import ascii_lowercase
from typing import List, Tuple


def _helper(correo: str) -> Tuple[str, str]:
    return correo.split("@")


def get_data() -> List[str]:
    correos = []
    n = int(input("Cantidad de correos a validar: "))
    for i in range(n):
        correos.append(input(f"[{i+1}] Ingrese un correo: "))
    return correos


def _get_data(filename: str) -> List[str]:
    with open(filename, "r") as f:
        return [line.strip() for line in f]


def _validar_usuario(usuario: str) -> str:
    if usuario[0] not in ascii_lowercase:
        raise ValueError("El nombre debe comenzar con una letra")
    if not usuario.isalnum():
        raise ValueError("El usuario no es válido")
    if len(usuario) < 5 or len(usuario) > 20:
        raise ValueError("El usuario debe tener al menos 3 caracteres")
    return usuario


def _validar_dominio(dominio: str) -> str:
    if "." not in dominio:
        raise ValueError("Dominio inválido")
    ss = dominio.split(".")
    for s in ss:
        if len(s) < 2 or len(s) > 5:
            raise ValueError("Tamaño inválido de dominio")
        if not s.isalnum():
            raise ValueError("No puede contener caracteres especiales")
    return dominio


def validar_correo(correo: str) -> str:
    if correo.find(" ") != -1:
        raise ValueError("El correo no debe contener espacios")
    if "@" not in correo:
        raise ValueError("El correo no tiene @")
    usuario, dominio = _helper(correo)
    usuario = _validar_usuario(usuario)
    dominio = _validar_dominio(dominio)
    return correo


def main():
    # data = get_data()
    data = _get_data("data.txt")
    for email in data:
        try:
            print(validar_correo(email))
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
