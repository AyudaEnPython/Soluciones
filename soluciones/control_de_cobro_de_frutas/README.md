# Enunciado Original

## Control de cobro de frutas

La dinámica es que el cajero de un negocio donde venden frutas utiliza un pequeño
programa para sumar todos los productos que compra un cliente basándose en su
cantidad en kilos y su precio por kilo.

El programa tiene un Menú en donde tiene opciones sobre cada producto que se compra.
Cada producto tiene su precio por kilo ya establecido.

|Articulo|Precio x kilo|
|--------|-------------|
|Tomate  |         750 |
|Yuca    |         900 |
|Papa    |         550 |
|Sandia  |       1.200 |

- Después de ingresar el primer producto se debe controlar si se necesita ingresar otro
  producto.
- Si la cantidad a pagar es de más de 10.000 el cliente obtiene un 5% de descuento.
- Si no se van a ingresar más productos entonces se le indica cual es el monto final por
  todos los artículos.
- Se pide el monto de dinero con el cual el cliente desea pagar y comprobar si éste alcanza,
  sino volverle a pedir el dinero al cliente hasta que sea suficiente.
- Al final mostrar la cantidad de productos comprados en total, con cuanto pagó el cliente
  y su vuelto.

**Por ejemplo**: Por la compra de los N productos el total a pagar es de N, el pago fue de N y
el vuelto es de N. Gracias por su compra.

Puede comprobar con los siguientes datos:

**Con Descuento:**

<table>
<thead>
  <tr>
    <th>Articulo</th>
    <th>Cantidad</th>
    <th>Precio</th>
    <th>Subtotal</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Sandia</td>
    <td>2</td>
    <td>1200</td>
    <td>$ 2400,00</td>
  </tr>
  <tr>
    <td>Papa</td>
    <td>4</td>
    <td>550</td>
    <td>$ 2200,00</td>
  </tr>
  <tr>
    <td>Yuca</td>
    <td>3</td>
    <td>900</td>
    <td>$ 2700,00</td>
  </tr>
  <tr>
    <td>Tomate</td>
    <td>5</td>
    <td>750</td>
    <td>$ 3750,00</td>
  </tr>
  <tr>
    <td colspan="3">Subtotal</td>
    <td>$ 11050,00</td>
  </tr>
  <tr>
    <td colspan="3">Descuento</td>
    <td>$ 553</td>
  </tr>
  <tr>
    <td colspan="3">Total</td>
    <td>$ 10 497,50</td>
  </tr>
</tbody>
</table>

**Sin Descuento:**

<table>
<thead>
  <tr>
    <th>Articulo</th>
    <th>Cantidad</th>
    <th>Precio</th>
    <th>Subtotal</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Sandia</td>
    <td>2</td>
    <td>1200</td>
    <td>$ 2400,00</td>
  </tr>
  <tr>
    <td>Papa</td>
    <td>4</td>
    <td>550</td>
    <td>$ 2200,00</td>
  </tr>
  <tr>
    <td>Yuca</td>
    <td>3</td>
    <td>900</td>
    <td>$ 2700,00</td>
  </tr>
  <tr>
    <td>Tomate</td>
    <td>5</td>
    <td>750</td>
    <td>$ 3750,00</td>
  </tr>
  <tr>
    <td colspan="3">Subtotal</td>
    <td>$ 11050,00</td>
  </tr>
  <tr>
    <td colspan="3">Descuento</td>
    <td>$ 553</td>
  </tr>
  <tr>
    <td colspan="3">Total</td>
    <td>$ 10 497,50</td>
  </tr>
</tbody>
</table>

> __**NOTA**__: el enunciado no es claro en cuanto al menu.
