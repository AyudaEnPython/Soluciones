from random import choice, randint


def generar_archivo(fichero: str) -> None:
    with open(fichero, "w") as f:
        for i in range(1, 1001):
            tipo = choice(("auxiliar", "asociado", "principal"))
            tipos = {
                "auxiliar": randint(2_000, 6_000),
                "asociado": randint(4_000, 7_000),
                "principal": randint(6_000, 9_000),
            }
            f.writelines(
                f"Nombre{i:04} Apellido{i:04} {tipo:<9} {tipos[tipo]}\n"
            )


def leer_archivo(fichero: str) -> None:
    auxiliares, asociados, principales = 0, 0, 0
    mayor_salario, profesor_mayor_salario = 0, ""
    with open(fichero, "r") as f:
        for linea in f:
            nombre, apellido, categoria, salario = linea.split()
            salario = int(salario)
            if categoria == "auxiliar":
                auxiliares += 1
            if categoria == "asociado":
                asociados += 1
            if categoria == "principal":
                principales +=1
            if salario > mayor_salario:
                mayor_salario = salario
                profesor_mayor_salario = f"{nombre} {apellido}"
    print(f"Cantidad de auxiliares: {auxiliares}")
    print(f"Cantidad de asociados: {asociados}")
    print(f"Cantidad de principales: {principales}")
    print(f"Profesor con mayor salario: {profesor_mayor_salario}")


def main():
    generar_archivo("data/salario.txt")
    leer_archivo("data/salario.txt")


if __name__ == "__main__":
    main()
