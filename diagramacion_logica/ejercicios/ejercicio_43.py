"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""


def promedio(datos):
    if len(datos) == 0:
        return 0
    else:
        return sum(datos) / len(datos)


varones = []
mujeres = []
edades = []

i = 1
while True:
    print(f"Participante {i}")
    try:
        altura = float(input("Altura: "))
        if altura < 0:
            break
        edad = int(input("Edad: "))
        while True:
            sexo = input("Sexo (m/f): ").lower()
            if sexo == "m":
                varones.append(altura)
                break
            elif sexo == "f":
                mujeres.append(altura)
                break
            else:
                print("Sexo inválido")
        edades.append(edad)
        i += 1
    except ValueError:
        print("Error de datos, intente nuevamente")
        continue

print(f"\nAltura promedio de varones: {promedio(varones):.2f}")
print(f"Altura promedio de mujeres: {promedio(mujeres):.2f}")
print(f"Edad promedio: {promedio(edades):.2f}")