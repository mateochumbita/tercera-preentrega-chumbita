from django.urls import path
from existencias.views import *
urlpatterns = [
    path('bienvenida/',  bienvenida),
    path('inicio/', inicio),
    path('stock/', stock, name=stock),
    path('proveedores/', proveedores, name=proveedores),
    path('compra/', compra, name=compra),
    path('cliente/', cliente, name=cliente),
]