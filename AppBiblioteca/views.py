from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppBiblioteca.forms import *

# Create your views here.
def inicio(request):
    return render (request, "inicio.html")
    #return HttpResponse("Inicio")

def empleados(request):
    return render (request, "empleados.html")

def socios(request):
    return render (request, "socios.html")

def libros(request):
    return render (request, "libros.html")





"""def librosformulario(request):
    if request.method=="POST":
        titulo= request.POST["titulo"]
        autor= request.POST["autor"]
        codigo= request.POST["codigo"]
        libro= Libros(titulo=titulo, autor=autor, codigo=codigo)
        libro.save()
        return render (request, "inicio.html", {"mensaje": "Libro guardado correctamente"})

    else:
        return render (request, "libros.html")"""

def librosformulario(request):
    if request.method=="POST":
        formulario= librosform(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            titulo= informacion["titulo"]
            autor= informacion["autor"]
            codigo= informacion["codigo"]
            libro= Libros(titulo=titulo, autor=autor, codigo=codigo)
            libro.save()
            return render(request, "libros.html", {"mensaje" : "Libro guardado correctamente"})

        else:
            return render (request, "librosform.html", {"form": formulario, "mensaje": "Informacion no valida"})
    
    else:
        formulario= librosform()
        return render (request, "librosform.html", {"form": formulario})


def busquedalibro(request):
    return render(request, "libros.html")

def buscarlibro(request):
    
    titulo= request.GET["titulo"]
    if titulo != "":
        libros= Libros.objects.filter(titulo__icontains=titulo)
        return render(request, "resultadobusquedalibro.html", {"libros": libros})
    else:
        return render(request, "libros.html", {"mensaje": "Ingrese el nombre del libro"})

#hasta aca libros

def empleadosformulario(request):
    if request.method=="POST":
        formulario= empleadosform(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            email= informacion["email"]
            empleado= Empleados(nombre=nombre, apellido=apellido, email=email)
            empleado.save()
            return render(request, "empleados.html", {"mensaje" : "Empleado guardado correctamente"})

        else:
            return render (request, "empleadosform.html", {"form": formulario, "mensaje": "Informacion no valida"})
    
    else:
        formulario= empleadosform()
        return render (request, "empleadosform.html", {"form": formulario})


def busquedaempleados(request):
    return render(request, "empleados.html")

def buscarempleado(request):
    
    nombre= request.GET["nombre"]
    if nombre != "":
        empleados= Empleados.objects.filter(nombre__icontains=nombre)
        return render(request, "resultadobusquedaempleado.html", {"empleados": empleados})
    else:
        return render(request, "empleados.html", {"mensaje": "Ingrese el nombre del Empleado"})