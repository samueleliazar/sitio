from django.shortcuts import render

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

def nuevosproductos(request):
    return render(request,'aplicacion/nuevosproductos.html')