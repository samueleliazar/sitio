from django import forms
from .models import Producto, Persona

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombre','descripcion', 'precio','imagen']
        

class UpdateProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen']
        

class UpdatePersonaForm(forms.ModelForm):
    
    class Meta:
        model= Persona
        fields = ['rut', 'nombre', 'apellido', 'direccion', 'telefono', 'correo']