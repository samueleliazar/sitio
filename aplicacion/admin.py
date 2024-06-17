from django.contrib import admin
from .models import Persona

# Register your models here.

class AdmPersona(admin.ModelAdmin):
    list_display=['nombre', 'apellido', 'fecha_crea', 'direccion', 'telefono', 'correo']
    list_filter=['apellido']
    
admin.site.register(Persona,AdmPersona)