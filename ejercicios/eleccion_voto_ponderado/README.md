# Enunciado Original

**Construya un programa en Python que realice el proceso completo de la
elección de voto ponderado** realizando los procesos de solicitar las
opciones de voto, el ingreso y validación de los sufragios, y el cálculo
de los resultados, cumpliendo con las necesidades que a continuación se
mencionan. Considere para su desarollo que cada ejecución del programa
correspondería a una elección distinta.

Un mecanismo usado en distintos sistemas eleccionarios en el mundo es el
**voto ponderado**. En este caso, el valor de cada voto depende de la
representatividad o el "peso" de cada representante, es decir, el voto de
un representante vale una cantidad determinada de votos, a diferencia del
voto popular, dónde todos los votos valen los mismo. Procedimientos de este
estilo se pueden ver en algunos parlamentos del mundo y son comunes también
en organizaciones estudiantiles universitarias, donde individuos de distintas
carreras representan a universos de estudiantes de distinto tamaño.

Una universidad de la Región Metropolitana busca implementar el voto ponderado
tanto para su congreso triestamental como para su federación de estudiantes,
desea una herramienta de apoyo tecnológico que permita manejar el proceso del
cálculo de resultados para el voto ponderado. Para elloo ha definido las
siguientes necesidades (o requerimientos):

- El programa debe evitar que un representante pueda votar más de una vez en
  una misma elección.
- El programa debe solicitar al usuario las opciones de voto en una lista de
  elementos, por ejemplo: ['A FAVOR', 'EN CONTRA'] o ['ALEJANDRA PÉREZ', 
  'CLAUDIA GONZÁLEZ', 'JUAN ZARATE', 'PEDRO MÉNDEZ'].
- En todo proceso de sufragio es posible de abstenerse de votar ("voto en
  blanco") o emitir el voto de manera incorrecta ("voto nulo"), por lo que su
  programa debe considerar, para cualquier proceso de votación, estas dos
  opciones adicionales de voto.
- El programa debe calcular los resultados de la elección y mostrar, para cada
  opción de voto, la cantidad de votos obtenidos y el porcentaje que esta
  representa del total de votos emitidos.
- Cada representante emite su voto identificando a quién representa (string en
  mayúsculas), cuál es su opción escogida en la votación (string en mayúsculas)
  y el valor de su voto (entero positivo). Por ejemplo, si el representante de
  Ingeniería Civil en Telecomunicaciones vota a favor en una votación en particular
  y su voto representa a 233 estudiantes, entonces se deben ingresar al programa
  estos tres datos para emitir el voto: o 'INGENIERÍA CIVIL EN TELECOMUNICACIONES'
  o 'A FAVOR' o 233.
- Cada grupo de personas tiene un único representante, por lo que más de un voto
  emitido por una misma entidad correspondería a un error y el programa debería
  informarlo. Solo se debe contabilizar el primer voto de una entidad.
- Se debe validar que cada voto cumpla con el formato especificado y considere
  opciones de voto válidas. Cualquier voto contabilizado que no respete el formato
  solicitado debe ser considerado nulo.

> *__NOTA__*: Se opta por mejorar algunos aspectos.
