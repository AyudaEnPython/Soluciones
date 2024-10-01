# Enunciado Original

La aerolínea "Alitas de Murciélago" necesita un sistema para la venta de pasajes
de su único Avión, el cual posee 42 asientos cuyos números se deben asignar en
forma automática al momento de ejecutar el sistema, considerando el siguiente
formato:

    |   1   2   3         4   5   6  |
    |                                |
    |   7   8   9        10  11  12  |
    |                                |
    |  13  14  15        16  17  18  |
    |                                |
    |  19  20  21        22  23  24  |
    |                                |
    |  25  26  27        28  29  30  |
    +-------------      -------------+
    +-------------      -------------+
    |  31  32  33        34  35  36  |
    |                                |
    |  37  38  39        40  41  42  |

(arreglo de tamaño 7x6)

Desde el asiento 31 al 42 son asientos Vip cuyo valor es de $250000 y el resto son
asientos normales cuyo valor es de $75000.

Una vez asignados los asientos de forma automática, debe mostrar y ejecutar el siguiente
menú:

       Alitas de Murciélago
       ********************
    1. Mostrar asientos disponibles
    2. Comprar Pasaje
    3. Totales
    4. Anular venta
    5. Listado de pasajeros
    6. Salir

            Elija Opción:

- **Opción 1**: debe mostrar todos los asientos disponibles con su número de asiento y los no
  disponibles con una "X".
  Ejemplo:

        |   1   2   3         4   5   6  |
        |                                |
        |   7   X   9        10  11   X  |
        |                                |
        |  13  14  15        16  17  18  |
        |                                |
        |  19  20  21        22  23  24  |
        |                                |
        |  25  26  27         X  29  30  |
        +-------------      -------------+
        +-------------      -------------+
        |  31  32  33        34  35  36  |
        |                                |
        |   X  38  39        40  41  42  |

- **Opción 2**: debe solicitar el número de asiento.
  - Si está disponible:
      - Debe almacenar en un arreglo del Rut del pasajero (sin puntos ni dígito verificador;
        ejemplo: 21111222)
      - Mostrar el total a pagar
      - Dejar una X en el asiento
      - Volver al menú principal
  - Si no está disponible:
      - Mostrar el mensaje adecuado
      - Volver al menú principal

- **Opción 3**: Mostrará las siguientes estadísticas:
  - Cantidad de asientos Vip vendidos => xx
  - Cantidad de asientos Normales vendidos => xx
  - Total Recaudado => $xxxx
  - Y volverá al menú principal

- ***Opción 4***: Deja disponible el número de asiento solicitado y eliminará el Rut del pasajero.
  Si el asiento estaba disponible, mostrar mensaje de error.

- **Opción 5**: Debe mostrar el listado de pasajeros (sus Rut), ordenados de menor a mayor. Si no
  hay pasajeros, mostrar el mensaje adecuado.

El sistema debe contemplar dos archivos. Uno, donde se encuentra el programa principal donde
se solicita la información (**validada**), llamadas a las distintas funciones y muestra de
datos y el otro, donde se encuentra las funciones que realizan los procesos de cada opción.

> __**NOTA**__: El enunciado propuesto no esta bien diseñado.