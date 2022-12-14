from django import forms

class librosform(forms.Form):
    titulo= forms.CharField(label="Titulo", max_length=50)
    autor= forms.CharField(label="Autor", max_length=50)
    codigo= forms.IntegerField(label="Codigo")