"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Cree un nuevo archivo, el cual contenga la siguiente frase:

"Bienvenidos a la última sesión de clase. Ha sido un gusto, un placer,
haber compartido estás 14 semanas con ustedes. Sigan adelante y
nunca tiren la toalla futuros colegas."

Acceder al archivo y leer la frase línea por línea. Por último, capture
la pantalla de todo lo realizado en consola y péguela en este documento
Word.
"""
from time import sleep
from typing import List


def obtener_texto(ruta: str) -> List[str]:
    """Lee un archivo de texto y devuelve una lista de líneas

    :param ruta: Ruta del archivo a leer
    :ruta type: str
    :return: Lista de líneas del archivo
    :ruta type: List[str]
    """
    with open(ruta, encoding="utf-8") as f:
        return f.read().splitlines()


def mostrar(texto: List[str]) -> None:
    """Muestra linea por linea el texto con un retardo de 1.5 segundos

    :param texto: Lista de líneas del texto
    :texto type: List[str]
    """
    for linea in texto:
        print(linea, end="\n", flush=True)
        sleep(1.5)


def main():
    mostrar(obtener_texto("frase.txt"))


if __name__ == "__main__":
    main()
