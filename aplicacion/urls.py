from django.urls import path
from .views import index, productos, contacto, comprar, pedidos, login, olvidocon, usuariosnuevos, dashboard, editarcompra, usuarios, editarcliente, estadisticas, nuevosproductos

urlpatterns = [
    path('',index,name='index'),
    path('producto/', productos,name='productos'),
    path('contacto/', contacto,name='contacto'),
    path('comprar/', comprar,name='comprar'),
    path('pedidos/',pedidos,name='pedidos'),
    path('login/',login,name='login'),
    path('olvidocon/',olvidocon,name='olvidocon'),
    path('usuariosnuevos/',usuariosnuevos,name='usuariosnuevos'),
    path('dashboard/',dashboard,name='dashboard'),
    path('editarcompra/',editarcompra,name='editarcompra'),
    path('usuarios/',usuarios,name='usuarios'),
    path('editarcliente/',editarcliente,name='editarcliente'),
    path('estadisticas/',estadisticas,name='estadisticas'),
    path('nuevosproductos/',nuevosproductos,name='nuevosproductos'),
]

