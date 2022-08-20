# Proyecto Mi Red: Usando archivos

# Pregunta 1

Tras examinar, ejecutar y resolver los ejercicios en el código "MiRedS5-Archivos.py",
responde a las siguientes preguntas. Marca las alternativas verdaderas.

- [X] El archivo con extensión .user es un archivo de texto.
- [ ] El programa escribe datos en el archivo nuevo a medida que el usuario los va ingresando por el teclado.
- [X] El programa sabe que un usuario ya existe porque hay un archivo con ese nombre.
- [ ] El programa requiere que el archivo de cada usuario exista antes de poder funcionar.

# Pregunta 2

Respecto a las razones por las cuales los datos leídos desde el archivo incluyen el
carácter de cambio de línea ('\**n**') al leerlos desde un archivos, marca las
alternativas totalmente correctas.

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  pais = archivo.readline()
  pais = pais.rstrip()
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  pais = archivo.readline().rstrip()
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  pais = pais[0:len(pais)-1]
  ```
  </span>

- [ ] <span>
  ```python
  pais = archivo.readline()
  pais.rstrip()
  ```
  </span>

- [ ] <span>
  ```python
  pais = archivo.rstrip().readline()
  ```
  </span>

# Pregunta 3

¿Cómo encapsularías el código para escribir tres valores a un archivo, de manera
que cada uno quede en una línea distinta?
<br><br>
Marca las funciones que permiten hacer esto de manera correcta.

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def escribir_archivo(nombre, edad, pais):
      archivo_usuario = open(nombre+".user","w")
      archivo_usuario.write(nombre+"\n")
      archivo_usuario.write(str(edad)+"\n")
      archivo_usuario.write(pais+"\n")
      archivo_usuario.close()
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  def escribir_archivo(nombre, edad, pais):
      archivo_usuario = open(nombre+".user","w")
      archivo_usuario.write(nombre+"\n"+str(edad)+"\n"+pais+"\n")
      archivo_usuario.close()
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  def escribir_archivo(nombre, edad, pais):
      archivo_usuario = open(nombre+".user","w")
      archivo_usuario.write(nombre)
      archivo_usuario.write(str(edad))
      archivo_usuario.write(pais)
      archivo_usuario.close()
  ```
  </span>

- [ ] <span>
  ```python
  def escribir_archivo(nombre, edad, pais):
      archivo_usuario = open(nombre+".user","r")
      archivo_usuario.write(nombre+"\n")
      archivo_usuario.write(str(edad)+"\n")
      archivo_usuario.write(pais+"\n")
      archivo_usuario.close()
  ```
  </span>
