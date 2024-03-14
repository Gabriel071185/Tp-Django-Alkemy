from django.db import models

# Create your models here.


class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, )
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField()
    razon_social = models.CharField(max_length=100)
    cuit = models.CharField(max_length=11)
    celular = models.IntegerField()

    class Meta:
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor , on_delete=models.CASCADE, related_name= "producto")

    def __str__(self):
        return self.nombre




