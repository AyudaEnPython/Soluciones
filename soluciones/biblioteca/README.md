Según el diagrama, los volúmenes de una biblioteca *Volumen* pueden ser
de dos tipos: *Book* o *Newspaper*

                     ,----------------------------.
                     |Library                     |
         ,-------.   |----------------------------|
         |Volumen|   |- name                      |
         |-------|   |- address                   |
         |- id   |---|- volumens: Volumen[0..*]   |
         |- name |   |+ add_volumen(self, volumen)|
         `-------'   |+ remove_volumen(self, id)  |
           /    \    |+ save_volumens(self)       |
          /      \   `----------------------------'
         /        \                               
        /          \                             
    ,-----------.  ,-----------.                       
    |Book       |  |Newspaper  |                       
    |-----------|  |-----------|                       
    |- isbn_code|  |- issn_code|                       
    `-----------'  `-----------' 

Se pide lo siguiente:

1. Implementar la jerarquía de clases para registrar las instancias
  correspondientes en la clase Volumen o subclases Book o Newspaper así
  como en la colección Library.

2. Completar el desarrollo siguiendo las siguientes precisiones: en las
  subclases *Book* y *Newspaper*, mostrar sus propiedades \_\_str\_\_(self)
  mostrando el *id*, *name* y dependiendo de tipo del código *isbn* para
  el caso de libros y *issn* para revistas. Los volúmenes deber ser
  agregados a la clase Library (biblioteca) usando el método *add_volumen*
  y podrá ser removido ubicándolos por el id y usando el método *remove_volumen*
  , no debe permitirse almacenar en la biblioteca 2 volúmenes con el mismo
  id, el método *save_volumens* permitirá grabar los volúmenes de la biblioteca
  en un archivo Excel. Deben crear por lo menos 3 instancias por cada clase.
