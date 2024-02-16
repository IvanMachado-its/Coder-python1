# mywebapp/urls.py

from django.urls import path
from .views import index, agregar_categoria, agregar_producto, agregar_cliente

urlpatterns = [
    path('', index, name='index'),
    path('agregar_categoria/', agregar_categoria, name='agregar_categoria'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('agregar_cliente/', agregar_cliente, name='agregar_cliente'),
    path('buscar/', buscar, name='buscar'),
]
