# mywebapp/forms.py
from django import forms
from .models import Categoria, Cliente, Producto

class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(max_length=255, required=True)

class CategoriaForm(forms.ModelForm):
    descripcion = forms.CharField(max_length=255)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion', 'imagen']

class ClienteForm(forms.ModelForm):
    direccion = forms.CharField(max_length=255)
    ciudad = forms.CharField(max_length=100)
    codigo_postal = forms.CharField(max_length=10)

    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'direccion', 'ciudad', 'codigo_postal']

class ProductoForm(forms.ModelForm):
    descripcion = forms.CharField(max_length=255)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = forms.IntegerField()

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'cantidad_disponible']
