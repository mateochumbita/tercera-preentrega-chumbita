from django.db import models
class Proveedor(models.Model):
    nombre = models.CharField(max_length=256)
    rubro = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)
    telefono = models.IntegerField()
    email = models.EmailField()
class Compra(models.Model):
    proveedor = models.CharField(max_length=256)
    producto = models.CharField(max_length=256)
    cantidad = models.IntegerField()
    monto = models.IntegerField()

class Cliente(models.Model):
    nombre= models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)
    telefono = models.IntegerField()
    email = models.EmailField()
class Venta(models.Model):
    cliente = models.CharField(max_length=256)
    producto = models.CharField(max_length=256)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

class Stock(models.Model):
    producto = models.CharField(max_length=256)
    cantidad = models.IntegerField()
    