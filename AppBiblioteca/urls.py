from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="inicio"),

    path('empleados/', empleados, name="empleados"),
    path('empleadosformulario/', empleadosformulario, name="empleadosformulario"),
    path('busquedaempleados/', busquedaempleados, name="busquedaempleados"),
    path('buscarempleado/', buscarempleado, name="buscarempleado"),


    path('socios/', socios, name="socios"),
    path('sociosformulario/', sociosformulario, name="sociosformulario"),
    path('busquedasocios/', busquedasocios, name="busquedasocios"),
    path('buscarsocio/', buscarsocio, name="buscarsocio"),


    path('libros/', libros, name="libros"),
    path('librosformulario/', librosformulario, name="librosformulario"),
    path('busquedalibro/', busquedalibro, name="busquedalibro"),
    path('buscarlibro/', buscarlibro, name="buscarlibro"),
    path("eliminarlibro/<id>", eliminarlibro, name="eliminarlibro"),
    path("editarlibro/<id>", editarlibro, name="editarlibro"),

    path("registro/", registro, name="registro"),
    path("login/", login_request, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("editarperfil/", editarperfil, name="editarperfil"),
    path("agregaravatar/", agregaravatar, name="agregaravatar"),

]