from .models import Producto, Pedido, PedidoProducto
from django.contrib import messages
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.carrito = self.session.get("carrito")
        if not self.carrito:
            self.carrito = self.session["carrito"] = {}

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
            }
        else:
            if self.carrito[id]["cantidad"] < producto.cantidad_maxima:
                self.carrito[id]["cantidad"] += 1
                self.carrito[id]["acumulado"] += producto.precio
            else:
                messages.error(self.request, 'Has alcanzado la cantidad máxima permitida para este producto.')
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
        
    def procesar_compra(self, user):
        if not self.carrito:
            return None
        
        pedido = Pedido.objects.create(user=user, total=self.total_carrito())
        for key, value in self.carrito.items():
            producto = Producto.objects.get(id=value["producto_id"])
            PedidoProducto.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=value["cantidad"],
                precio=value["acumulado"]
            )
        self.limpiar()
        return pedido

    def total_carrito(self):
        total = 0
        for key, value in self.carrito.items():
            total += int(value["acumulado"])
        return total