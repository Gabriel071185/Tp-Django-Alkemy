
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name= 'inicio' ),
    path('listado_productos/', views.listadoProducto, name= 'listado_producto'),
    path('listado_proveedor/', views.listadoProveedor, name= "listado_proveedor"),
    path('agregar_productos/', views.agregarProducto, name= 'agregar_producto'),
    path('agregar_proveedor/', views.agregarProveedor, name= 'agregar_proveedor'),
    path('editar_producto/<int:id>/', views.editarProducto, name='editar_producto'),
    path('eliminar_producto/<int:id>/', views.eliminarProducto, name='eliminar_producto'),
    path('editar_proveedor/<int:id>/', views.editarProveedor, name='editar_proveedor'),
    path('eliminar_proveedor/<int:id>/', views.eliminarProveedor, name='eliminar_proveedor'),
]

