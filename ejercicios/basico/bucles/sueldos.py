"""AyudaEnPython: https://www.facebook.com/groups/ayudapython

# ------------------------- Enunciado Original ------------------------
Plaza Vea es una empresa que tiene varios empleados cuyos sueldos
oscilan entre S/. 1000 y S/. 2000.
Elabore un programa que lea los sueldos que cobra cada empleado e
informe cuántos empleados cobran entre S/. 1000 y S/. 1500 y cuántos
cobran mas de S/. 1500. Además, el programa deberá informar el importe
que gasta Plaza Vea en la planilla de sueldos del personal.
"""

MIN, MAX = 1_000, 2_000
a = b = total = 0  # a: cobran entre 1000 y 1500; b: cobran más de 1500

while True:
    sueldo = input("Ingresar sueldo: ")
    if not sueldo.replace("-", "").replace(".", "").isdigit():
        print("Ingresar solo números!")
        continue
    sueldo = float(sueldo)
    if sueldo <= 0:
        break
    if MIN <= sueldo <= MAX:
        total += sueldo
        if sueldo <= 1500:
            a += 1
        else:
            b += 1
    else:
        print("Ingresar un sueldo válido!")

print(f"N° de empleados que cobran entre S/.1000 y S/.1500: {a}")
print(f"N° de empleados que cobran más de S/.1500: {b}")
print(f"Gasto total de la plantilla de sueldos: {total}")
