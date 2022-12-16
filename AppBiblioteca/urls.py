from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('empleados/', empleados, name="empleados"),
    path('socios/', socios, name="socios"),
    path('libros/', libros, name="libros"),
    path('librosformulario/', librosformulario, name="librosformulario"),
    path('busquedalibro/', busquedalibro, name="busquedalibro"),
    path('buscarlibro/', buscarlibro, name="buscarlibro"),
    path('empleadosformulario/', empleadosformulario, name="empleadosformulario"),
    path('busquedaempleados/', busquedaempleados, name="busquedaempleados"),
    path('buscarempleado/', buscarempleado, name="buscarempleado"),
]