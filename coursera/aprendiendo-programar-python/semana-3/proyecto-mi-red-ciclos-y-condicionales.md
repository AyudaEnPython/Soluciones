# Proyecto Mi Red: Ciclos y condicionales

## Pregunta 1

Tras ejecutar el código "MiRedS3-Ciclos" y realizar los ejercicios propuestos,
marca las opciones que son verdaderas.

- [X] Si se agrega la línea **continuar = True** dentro de las instrucciones
  asociadas al **if**, el programa se comporta de la misma manera.

- [X] El programa permite mostrar múltiples estados del usuario, mientras éste
  ingrese "S", "s", o nada en la instrucción de input.

- [ ] Si el usuario ingrese una opción distinta "S", "s", o un texto vacío, el
  programa vuelve a consultar si el usuario desea escribir un mensaje.

- [ ] El programa termina solamente cuando se ingresa "N", ó "n"

- [ ] En cada repetición (iteración) del ciclo, el programa solicita al usuario
  que ingrese sus datos (_nombre_, _edad_, _estatura_, etc) nuevamente.


## Pregunta 2

Si, en el código presentado, reemplazamos las líneas

```python
    else:
        continuar = False
```

por

```python
    continuar = False
```

(Atención a la indentación mostrada)

Marque las opciones verdaderas

- [ ] El programa se comporta de la misma manera.

- [ ] El programa nunca sale ciclo

- [ ] El programa nunca entra el ciclo

- [ ] El programa genera un error y no termina su ejecución.

- [X] El programa solo permite mostrar un mensaje y luego termina.

## Pregunta 3

Pregunta 3

El programa presentado termina cuando el usuario, al preguntársele si desea
escribir un mensaje, ingresa algo que no es "_S_", "_s_", ni el string vacío "".\
<br>
Supongamos que queremos modificar el programa de manera que termine **solamente**
cuando el usuario ingrese "N" ó "n", ¿cuáles de las siguientes modificaciones
al ciclo **while** cumplen ese objetivo?

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  while continuar:
      #Solicitamos opción al usuario
      escribir = str(input("¿Deseas escribir un mensaje? (S/N) "))
      if escribir == "S" or escribir == "s" or escribir == "":
          mensaje = input("¿Qué piensas hoy? ")
          print(nombre, "dice:", mensaje)
      if escribir == "N" or escribir == "n":
          continuar = False
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  while continuar:
      #Solicitamos opción al usuario
      escribir = str(input("¿Deseas escribir un mensaje? (S/N) "))
      if escribir == "S" or escribir == "s" or escribir == "":
          mensaje = input("¿Qué piensas hoy? ")
          print(nombre, "dice:", mensaje)
      elif escribir == "N" or escribir == "n":
          continuar = False
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  while continuar:
      #Solicitamos opción al usuario
      escribir = str(input("¿Deseas escribir un mensaje? (S/N) "))
      if escribir == "S" or escribir == "s" or escribir == "":
          mensaje = input("¿Qué piensas hoy? ")
          print(nombre, "dice:", mensaje)
      if escribir == "N" or escribir == "n" or escribir == "":
        continuar = False
  ```
  </span>

- [ ] <span>
  ```python
  while continuar:
      #Solicitamos opción al usuario
      escribir = str(input("¿Deseas escribir un mensaje? (S/N) "))
      if escribir == "S" or escribir == "s" or escribir == "":
          mensaje = input("¿Qué piensas hoy? ")
          print(nombre, "dice:", mensaje)
      if not(escribir == "S" or escribir == "s" or escribir == ""):
          continuar = False
  ```
  </span>

- [ ] <span>
  ```python
  while continuar:
      #Solicitamos opción al usuario
      escribir = str(input("¿Deseas escribir un mensaje? (S/N) "))
      if escribir == "S" or escribir == "s" or escribir == "":
          mensaje = input("¿Qué piensas hoy? ")
          print(nombre, "dice:", mensaje)
  continuar = False
  ```
  </span>

- [ ] <span>
  ```python
  while continuar:
      #Solicitamos opción al usuario
      escribir = str(input("¿Deseas escribir un mensaje? (S/N) "))
      if escribir == "S" or escribir == "s" or escribir == "":
          mensaje = input("¿Qué piensas hoy? ")
          print(nombre, "dice:", mensaje)
      else escribir == "N" or escribir == "n":
          continuar = False
  ```
  </span>

- [ ] <span>
  ```python

  ```
  </span>

## Pregunta 4

El programa presentado otorga solamente dos opciones al usuario: escribir un
mensaje o salir, por lo tanto basta con una variable de tipo _bool_.\
<br>
De las siguientes alternativas, ¿cuáles permiten que el usuario escoja entre 3
opciones, de las cuales **solamente** la opción 0 permite salir del ciclo?\
<br>
Nota: se ha omitido parte del código para hacerlo más legible

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  opcion = -1
  while opcion != 0:
      opcion = int(input("Elija opcion 1, 2 o 0 (salir):"))
      if opcion != 0:
          if opcion == 1:
            print("Ejecutamos la opcion 1")
          elif opcion == 2:
            print("Ejecutamos la opcion 2")
      else:
          print("Has decidido salir.")
  ```
  <p>
  </detailes>


- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  opcion = -1
  while opcion != 0:
      opcion = int(input("Elija opcion 1, 2 o 0 (salir):"))
      if opcion == 1:
          print("Ejecutamos la opcion 1")
      elif opcion == 2:
          print("Ejecutamos la opcion 2")
      elif opcion == 0:
          print("Has decidido salir.")
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  opcion = -1
  while opcion != 0:
      opcion = int(input("Elija opcion 1, 2 o 0 (salir):"))
      if opcion == 0:
          print("Has decidido salir")
      if opcion == 1:
          print("Ejecutamos la accion 1")
      elif opcion == 2:
          print("Ejecutamos la accion 2")
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  opcion = 0
  while opcion != 0:
      opcion = int(input("Elija opcion 1, 2 o 0 (salir):"))
      if opcion == 1:
          print("Ejecutamos la opcion 1")
      elif opcion == 2:
          print("Ejecutamos la opcion 2")
      elif opcion == 0:
          print("Has decidido salir.")
  ```
  </span>

- [ ] <span>
  ```python
  opcion = 0
  while opcion == 0:
      opcion = int(input("Elija opcion 1, 2 o 0 (salir):"))
      if opcion == 1:
          print("Ejecutamos la opcion 1")
      elif opcion == 2:
          print("Ejecutamos la opcion 2")
      elif opcion == 0:
          print("Has decidido salir.")
  ```
  </span>

- [ ] <span>
  ```python
  opcion = -1
  while opcion != 0:
      opcion = int(input("Elija opcion 1, 2 o 0 (salir):"))
      if opcion == 1:
          print("Ejecutamos la opcion 1")
      elif opcion == 2:
          print("Ejecutamos la opcion 2")
      else:
          print("Has decidido salir.")
          opcion = 0
  ```
  </span>
