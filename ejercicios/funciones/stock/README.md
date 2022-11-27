# Enunciado Original

Funciones:

a. Programar una función llamada **disminuir_stock** sin retorno que tome dos
  parámetros: una String (variedad) y el diccionario **datos**. De acuerdo a la
  variedad informada disminuir el stock respectivo en **1 (una) unidad**.

Programa principal:

b. Declarar el diccionario **datos** con los siguientes valores iniciales:
  
  | {Variedad: | [Precio, | Stock]} |
  |------------|----------|---------|
  | ipa        | 1.4      | 10      | 
  | pils       | 1.2      | 50      | 
  | amber      | 1.1      | 100     | 

  **Ejecutar una instrucción print** con el diccionario como parámetro.

c. Solicitar al usuario dos inputs: la variedad que desea tomar, con el mensaje:
  "Ingrese la variedad: " y la cantidad con el mensaje "Ingrese la cantidad: ".
  Almacenar estos inputs en correspondientes variables.

d. En base a la variedad ingresada y la cantidad solicitada, disminuir el stock
  utilizando la función **disminuir_stock**, obtener el precio por unidad consultando
  el diccionario y acumular el costo (precio * cantidad) en una variable llamada **total**.

e. Ciclar infinitamente entre los items d) y e) hasta que el usuario ingrese una
  variedad inexistente (es decri, una String que no corresponda con ninguna llave del
  diccionario). En cada iteración acumular el costo en **total**.

f. Informar el total de la cuenta, acumulando en la variable **total**, con el mensaje
  "Total=$ ". Seguido del total **redondeado hacia abajo**. Es decir: si el total es 9.9,
  se deberá informar en total de 9, si el total es de 25.2 se deberá informar 25.

g. Ejecutar una instrucción print con el diccionario **datos** como parámetro.

_Ejemplo de funcionamiento esperado:

    {'ipa': [1.4, 40], 'pils': [1.2, 50], 'amber': [1.1, 100]}
    Ingrese la variedad: ipa
    Ingrese la cantidad: 5
    Ingrese la variedad: amber
    Ingrese la cantidad: 2
    Ingrese la variedad: pils
    Ingrese la cantidad: 1
    Ingrese la variedad: salir
    Total: 10
    {'ipa': [1.4, 35], 'pils': [1.2, 49], 'amber': [1.1, 98]}

*** 5 ipa cuestan 7, 2 amber cuestan 2.2 y una pils cuesta 1.2, por un total de 10.4,
redondeado hacia abajo es un total de 10. Los stocks después de la venta disminuyen
acorde a las variedades vendidas.

> __**NOTA**__: El enunciado contiene varias partes erradas, se opta por rediseñar.
