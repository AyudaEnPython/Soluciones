# Enunciado Original

## Radares de tramo

Debido a la alta accidentalidad presentada en el último año en las carreteras
del territorio nacional, el Gobierno Colombiano ha decidido implementar
controles que permitan sancionara a los conductores que no respeten los
límites de velocidad establecidos por los organismos de control. Con este fin,
el Ministerio de Transporte ha decidido implementar radares de tramo en las
carreteras con mayores índices de accidentalidad en el país. Los radares de
tramo funcionan colocando dos cámaras en dos puntos alejados de una carretera
con el fin de comprobar cuánto tiempo tarda un conductor recorrer dicho tramo.

Estos radares no miden la velocidad de paso, sino el tiempo de paso representado
como la velocidad media de un conductor en un trayecto con una longitud determinada.
La interpretación del funcionamiento de los radares es simple: si colocamos las
cámaras separadas 10 Km en un tramo cuya velocidad máxima es de 110 Km/h y un
conductor tarda 5 minutos en ser visto por la segunda cámara, sabremos que su
velocidad media ha sido de 120 Km/h, y por tanto, en algún sitio ha superado la
velocidad permitida. Usted hace parte del equipo de desarrollo encargado de
construir el software que procesará los datos registrados por las cámaras.

Su misión es crear un programa en Python que permita saber si un conductor debe
ser multado o no.

<table>
<tbody>
  <tr>
    <td>Entrada</td>
    <td>
      El programa recibirá 3 parámetros:<br>
      - La distancia en metros que separa dos cámaras<br>
      - La velocidad máxima permitida en ese tramo en km/h<br>
      - El tiempo en segundos que tarda el conductor en<br>&nbsp;&nbsp;recorrer el trayecto
    </td>
  </tr>
  <tr>
    <td>Salida</td>
    <td>
      El programa imprimirá una línea indicando si el conductor<br>
      debe ser multado o no. Se debe considerar lo siguiente:<br>
      - Imprimirá "OK" si el conductor no superó la velocidad<br>&nbsp;&nbsp;máxima.<br>
      - Imprimirá "MULTA" si se superó la velocidad máxima en<br>&nbsp;&nbsp;menos de un 20% de la velocidad permitida.<br>
      - Imprimirá "CURSO SENSIBILIZACION" si la velocidad<br>&nbsp;&nbsp;fue superada en un 20% o más de la velocidad permitida.<br>&nbsp;&nbsp;En este caso además de la multa deberá realizar un curso<br>&nbsp;&nbsp;sensibilización.<br>
      - Debido a que los sistemas pueden fallar y registrar valores<br>&nbsp;&nbsp;errados (por ejemplo, indicando que el tiempo que ha<br>&nbsp;&nbsp;tardado el conductor es negativo). En esos casos, se<br>&nbsp;&nbsp;deberá imprimir "ERROR".
    </td>
  </tr>
</tbody>
</table>
