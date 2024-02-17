# mywebapp/views.py
from django.shortcuts import render, redirect
from .forms import CategoriaForm, BusquedaForm, ClienteForm, ProductoForm
from .models import Categoria, Producto, Cliente, Articulo

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buscar')
    else:
        form = CategoriaForm()
    return render(request, 'agregar_categoria.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buscar')
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def index(request):
    articulos = Articulo.objects.all()
    productos_recientes = Producto.objects.all()[:5]
    
    return render(request, 'index.html', {'articulos': articulos, 'productos_recientes': productos_recientes})

def buscar(request):
    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados_categorias = Categoria.objects.filter(nombre__icontains=termino_busqueda)
            resultados_productos = Producto.objects.filter(nombre__icontains=termino_busqueda)
            resultados_clientes = Cliente.objects.filter(nombre__icontains=termino_busqueda)
            return render(request, 'resultados_busqueda.html', {
                'resultados_categorias': resultados_categorias,
                'resultados_productos': resultados_productos,
                'resultados_clientes': resultados_clientes,
            })
    else:
        form = BusquedaForm()

    return render(request, 'buscar.html', {'form': form})
