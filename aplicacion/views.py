from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm, UpdateProductoForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
def index(request):
    return render(request,'aplicacion/index.html')

def productos(request):
    return render(request,'aplicacion/productos.html')

def contacto(request):
    return render(request,'aplicacion/contacto.html')

def comprar(request):
    return render(request,'aplicacion/comprar.html')

def pedidos(request):
    return render(request,'aplicacion/pedidos.html')

def login(request):
    return render(request,'aplicacion/login.html')

def olvidocon(request):
    return render(request,'aplicacion/olvidocon.html')

def usuariosnuevos(request):
    return render(request,'aplicacion/usuariosnuevos.html')

def dashboard(request):
    return render(request,'aplicacion/dashboard.html')

def editarcompra(request):
    return render(request,'aplicacion/editarcompra.html')

def usuarios(request):
    return render(request,'aplicacion/usuarios.html')

def editarcliente(request):
    return render(request,'aplicacion/editarcliente.html')

def estadisticas(request):
    return render(request,'aplicacion/estadisticas.html')

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

def catalogo(request):
    producto=Producto.objects.all()
    
    datos={
        "producto":producto
    }
    return render(request, 'aplicacion/catalogo.html', datos)

