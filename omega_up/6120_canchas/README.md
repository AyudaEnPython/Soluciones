# 6120. [Canchas](https://omegaup.com/arena/problem/COMI-Canchas/)

<table style="margin-left: auto; margin-right: auto;">
<tbody>
  <tr>
    <td>Puntos</td>
    <td>12.21</td>
    <td>Limite de memoria</td>
    <td>32 MiB</td>
  </tr>
  <tr>
    <td>Límite de tiempo (caso)</td>
    <td>1s</td>
    <td>Límite de tiempo (total)</td>
    <td>1m0s</td>
  </tr>
  <tr>
    <td>Tamaño límite de entrada (bytes)</td>
    <td>10 KiB</td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

## Descripción

El director de la escuela necesita tu ayudas par redistribuir la cancha
de basket y de volley en el patio de la escuela. Ambas canchas ahora
serán rectángulos cuyas esquinas estarán en coordenadas enteras dentro
del nuevo patio.

El director te dará las coordenadas de las esquinas opuestas de cada
cancha nueva y quiere que calcules cuál será el área total del patio
que quedará cubierta por ambas canchas.

A pesar el tamaño del patio de la escuela, puede ser que ambas canchas
puedan encaminarse, por lo que deberás tomar eso en cuenta para no
contar contar dos veces el área.

## Tarea

Escribe un programa qu dadas las coordenadas de un par de esquinas
opuestas de cada cancha calcule el área total cubierta por ambas
canchas.

## Entrada

Tu programa deberá leer del teclado dos líneas, cada una con 4 números
enteros separados por un espacio que representan las coordenadas x1,
y1, x2, y2 de cada una de las canchas.

## Salida

Tu programa deberá escribir en la pantalla un único número que
represente el área total cubierta por ambas canchas.

## Ejemplo

|Entrada             |Salida|Descripción
|--------------------|------|:-:
|1 1 3 4 <br> 2 3 6 7|21|![img](/omega_up/6120_canchas/6120_img.png)



## Límites

0 <= x1, y1, x2, y2 <= 10,000

---


`main.py`
```python
#!/usr/bin/python3

def _main() -> None:
    # TODO: fixme.
    pass

if __name__ == '__main__':
    _main()
```