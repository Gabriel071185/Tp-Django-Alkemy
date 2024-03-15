from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProductoForm 
from .forms import ProveedorForm
from .models import Producto, Proveedor

# Create your views here.

def index(request):
    return render(request, 'index.html', context={'activo': 'inicio'})

def listadoProducto(request):
    productos = Producto.objects.all()
    context={'activo': 'listado_producto', 
              'productos' : productos}
    
    return render(request,'listado_producto.html', context )


def listadoProveedor(request):
    proveedor = Proveedor.objects.all()
    context={'activo': 'listado_proveedor',
            'proveedor' : proveedor  }
    return render(request,'listado_proveedor.html', context )




def agregarProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('listado_producto'))
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form,'activo': 'agregar_producto'} )
    

def agregarProveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listado_proveedor')
    else:
        form = ProveedorForm()
    return render(request, 'agregar_proveedor.html', {'form': form,'activo': 'agregar_proveedor'} )



   
          