# Enunciado Original

- Buscar una librería que de soporte a llmadas HTTP.
- El API a utilizar será el API para testing https://jsonplaceholder.typicode.com/.
- El fichero Python se llamará main.py
- Recibirá los siguientes parámetros:
  - **method**: obligatorio. Método que se usará para llamar al API. los
    posibles valores serán GET, POST, PUT, DELETE.
  - **resource**: obligatorio: Recurso sobre el que se realiza la operación.
    los posibles valores serán post y comments.
  - **resource_id**: opcional en el método GET y obligatorio en los métodos
    PUT y DELETE. Identificador único del recurso.
- El programa invocará al API con el método y recurso pasado por parámetros. En
  la petición GET, si se informa el identificador único, se utilizará para obtener
  dicho recurso.
- Para las peticiones POST y GET, se creará un fichero JSON con los datos del
  recurso. El programa, para estos métodos, leerá el fichero JSON del recurso
  correspondiente obtendrá los datos y los pasará en las llamadas.

Los ficheros serán los siguientes:
- **comments.json**: será el fichero con los datos de un recurso comment.
- **posts.json**: será el fichero con los datos de un recurso post.

- Se usará un fichero de configuración en formato JSON llamado config.json. El
  contenido de este fichero será el siguiente:

        {
            "url": "https://jsonplaceholder.typicode.com/",
            "request_time_out": 60,
            "response_data": "./response/data.json",
            "response_status": "./response/response.json"
        }

  Donde:
  - **url**: es la url donde se encuentra el API.
  - **resquest_time_out**: tiempo de espera para tener una respuesta en la llamada al API.
  - **response_data**: los recursos obtenidos del método GET se guardará en este fichero.
  - **response_status**: la respuesta de la llamada realizada se guardará en este fichero.
  - Los recursos obtenidos en el servicio GET se tratarán para adaptarlos, en la medida
    posible, a la estructura recomendada por JSON:API.
    Esta nueva estructura será la que se almacene en el fichero JSON, con indentación de 4
    caracteres.
    Para pasar los recursos a JSON, se debe utilizar la codificación (encoding) que el
    método invocado retorne.
  - En el fichero de respuesta (response_status) se guardarán, en formato JSON, los siguientes
    campos:
    - **method**: método usado en la llamada al API.
    - **url**: Url completa para llamar al API.
    - **status**: código de respuesta de la llamada al API.
    - **content-type**: tras la invocación a un método, se consultarán las cabeceras para
      obtener el tipo de contenido retornado, y ese valor se guardará en este atributo.
    - **enconding**: tras la invocación a un método, se consultarán las cabeceras para
      obtener la codificación del contenido y ese valor se guardará en este atributo.

- Para evitar tener exceso de código en el fichero main.py, se recomienda crear métodos en
  otros ficheros de apoyo en Python donde distribuir la lógica implementada.

  Un ejemplo de llamada al programa sería:

        main.py -method GET -resource posts

  y la respuesta guardada (response_status) sería:

        {
            "method": "GET",
            "url": "https://jsonplaceholder.typicode.com/posts",
            "status": 200,
            "content-type": "application/json",
            "encoding": "utf-8"
        }

> __**NOTE**__: Se opta por rediseñar algunas partes.
