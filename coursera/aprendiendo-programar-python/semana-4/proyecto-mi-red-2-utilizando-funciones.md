# Proyecto Mi Red: Utilizando funciones

# Pregunta 1

Tras descargar, examinar, ejecutar y realizar los ejercicios del código
"MiRedS4b-Funciones.py", marca las alternativas verdaderas: 

- [X] Variables como **metros** y **estatura** no pueden ser leídas dentro del
  código principal (por ejemplo dentro del while), posteriormente a la
  ejecución de la función **obtener_estatura()**.

- [X] La función **mostrar_bienvenida()** no recibe parámetros.

- [ ] Todas las funciones creadas retornan un valor

- [ ] La función **mostrar_perfil()** entrega como resultado, es decir,
  **RETORNA** el texto con los datos del usuario.

- [ ] En la función **opcion_menu()** podríamos eliminar la instrucción
  **return opcion**, ya que esta variable existe fuera de la función, por ejemplo,
  dentro del ciclo **while**

# Pregunta 2

Para evitar múltiples llamados a funciones, podemos agregar una función que se
llame **obtener_datos()**, y que se encargue de obtener los datos del usuario.\
<br>
A partir del código presentado, cuál de las siguientes alternativas implementa
correctamente la función **obtener_datos()**?\
<br>
_Hint: Puedes probar este código en tu implementación_

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def obtener_datos():
      nombre = obtener_nombre()
      edad = obtener_edad()
      (est_m, est_c) = obtener_estatura()
      num_amigos = obtener_num_amigos()
      return (nombre,edad,est_m,est_c,num_amigos)
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  def obtener_datos(nombre,edad,est_m,est_c,num_amigos):
      nombre = obtener_nombre()
      edad = obtener_edad()
      (est_m, est_c) = obtener_estatura()
      num_amigos = obtener_num_amigos()
      return (nombre,edad,est_m,est_c,num_amigos)
  ```
  </span>

- [ ] <span>
  ```python
  def obtener_datos():
      nombre = obtener_nombre()
      edad = obtener_edad()
      (est_m, est_c) = obtener_estatura()
      num_amigos = obtener_num_amigos()
      return nombre
      return edad
      return est_m
      return est_c
      return num_amigos
  ```
  </span>
