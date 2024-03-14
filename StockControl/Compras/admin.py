from django.contrib import admin
from .models import Producto, Proveedor
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock_actual', 'proveedor']
    search_fields = ['nombre', 'precio', 'stock_actual', 'proveedor__nombre']

class ProoveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'dni', 'razon_social', 'cuit', 'celular']
    search_fields = ['nombre', 'apellido', 'dni', 'razon_social', 'cuit', 'celular']

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Proveedor,ProoveedorAdmin)