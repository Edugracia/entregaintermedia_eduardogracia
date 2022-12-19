# entregaintermedia_eduardogracia

La premisa del sitio es generar una base de datos para una librería en la cual se pueden cargar empleados, socios y libros.
El sitio está organizado de la siguiente manera:

AppBiblioteca/

Es nuestro inicio desde la cual se puede acceder a:

AppBiblioteca/empleados/
AppBiblioteca/socios/
AppBiblioteca/libros/

No es necesario hacerlo a través de la url, los botones llevan a los path correspondientes.


Formularios de búsqueda

Cada una tiene un formulario de búsqueda del tipo “filter”, tanto empleados como socios se buscan a partir del nombre mientras que libros a partir de un título.
Para probar las views de búsqueda detallo algunos de los nombres incluidos en la DB:

Empleados:
Gabriela
Victoria
Eduardo
Romina

Socios:
Aurelia
Marcelo
Eduardo

Libros:
Don Quijote
Madame Bovary
Romeo y Julieta
Una mente inquieta


En todos los casos tanto para una búsqueda positiva como para una sin resultados se mantiene el formulario búsqueda con la idea de que sea más accesible al usuario.


Formularios de carga

Se accede a través de las siguientes urls:

AppBiblioteca/empleadosformulario/
AppBiblioteca/sociosformulario/
AppBiblioteca/librosformulario/

En caso de cargar los datos de forma correcta carga la template informando de la carga exitosa, en caso de información no valida carga nuevamente la template con el formulario.

admin
admin
