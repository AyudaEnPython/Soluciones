# Enunciado Original

Escriba una función llamada encontrarTesoro que reciba como entrada un string
que represente el nombre de un archivo conteniendo las instrucciones para llegar
a un tesoro, y que devuelva la ubicación del tesoro después de seguir las
instrucciones. Dentro del archivo, cada línea representa una instrucción, y
está compuesta por una letra seguida de un espacio y un número. La letra
representa una dirección (Este, Oeste, Norte, Sur), y el número, el número de
pasos a tomar en esa dirección.

Por ejemplo, considere el siguiente archivo de muestra, con 6 instrucciones:

    E 5
    N 6
    O 43
    S 9
    E 12
    S 31

Las instrucciones de este archivo se leen de la siguiente manera:
- 5 pasos al este
- 6 pasos al norte
- 43 pasos al oeste
- 9 pasos al sur
- 12 pasos al este
- 31 pasos al sur

Siempre vamos a empezar buscando el tesoro desde la ubicación 0,0.
La primera coordenada representa el eje X e incrementa hacia el este y decrementa
hacia el oeste, y la segunda coordenada representa el eje y e incrementa hacia al
sur y decrementa hacia el norte:

La consola solamente imprimiría lo siguiente:
- Nos movemos al este 5 pasos, estando ahora en la posición 5,0
- Nos movemos al norte 6 pasos, estando ahora en la posición 5,-6
- Nos movemos al oeste 43 pasos, estando ahora en la posición -38,-6
- Nos movemos al sur 9 pasos, estando ahora en la posición -38,3
- Nos movemos al este 12 pasos, estando ahora en la posición -26,3
- Nos movemos al sur 31 pasos, estando ahora en la posición -26,34

Esto quiere decir que el tesoro está en la posición -26,34
