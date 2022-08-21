# Proyecto Mi Red: Archivos y módulos

# Pregunta 1

Tras examinar, ejecutar y resolver los ejercicios en el código "MiRedS5b-Archivos.py"
y "S5Red2.py", responde a las siguientes preguntas. Marca las alternativas verdaderas.

 - [X] Si queremos modificar la manera en que se leen los datos, por ejemplo, considerar
   todos los nombres con letras mayúsculas, debemos modificar la función leer_usuario
   definida en el módulo S5Red2.py, sin necesidad de modificar el archivo principal.

 - [ ] Si agregamos, usando un editor de texto, una nueva línea al final del
   archivo ".user", ésta será leída por el programa.

 - [ ] Si omitimos el llamado a la función escribir_usuario() en el código principal,
   y el usuario ya existía, el programa sigue comportándose de la misma manera, ya que
   al ingresar con el mismo usuario, se cargarán los datos ya existentes desde el
   archivo ".user".

 - [X] Es posible leer archivos que no hayan sido creados mediante el programa, sino
   que hayan sido modificados con un editor de textos o con otro programa externo.

 - [X] La función escribir_usuario() recibe un parámetro por cada dato del perfil del
   usuario que queremos almacenar.

# Pregunta 2

Supongamos que agregamos un opción número 5 al menú con este código:

```python
elif opcion==5:
  nuevo_nombre = intput("¿A que perfil quieres cambiar?")
  (nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado) = Red.cambiar_usuario(nuevo_nombre)
```
De las siguientes alternativas, ¿cuáles permiten implementar la función
**cambiar_usuario(nombre)**, la cual cambia el perfil a un usuario nuevo en
caso que el archivo correspondiente a ese usuario exista?

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def cambiar_usuario(nombre):
      if existe_archivo(nombre + ".user"):
          return leer_usuario(nombre)
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def cambiar_usuario(nuevo_nombre):
      if existe_archivo(nuevo_nombre + ".user"):
          return leer_usuario(nuevo_nombre)
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def cambiar_usuario(nombre):
      if existe_archivo(nombre + ".user"):
          archivo_usuario = open(nombre+".user","r")
          nombre = archivo_usuario.readline().rstrip()
          edad = int(archivo_usuario.readline())
          estatura = float(archivo_usuario.readline())
          estatura_m = int(estatura)
          estatura_cm = int( (estatura - estatura_m)*100 )
          sexo = archivo_usuario.readline().rstrip()
          pais = archivo_usuario.readline().rstrip()
          num_amigos = int(archivo_usuario.readline())
          estado = archivo_usuario.readline().rstrip()
          archivo_usuario.close()
          return (nombre, edad, estatura_m, estatura_cm, sexo, pais, num_amigos, estado)
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  def cambiar_usuario(nombre):
      if existe_archivo(nombre):
          return leer_usuario(nombre)
  ```
  </span>

- [ ] <span>
  ```python
  def cambiar_usuario(nombre):
      return leer_usuario(nombre)
  ```
  </span>
