from django.db import models
# Create your models here.


class Persona(models.Model):
    fecha_crea=models.DateField(verbose_name='Fecha de creacion')
    nombre=models.CharField(max_length=50,null=False)
    apellido=models.CharField(max_length=50,null=False)
    direccion=models.CharField(max_length=100,null=False)
    telefono=models.IntegerField()
    correo=models.EmailField(error_messages='Introduce bien el correo')


class Producto (models.Model):
    nombre=models.CharField(max_length=100,null=False)
    descripcion=models.CharField(max_length=200,null=False)
    precio=models.IntegerField(null=False)
    imagen=models.ImageField(upload_to='nuevosproductos',null=False)
    
    