from django.contrib import admin
from .models import Persona, Producto

# Register your models here.

class AdmPersona(admin.ModelAdmin):
    list_display=['nombre', 'apellido', 'fecha_crea', 'direccion', 'telefono', 'correo']
    list_filter=['apellido']
    
    
class AdmProducto(admin.ModelAdmin):
    list_display=['nombre', 'descripcion']

admin.site.register(Persona,AdmPersona)
admin.site.register(Producto,AdmProducto)