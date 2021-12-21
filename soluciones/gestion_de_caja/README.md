
## Enunciado

Una empresa lo contrata para desarrollar un sistema de gestión de caja
nacional e internacional, con las siguientes condiciones:

- Tiene que vivir los datos mientras el sistema esté funcionando.
- Debe ser cómodo/entendible de usar.
- Debe tener una pantalla dividiva; en una parte, se debe poder agregar
  gastos e ingresos (nacionales o internacionales); por otra parte, se
  debe poder listar la información con sus respectivos totales.
- Gastos e ingresos nacionales consideran solo valores netos, por lo
  tanto, se debe calcular el IVA con un 18%.
- Gastos e ingresos internacionales deben ser en USD, considere el cambio
  de $844 por USD. (Se debe ingresar en USD y se debe hacer la conversión)
- El sistema deberá mostrar:
  - Listado de ingresos nacionales
  - Listado de ingresos internacionales
  - Totales de gastos nacionales
  - Totales de ingresos nacionales
  - Totales de gastos internacionales
  - Totales de ingresos internacionales
  - Totales nacionales
  - Totatles internacionales
  - Total (nacional + internacional)

## Ingreso

- Nacionales:
  - Valor neto: $ 49.990
  - Detalle: Gastos de papelería
- Internacionales:
  - Valor en USD: $ 1099,00
  - Detalle: Computador Lenovo para programador Jr.

## Importante

- Considere si usted quiere reemplazar una nota, debe considerar los gastos
  e ingresos internacionales, si no, realice el programa con solo los gastos
  e ingresos nacionales.

## Pauta de evaluación

- Uso de Tkinter
- Uso de listas
- Funciones propias
- Funciones predefinidas
- Ingresos nacionales
- Ingresos internacionales
- Lista de ingresos nacionales
- Lista de ingresos internacionales
- Totales

## Ayudas

- Considere atributos de listado nacional:

    [ingreso/gasto, Detalle, valorNeto, iVA, valorTotal]

    Ejemplo:
        
        [1, "Gastos de papeleria", 49990, 8998, 58988]

- Considere atributos de listado internacional:

    [ingreso/gasto, Detalle, valorUSD, valorTotal]
    
    Ejemplo: 
        
        [1, "Computador Lenoveo para programador jr", 1099, 957556]


> _**NOTA**_: El enunciado original presentaba errores ortográficos
> (se modificó). Todo el documento presenta inconsistencias.