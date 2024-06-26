from django import forms
from .models import Producto, Persona
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name",  "email", "password1", "password2" ]