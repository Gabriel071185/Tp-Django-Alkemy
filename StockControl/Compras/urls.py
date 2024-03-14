
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name= 'inicio' ),
    path('listado_productos/', views.listadoProducto, name= 'listado_productos'),
    path('listado_proveedor/', views.listadoProveedor, name= "listado_proveedor"),
    path('agregar_productos/', views.agregarProducto, name= 'agregar_producto'),
    path('agregar_proveedor/', views.agregarProveedor, name= 'agregar_proveedor'),
]