"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Definir una función denominada "definir_orden" que reciba por
parámetros tres cadenas de texto distintos cad_a, cad_b y cad_c y las
devuelva en orden alfabético de izquierda a derecha.

Definir una función denominada "ordenar_palabras" que solicite tres
palabras a la persona usuaria. Debe controlar que sean palabras 
distintas y en caso contrario solicitar reingresos hasta que lo sean.
Luego debe invocar a la función "definir_orden" y mostrar las palabras
ordenadas.

NOTE: El enunciado no es claro, no especifica si "definir_orden" va a
    ser utilizado dentro de "ordenar_palabras". No se tiene ejemplos de
    salida.
    Una de las personas que solicita ayuda menciona que no puede usar
    listas ni tuplas (no indicado en el enunciado).

TODO: add tests later...
"""


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr


def definir_orden_bubble_naive(a, b, c):
    p, q, r = bubble_sort([a.lower(), b.lower(), c.lower()])
    if a.lower() == p:
        p = a
    elif b.lower() == p:
        p = b
    else:
        p = c
    if a.lower() == q:
        q = a
    elif b.lower() == q:
        q = b
    else:
        q = c
    if a.lower() == r:
        r = a
    elif b.lower() == r:
        r = b
    else:
        r = c
    return f"{p}, {q}, {r}"


def definir_orden_naive(a, b, c):
    if a.lower() < b.lower():
        if b.lower() < c.lower():
            return f"{a}, {b}, {c}"
        elif a.lower() < c.lower():
            return f"{a}, {c}, {b}"
        else:
            return f"{c}, {a}, {b}"
    elif b.lower() < c.lower():
        if a.lower() < c.lower():
            return f"{b}, {a}, {c}"
        else:
            return f"{b}, {c}, {a}"
    else:
        return f"{c}, {b}, {a}"


def ordenar_palabras_naive():
    p = q = r = s = ""
    i = 0
    while True:
        if i == 3:
            break
        w = input("Ingrese una palabra: ")
        if w in s:
            print("La palabra ya existe.")
            continue
        if i == 0:
            p = w
        elif i == 1:
            q = w
        else:
            r = w
        s += f"{w}, "
        i += 1
    print(definir_orden_naive(p, q, r))


def definir_orden_builtin(a: str, b: str, c: str) -> str:
    """Devuelve tres palabras en orden alfabético de izquierda a derecha.

    :param a: Primera palabra.
    :a type: str
    :param b: Segunda palabra.
    :b type: str
    :param c: Tercera palabra.
    :c type: str
    :return: Las tres palabras en orden alfabético de izquierda a derecha.
    :rtype: str
    """
    return ", ".join(sorted([a, b, c], key=str.lower))


def ordenar_palabras_alt() -> None:
    """Pide tres palabras distintas y las devuelve en orden alfabético.
    """
    palabras = []
    while True:
        if len(palabras) == 3:
            break
        palabra = input("Ingrese una palabra: ")
        if palabra in palabras:
            print("La palabra ya existe.")
            continue
        palabras.append(palabra)
    print(definir_orden_builtin(*palabras))


def main():
    ordenar_palabras_naive()
    # ordenar_palabras_alt()


if __name__ == '__main__':
    main()