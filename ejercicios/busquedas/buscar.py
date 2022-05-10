"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# Motor de Búsqueda

Estás trabajando en un motor de búsqueda. ¡Vigila tu espalda Google!

El código dado toma un `text` y un `word` como entrada y los pasa a
una función llamada `search()`.

La función `search()` debe devolver `"Word found"` si la palabra está
presente en el texto, o `"Word not found"`, si no es así.

## Ejemplo de entrada
"This is awesome"
"awesome"

## Ejeplo de salida
"Word found"
"""


def search(text: str, word: str) -> str:
    """Busca una palabra en un texto.

    :param text: Texto en el que se buscará la palabra.
    :text type: str
    :param word: Palabra a buscar.
    :word type: str
    :return: "Word found" si la palabra está presente en el texto,
        o "Word not found" si no es así.
    :rtype: str

    >>> search("This is awesome", "awesome")
    'Word found'
    """
    return "Word found" if word in text else "Word not found"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
