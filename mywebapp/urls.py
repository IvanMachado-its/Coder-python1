# mywebproject/urls.py
from django.contrib import admin
from django.urls import path
from mywebapp.views import index, agregar_categoria, agregar_cliente, buscar, agregar_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('agregar_categoria/', agregar_categoria, name='agregar_categoria'),
    path('agregar_cliente/', agregar_cliente, name='agregar_cliente'),
    path('buscar/', buscar, name='buscar'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
]
