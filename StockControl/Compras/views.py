from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProductoForm 
from .forms import ProveedorForm
from .models import Producto, Proveedor
from django.shortcuts import get_object_or_404


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


def editarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect(reverse('listado_producto'))
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto, 'activo': 'editar_producto'})

   
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect(reverse('listado_producto'))
    return render(request, 'eliminar_producto.html', {'producto': producto, 'activo': 'eliminar_producto'})



def editarProveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect(reverse('listado_proveedor'))
    else:
        form = ProveedorForm(instance=proveedor)
    return render(request, 'editar_proveedor.html', {'form': form, 'proveedor': proveedor})
          
def eliminarProveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect(reverse('listado_proveedor'))
    return render(request, 'eliminar_proveedor.html', {'proveedor': proveedor, 'activo': 'eliminar_proveedor'})