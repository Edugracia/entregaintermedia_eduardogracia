from django import forms


class empleadosform(forms.Form):
    nombre= forms.CharField(label="Nombre", max_length=50)
    apellido= forms.CharField(label="Apellido", max_length=50)
    email=forms.EmailField(label="Email")



class librosform(forms.Form):
    titulo= forms.CharField(label="Titulo", max_length=50)
    autor= forms.CharField(label="Autor", max_length=50)
    codigo= forms.IntegerField(label="Codigo")