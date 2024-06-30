from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Producto (models.Model):
    nombre=models.CharField(max_length=100,null=False)
    descripcion=models.CharField(max_length=200,null=False)
    precio=models.IntegerField(null=False)
    imagen=models.ImageField(upload_to='productos',null=True)
    
    def __str__(self):
        return f"NOMBRE: {self.nombre}"
    
class Pedido(models.Model):
    ESTADOS_PEDIDO = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Enviado', 'Enviado'),
        ('Entregado', 'Entregado'),
        ('Cancelado', 'Cancelado'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO, default='Pendiente')

    def __str__(self):
        return f'Pedido {self.id} de {self.user.username}'

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    
    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre}"
    
