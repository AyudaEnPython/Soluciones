# Proyecto Mi Red 3: Usando módulos

# Pregunta 1

Tras descargar y examinar los códigos "MiRedS4c-Funciones.py" y
"S4Red.py" selecciona de la lista la función permite llamar correctamente
a la función **obtener_mensaje()**, disponible en el archivo **S4Red.py**. 

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  import S4Red as Red
  msj = Red.obtener_mensaje()
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  from S4Red import obtener_mensaje
  msj = obtener_mensaje()
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  from S4Red import obtener_mensaje as el_estado
  msj = el_estado()
  ```
  <p>
  </detailes>

- [X] <details><summary>Ver código (respuesta correcta)</summary>
  <p>

  ```python
  import S4Red
  msj = S4Red.obtener_mensaje()
  ```
  <p>
  </detailes>

- [ ] <span>
  ```python
  import S4Red.py as LaRed
  msj = LaRed.obtener_mensaje()
  ```
  </span>

- [ ] <span>
  ```python
  import S4Red
  msj = obtener_mensaje()
  ```
  </span>

# Pregunta 2

Respecto al uso de módulos en MiRedS4c-Funciones.py, marque las alternativas
verdaderas.

- [ ] El programa puede importar a lo más un módulo.
- [ ] Los módulos importados deben tener código fuera de las funciones.
- [X] Este archivo utiliza solamente un módulo.
- [ ] Los módulos importados no pueden ser ejecutados.
