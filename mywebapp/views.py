# mywebapp/views.py

from django.shortcuts import render, redirect
from .models import Categoria, Producto, Cliente
from .forms import CategoriaForm, ProductoForm, ClienteForm

def index(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'index.html', {'categorias': categorias, 'productos': productos, 'clientes': clientes})

def agregar_categoria(request):
    # Implementa lógica para agregar categorías
    # ...

def agregar_producto(request):
    # Implementa lógica para agregar productos
    # ...

def agregar_cliente(request):
    # Implementa lógica para agregar clientes
    # ...
