from django.shortcuts import render
from django.shortcuts import HttpResponse
from existencias.models import *

def bienvenida(request):
    return HttpResponse("Hola usuario")

def inicio(request):
    return render(
        request=request,
        template_name='existencias/base.html',
    )


def cliente(request):
    contexto = {
        'cliente': Cliente.objects.all()
    }
    return render(request=request, template_name='existencias/cliente.html',
     context=contexto )



def proveedores(request):
    contexto = {
        'proveedor': Proveedor.objects.all()
    }
    return render(request=request, template_name='existencias/proveedores.html',
     context=contexto )

def stock(request):
    contexto = {
        'stock': Stock.objects.all()
    }

    return render(request=request, template_name='existencias/stock.html', context=contexto)

def compra(request):
    contexto = {
        'compra': Compra.objects.all()
    }

    return render(request=request, template_name='existencias/compra.html', context=contexto)

def venta(request):
    contexto = {
        'venta': Venta.objects.all()
    }

    return render(request=request, template_name='existencias/venta.html', context=contexto)