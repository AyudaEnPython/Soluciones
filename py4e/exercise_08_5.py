"""Escribe un programa para leer mbox-short.txt Cuando encuentres una
línea que comience con 'From' como la siguiente línea:

    +------------------------------------------------------------+
    | De stephen.marquard@uct.ac.za Sáb 5 de enero 09:14:16 2008 |
    +------------------------------------------------------------+

Analiza la línea From utilizando split () e imprime la segunda palabra
en la línea (es decir, la dirección completa de la persona que envió el
mensaje). A continuación, imprime un recuento al final.

    Salida deseada
    +-------------------------------------------------------------+
    | stephen.marquard@uct.ac.za                                  |
    | louis@media.berkeley.edu                                    |
    | zqian@umich.edu                                             |
    | rjlowe@iupui.edu                                            |
    | zqian@umich.edu                                             |
    | rjlowe@iupui.edu                                            |
    | cwen@iupui.edu                                              |
    | cwen@iupui.edu                                              |
    | gsilver@umich.edu                                           |
    | gsilver@umich.edu                                           |
    | zqian@umich.edu                                             |
    | gsilver@umich.edu                                           |
    | wagnermr@iupui.edu                                          |
    | zqian@umich.edu                                             |
    | antranig@caret.cam.ac.uk                                    |
    | gopal.ramasammycook@gmail.com                               |
    | david.horwitz@uct.ac.za                                     |
    | david.horwitz@uct.ac.za                                     |
    | david.horwitz@uct.ac.za                                     |
    | david.horwitz@uct.ac.za                                     |
    | stephen.marquard@uct.ac.za                                  |
    | louis@media.berkeley.edu                                    |
    | louis@media.berkeley.edu                                    |
    | ray@media.berkeley.edu                                      |
    | cwen@iupui.edu                                              |
    | cwen@iupui.edu                                              |
    | cwen@iupui.edu                                              |
    | Hay 27 lineas en el archivo con From como la primer palabra |
    +-------------------------------------------------------------+

Sugerencia: asegúrate de no incluir las líneas que comienzan con 'From:'.

En http://es.py4e.com/code3/romeo.txt puedes descargar los datos de
muestra.
"""

archivo = input("Nombre de archivo: ") # mbox-short.txt
f = open(archivo)
i = 0
for linea in f:
    if linea.startswith("From "):
        print(linea.split()[1])
        i += 1
print("Hay", str(i), "lineas en el archivo con From como la primer palabra")