"""
Escriba un programa para leer mbox-short.txt y calcule la distribución
por hora del día para cada uno de los mensajes. Puede obtener la hora
desde las líneas que comienzan con 'From' para encontrar el tiempo y
luego dividir la cadena por segunda vez con dos puntos.

    +---------------------------------------------------------------+
    | De stephen.marquard@uct.ac.za Sáb 5 de enero 09 : 14: 16 2008 |
    +---------------------------------------------------------------+

Una vez que haya acumulado los recuentos de cada hora, imprima los
recuentos, ordenados por hora como se muestra a continuación.

    Salida deseada
    +------------+
    | 04 3       |
    | 06 1       |
    | 07 1       |
    | 09 2       |
    | 10 3       |
    | 11 6       |
    | 14 1       |
    | 15 2       |
    | 16 4       |
    | 17 2       |
    | 18 1       |
    | 19 1       |
    +------------+
"""

archivo = input("Nombre de archivo: ") # mbox-short.txt
f = open(archivo)
horas = []
for linea in f:
    if linea.startswith("From "):
        horas.append(linea.split()[5].split(":")[0])
f.close()
resultado = dict([(i, horas.count(i)) for i in sorted(horas)])

for k, v in resultado.items():
    print(k, v)