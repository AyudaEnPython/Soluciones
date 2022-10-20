"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

Creen un diccionario que permita almacenar los datos de tres empleados,
utilizar como clave el nombre del empleado y su sueldo bruto. El
programa solicitará los datos al usuario (nombre y sueldo) y los
almacenará (de los tres empleados), para lo que debe crear una función.

Deben considerar que si la persona gana menos de $10.000 no paga
impuesto. En los siguientes casos si paga impuesto y será en base a el
sueldo bruto:
- Entre $10.000 y $30.000, el impuesto será del 10% del sueldo
- Mayor $30.000 hasta $50.000, el impuesto será del 20% del sueldo
- Superior a $50.000 el impuesto será del 35% del sueldo

Además, por concepto de AFP pagará el 11% de su sueldo bruto y por
previsión de salud el 7% de su sueldo bruto.
"""
AFP = 0.11
SALUD = 0.07


def impuesto(sueldo):
    if 10_000 <= sueldo <= 30_000:
        return 0.1
    elif 30_000 < sueldo <= 50_000:
        return 0.2
    else:
        return 0.35


def calcular_sueldo(sueldo):
    if sueldo < 10_000:
        return sueldo
    return sueldo - impuesto(sueldo)*sueldo


def empleados_datos(n=3):
    datos = {}
    for i in range(1, n+1):
        nombre = input(f"[Empleado N°{i}] Ingresar nombre:")
        sueldo_bruto = float(input(f"[Empleado N°{i}] Ingresar sueldo:"))
        sueldo = calcular_sueldo(sueldo_bruto)
        sueldo -= sueldo_bruto * (AFP + SALUD)
        datos[nombre] = sueldo
    return datos


def main():
    datos = empleados_datos()
    print(datos)


if __name__ == "__main__":
    main()
