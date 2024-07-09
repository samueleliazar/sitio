from django.shortcuts import render
from .Carrito import Carrito
from .models import Producto, Pedido
from .forms import ProductoForm, UpdateProductoForm, CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages
from os import path, remove
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index(request):
    return render(request,'aplicacion/index.html')

def productos(request):
    
    producto=Producto.objects.all()
    
    datos={
        "producto":producto
    }
    return render(request,'aplicacion/productos.html', datos)

def contacto(request):
    return render(request,'aplicacion/contacto.html')

def carrito(request):
    return render(request, 'aplicacion/carrito.html')

def comprar(request):
    return render(request,'aplicacion/comprar.html')

def pedidos(request):
    return render(request,'aplicacion/pedidos.html')

#def login(request):
    return render(request,'aplicacion/login.html')

def olvidocon(request):
    return render(request,'aplicacion/olvidocon.html')

def usuariosnuevos(request):
    data= {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Registro hecho correctamente")
            return redirect(to="index")
        data["form"] = formulario
    return render(request,'registration/usuariosnuevos.html', data)

@permission_required('dashboard')
def dashboard(request):
    compras_recientes = Pedido.objects.all()

    context = {
        'compras_recientes': compras_recientes,
    }
    return render(request,'aplicacion/dashboard.html', context)

def editarcompra(request):
    return render(request,'aplicacion/editarcompra.html')

@permission_required('elimcliente')
def elimcliente(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios')  
    return render(request, 'aplicacion/elimcliente.html', {'usuario': usuario})
        
@permission_required('usuarios')
def usuarios(request):
    users = User.objects.all()
    return render(request,'aplicacion/usuarios.html', {'users': users})

@permission_required('editarcliente')
def editarcliente(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request,'aplicacion/editarcliente.html',{'form': form, 'user': user})



@permission_required('editprod')
def editprod(request, id):
    producto=get_object_or_404(Producto, id=id)
    
    form=UpdateProductoForm(instance=producto)
    datos={
        "form":form,
        "producto":producto
    }
    
    if request.method=="POST":
        form=UpdateProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.warning(request,'Producto modificado exitosamente')
            return redirect(to="catalogo")
        
    return render(request,'aplicacion/editprod.html', datos)
@permission_required('nuevosproductos')
def nuevosproductos(request):
    
    form=ProductoForm()
    
    if request.method=="POST":
        form=ProductoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request,'Producto agregado exitosamente')
            return redirect(to="catalogo")
        
    datos={
        "form":form
    }
    return render(request,'aplicacion/nuevosproductos.html', datos)
@permission_required('catalogo')
def catalogo(request):
    producto=Producto.objects.all()
    
    datos={
        "producto":producto
    }
    return render(request, 'aplicacion/catalogo.html', datos)
@permission_required('eliminarprod')
def eliminarprod(request, id):
    producto=get_object_or_404(Producto, id=id)
    
    datos={
        "producto":producto
    }
    
    if request.method=="POST":
        if producto.imagen:
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media','')+producto.imagen.url))
        producto.delete()
        messages.error(request, 'Producto eliminado exitosamente')
        return redirect(to='catalogo')
    
    return render(request, 'aplicacion/eliminarprod.html',datos)

@login_required
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    if carrito.carrito.get(str(producto.id), {}).get('cantidad', 0) < producto.cantidad_maxima:
        carrito.agregar(producto)
    else:
        messages.error(request, f'No puedes agregar más de {producto.cantidad_maxima} unidades de este producto.')
    return redirect(to="productos")
@login_required
def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.eliminar(producto)
    return redirect(to="productos")
@login_required
def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.restar(producto)
    return redirect(to="productos")

@login_required
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(to="productos")

def realizar_compra(request):
    carrito = Carrito(request)
    pedido = carrito.procesar_compra(request.user)
    if pedido:
        messages.success(request, 'Compra realizada exitosamente')
        return redirect('detalle_pedido', pedido_id=pedido.id)
    else:
        messages.error(request, 'No hay productos en el carrito')
    return redirect(to="productos")

def detalle_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, user=request.user)
    items = pedido.pedidoproducto_set.all()
    detalles = []
    for item in items:
        detalles.append({
            'producto': item.producto,
            'cantidad': item.cantidad,
            'precio': item.precio,
            'total': item.cantidad * item.precio
        })
    return render(request, 'aplicacion/detalle_pedido.html', {'pedido': pedido, 'detalles': detalles})

def lista_pedidos(request):
    pedidos = Pedido.objects.filter(user=request.user)
    return render(request, 'aplicacion/lista_pedidos.html', {'pedidos': pedidos})

def cambiar_estado_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in dict(Pedido.ESTADOS_PEDIDO):
            pedido.estado = nuevo_estado
            pedido.save()
            messages.success(request, 'El estado del pedido ha sido actualizado.')
        else:
            messages.error(request, 'Estado no válido.')

    return redirect(to="dashboard")