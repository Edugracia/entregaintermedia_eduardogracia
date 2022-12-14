from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('empleados/', empleados, name="empleados"),
    path('socios/', socios, name="socios"),
    path('libros/', libros, name="libros"),
    #el path del formulario
]