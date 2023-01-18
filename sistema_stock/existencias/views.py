from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import HttpResponse
from existencias.models import *
from existencias.forms import ProveedorFormulario, CompraFormulario, ClienteFormulario, FormularioStock, VentaFormulario
#FUNCIONES/URLS

def bienvenida(request):
    return HttpResponse("Hola usuario")

def inicio(request):
    return render(
        request=request,
        template_name='existencias/inicio.html',
    )


def cliente(request):
    contexto = {
        'clientes': Cliente.objects.all()
    }
    return render(request=request, template_name='existencias/cliente.html',
     context=contexto )



def proveedores(request):
    contexto = {
        'proveedores': Proveedor.objects.all()
    }
    return render(request=request, template_name='existencias/proveedores.html',
     context=contexto )

def stock(request):
    contexto = {
        'stocks': Stock.objects.all()
    }

    return render(request=request, template_name='existencias/stock.html', context=contexto)

def compra(request):
    contexto = {
        'compras': Compra.objects.all()
    }

    return render(request=request, template_name='existencias/compra.html', context=contexto)

def venta(request):
    contexto = {
        'ventas': Venta.objects.all()
    }

    return render(request=request, template_name='existencias/venta.html', context=contexto)




#FORMULARIOS

def crear_proveedor(request):
    if request.method == "POST":
        formulario = ProveedorFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            proveedor = Proveedor(nombre=data['nombre'], rubro=data['rubro'], direccion=data['direccion'], telefono=data['telefono'], email=data['email'])
            proveedor.save()
            url_exitosa = reverse('proveedores')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ProveedorFormulario()
    return render(
        request=request,
        template_name='existencias/formulario_proveedor.html',
        context={'formulario': formulario},
    )

def crear_compra(request):
    if request.method == "POST":
        formulario = CompraFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            compra = Compra(proveedor=data['proveedor'], producto=data['producto'],  cantidad=data['cantidad'], monto=data['total'])
            compra.save()
            url_exitosa = reverse('compras')
            return redirect(url_exitosa)
    else:  # GET
        formulario = CompraFormulario()
    return render(
        request=request,
        template_name='existencias/formulario_compras.html',
        context={'formulario': formulario},
    )


def crear_cliente(request):
    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            cliente = Cliente(nombre=data['nombre'], direccion=data['direccion'],  telefono=data['telefono'], email=data['email'])
            cliente.save()
            url_exitosa = reverse('clientes')
            return redirect(url_exitosa)
    else:  # GET
        formulario = ClienteFormulario()
    return render(
        request=request,
        template_name='existencias/formulario_clientes.html',
        context={'formulario': formulario},
    )



def crear_stock(request):
    if request.method == "POST":
        formulario = FormularioStock(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            cliente = Stock(producto=data['producto'],  cantidad=data['cantidad'])
            cliente.save()
            url_exitosa = reverse('stock')
            return redirect(url_exitosa)
    else:  # GET
        formulario = FormularioStock()
    return render(
        request=request,
        template_name='existencias/formulario_stock.html',
        context={'formulario': formulario},
    )




def crear_venta(request):
    if request.method == "POST":
        formulario = VentaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            venta = Venta(cliente=data['cliente'], producto=data['producto'],  cantidad=data['cantidad'], precio=data['total'])
            venta.save()
            url_exitosa = reverse('ventas')
            return redirect(url_exitosa)
    else:  # GET
        formulario = VentaFormulario()
    return render(
        request=request,
        template_name='existencias/formulario_venta.html',
        context={'formulario': formulario},
    )



def buscar_proveedores(request):
    if request.method == "POST":
        data = request.POST
        proveedores = Proveedor.objects.filter(
            Q(nombre__contains=data['busqueda']) |Q(rubro__contains=data['busqueda']) )
        
        contexto = {
            'proveedores': proveedores
        }
        return render(
            request=request,
            template_name='existencias/proveedores.html',
            context=contexto,
        )
        

def ayuda(request):
    return render(
        request=request,
        template_name='existencias/ayuda.html',
    )