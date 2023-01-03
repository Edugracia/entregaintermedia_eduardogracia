from django.contrib import admin
from .models import Empleados, Socios, Libros, Avatar

# Register your models here.

admin.site.register(Empleados)
admin.site.register(Socios)
admin.site.register(Libros)
admin.site.register(Avatar)
