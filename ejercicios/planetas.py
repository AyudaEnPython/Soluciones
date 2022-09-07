"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Dado una cadena de texto llamada "planetas" que contiene los planetas
del sistema solar que incluye la estrella Sol separados por el texto
'@plantea$' de la siguiente forma:

planetas = "Sol@plantea$Mercurio@plantea$Venus@plantea$Tierra" \
    "@plantea$Marte@plantea$Jupiter@plantea$Saturno@plantea$Urano" \
    "@plantea$Neptuno@plantea$Pluton"

Se pide resolver lo siguiente:

- Crear un diccionario con llave entera desde 1 hasta 10 en forma
    correlativa y valor string que represente el planeta a partir de la
    cadena 'planetas'.
- Se pide crear una función que reciba como parámetro el índice y
    retorne el valor. El índice es leído por teclado.
- Se pide crear una función que reciba como parámetro el valor y
    retorne el índice. El valor es leído por teclado.

Nota:
    - Validar que la llave y el valor ingresado sea del tipo de dato
        correspondiente y en el caso de la llave que este en el rango
        desde 1 hasta 10.

Algunos ejemplos de diálogo de este programa serían:

    +-----------------------------------------------+
    | Ingrese una llave desde 1 hasta 10: 5         |
    | El valor con llave 5 es Marte                 |
    | Ingrese el nombre de un planeta: tierra       |
    | El valor con llave tierra es 4                |
    +-----------------------------------------------+

    +-----------------------------------------------+
    | Ingrese una llave desde 1 hasta 10: 11        |
    | Ingrese una llave desde 1 hasta 10: -1        |
    | Ingrese una llave desde 1 hasta 10: 10        |
    | El valor con llave 10 es Pluton               |
    | Ingrese el nombre de un planeta: 123          |
    | Ingrese el nombre de un planeta: planeta      |
    | Ingrese el nombre de un planeta: sol          |
    | El valor con llave sol es 1                   |
    +-----------------------------------------------+

    +-----------------------------------------------+
    | Ingrese una llave desde 1 hasta 10: 4         |
    | El valor con llave 4 es Tierra                |
    | Ingrese el nombre de un planeta: sol          |
    | El valor con llave sol es 1                   |
    +-----------------------------------------------+
"""
planetas = "Sol@plantea$Mercurio@plantea$Venus@plantea$Tierra@plantea$" \
    "Marte@plantea$Jupiter@plantea$Saturno@plantea$Urano@plantea$Neptuno" \
    "@plantea$Pluton"

planetas = planetas.split("@plantea$")
datos = dict(zip(range(1, 11), planetas))


def retorna_valor(indice: str) -> str:
    return datos[indice]


def retorna_llave(valor: str) -> str:
    for llave, val in datos.items():
        if valor == val:
            return llave
    # return list(datos.keys())[list(datos.values()).index(valor)]


def ingresar_llave() -> int:
    while True:
        try:
            llave = int(input("Ingrese una llave desde 1 hasta 10: "))
            if llave in range(1, 11):
                return llave
            else:
                continue
        except ValueError:
            continue


def ingresar_valor() -> str:
    while True:
        try:
            valor = input("Ingrese el nombre de un planeta: ")
            valor = valor.capitalize()
            if valor in datos.values():
                return valor
            else:
                continue
        except ValueError:
            continue


def main():
    llave = ingresar_llave()
    print(f"El valor con llave {llave} es {retorna_valor(llave)}")
    valor = ingresar_valor()
    print(f"El valor con llave {retorna_llave(valor)} es {valor}")


if __name__ == "__main__":
    main()
