from typing import List, Dict


def _añadir(
    directorio: Dict[str, List[str]],
    nombre: str,
    telefono: str
) -> None:
    if nombre in directorio:
        if not telefono in directorio[nombre]:
            directorio[nombre].append(telefono)
    else:
        directorio[nombre] = [telefono]


def _consultar(directorio: Dict[str, List[str]], nombre: str) -> str:
    if nombre in directorio:
        return directorio[nombre]
    return f"El nombre {nombre} no se encuentra en el directorio"


def _eliminar(directorio: Dict[str, List[str]], nombre: str) -> None:
    if nombre in directorio:
        del directorio[nombre]
        print("Datos eliminados!")
    else:
        print("No se encontró el nombre")


def añadir_telefornos(
    directorio: Dict[str, List[str]],
) -> None:
    nombre = input("Ingrese un nombre: ")
    while True:
        telefono = input("Ingrese un telefono: ")
        _añadir(directorio, nombre, telefono)
        respuest = input(f"¿Desea añadir otro telefono a {nombre} (s/n)?: ")
        if respuest == "n":
            break


def consultar_persona(directorio: Dict[str, List[str]]) -> None:
    nombre = input("Ingrese un nombre: ")
    telefonos = _consultar(directorio, nombre)
    if isinstance(telefonos, list):
        print(f"{nombre} tiene los siguientes telefonos:")
        for telefono in telefonos:
            print(f"- {telefono}")
    else:
        print(telefonos)


def eliminar_persona(directorio: Dict[str, List[str]]) -> None:
    nombre = input("Ingrese un nombre: ")
    _eliminar(directorio, nombre)


def menu():
    print("MENU PRINCIPAL\n")
    print("1) Añadir teléfonos al directorio")
    print("2) Consultar persona en el directorio")
    print("3) Eliminar persona del directorio")
    print("4) Salir")
    while True:
        opcion = input("Seleccione una opcion: ")
        if opcion in ("1", "2", "3", "4"):
            return opcion
        print("Opcion invalida, intentar de nuevo")


def main():
    directorio = {}
    while True:
        opcion = menu()
        print()
        if opcion == "4":
            print("Saliste...")
            break
        if opcion == "1":
            añadir_telefornos(directorio)
        elif opcion == "2":
            consultar_persona(directorio)
        elif opcion == "3":
            eliminar_persona(directorio)


if __name__ == "__main__":
	main()
