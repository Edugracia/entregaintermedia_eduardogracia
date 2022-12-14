from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppBiblioteca.forms import librosform

# Create your views here.
def inicio(request):
    return render (request, "inicio.html")
    #return HttpResponse("Inicio")

def empleados(request):
    return render (request, "empleados.html")

def socios(request):
    return render (request, "socios.html")

"""def libros(request):
    return render (request, "libros.html")"""


    #FALTARIA HACER LAS FORMS TANTO PARA METER DATOS COMO PARA BUSCAR EN LA BD, LA BOCHA SERIA HACER QUE DENTRO DE CADA TEMPLATE METER LA VIEW DE LOS FORMULARIOS


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

def libros(request):
    if request.method=="POST":
        formulario= librosform(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            titulo= formulario["titulo"]
            autor= formulario["autor"]
            codigo= formulario["codigo"]
            libro= Libros(titulo=titulo, autor=autor, codigo=codigo)
            libro.save()
            return render(request, "inicio.html", {"mensaje" : "Libro guardado correctamente"})

    else:
        formulario= librosform()
        return render (request, "libros.html", {"form": formulario, "mensaje": "Informacion no valida"})