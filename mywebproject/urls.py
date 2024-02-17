# mywebproject/urls.py
from django.contrib import admin
from django.urls import path, include
from mywebapp.views import index, agregar_categoria, agregar_cliente, buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mywebapp.urls')),
]
