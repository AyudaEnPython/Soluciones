"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Escribir un bucle que pida a los usuarios su nombre. Recopile todos los
nombres introducidos por los usuarios. A continuación, escríbalos en un
archivo llamado libro-invitados.txt. Asegúrese que cada entrada aparece
en una nueva línea del archivo.
"""
from pathlib import Path


def get_names():
    names = []
    while True:
        name = input("Ingresar nombre (o presionar 'Enter' para terminar): ")
        if name == "":
            break
        names.append(name)
    return names


def save(names, file):
    file.write_text("\n".join(names), encoding="utf-8")
    print(f"Se han guardado {len(names)} nombres en {file}")


def main():
    names = get_names()
    file = Path("libro-invitados.txt")
    save(names, file)


if __name__ == "__main__":
    main()
