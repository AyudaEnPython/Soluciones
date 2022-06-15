# Enunciado Original

Dada una colección de N textos que se introducen por teclado, usted
debe contar la cantidad de correos electrónicos válidos que existen.
Puede asumir con seguridad que nunca un correo será una sub-cadena, sino
que siempre viene como el texto introducido completo.

Una dirección email es válida si cumple los siguientes requisitos:

- El nombre de usuario es válido.
- Aparece un arroba "@" luego del nombre de usuario.
- Tiene un dominio válido.

Un nombre de usuario es válido si comienza por letras, solo incluye letras
minúsculas (ojo que usted puede forzarla) y números, no posee caracteres
especiales y su longitud debe estar entre 5 y 20 caracteres.

Un dominio es válido si se compone de dos o más textos separados por ".",
cada uno de esos textos tiene una longitud de 2 a 5 letras minúsculas.

---

Proponga una solución en Python para este problema que utilice funciones.
A continuación se muestra un ejemplo y salida esperada en Python.

Hint: 
- Puede usar la función `find`, que retorna la posición inicial de sub-cadena
  en el texto y -1 si no aparece:

      pos = str("Hola mundo cruel").find("mundo")

  `pos = 5`, pero `pos = -1` si buscamos la `"z"`.


Entradas:

    N = 5

    "Hola mundo cruel"
    "pepe234@abs.erty.es"
    "usuariovalido1@abcdef.erty.es"
    "juanitoperezmartinex234@cuart.ter.cl"
    "juanito!@google.com"
    "3nombre@uft.edu"

Salida:

    2


> __**NOTA**__: El enunciado fue modificado para mejorar la legibilidad del mismo.
> Las entradas deberían ser 6 y no 5. Además, la salida debería ser 1, solo "pepe234"
> sería un correo válido; "usuariovalido1" tiene un dominio de más de 5 caracteres
> ("abcdef").
