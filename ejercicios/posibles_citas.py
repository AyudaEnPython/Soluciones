"""
Wally busca novia y quiere que alguien que sea mayor de 30, que le
interese el arte y que viva en Mendoza. Escribir un programa que le
permita, dada la siguiente informacion, buscar y encontrar quienes
cumplen con sus requerimientos. En pantalla deberian verse todos los
nombres que podrian ser para Wally separados por coma.
Para cada persona, se guardan algunos datos como su edad, sus hobbies y
la ciudad donde vive.

TODO: add more implementations, docstring, testcases
"""

usuarios = [
    {
        "nombre": "Julia",
        "sexo": "femenino",
        "edad": 29,
        "hobbies": ["correr", "musica", "leer"], 
        "ciudad":"Cordoba"
    },
    {
        "nombre": "Camila",
        "sexo": "femenino",
        "edad": 18,
        "hobbies": ["escribir", "arte"], 
        "ciudad":"Mendoza"
    },
    {
        "nombre": "Lucia",
        "sexo": "femenino",
        "edad": 35,
        "hobbies": ["arte"], 
        "ciudad":"Mendoza"
    },
    {
        "nombre": "Daniel",
        "sexo": "masculino",
        "edad": 50,
        "hobbies": ["boxeo", "leer", "arte"], 
        "ciudad":"Mendoza"
    },
    {
        "nombre": "Pepe",
        "sexo": "masculino",
        "edad": 32,
        "hobbies": ["correr", "leer"], 
        "ciudad":"Cordoba"
    },
    {
        "nombre": "Juan",
        "sexo": "masculino",
        "edad": 41,
        "hobbies": ["leer", "alpinismo", "juegos de mesa"], 
        "ciudad":"Cordoba"
    }
]


def main():
    preferencias = lambda persona: (
        persona["sexo"] == "femenino" and
        persona["edad"] > 30 and
        persona["ciudad"] == "Mendoza" and
        "arte" in persona["hobbies"]
    )

    citas = [usuario["nombre"] for usuario in usuarios if preferencias(usuario)]
    print(", ".join(citas))


if __name__ == "__main__":
    main()