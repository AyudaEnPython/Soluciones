# Enunciado Original

Crear un programa en lenguaje Python que gestione una base de datos de clientes
que adquieren un producto con fecha de vencimiento.

El programa debe mostrar el estado del producto (vencido, a punto de vencer)
mediante colores.

## Requisitos

- Utilizar lenguaje Python
- Crear una base de datos para almancenar la información de clientes y productos
- Incluir campos para:
  - Nombre del cliente
  - Apellido del cliente
  - Cédula del cliente
    - Producto adquirido
  - Fecha de comprar del producto
    - Fecha de vencimiento
- Implementar una función que calcule la diferencia entre la fecha actual y la
  fecha de vencimiento
- Mostrar el estado del producto mediante colores:
  - Rojo: Vencido
  - Amarillo: A punto de vencer (dentro de los 5 días siguientes)
  - Verde: Vigente
  - Permitir la consulta de información por cliente o producto

---

## Notas

Para inicializar la base de datos, ir al directorio `/data` y ejecutar en la consola (python3 para Linux/macOS):

```sh
> python init_db.py
```

Crear un entorno virtual (python3 para Linux/macOS):

```
python -m venv .venv
```

Activar el entorno virtual:

Linux/macOS:

```sh
source .venv/bin/activate
```

Windows:

```sh
.venv\Scripts\activate
```

Actualizar `pip` e instalar dependecias (python3 para Linux/macOS):

```
python -m pip install --upgrade pip
```

```
python -m pip install -r requirements.txt
```
