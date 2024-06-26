from django.shortcuts import render
from .models import Producto, Persona
from .forms import ProductoForm, UpdateProductoForm, UpdatePersonaForm, CustomUserCreationForm
from django.contrib import messages
from os import path, remove
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import authenticate, login
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
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Se ha registrado correctamente!")
            return redirect(to='login')
        data["form"] = formulario
        
    return render(request,'registration/usuariosnuevos.html', data)

def dashboard(request):
    return render(request,'aplicacion/dashboard.html')

def editarcompra(request):
    return render(request,'aplicacion/editarcompra.html')

def elimcliente(request, id):
    persona=get_object_or_404(Persona, rut=id)
    
    datos={
        "persona":persona
    }
    
    if request.method=="POST":
        if persona.imagen:
            persona.delete()
            messages.error(request, 'Persona eliminado exitosamente')
            return redirect(to='usuarios')
    return render(request, 'aplicacion/elimcliente.html',datos)
        

def usuarios(request):
    
    personas=Persona.objects.all()
    
    datos={
        
        "persona":personas
    }
    
    return render(request,'aplicacion/usuarios.html', datos)

def editarcliente(request, id):
    persona=get_object_or_404(Persona, rut=id)
    
    form=UpdatePersonaForm(instance=persona)
    datos={
        "form":form,
        "persona":persona
    }
    
    if request.method=="POST":
        form=UpdatePersonaForm(data=request.POST, files=request.FILES, instance=persona)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Cliente modificado')
            return redirect(to='usuarios')
        
    return render(request,'aplicacion/editarcliente.html', datos)

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
        if productos.imagen:
            remove(path.join(str(settings.MEDIA_ROOT).replace('/media','')+productos.imagen.url))
        productos.delete()
        messages.error(request, 'Producto eliminado exitosamente')
        return redirect(to='catalogo')
    
    return render(request, 'aplicacion/eliminarprod.html',datos)