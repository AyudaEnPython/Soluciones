"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Eliminar los siguientes caracteres especiales de una cadena

!"#$%&\'()*+,-./:;<=>?@[]^_`{|}~©®°¦±¼½¾
"""
NOT_ALLOWED = "!\"#$%&\\\'()*+,-./:;<=>?@[]^_`{|}~©®°¦±¼½¾"


def sol(s: str) -> str:
    return "".join(c for c in s if c not in NOT_ALLOWED)


def main():
    print(sol(input("Entrada: ")))


if __name__ == "__main__":
    main()
