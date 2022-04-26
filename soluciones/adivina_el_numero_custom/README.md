# Enunciado Original

Usted y un grupo de amigos ha decidido realizar una rifa de 1'000.000 de pesos
para recaudar fondos en pro de los habitantes de calle del municipio en el que
usted habita.

La rifa se hará a través de un juego cuyas reglas son las siguientes:
- Cada participante debe adivinar un número `n` entre `0` y `b` (incluídos, `b`
  y `n` son los mismos para todos los concursantes).
- Cada concursante va ingresando números entre `0` y `b`, y mientras no haya
  acertado, el sistema debe decir si el número ingresado está por encima o por
  debajo del que debe adivinar.
- Una vez el concursante haya adivinado el número, el sistema deberá imprimir a
  los cuántos intentos el participante logró adivinar el número, y será el 
  jurado el encargado de dar como ganador a quien haya adivinado en menos
  intentos.

## Tareas

- Conocidos dos números `b` y `n` (Con las características mencionadas
  anteriormente) realizar un programa en Python que permita al concursante
  ingresar números entre `0` y `b` (incluídos los dos) hasta que adivine el
  número `n`, además en cada intento, el programa debe imprimir en consola lo
  siguiente:
  - Si el número ingresado por el concursante es mayor que `n`, entonces el
    programa debe imprimir **EXACTAMENTE** las siguientes palabras "¡Ups! Te
    pasaste" (Sin las comillas).
  - Si el número ingresado por el concursante es menor a `n`, entonces el
    programa debe imprimir **EXACTAMENTE** las siguientes palabras "¡Ups! Estás
    por debajo" (Sin las comillas).
  - Si el número ingresado por el concursante es igual a `n`, entonces el
    programa debe imprimir **EXACTAMENTE** las siguientes palabras "¡LO LOGRASTE!
    Usaste _x_ intentos" (Sin las comillas) donde `x` denota la cantidad de
    intenos que hizo el concursante para poder adivinar.
  - Si el número ingresado por el concursante es menor o mayor a `0` y `b`
    respectivamente, entonces el programa debe imprimir **EXACTAMENTE** las
    siguientes palabras "¡Te saliste del intervalo!" (No cuenta como intento).

> __*NOTA*__: Se opta por modificar el enunciado, el número aleatorio debería
> variar y no ser el mismo para todos los concursantes.