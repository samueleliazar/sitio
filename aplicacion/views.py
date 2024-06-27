from django.shortcuts import render
from .models import Producto
from .forms import ProductoForm, UpdateProductoForm, CustomUserCreationForm, CustomUserChangeForm
from django.contrib import messages
from os import path, remove
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
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

def dashboard(request):
    return render(request,'aplicacion/dashboard.html')

def editarcompra(request):
    return render(request,'aplicacion/editarcompra.html')

def elimcliente(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios')  
    return render(request, 'aplicacion/elimcliente.html', {'usuario': usuario})
        

def usuarios(request):
    users = User.objects.all()
    return render(request,'aplicacion/usuarios.html', {'users': users})

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