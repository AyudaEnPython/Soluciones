Construir la función calcular_estadisticas que recibe un DataFrame
con la información de las descargas y retorna un DataFrame con las
estadísticas.

El DataFrame de entrada tendrá una fila con la información de cada
descarga: el nombre del modelo descargado, el nombre del usuario
que la descargó, el dinero en dólares que pagó por el modelo
(número decimal), la cantidad de estrellas (entre 1 y 5) que el
usuario le dio al modelo (número decimal) y si dejó o no un
comentario sobre el modelo después de haberlo descargado (valor
booleano). El precio de un modelo particular podría ser diferente
entre descargas porque la plataforma suele hacer promociones y
porque los artistas que los crean pueden modificar el precio
cuando ellos quieran. El precio podría ser 0 en algunas descargas,
pero esos registros no se deberá tener en cuenta.

El siguiente es un ejemplo de un DataFrame que muestra los nombres
de las columnas y posibles valores que puede haber en el DataFrame.

![Imagen 1](assets/img_1.jpg)

El DataFrame que retorna la función tiene que tener una fila por
cada modelo. El DataFrame tendrá 7 columnas: CANTIDAD, que tendrá
un número entero con la cantidad de descargas que haya tenido el
modelo; PROMEDIO, que tendrá un número decimal con la cantidad
promedio que se pagó por el modelo; MAXIMO que tendrá un número
decimal con la cantidad máxima que se pagó por el modelo; MINIMO
que tendrá un número decimal con la cantidad mínima que se pagó
por el modelo; ESTRELLAS, que tendrá un número decimal con la
cantidad promedio de estrellas que se le dio al modelo; DESV.
ESTRELLAS, que tendrá un número decimal con la desviación estándar
de la cantidad de estrellas que se le hayan dado al modelo; y
COMENTARIOS, que tendrá un número entero con la cantidad de
comentarios que hayan dejado los compradores.
El siguiente es el ejemplo del DataFrame con las estadísticas
calculado a partir del DataFrame de descargas mostrado arriba:

![Imagen 2](assets/img_2.jpg)

_Notas importantes sobre el DataFrame resultado_:

1. El índice del DataFrame tendrá los nombres de los modelos y
  sólo deben aparecer aquellos para los que al menos un usuario
  haya pagado. Es decir que no deben   aparecer los modelos que hayan
  sido siempre gratuitos.
2. Los modelos deben aparecer en orden alfabético de acuerdo a su nombre.
3. Todos los números que no sean enteros deben aparecer redondeados a
  dos cifras decimales.
4. Como la desviación estándar no se puede calcular cuando haya sólo
  un dato, en lugar de NaN debe aparecer 0.0 en el resultado.