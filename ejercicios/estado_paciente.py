"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Ingresando los datos de un paciente determinamos si tiene amenia, tiene
glucosa, tiene colesterol y tiene sobrepeso.

Si se cumple 0 a 1 parámetro anormal, determine que la persona esta sana
Si se cumple 2 parámetros anormales, determine que la persona tiene
    principio de riesgo
Si se cumple 3 a 4 parámetros anormales, determinar que la persona
    tiene enfermedad

Se ingresa la edad, la estatura, resultado de glóbulos rojos, nivel de
colesterol y nivel de glucosa.

Glucosa : 0-120 niveles correctos, 131 en adelante diabetes
Colesterol :0-230 niveles correctos, 231 en adelante colesterol elevado
Anemia se considera si los glóbulos rojos en hombres es 5000000 y en
mujeres que 4000000.

NOTE: El enunciado original tiene errores.
"""


def estado(anormalias):
    if anormalias <= 1:
        return 'sana'
    elif anormalias == 2:
        return 'en riesgo'
    else:
        return 'enferma'


def resultados(sexo, globulos, colesterol, glucosa):
    anoramalias = 0
    if glucosa > 131:
        anoramalias += 1
    if colesterol > 231:
        anoramalias += 1
    if sexo == "m" and globulos < 5000000:
        anoramalias += 1
    if sexo == "f" and globulos < 4000000:
        anoramalias += 1
    return anoramalias


def main():
    sexo = input("Sexo (m/f): ")
    # edad = int(input("Edad: "))
    # estatura = float(input("Estatura: "))
    globulos = int(input("Globulos rojos: "))
    colesterol = int(input("Colesterol: "))
    glucosa = int(input("Glucosa: "))
    anormalias = resultados(sexo, globulos, colesterol, glucosa)
    print(f"Estado: {estado(anormalias)}")


if __name__ == "__main__":
    main()
