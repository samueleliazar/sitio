from django.urls import path
from django.conf.urls.static import static
from . import views



from sitio import settings
from .views import index, productos, contacto, comprar, pedidos, olvidocon, usuariosnuevos, dashboard, editarcompra, usuarios, editarcliente, estadisticas, nuevosproductos, catalogo, editprod, eliminarprod, elimcliente, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, realizar_compra, detalle_pedido, lista_pedidos

urlpatterns = [
    path('',index,name='index'),
    path('producto/', productos,name='productos'),
    path('contacto/', contacto,name='contacto'),
    path('comprar/', comprar,name='comprar'),
    path('pedidos/',pedidos,name='pedidos'),
    #path('login/',login,name='login'),
    path('olvidocon/',olvidocon,name='olvidocon'),
    path('usuariosnuevos/',usuariosnuevos,name='usuariosnuevos'),
    path('dashboard/',dashboard,name='dashboard'),
    path('editarcompra/',editarcompra,name='editarcompra'),
    path('usuarios/',usuarios,name='usuarios'),
    path('editarcliente/<int:id>/',editarcliente,name='editarcliente'),
    path('estadisticas/',estadisticas,name='estadisticas'),
    path('nuevosproductos/',nuevosproductos,name='nuevosproductos'),
    path('catalogo/', catalogo, name='catalogo'),
    path('editprod/<id>', editprod, name='editprod'),
    path('eliminarprod/<id>',eliminarprod, name='eliminarprod'),
    path('elimcliente/<int:usuario_id>/', elimcliente, name='elimcliente'),
    path('agregar/<int:producto_id>/', agregar_producto, name="add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="del"),
    path('restar/<int:producto_id>/', restar_producto, name="sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('realizar_compra/', realizar_compra, name="realizar_compra"),
    path('detalle_pedido/<int:pedido_id>/', detalle_pedido, name='detalle_pedido'),
    path('mis_pedidos/', lista_pedidos, name='lista_pedidos'),
    path('cambiar_estado_pedido/<int:pedido_id>/', views.cambiar_estado_pedido, name='cambiar_estado_pedido'),

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

