# PROBLEMA: LA BOLETA DEL SUPERMERCADO

## CONTEXTO

Mr. Oso, dueño del OXSO, necesita una solución que le permita calcular
rápidamente el total de una boleta y aplicar descuentos a sus clientes según
ciertos criterios (Cliente Frecuente, Lunes de Carnes, Martes Vegano, etc.).
Sin embargo, los lectores con los que su cajeros escanean los precios, no son
necesariamente los mejores y esto le ha traído muchas dificultades, por lo que
le han pedido a usted que con su experticia en Python resuelva el problema del
supermercado.

## PROBLEMA

Cada vez que los cajeros del OXSO escanean un producto, se ingresa como entrada
un string de la forma
`'nombre_producto, tipo_producto, precio_unitario_cantidad'`. Donde:

- `nombre_producto` es el nombre del producto comprado.
- `tipo_producto` es la categoría a la que pertenece.
- `precio_unitario` es el valor de una unidad del producto, sin considerar el
  valor del _impuesto al consumo_.
- `cantidad` es la cantidad de dicho elemento que compra.

Por ejemplo, el string: `'Fruna Carioca, galletas, 500, 20,'`, indicaría que el
cliente está comprando 20 galletas Carioca, con un precio sin IVA de $500 cada
una.

Una vez que el cajero ha ingresado todos los elementos, escribe `'FIN LECTURA'`
en el terminal para pasar a calcular el total de la boleta.

Para esto, en primer lugar se debe calcular el impuesto al consumo de cada
producto, el cuál corresponde a un 20% para todos los productos, más un
5% adicional para productos de las categorías
`'vinos'`, `'cigarros'`, `'bebidas alcohólicas'` y `'cosas de furros'`. Es
decir, los productos de estas cuatro categorías tienen un impuesto de 25%.

Luego de ello, se ingresan los descuentos. En OXSO existen dos formas distintas
de descuentos:

- Descuento por tipo de producto: en donde cierto día, un tipo de producto está
  con un porcentaje de descuento. Por ejemplo: Lunes de carnes, donde todos los
  productos de la categoría `'carnes'`, están con 10% de descuento.

- Descuento al total de la boleta: en donde se indica la razón del descuento y
  este se aplica al total de la boleta. Por ejemplo, el programa de amigos de
  Mr. Oso, otorga un 5% en el total de la compra a personas con el substring
  `'oso'` en su apellido.

Para el caso del descuento por tipo de producto, el cajero ingresa el descuento
en el formato `'tipo_descuento, tipo_producto, porcentaje_descuento'`, dónde:

- `tipo_descuento`: será siempre en este caso por producto.
- `tipo_producto`: corresponde al tipo de producto al que se aplica el descuento.
- `porcentaje`: corresponde al porcentaje de descuento a aplicar.

Por ejemplo: el string `'producto, verduras, 10'` estaría generando un 10% de
descuento sobre todos los productos de la categoría verduras.

Para el caso del descuento por total de la boleta, el cajero ingresa el
descuento en el formato `'tipo_descuento, motivo, porcentaje descuento'` dónde:

- `tipo_descuento`: será siempre en este caso al total.
- `motivo`: corresponde al motivo por el cuál se aplicó el descuento (programa
  de amigos de Mr. Oso, Cliente Frecuente, Cajera/o atendió a un/a amigo/a de
  toda la vida, etc.).
- `porcentaje`: corresponde al porcentaje de descuento a aplicar.

Por ejemplo: el string `'al total, amiga/o del cajero, 10'` estaría generando
un 10% de descuento al total de la boleta, porque la/el cajera/o estaba
atendiendo a un/a amigo/a. ~~Mr. Oso verá después que hace con ese cajera/o~~.

Una vez ingresados los descuentos, el cajero ingresa `'FIN DESCUENTOS'` y el
programa debería calcular y entregar:

- Cuánto se ahorra por cada descuento.
- El valor del total de la boleta con impuestos.
- La cantidad de OSO puntos acumulados, dónde 100 pesos equivale a 1 OSOpunto.

Considere para su solución que el programa deberá validar que las entradas
estén correctamente formateadas, es decir:

- Que el string con los productos tenga únicamente 4 campos.
- Que los campos precio unitario y cantidad sean enteros positivos mayores o iguales a 1.
- Que el string con los descuentos tenga únicamente 3 campos.
- Que los descuentos siempre sean un valor entero positivo entre 0 y 99.

En caso de que alguna línea sea ingresada con error debe indicarse el mensaje:

    Error de ingreso en <producto/descuento>: <N° linea con error>

Considerando que siempre se partirá contando desde 1, tanto en productos como en descuentos.

## ENTRADA

Se recibirán tantas líneas con productos como el cliente desee, todas en el
formato indicado (aunque podrían tener los errores indicados arriba), hasta que
el cajero ingrese `'FIN LECTURA'`.

Luego, se ingresarán tantos descuentos como el cajero desee, todos en el formato
indicado (aunque podrían tener los errores indicados arriba), hasta que el
cajero ingrese `'FIN DESCUENTOS'`.

En ningún caso las líneas requieren un texto en el `input()` para pedirse. Por
ejemplo:

    Fruna Carioca, galletas, 500, 20
    Monster Zero Blanca, bebidas energeticas, 1100, 20
    Pillows Cereal 1 Kg., cereales, 4700, 3
    FIN LECTURA
    por producto, galletas, 3
    al total, descuento por gamer, 10
    al total, descuento por ser amante de las mascotas, 5

Es una entrada válida, y sin errores.

## SALIDA

Si las entradas son correctas, se entregará una linea con el ahorro generado por
cada descuento en el formato:

    Con el descuento '<motivo/tipo_producto>' te ahorraste $<valor>

Luego una linea indicando el total en el formato:

    El total de su boleta es de $<valor>, impuestos incluidos

Para finalizar una línea informando de los OSO puntos acumulados por esta compra:

    Esta compra acumula <total OSOpuntos> oso puntos

Y una última línea de despedida:

    Gracias, vuelva prontos

Por ejemplo:

    Con el descuento 'galletas' te ahorraste $100
    Con el descuento 'descuento por gamer' te ahorraste $2430
    Con el descuento 'descuento por ser amante de las mascotas' te ahorraste $323
    El total de su boleta es de $35461.3, impuestos incluidos
    Esta compra acumula 354 oso puntos.
    Gracias, vuelva prontos

Si alguna de las entradas fuera incorrecta deberá responder con el texto:

    Error de ingreso en <producto/descuento>: <N° de linea con error>

Por ejemplo:

    Error de ingreso en producto: 2

En caso de errores, el programa debería informarlos, pero hacer el cálculo de
todos modos, ignorando las entradas erróneas.

## RESTRICCIONES

- En caso de errores, el programa deberá informar de todos los que ocurren e
  ignorarlos para seguir calculando.
- El cajero puede ingresar descuentos sobre productos que el cliente no ha comprado.
