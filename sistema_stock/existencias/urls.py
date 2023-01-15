from django.urls import path
from existencias.views import *
urlpatterns = [
    path('bienvenida/',  bienvenida),
    path('inicio/', inicio),
    path('stock/', stock, name="stock"),
    path('proveedores/', proveedores, name="proveedores"),
    path('compras/', compra, name="compras"),
    path('clientes/', cliente, name="clientes"),
    path('ventas', venta, name="ventas"),
    path('crear-proveedor/',crear_proveedor, name="crear_proveedor"),
    path('crear-compra/', crear_compra, name="crear_compra"),
    path('crear-cliente/', crear_cliente, name="crear_cliente"),
    path('crear-stock/', crear_stock, name="crear_stock"),
    path('crear-venta/', crear_venta, name="crear_venta"),
    path('buscar-proveedores/', buscar_proveedores, name="buscar_proveedores"),
    path('ayuda/', ayuda, name="ayuda" ),
]