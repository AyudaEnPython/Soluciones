# Enunciado Original 

## Parte A. Carga del archivo

Haga una función que lea el archivo MuseoJade.vis y cargue los datos al diccionario global.

## Parte B. Ingresar nuevo dato

Haga una función que reciba de parámetro dos hileras de caracteres: una fecha
en formato DD/MM/AAAA y un número de cédula de 9 dígitos. A partir de eso, debe
ingresarlo como una nueva visita al archivo MuseoJade.vis, sin borrar los
registros que había antes y siguiendo el formato. También deberá actualizar los
datos del diccionario global.

## Parte C. Interacción con el ususario

Realice una función que interactúe con el usuario. Esta función debe cargar al
inicio el archivo de texto al diccionario global, y luego mostrar un menú
continuo de 3 opciones:
- Ingresar nuevo dato (pedir fecha y cédula)
- Cononcer cantidad de visitas de una persona (por su cédula)
- Salir

Recuerde incorporar un llamado a la función interactiva.

_Opcional_: Agregue una funcionalidad a su programa para validar las entradas,
de forma que solo permita agregar un nuevo registro de visitante si se ingresa
una cédula y una fecha válidas. Caso contrario, deberá notificar el error y volver
a pedirlo.

Este prodría ser un ejemplor del contenido de ese archivo:

    20/06/2022 112340512
    20/06/2022 478944101
    20/06/2022 404789899
    21/06/2022 445467890
    21/06/2022 112340512
    22/06/2022 145784476
