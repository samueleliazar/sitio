from django.db import models
# Create your models here.


class Persona(models.Model):
    fecha_crea=models.DateField(verbose_name='Fecha de creacion')
    nombre=models.CharField(max_length=50,null=False)
    apellido=models.CharField(max_length=50,null=False)
    direccion=models.CharField(max_length=100,null=False)
    telefono=models.IntegerField()
    correo=models.EmailField(error_messages='Introduce bien el correo')
