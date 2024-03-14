from django import forms
from .models import Proveedor, Producto

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual', 'proveedor', ]
        widgets = {
                   'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese nombre de su producto'  }),
                   'precio': forms.NumberInput(attrs={'class':'form-control', 'placeholder': 'Ingrese el precio de su producto'  }),
                   'stock_actual' : forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el stock de su producto' }),
                   'proveedor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Su nombre de Proveedor' })
                   }


class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni', 'razon_social', 'cuit', 'celular']
        widgets = {
                   'nombre' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese sus nombres'  }),
                   'apellido': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese sus apellidos' }),
                   'dni' : forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Ingrese su número de documento'}),
                   'razon_social': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese la razón social de su negocio' }),
                   'cuit': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ingrese su número de cuit' }),
                   'celular': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'placeholder': 'Ingrese un número'})
                   }

