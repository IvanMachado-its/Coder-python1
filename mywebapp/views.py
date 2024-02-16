from django.shortcuts import render, redirect
from .forms import CategoriaForm, BusquedaForm
from .models import Categoria, Producto, Cliente

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_categoria')  # Reemplaza con la URL o nombre correcto de la vista exitosa
    else:
        form = CategoriaForm()
    return render(request, 'agregar_categoria.html', {'form': form})

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

def index(request):
    return render(request, 'index.html')
