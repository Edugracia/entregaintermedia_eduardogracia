from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from AppBiblioteca.forms import *
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    return render (request, "inicio.html")

def empleados(request):
    return render (request, "empleados.html")

def socios(request):
    return render (request, "socios.html")
@login_required
def libros(request):
    libros=Libros.objects.all()
    return render(request, "libros.html", {"libros": libros})


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
            libros=Libros.objects.all()
            return render(request, "libros.html", {"libros":libros, "mensaje" : "Libro guardado correctamente"})

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


"""def leerlibro(request):

    libros=Libros.objects.all()
    return render(request, "libros.html", {"libros": libros})"""

@login_required
def eliminarlibro(request, id):
    libro=Libros.objects.get(id=id)
    libro.delete()
    libros=Libros.objects.all()
    return render(request, "libros.html", {"libros": libros, "mensaje": "Libro eliminado correctamente"})

def editarlibro(request, id):
    libro=Libros.objects.get(id=id)
    if request.method=="POST":
        form= librosform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            libro.titulo= informacion["titulo"]
            libro.autor= informacion["autor"]
            libro.codigo= informacion["codigo"]
            libro.save()
            libros=Libros.objects.all()
            return render(request, "libros.html", {"libros": libros, "mensaje" : "Libro editado correctamente"})            
        pass
    else:
        formulario= librosform(initial={"titulo":libro.titulo, "autor":libro.autor, "codigo":libro.codigo})
        return render(request, "editarlibros.html", {"form": formulario, "libro": libro})


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

#hasta aca empleados

def sociosformulario(request):
    if request.method=="POST":
        formulario= sociosform(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            email= informacion["email"]
            numero_socio= informacion["numero_socio"]
            socio= Socios(nombre=nombre, apellido=apellido, email=email, numero_socio=numero_socio)
            socio.save()
            return render(request, "socios.html", {"mensaje" : "Socio guardado correctamente"})

        else:
            return render (request, "sociosform.html", {"form": formulario, "mensaje": "Informacion no valida"})
    
    else:
        formulario= sociosform()
        return render (request, "sociosform.html", {"form": formulario})


def busquedasocios(request):
    return render(request, "socios.html")

def buscarsocio(request):
    
    nombre= request.GET["nombre"]
    if nombre != "":
        socios= Socios.objects.filter(nombre__icontains=nombre)
        return render(request, "resultadobusquedasocio.html", {"socios": socios})
    else:
        return render(request, "socio.html", {"mensaje": "Ingrese el nombre del Socio"})

#accounts

def registro(request):
    if request.method=="POST":
        form=registrousuarioform(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "registro.html", {"form":form, "mensaje": "Error al crear el usuario"})
    else:
        form= registrousuarioform()
        return render(request, "registro.html", {"form":form})


def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            usu=informacion["username"]
            clave=informacion["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "inicio.html", {"mensaje":f"Usuario {usu} logueado correctamente"})
            else:
                return render(request, "login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "login.html", {"form": form, "mensaje":"Usuario o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "login.html", {"form":form})

