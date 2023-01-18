from django import forms

class ProveedorFormulario(forms.Form):
    nombre= forms.CharField(max_length=64)
    rubro= forms.CharField(max_length=64)
    direccion= forms.CharField(max_length=64)
    telefono= forms.IntegerField(required=True)
    email= forms.EmailField()


class CompraFormulario(forms.Form):
    proveedor= forms.CharField(max_length=64)
    producto= forms.CharField(max_length=64)
    cantidad= forms.IntegerField(required=True)
    total= forms.IntegerField(required=True)


class ClienteFormulario(forms.Form):
    nombre= forms.CharField(max_length=64)    
    direccion= forms.CharField(max_length=64)
    telefono= forms.IntegerField(required=True)
    email= forms.EmailField()


class FormularioStock(forms.Form):
    producto= forms.CharField(max_length=64)
    cantidad= forms.IntegerField(required=True)


class VentaFormulario(forms.Form):
    cliente= forms.CharField(max_length=64)
    producto= forms.CharField(max_length=64)
    cantidad= forms.IntegerField(required=True)
    total= forms.IntegerField(required=True)
    
    
    

