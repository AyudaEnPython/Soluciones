# Ejercicios

## Repaso

- Escriba una clase Python, Flower, que tiene tres propiedades de tipo
  str, int y float, que respectivamente representa el nombre de la flor,
  su cantidad de pétalos y su precio. La clase debe incluir un método
  constructor que inicialice cada variable con su valor apropiado, y la
  clase debe incluir métodos para establecer el valor de cada propiedad
  y recuperar el valor de cada propiedad.

- Modifique los métodos cargar y pagar de la clase TarjetaCredito
  de forma que se asegure que al llamarlos se les envíe un número como
  parámetro.

- Si el parámetro para el método pagar de la clase TarjetaCredito fue
  un número negativo, tendría el efecto de subir el balance de la cuenta.
  Revisa la implementación de este método de forma que se origine un
  ValueError si se envía un valor negativo.

- La clase TarjetaCredito inicializa el balance de una cuenta nueva a
  cero. Modifica la clase de modo que una nueva cuenta se pueda
  inicializar con un valor diferente de cero usando un quinto parámetro
  opcional del constructor. La sintaxis de cuatro parámetros del
  constructor debe continuar produciendo un cuenta con balance cero.

- Modifique el método __sub__ para la clase Vector, de forma que la
  expresión u-v devuelva una instancia de vector representando la
  diferencia entre dos vectores.

- Implemente el método __neg__ para la clase Vector, de forma que la
 expresión –v devuelva una nueva instancia de vector en la cual las
 coordenadas son el negativo de las respectivas coordenadas de v.

- Implemente el método __mul__ para la clase Vector, de forma que la
 expresión v*3 devuelva una nueva instancia de vector con coordenadas
 que son 3 veces las respectivas coordenadas de v

- Implemente el método __mul__ para la clase Vector, de forma que la
  expresión u*v devuelva un escalar que represente el producto punto de
  los vectores, esto es <img src="https://render.githubusercontent.com/render/math?math=\sum_{i=1}^{d} u_{i}.v_{i}">

- La clase Vector proporciona un constructor que toma un entero d, y
  produce un vector d-dimensional con todas las coordenadas iguales a 0.
  Otra forma conveniente de crear un nuevo vector sería enviar al
  constructor un parámetro que es un iterable que represente una
  secuencia de números, y se cree un vector con iguales dimensiones a la
  longitud de la secuencia y coordenadas iguales a os valores de la
  secuencia. Por ejemplo, Vector([4, 5, 7]) produciría un vector
  tridimensional con coordenadas <4, 5, 7>. Modifique el constructor
  de la clase Vector, de forma que ambas formas sean aceptables, es decir
  que si se le envía un número único produzca un vector de esta dimensión
  con ceros en las coordenadas, pero si se le envía una secuencia de
  números, produzca un vector con las coordenadas en base a la
  secuencia.

## Creatividad

- La clase TarjetaCreditoDepredadora proporciona un método
  proceso_mensual que modele el cierre de un ciclo mensual.
  Modifique la clase de forma que cuando un cliente hace diez llamadas
  al método cargar en el mes actual, cada llamada adicional a la función
  resulte en un cargo de $1.

- Modifique la clase TarjetaCreditoDepredadora de forma que a un
 cliente le es asignado un pago mínimo mensual, como un porcentaje del
 balance, de esta forma se le carga un impuesto por mora si el cliente no
 paga el monto mínimo antes del siguiente ciclo mensual.

- Implemente un método _set_balance(b) para la clase
  TarjetaCredito, de modo que pueda ser usada por las clases
  derivadas, sin que esta tenga que acceder directamente al miembro de
  datos _balance.

## Proyecto

- Desarrolle herencia jerárquica en base a una clase Poligono que tiene
  métodos abstractos area() y perímetro(). Implemente la clase
  Triangulo, Cuadrilatero, Pentagono, Hexagono, y Octagono que
  extienda esta clase base, con los métodos area() y perímetro().
  También implemente la clase TriaguloIsosceles,
  TrianguloEquilatero, Rectangulo y Cuadrado, que tienen las
  relaciones de herencia apropiadas. Finalmente escriba un programa
  sencillo que permita a los usuarios crear polígonos de varios tipos
  introduciendo sus dimensiones geométricas y el programa muestre el
  área y el perímetro.