from django.urls import path
from django.conf.urls.static import static

from sitio import settings
from .views import index, productos, contacto, comprar, pedidos, login, olvidocon, usuariosnuevos, dashboard, editarcompra, usuarios, editarcliente, estadisticas, nuevosproductos, catalogo, editprod

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
    path('catalogo/', catalogo, name='catalogo'),
    path('editprod/<id>', editprod, name='editprod'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

