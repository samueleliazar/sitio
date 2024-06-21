from django.db import models
# Create your models here.


class Persona(models.Model):
    rut = models.CharField(max_length=12, primary_key=True, null=False)
    nombre=models.CharField(max_length=50,null=False)
    apellido=models.CharField(max_length=50,null=False)
    direccion=models.CharField(max_length=100,null=False)
    telefono=models.IntegerField()
    correo=models.EmailField(error_messages='Introduce bien el correo')
    
    def __str__(self):
        return f"RUT:{self.rut} NOMBRE: {self.nombre} {self.apellido}"


class Producto (models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100,null=False)
    descripcion=models.CharField(max_length=200,null=False)
    precio=models.IntegerField(null=False)
    imagen=models.ImageField(upload_to='productos',null=True)
    
    def __str__(self):
        return f"ID:{self.id} NOMBRE: {self.nombre}"
    