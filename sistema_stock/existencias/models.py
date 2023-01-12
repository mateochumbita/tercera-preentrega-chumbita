from django.db import models
class Proveedor(models.Model):
    nombre = models.CharField(max_length=256)
    rubro = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)
    telefono = models.IntegerField()
    email = models.EmailField()
    def __str__(self):
        return f" {self.nombre}, {self.rubro},  {self.telefono}, {self.email}"
class Compra(models.Model):
    proveedor = models.CharField(max_length=256)
    producto = models.CharField(max_length=256)
    cantidad = models.IntegerField()
    monto = models.IntegerField()
    def __str__(self):
        return f" {self.proveedor}, {self.producto},  {self.cantidad}, {self.monto}"

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
    def __str__(self):
        return f" {self.producto}, {self.cantidad},  {self.cliente}, {self.precio}"

class Stock(models.Model):
    producto = models.CharField(max_length=256)
    cantidad = models.IntegerField()
    def __str__(self):
        return f" {self.producto}, {self.cantidad}"

    