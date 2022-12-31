from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User



class empleadosform(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=50)
    apellido= forms.CharField(label="Apellido", max_length=50)
    email=forms.EmailField(label="Email")


class sociosform(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    numero_socio= forms.IntegerField()


class librosform(forms.Form):
    titulo= forms.CharField(label="Titulo", max_length=50)
    autor= forms.CharField(label="Autor", max_length=50)
    codigo= forms.IntegerField(label="Codigo")


class registrousuarioform(UserCreationForm):
    email= forms.EmailField(label="Email")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}