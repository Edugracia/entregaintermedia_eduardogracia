from django.db import models

# Create your models here.

class Empleados(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email=models.EmailField()

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"


class Socios(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    numero_socio= models.IntegerField()

    class Meta:
        verbose_name = "Socio"
        verbose_name_plural = "Socios"

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {str(self.numero_socio)}"


class Libros(models.Model):
    titulo= models.CharField(max_length=50)
    autor= models.CharField(max_length=50)
    codigo= models.IntegerField()

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return f"{self.titulo} - {self.autor} - {str(self.codigo)}"